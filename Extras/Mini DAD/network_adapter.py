"""Authenticated HTTP adapter for Azure hosting; shared core MCP and REST operations.

API keys identify a connection, not a human. Review/promotion is never exposed
through this network adapter. Terminate TLS at the configured Azure ingress.
"""
from __future__ import annotations
import asyncio
import hmac
import json
import os
import re
from typing import Any
from runtime import AssetError, dispatch, tool_specs
from server import create_mcp_server

MAX_BODY = 64 * 1024
WRITE_TOOLS = {'SubmitLessonCandidate'}
DENIED_TOOLS = {'ReviewLessonCandidate'}

def _json(raw: bytes) -> Any:
    def unique(items):
        out = {}
        for key, value in items:
            if key in out: raise ValueError('duplicate JSON key')
            out[key] = value
        return out
    return json.loads(raw, object_pairs_hook=unique)

def _configuration():
    key = os.environ.get('ALBERT_API_KEY', '')
    intake = os.environ.get('ALBERT_INTAKE_API_KEY', '')
    hosts = [x.strip().lower() for x in os.environ.get('ALBERT_ALLOWED_HOSTS', '').split(',') if x.strip()]
    origins = [x.strip() for x in os.environ.get('ALBERT_ALLOWED_ORIGINS', '').split(',') if x.strip()]
    if len(key) < 32 or any(ord(x) < 33 or ord(x) > 126 for x in key):
        raise RuntimeError('ALBERT_API_KEY must contain at least 32 printable non-space ASCII characters')
    if intake and (len(intake) < 32 or intake == key or any(ord(x) < 33 or ord(x) > 126 for x in intake)):
        raise RuntimeError('ALBERT_INTAKE_API_KEY must be a distinct key of at least 32 printable non-space ASCII characters')
    if not hosts or any(not re.fullmatch(r'[a-z0-9.-]+(?::[0-9]{1,5})?', x) or '*' in x for x in hosts):
        raise RuntimeError('ALBERT_ALLOWED_HOSTS requires exact hostnames, optionally with ports; wildcards are not allowed')
    if any(not re.fullmatch(r'https://[A-Za-z0-9.-]+(?::[0-9]{1,5})?', x) for x in origins):
        raise RuntimeError('Allowed browser origins must be exact HTTPS origins')
    return key.encode(), intake.encode(), hosts, origins

async def _respond(send, status: int, body: Any):
    raw = json.dumps(body, separators=(',', ':')).encode()
    await send({'type':'http.response.start','status':status,'headers':[(b'content-type',b'application/json'),(b'cache-control',b'no-store'),(b'x-content-type-options',b'nosniff')]})
    await send({'type':'http.response.body','body':raw})

class AuthenticatedApplication:
    def __init__(self, inner, key: bytes, intake: bytes, hosts: list[str], origins: list[str]):
        self.inner, self.key, self.intake = inner, key, intake
        self.hosts, self.origins = set(hosts), set(origins)

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'lifespan':
            return await self.inner(scope, receive, send)
        if scope['type'] != 'http':
            return
        path, method = scope.get('path',''), scope.get('method','')
        if path == '/healthz' and method == 'GET':
            return await _respond(send, 200, {'status':'ok'})
        values = {}
        for k,v in scope.get('headers',[]): values.setdefault(k.lower(),[]).append(v)
        if any(len(values.get(k,[])) != 1 for k in [b'host',b'x-api-key']):
            return await _respond(send,401,{'error':'authentication_required'})
        host = values[b'host'][0].decode('latin-1').lower()
        if host not in self.hosts: return await _respond(send,421,{'error':'host_not_allowed'})
        supplied = values[b'x-api-key'][0]
        is_reader = hmac.compare_digest(supplied,self.key)
        is_writer = bool(self.intake) and hmac.compare_digest(supplied,self.intake)
        if not (is_reader or is_writer): return await _respond(send,401,{'error':'authentication_required'})
        origins=values.get(b'origin',[])
        if len(origins)>1 or (origins and origins[0].decode('latin-1') not in self.origins):
            return await _respond(send,403,{'error':'origin_not_allowed'})
        if path == '/openapi.json' and method == 'GET':
            return await _respond(send,200,openapi_document())
        if path != '/mcp' and not path.startswith('/api/tools/'):
            return await _respond(send,404,{'error':'not_found'})
        raw=b'';payload=None
        if method == 'POST':
            if len(values.get(b'content-type',[])) != 1 or values[b'content-type'][0].split(b';',1)[0].strip().lower() != b'application/json':
                return await _respond(send,415,{'error':'application_json_required'})
            while True:
                message=await receive()
                if message['type']=='http.disconnect': return
                raw+=message.get('body',b'')
                if len(raw)>MAX_BODY: return await _respond(send,413,{'error':'request_too_large'})
                if not message.get('more_body',False): break
            try: payload=_json(raw)
            except (ValueError,UnicodeDecodeError): return await _respond(send,400,{'error':'invalid_json'})
            if not isinstance(payload,dict): return await _respond(send,400,{'error':'json_object_required'})
        tool=None
        if path.startswith('/api/tools/'):
            if method != 'POST': return await _respond(send,405,{'error':'post_required'})
            tool=path[len('/api/tools/'):]
        elif method == 'POST' and payload.get('method')=='tools/call':
            params=payload.get('params')
            if not isinstance(params,dict): return await _respond(send,400,{'error':'invalid_tool_call'})
            tool=params.get('name')
            if not isinstance(tool,str): return await _respond(send,400,{'error':'invalid_tool_call'})
        if tool in DENIED_TOOLS: return await _respond(send,403,{'error':'local_review_only'})
        if tool in WRITE_TOOLS and not is_writer: return await _respond(send,403,{'error':'intake_key_required'})
        if path.startswith('/api/tools/'):
            try: result=await asyncio.to_thread(dispatch,tool,payload)
            except AssetError as exc: return await _respond(send,400,{'error':'invalid_request','message':str(exc)})
            return await _respond(send,200,{'result':result})
        sent=False
        async def replay():
            nonlocal sent
            if method=='POST' and not sent:
                sent=True;return {'type':'http.request','body':raw,'more_body':False}
            return await receive()
        return await self.inner(scope,replay,send)

def openapi_document():
    paths={}
    for spec in tool_specs():
        if spec['name'] in DENIED_TOOLS: continue
        paths['/api/tools/'+spec['name']]={'post':{'operationId':spec['name'],'description':spec['description'],'requestBody':{'required':True,'content':{'application/json':{'schema':spec['inputSchema']}}},'responses':{'200':{'description':'Bounded operation result'},'400':{'description':'Invalid input'},'401':{'description':'Missing or invalid API key'},'403':{'description':'Intake key required or operation denied'}},'security':[{'ApiKey':[]}]}}
    return {'openapi':'3.0.3','info':{'title':'Digital Assets with MCP API','version':'1.0'},'paths':paths,'components':{'securitySchemes':{'ApiKey':{'type':'apiKey','in':'header','name':'x-api-key'}}}}

def create_network_app():
    key,intake,hosts,origins=_configuration()
    from mcp.server.transport_security import TransportSecuritySettings
    # Review is a local operator action. Do not advertise it through the
    # network MCP surface even when the local review flag is enabled.
    mcp=create_mcp_server('127.0.0.1', include_review=False)
    mcp.settings.transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=True,allowed_hosts=hosts,allowed_origins=origins)
    return AuthenticatedApplication(mcp.streamable_http_app(),key,intake,hosts,origins)

def main():
    import uvicorn
    app=create_network_app()
    uvicorn.run(app,host=os.environ.get('ALBERT_BIND_HOST','0.0.0.0'),port=int(os.environ.get('ALBERT_BIND_PORT','8765')),access_log=False,proxy_headers=False)

if __name__=='__main__': main()
