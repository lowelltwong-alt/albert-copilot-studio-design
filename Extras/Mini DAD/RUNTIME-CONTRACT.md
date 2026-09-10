# Runtime contract: version 1.0.0-local-candidate

`mcp_stdio.py` is the tested local MCP endpoint. It accepts line-delimited
JSON-RPC `initialize`, `notifications/initialized`, `ping`, `tools/list`, and
`tools/call`; unknown methods and invalid calls fail closed. Its tool list is
the source of exact input schemas.

Read-only tools are `SearchAssets`, `GetAsset`, `GetNeighbors`,
`GetAssetContent`, `GetLifecycleStatus`, `GetRuntimeStatus`, and
`GetLessonCandidate`. They operate on `catalog.json`, which validates asset
IDs, package-relative UTF-8 paths, SHA-256 content digests, typed edges, and
cycles in `requires` edges. Search is token based and returns at most 25 rows.
`GetAssetContent` returns only a verified local file. Lifecycle reports expiry
as `unexpired` or `stale`; it never establishes qualification.

`SubmitLessonCandidate` exists only when `ALBERT_LESSON_INTAKE_ENABLED=true`.
It writes a bounded append-only candidate/event log under `state/`; no other AI
is observed. Required source identity is opaque caller metadata plus a source
hash. Candidate identity uses caller `failure_key`, category, reuse scope, and
linked asset IDs. The receipt disposition is exactly `noise`, `duplicate`,
`needs_evidence`, `candidate`, `reopened_verification`, or `quarantine`.
Duplicates add no quality or independent-context count. A recurrence linked to
an existing candidate returns `reopened_verification`, a `regresses` link, and
review due. This package does not assess semantic near duplicates.

`ReviewLessonCandidate` additionally requires
`ALBERT_LESSON_REVIEW_ENABLED=true`; it records a declared-distinct opaque
reviewer identity. The identity is not authenticated independence. Both tools
return `human_review_required` and never promote an asset, change instructions,
or modify a source repository. Network deployment denies review.

`server.py` is an optional FastMCP Streamable-HTTP factory. It blocks a
non-loopback bind because it does not validate Entra/OAuth requests itself.
`network_adapter.py` is the separate API-key guarded HTTP adapter for a managed
ingress: exact host/origin allowlists, 64 KiB request bound, separate intake
key, and no network review. API keys authenticate a connection, not a person.
Azure/Studio/Foundry setup must use that adapter and a managed secret store.

Run `python -B tests/test_runtime.py` from this directory with Python 3.12. The test proves local catalog,
lifecycle/cycle, dispositions/concurrency, and a stdio initialize/list/call
exchange. It does not prove tenant authentication, managed ingress, Foundry,
Copilot Studio, Entra/OAuth, or a cross-AI host hook.
