# Mini DAD: digital assets with MCP

An optional service for searching reusable agents, workflows and harnesses, following their graph links, checking expiry and reporting learning candidates. It runs independently of Albert and of the original private DAD installation.

**Rights first:** proprietary IP of Lowell Wong. Public inspection is allowed; use/deployment needs separate written permission. See LICENSE-PROPRIETARY.md.

## Local setup and first use

1. Keep this whole folder together. Install Python 3.12 or use an approved compatible interpreter.
2. From this folder run `python -B tests/test_runtime.py`. The core and stdio endpoint use the standard library.
3. Configure your MCP host to launch `python` with the absolute path to `mcp_stdio.py` as its argument and this folder as its working directory.
4. Have the host initialize, list tools, call SearchAssets, then GetAsset and GetAssetContent for a returned ID. Use tools/list for exact schemas. GetNeighbors follows links; GetLifecycleStatus reports stale evidence.
5. Leave intake and review disabled for the first run. Retrieved assets are candidates for review, not authority to execute.

## How learning works

Another AI must explicitly submit a privacy-safe observation. Mini DAD does not monitor other AIs or read their chats. When ALBERT_LESSON_INTAKE_ENABLED=true, SubmitLessonCandidate records bounded candidates in state/. Noise is not stored; exact duplicates do not add evidence; unsafe input is quarantined; linked recurrence after a fix reopens verification. Semantic near-duplicate judgment needs review. Human review precedes adoption; the service never promotes a lesson or rewrites instructions automatically.

## Deploy for Copilot Studio / Foundry

1. Run the local tests above. For HTTP install the pinned requirements with `python -m pip install -r requirements.txt`, then run `python -B tests/test_network.py`.
2. Build Dockerfile into your approved registry. Use azure/containerapp.bicep and azure/parameters.example.json with your existing Container Apps environment and Azure Files state mount. Supply secret references through your approved secret store.
3. Deploy network_adapter.py behind managed HTTPS ingress. Set the reader key and exact allowed hosts/origins using the names in MCP-API.md. Enable intake only with a separate key and review owner. No network review endpoint is exposed.
4. Connect the tenant to `/mcp` with Streamable HTTP and the `x-api-key` header. The API backup is `POST /api/tools/{tool}`; schemas are at `/openapi.json`; `/healthz` is process health only.
5. Test initialize/list/call, denied missing/wrong keys, read/API parity, allowed hosts, persistent storage and rollback through the actual tenant. Entra/OAuth requires a separately validated gateway; the adapter does not validate Entra tokens.

| Environment variable | Configure |
|---|---|
| ALBERT_API_KEY | Reader key: at least 32 printable non-space ASCII characters; secret store only |
| ALBERT_INTAKE_API_KEY | Distinct key with the same minimum, only when intake is enabled |
| ALBERT_ALLOWED_HOSTS | Exact hostnames, optionally ports, comma-separated; no wildcards |
| ALBERT_ALLOWED_ORIGINS | Exact approved origins, comma-separated |
| ALBERT_BIND_HOST / ALBERT_BIND_PORT | Container bind address and port; default 0.0.0.0 / 8765 |
| ALBERT_LESSON_INTAKE_ENABLED | false initially |
| ALBERT_LESSON_REVIEW_ENABLED | false for network deployment |

The detailed deployment parameters and commands are in [azure/README.md](azure/README.md). This is a deployment recipe; Azure, Studio and Foundry acceptance are pending. Install/deploy only within your separate license and tenant authorization.

## AI and engineering map

Ask your AI: "Read AI_FRONT_DOOR.md in this folder and follow every endpoint and internal reading reference. Explain what is implemented, how candidate review works, and what remains unverified before suggesting deployment."

The [front door](AI_FRONT_DOOR.md) maps RUNTIME-CONTRACT.md, DATA-MODEL.md, LEARNING-LOOP.md, MCP-API.md, catalog.json, assets, tests and Azure. In the full Albert repository the root AI_FRONT_DOOR.md and AI-TOC.md link here. The original DAD private corpus is not included; this is the complete standalone Mini DAD implementation.

[Proprietary license](LICENSE-PROPRIETARY.md) · [Provenance](PROVENANCE.md).
