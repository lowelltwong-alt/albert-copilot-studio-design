# Provenance and licensing boundary

This is a new standalone runtime. It imports no DAD module, registry, corpus,
private row, credential, source repository, or absolute path.

The implementation adapts generic design patterns from the DAD donor at commit
`a304c9ba3b91f828c46e77c6266c030b12e54bba`: bounded JSON-RPC dispatch,
allowlisted tools, public-metadata graph queries, privacy-safe candidate
screening, exact-id deduplication, evidence-gated review, and human-only
promotion. The donor `src/digital_asset_directory/mcp_server.py` fingerprint
was `6f8d3e47c270d290f08287392e80848464df134d65885fbc22844c4f5a4517b6`.
Its MCP server is read-only; this package's lesson submission/review log is a
new standalone mechanism, not a donor capability.

`albert:agent:*`, workflow, skill, prompt, and fixture reference cards index
selected Albert Team Toolkit 0.2.0 metadata. They deliberately do not copy the
full source instructions. The Toolkit catalog observed fingerprint was
`198b80ff60557a6c99e86f5e3bd072b7699df1355383a0006da67e19060d2fd8`.

The inspected DAD donor had no confirmed permissive license in the reviewed
scope. Lowell Wong authorized public presentation of this standalone package
under the proprietary notice in LICENSE-PROPRIETARY.md on 2026-09-10.
Public inspection does not grant deployment, modification or redistribution
rights. Do not treat that boundary as CC BY. Third-party MCP/ASGI dependencies retain
their own licenses; they are not vendored here.
