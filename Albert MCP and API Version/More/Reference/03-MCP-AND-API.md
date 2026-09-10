# MCP and API implementation contract

There are three editions. MVP is prompt-only and uses neither API nor MCP. Full connected exposes one approved service through MCP-primary or API-only profiles for the same eight agent operations. Full prompt workflow is a separate manual-completion pack with no API/MCP/backend claim. These files describe only the full connected edition; they are specifications and import templates, not a running MCP server or exported Power Platform solution.

## Copilot Studio target

The connected target is the Standard harness in Teams and a public HTTPS `/mcp` endpoint with Streamable HTTP. Implement protocol initialize, initialized notification, version negotiation, tools/list and tools/call with the official MCP SDK; test the version negotiated by the actual tenant. Expose only the eight tools in `albert-mcp-tools.json`; prompts/resources, stdio and legacy SSE are not integration dependencies. Support both JSON and event-stream responses as required by the negotiated transport. No browser-login HTML may replace protocol responses. Teams import, authentication, invocation and published-channel testing remain pending.

Microsoft documents direct MCP onboarding and a Swagger 2.0 custom-connector route using `x-ms-agentic-protocol: mcp-streamable-1.0` on the POST operation. The two connector templates here follow that documented shape; importing them in a tenant remains an acceptance test. See [Microsoft MCP setup](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent).

1. Deploy the service to an approved host; install a trusted TLS certificate. Configure tenant/audience validation and scoped case access before attaching an agent.
2. Register the OAuth application for the intended tenant. Replace `REPLACE_TENANT`, the example host and scope names with that registration's actual audience-qualified scopes. Do not put a secret in prompts or commit it in either template.
3. Direct route: agent Tools → Add a tool → New tool → MCP; enter endpoint and configure OAuth 2.0. Register the callback URI shown by Copilot Studio exactly in the identity provider. Validate token audience/scopes at the backend. Alternatively import `copilot-mcp-connector.swagger.json` as a Power Platform custom connector and configure its connection/security fields.
4. Permit the exact connector under environment DLP and bind an approved connection. Test discovery plus every authorized tool, expired tokens, a second user and a forbidden case. Validate end-user identity propagation; a maker connection must not grant all users the maker's rights.
5. Publish only to the pilot channel after the tenant probes pass. Test again there; a maker test-chat success alone is insufficient. Record tenant, environment, channel, service revision, connector export hash, principal mapping, negotiated protocol and timestamp.

## Contract files and mapping

`albert-api.openapi.json` is canonical OpenAPI 3.0.3 with typed request/response envelopes. `copilot-api-connector.swagger.json` provides a Swagger 2.0 API connector candidate. All eight exposed operations use POST, including read-only operations, so method alone never determines side effects. `albert-mcp-tools.json` is the tools/list payload with protocol extension metadata; it is not a standalone server or a file to import as a Copilot solution. `06-contracts.schema.json` defines the richer domain records. A backend adapter must translate transport DTOs to those records and enforce the service rules in `02-FLOWS-AND-STATE.md`; shape validation cannot enforce authorization or quality.

The mapping is explicit: Binding supplies the case, source, graph snapshot, witness-view and policy revisions/digests; ReadGraph maps to the closed domain GraphQuery kinds, subject, `atTime`, depth, limit, cursor and view grant; its result maps to a bounded GraphResult projection. SaveCandidate maps a typed proposal or artifact candidate to its CaseCandidateGrant or WitnessViewGrant and ExecutionAssignment. RequestEvaluation creates an S04 evaluation job and an independently assigned P06 worker context; P06 does not receive a direct unbounded evaluation action. RecordHumanDecision maps the screen-compatible ReviewSubject to a revision-bound HumanDecision. These are proposed adapters, not deployed code.

| Agent operation | API route | Effect |
|---|---|---|
| StartJob | /v1/jobs/start | Create an approved bounded asynchronous job |
| GetJob | /v1/jobs/get | Read status |
| CancelJob | /v1/jobs/cancel | Fence current work and request cancellation |
| LookupOperation | /v1/operations/lookup | Reconcile an unknown response under same principal |
| ReadGraph | /v1/graph/read | Read an attributed permitted view, max 50 records |
| ReadArtifact | /v1/artifacts/read | Read one allowed section, max 12,000 characters |
| SaveCandidate | /v1/candidates/save | Persist draft only, max 100,000 characters |
| RequestEvaluation | /v1/evaluations/request | Enqueue independent evaluation |

RecordHumanDecision exists only in the canonical API for the authenticated human portal and is omitted from both agent connectors. Its typed review subject is compatible with the screen: H01 data-movement approval, H02 layout/exhibit review, H03 case/witness profile, H04 quality/rework plan, H05 exact artifact pair, H06 study custody and H07 vendor handoff. Only H05 approval of an exact current artifact pair can return a non-null export job ID. Approval requires server-issued single-use nonce, current version and authorized human principal; passing a decision string is insufficient. Review UI bootstrap/listing and upload/custody adapters are internal implementation tasks, not advertised MCP tools.

The backend enforces this screen-kind matrix and rejects every other pair. It also enforces per-tool authorization after OAuth: GetJob, LookupOperation, ReadGraph and ReadArtifact require a current `read` capability plus case/grant checks; StartJob, CancelJob, SaveCandidate and RequestEvaluation require `write` plus their operation-specific approval/assignment checks; RecordHumanDecision requires `review` in the human portal. The single MCP connector's read/write consent is not per-tool authorization.

For initial intake, absent graph/view revisions are the explicit sentinel `not_created`; the backend permits that only for approved intake-related jobs and resolves real revisions before any witness read or generation. For a first candidate, `parentArtifactId` is `baseline`; later candidates must resolve an immutable parent in the same series. SaveCandidate accepts source-review, case-profile and witness-settings proposals with a CaseCandidateGrant before a witness grant exists; packet/script candidates require a current WitnessViewGrant. These sentinels are validated by job/candidate kind, never treated as wildcard access. `movementApprovalId` can refer to an approved local/no-egress policy; `budgetApprovalId` always resolves server-side. Service-generated job/artifact IDs and digests are authoritative.

## Identity, idempotency and fallback

Resolve the caller from verified credentials and explicit delegation; never accept a principal string from model arguments. Check case role, witness view, processor/data approval and current snapshot again in the canonical service for every operation. Case IDs, opaque cursors and artifact IDs do not confer access. Cursor contents bind principal, view, snapshot and query. Split overlarge packets into service-defined sections; do not silently truncate evidence.

The model never authors an operation ID or idempotency key. A proposed trusted Topic adapter or human-portal session adapter creates a server-issued command authorization token after it has canonicalized the exact payload. The backend validates that the token is single-operation, bound to the verified principal, operation name, canonical parameter digest, case, expiry and intended tool; it resolves the hidden operation ID and idempotency key. The adapter persists those values for reconciliation. This injection path is a required implementation and tenant acceptance test; without it, connected mutations do not go live.

For every mutation the backend atomically reserves `(case, verified principal, operation name, idempotency key)` with its canonical request digest and operation ID. A matching duplicate returns the original receipt; a mismatched duplicate is a 409. Commit job/candidate/decision changes with the operation receipt and outbox in one transaction. Distinct transports do not mean distinct transactions. Read requests carry a stable read-operation ID and digest across MCP-to-HTTPS fallback; graph responses echo graph snapshot and access-policy digests.

On connection loss or response timeout, use read-only API LookupOperation first. If found, return that authoritative receipt; if still pending, poll. A 404 is not proof a concurrent write cannot commit: do not automatically submit a fresh mutation. Operator-directed switching to API-only may retry the SAME stored operation ID, key and digest after reconciliation, relying on atomic uniqueness. Automatic fallback is limited to read operations after transient transport unavailability and only under the same verified principal/audience/grants. No fallback for 401/403, revoked grants, stale bindings, 409/422, exhausted budget, quality rejection, cancellation, invalid TLS or untrusted redirect. Invalid TLS is a hard failure, never a fallback trigger. Do not downgrade authentication.

Error bodies are bounded safe messages plus a correlation ID; they contain no tokens, case excerpts or stack traces. Map MCP domain failures to `isError: true` with this envelope; use protocol errors only for malformed protocol calls. Tool annotations are hints, not authorization. Return StartJob/RequestEvaluation promptly (pilot target under 10 seconds); expensive work is asynchronous. Poll defaults: 5 seconds with bounded backoff to 30 seconds, configurable per load test. Confirm actual response-size, timeout and rate limits in tenant; these payload caps are proposed conservative application bounds, not Microsoft guarantees.

## Required compatibility evidence

The team must demonstrate: Teams connector/direct onboarding; TLS/OAuth callback; trusted token injection; tools/list; all eight calls; no human decision tool; same operation via both transports; lost response without duplicate work; denied wrong-case read; token expiration/revocation; cancellation with late callback; repeated published-channel use; DLP denial; model/tool context limits. Store sanitized request metadata and result digests. Compatibility remains **not tenant verified** until these pass on the release revision. No honest predeployment promise can substitute for those checks.


## Dialects and complete request semantics

`albert-transport.schema.json` is the complete Draft 2020-12 request/response schema, including conditional human-decision/export constraints. OpenAPI 3.0 projects nullable values using `nullable`; Swagger 2 projects them with `x-nullable`. Those transport dialects do not express every conditional rule. The backend must validate the complete JSON Schema plus the cross-record rules, regardless of connector-side validation. No OpenAPI/Swagger import was executed in the tenant.

For pre-intake bindings, a missing revision uses `not_created` and the corresponding digest is 64 zero characters. The service accepts that pair only where the job/candidate phase legitimately predates the record; a real witness/artifact read requires resolved non-sentinel bindings. Canonical request digests exclude their own digest field, the command token, OAuth credentials and transport-only metadata; include all semantic parameters and current bindings. Trusted adapters compute them, not model text.

`coach_annex` is a separate SaveCandidate kind with a separate series, coach-scoped grant and explicit writer assignment. It cannot be embedded in the witness packet or returned by a witness grant. The service validates candidate kind against grant/assignment kind and audience before persistence. P01/P02/P03 proposals use appropriate CaseCandidateGrant assignments before witness grants exist; P04/P05 witness artifacts use WitnessViewGrant. Source proposal reads use the approved internal source-review adapter, not unrestricted graph traversal.

The trusted command token is reusable only for a matching replay of its one bound logical operation while the backend retains its idempotency receipt; it is not a generic bearer credential. Reconciliation checks the stored operation ID/request digest under the same caller. A nonce used for a human decision remains single-use for a new decision. The adapter must preserve logical operation identity through timeout/retry and never ask the model to mint a replacement key.
