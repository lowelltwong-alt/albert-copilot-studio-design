"""Dependency-free, line-delimited JSON-RPC MCP adapter for local operation."""
from __future__ import annotations
import json, sys
from typing import Any
from runtime import AssetError, dispatch, tool_specs

PROTOCOL = "2025-06-18"

def response(request: dict[str, Any]) -> dict[str, Any] | None:
    request_id, method, params = request.get("id"), request.get("method"), request.get("params") or {}
    try:
        if not isinstance(params, dict): raise AssetError("parameters must be an object")
        if method == "notifications/initialized": return None
        if method == "initialize": result = {"protocolVersion": PROTOCOL, "capabilities": {"tools": {}}, "serverInfo": {"name": "albert-digital-assets", "version": "1.0.0"}}
        elif method == "ping": result = {}
        elif method == "tools/list": result = {"tools": tool_specs()}
        elif method == "tools/call":
            name = params.get("name"); arguments = params.get("arguments", {})
            if not isinstance(name, str) or not isinstance(arguments, dict): raise AssetError("tool call is invalid")
            payload = dispatch(name, arguments)
            result = {"content": [{"type": "text", "text": json.dumps(payload, sort_keys=True)}], "structuredContent": payload}
        else: raise LookupError("method not found")
        return {"jsonrpc": "2.0", "id": request_id, "result": result}
    except LookupError:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": "Method not found"}}
    except AssetError as exc:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32602, "message": str(exc)}}
    except Exception:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32603, "message": "Internal error"}}

def main() -> None:
    for line in sys.stdin:
        try: item = json.loads(line)
        except json.JSONDecodeError: item = None
        if not isinstance(item, dict): result = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
        else: result = response(item)
        if result is not None:
            sys.stdout.write(json.dumps(result, separators=(",", ":")) + "\n"); sys.stdout.flush()
if __name__ == "__main__": main()
