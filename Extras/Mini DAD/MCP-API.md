# MCP and API contract

## Local stdio

Run `python -B mcp_stdio.py`. The server accepts JSON-RPC lines for `initialize`, `notifications/initialized`, `ping`, `tools/list`, and `tools/call`, using MCP protocol `2025-06-18`. Invalid methods, unknown tools, unknown arguments, malformed JSON and invalid values fail closed. This is the easiest no-Azure smoke test.

## Streamable HTTP

`server.py` exposes `/mcp` only on loopback and refuses non-loopback hosting because it does not validate Entra/OAuth requests. `network_adapter.py` is the deployment adapter. It requires `ALBERT_API_KEY` (at least 32 printable non-space characters), exact `ALBERT_ALLOWED_HOSTS`, and exact HTTPS `ALBERT_ALLOWED_ORIGINS`. `ALBERT_INTAKE_API_KEY` is optional and must be distinct; it is the only network key allowed to submit candidates. API keys authenticate a connection, not a person. Put TLS, secret storage, rate limits and network policy at the Azure ingress.

For MCP requests send `x-api-key`, `Content-Type: application/json`, and the normal Streamable HTTP JSON-RPC body to `/mcp`. Copilot Studio currently supports the Streamable transport and API-key or OAuth connection configuration; this package supplies an API-key adapter and does not claim Entra/OAuth validation.

## REST backup

Send the same argument object as JSON to `POST /api/tools/SearchAssets` (or another exposed tool). `GET /openapi.json` describes the exposed operations and `x-api-key` security scheme. `GET /healthz` is a process probe and intentionally does not authenticate; it reveals no catalog data.

The network surface never exposes review/promotion. Candidate intake is opt-in and remains append-only, local to the mounted state directory, and human-review-required. Unknown routes, duplicate keys, oversized bodies, invalid content types, incorrect keys, disallowed hosts/origins and denied tools return errors without invoking the core dispatcher.

## Tool summary

`SearchAssets` searches bounded public metadata. `GetAsset` returns metadata without package paths or digests. `GetNeighbors` returns typed candidate edges. `GetAssetContent` returns verified UTF-8 content for a selected asset. `GetLifecycleStatus` reports expiry and qualification state. `GetRuntimeStatus` reports enabled surfaces and explicitly says cross-instance detection is caller-driven. `GetLessonCandidate` returns a candidate and its append-only events/reviews. `SubmitLessonCandidate` and local `ReviewLessonCandidate` are described in `LEARNING-LOOP.md` and are disabled unless their environment flags are set.

