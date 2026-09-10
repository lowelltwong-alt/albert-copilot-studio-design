"""Real HTTP integration checks. Starts and stops only its own local child server."""
import json, os, socket, subprocess, sys, time, unittest
from pathlib import Path
import urllib.error, urllib.request
ROOT=Path(__file__).resolve().parents[1]

class NetworkIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import secrets
        with socket.socket() as s:
            s.bind(('127.0.0.1',0));cls.port=s.getsockname()[1]
        cls.key=secrets.token_urlsafe(32);cls.intake=secrets.token_urlsafe(32)
        env=os.environ.copy();env.update(ALBERT_API_KEY=cls.key,ALBERT_INTAKE_API_KEY=cls.intake,ALBERT_ALLOWED_HOSTS=f'127.0.0.1:{cls.port}',ALBERT_ALLOWED_ORIGINS='https://approved.example',ALBERT_BIND_HOST='127.0.0.1',ALBERT_BIND_PORT=str(cls.port),ALBERT_LESSON_INTAKE_ENABLED='false',ALBERT_LESSON_REVIEW_ENABLED='false')
        cls.proc=subprocess.Popen([sys.executable,'-B',str(ROOT/'network_adapter.py')],cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        cls.base=f'http://127.0.0.1:{cls.port}'
        deadline=time.monotonic()+30
        while time.monotonic()<deadline:
            if cls.proc.poll() is not None:
                _,err=cls.proc.communicate();raise RuntimeError('server startup failed: '+err.decode(errors='replace')[-1800:])
            try:
                with urllib.request.urlopen(cls.base+'/healthz',timeout=1) as r:
                    if r.status==200:return
            except (OSError,urllib.error.URLError):time.sleep(.15)
        cls.proc.terminate();cls.proc.wait(timeout=5);raise RuntimeError('server startup timed out')
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        try:cls.proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:cls.proc.kill();cls.proc.communicate(timeout=5)
    def request(self,path,payload=None,headers=None,raw=None):
        hs={'x-api-key':self.key,'Accept':'application/json, text/event-stream'}
        if headers:hs.update(headers)
        data=raw if raw is not None else (json.dumps(payload).encode() if payload is not None else None)
        if data is not None:hs['Content-Type']='application/json'
        req=urllib.request.Request(self.base+path,data=data,headers=hs)
        try:
            with urllib.request.urlopen(req,timeout=10) as r:return r.status,json.loads(r.read()) if r.status!=202 else None
        except urllib.error.HTTPError as e:
            body=e.read()
            try:body=json.loads(body)
            except ValueError:body=body.decode(errors='replace')
            return e.code,body
    def test_real_mcp_initialize_list_call_and_api_parity(self):
        status,init=self.request('/mcp',{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18','capabilities':{},'clientInfo':{'name':'local-acceptance','version':'1'}}})
        self.assertEqual(status,200);self.assertIn('serverInfo',init['result'])
        status,_=self.request('/mcp',{'jsonrpc':'2.0','method':'notifications/initialized'});self.assertEqual(status,202)
        status,listed=self.request('/mcp',{'jsonrpc':'2.0','id':2,'method':'tools/list'});self.assertEqual(status,200)
        specs={s['name']:s for s in listed['result']['tools']};self.assertIn('SearchAssets',specs)
        self.assertIn('query',specs['SearchAssets']['inputSchema']['properties']);self.assertNotIn('kwargs',specs['SearchAssets']['inputSchema']['properties'])
        args={'query':'review','limit':3}
        status,called=self.request('/mcp',{'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'SearchAssets','arguments':args}})
        self.assertEqual(status,200);self.assertFalse(called['result'].get('isError',False))
        mcp_result=called['result'].get('structuredContent')
        if mcp_result is None:mcp_result=json.loads(called['result']['content'][0]['text'])
        status,api=self.request('/api/tools/SearchAssets',args);self.assertEqual(status,200);self.assertEqual(mcp_result,api['result']);self.assertTrue(api['result']['assets'])
    def test_authentication_host_origin(self):
        self.assertEqual(self.request('/api/tools/GetRuntimeStatus',{}, {'x-api-key':'invalid'})[0],401)
        self.assertEqual(self.request('/api/tools/GetRuntimeStatus',{}, {'Host':'untrusted.example'})[0],421)
        self.assertEqual(self.request('/api/tools/GetRuntimeStatus',{}, {'Origin':'https://untrusted.example'})[0],403)
        self.assertEqual(self.request('/api/tools/GetRuntimeStatus',{}, {'Origin':'https://approved.example'})[0],200)
    def test_write_separation_and_review_denied(self):
        self.assertEqual(self.request('/api/tools/SubmitLessonCandidate',{})[0],403)
        self.assertEqual(self.request('/api/tools/ReviewLessonCandidate',{}, {'x-api-key':self.intake})[0],403)
        status,_=self.request('/mcp',{'jsonrpc':'2.0','id':4,'method':'tools/call','params':{'name':'ReviewLessonCandidate','arguments':{}}},{'x-api-key':self.intake});self.assertEqual(status,403)
    def test_bad_inputs_and_openapi(self):
        self.assertEqual(self.request('/api/tools/Unknown',{})[0],400)
        self.assertEqual(self.request('/api/tools/SearchAssets',{'query':'review','limit':0})[0],400)
        self.assertEqual(self.request('/api/tools/SearchAssets',raw=b'{"query":"review","query":"duplicate"}')[0],400)
        self.assertEqual(self.request('/api/tools/SearchAssets',raw=b' '*65537)[0],413)
        self.assertEqual(self.request('/api/tools/GetRuntimeStatus',{'unknown':'field'})[0],400)
        status,api=self.request('/openapi.json');self.assertEqual(status,200);self.assertEqual(api['components']['securitySchemes']['ApiKey']['name'],'x-api-key')
        self.assertNotIn('/api/tools/ReviewLessonCandidate',api['paths'])
if __name__=='__main__':unittest.main(verbosity=2)
