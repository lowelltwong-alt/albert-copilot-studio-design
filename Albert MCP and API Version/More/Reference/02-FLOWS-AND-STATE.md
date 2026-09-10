# Flows and state

## Scope and authority

This is proposed implementation wiring. It does not establish a tenant connection, publish an agent, invoke a provider, or create a backend. The backend, rather than Copilot conversation state, is authoritative for authorization, persistent state, cost, artifact eligibility, and every state transition. All examples use synthetic records only.

Each request is authenticated before its case path is interpreted. The dispatcher derives the principal and case permissions from the verified identity; a supplied case ID, witness ID, grant ID, or model-produced text never supplies authority. Every mutation uses a canonical request digest, an operation ID, an idempotency key, and an expected revision or state version as applicable.

## Common operation envelope

MCP and HTTPS use one canonical operation envelope and one backend dispatcher. The transport adapter maps its native request into the envelope before policy or workflow logic begins.

| Field | Required behavior |
|---|---|
| `operation_id` | Client-generated opaque UUID, persisted before side effects; used to reconcile an uncertain submission. |
| `idempotency_key` | Unique within verified principal, case, and operation name; it is permanently bound to the canonical request digest. The same key with a different digest is an `idempotency_conflict`. |
| `canonical_request_sha256` | Digest of a canonicalized request body after transport mapping. |
| `case_id`, revision/snapshot bindings | Checked against the authoritative case, grant, and dependency records. |
| `correlation_id` | Returned in every safe status or error response. |
| response | Returns `operation_id`, state and state version, job ID when one exists, result/snapshot binding when allowed, error code, and served transport. |

The dispatcher records request acceptance and the job/transition in one transaction. An operation lookup is a read-only operation and can locate a start request before the caller knows its server-issued job ID.

## F01 through F10

| Flow | Owner | Inputs | Output | Closed errors | Restart rule |
|---|---|---|---|---|---|
| F01 Intake | S04 dispatcher with S01 | approved source binding, H01 approval, expected case revision, operation envelope | intake job and immutable source/layout references | `not_authorized`, `stale_input`, `boundary_review_required`, `budget_exhausted`, `provider_outcome_unknown`, `invalid_contract` | Correct a rejected/expired approval or input by starting a new job. Reconcile an unknown provider outcome before any retry. |
| F02 Source review | H02 UI and S05 | layout/exhibit proposal binding, page render binding, expected review revision | signed boundary decision or request-changes decision | `not_authorized`, `stale_input`, `revision_conflict`, `invalid_contract` | A request for changes returns a proposal to its producer; a reject fails the dependent work. No automatic boundary promotion. |
| F03 Normalize and chunk | S02 | H02-approved boundaries, layout/source binding, expected revision | immutable chunk manifest and graph-ready source binding | `boundary_review_required`, `stale_input`, `invalid_contract`, `cancelled` | Start a new chunk job from current approvals. A changed boundary invalidates chunks and descendants. |
| F04 Case and witness profile | S03/S05 with H03 | graph snapshot, rule/profile proposals, witness roster, expected case revision | H03-signed profile/settings and current witness-view grants | `missing_rule_profile`, `not_authorized`, `stale_input`, `revision_conflict` | Supply/approve a rule profile or use a new graph/profile job. Missing rules stop domain conclusions. |
| F05 Witness view | S03 | current H03, witness ID, graph snapshot, recipient assignment | immutable recipient-specific witness view/grant | `not_authorized`, `stale_input`, `invalid_contract` | Reissue a grant after H03, graph, policy, or recipient change; do not extend an old grant. |
| F06 Packet quality series | S04, P04 writer, P06 evaluator | current packet assignment, witness grant, frozen policy/rubric, A0 or prior revision | immutable packet artifact, evaluation, revision receipt, quality decision | `quality_unresolved`, `provider_outcome_unknown`, `cancelled`, `budget_exhausted`, `stale_input` | Resume only from a frozen checkpoint with current lease/grant. Each request-change starts the next attempt in the same valid series. |
| F07 Script quality series | S04, P05 writer, P06 evaluator | approved packet binding, witness grant, chapter plan, frozen policy/rubric | immutable chapter/script artifacts, evaluation, revision receipt, quality decision | same as F06 plus `missing_rule_profile` | Rebuild only affected frozen chapters, then run merge and full evaluation. A packet change stales dependent script work. |
| F08 Cross-artifact review/export | S04/S05 and H05 | exact current packet/script bindings, consistency result, H05 decision, intended audience | artifact approval ledger entry and a distinct export job/manifest | `quality_unresolved`, `stale_input`, `not_authorized`, `invalid_contract` | A consistency finding returns the affected artifact to its own rework series. H05 approval never rewrites a generation job. |
| F09 Status, reconcile, retry, cancel | S04 | job ID or operation ID, expected state version for a mutation, operation envelope | safe job state, reconciliation receipt, retry job, or cancellation receipt | `not_authorized`, `revision_conflict`, `provider_outcome_unknown`, `cancelled` | A lost response is reconciled by the same operation ID and idempotency key. A retry uses the same primary operation only after non-acceptance is proven. |
| F10 Optional human study | study custodian service and H06 | approved protocol/consent, sealed question-bank binding, assignment, delay window | study-custody record and independent scores | `not_authorized`, `invalid_contract`, `stale_input` | Disabled until H06. Custodian reassigns only under the approved protocol; writers never receive hidden questions. |

P00 may route a user to a flow and display safe status. It cannot manufacture a state, quality result, human decision, or completion flag. P01-P05 can save only narrowly assigned candidates. P06 can save only an evaluation. S04 persists the authoritative result of every long-running step.

## Job lifecycle

The service rejects every transition not listed below. State version increases exactly once per accepted transition. A transition must name the actor, current attempt where applicable, and evidence binding.

| State | Allowed next states | Guard |
|---|---|---|
| `queued` | `running`, `cancelled`, `stale`, `budget_exhausted` | current input/approval/grant and budget must be valid before lease acquisition |
| `running` | `waiting_human`, `retry_wait`, `reconciling`, `needs_rework`, `review_ready_pending_human`, `succeeded`, `failed`, `cancel_requested`, `stale`, `budget_exhausted` | live lease fence and current cancel generation |
| `waiting_human` | `queued`, `needs_rework`, `failed`, `cancelled`, `stale` | signed decision has the required scope; `failed` represents a rejected required decision |
| `retry_wait` | `running`, `cancelled`, `stale`, `budget_exhausted` | retry is a classified retryable failure, backoff has elapsed, and budget remains |
| `reconciling` | `running`, `failed`, `cancel_requested` | provider request fingerprint has an evidence-backed outcome |
| `needs_rework` | `queued`, `unresolved_not_parity`, `cancelled`, `stale` | authenticated rework plan and a current series/policy |
| `cancel_requested` | `cancelled` | active attempt cannot publish after its cancellation generation changes |

`failed`, `cancelled`, `stale`, `budget_exhausted`, and `unresolved_not_parity` are terminal. For packet and script generation, `review_ready_pending_human` is terminal success-equivalent: it means quality gates passed and awaits artifact approval. Only eligible non-generation operations use `succeeded`. Raising a budget, changing an input, or seeking another draft creates a new job or series; it never revives a terminal job.

## Artifact and quality state

Artifact state is separate from job state. A frozen candidate may be evaluated. An evaluation drives it to `needs_rework` or `review_ready_pending_human`; H05 alone may change an exact current artifact from `review_ready_pending_human` to `approved_exact_scope`. H05 rejection changes it to `rejected`; a dependency change changes it to `stale` and disables download eligibility. Each change produces an immutable artifact-transition ledger record. Historical artifacts remain available only to audit-authorized principals.

F08 checks a result bound to the exact packet hash, script hash, grants, and quality decisions. A cross-artifact finding returns the affected artifact to `needs_rework`; its own next write/evaluate cycle and another cross-check are required before approval. A stale earlier pair cannot be approved.

## Attempts, cancellation, and reconciliation

An attempt has a lease fence, expiration, cancel generation, provider request fingerprint, callback nonce digest, charged-use record, and immutable outcome. A worker must compare all of those values before publishing. A provider timeout is an unknown outcome, not a failed generation and not permission to duplicate a potentially charged request.

The internal callback handler accepts a callback exactly once using the attempt ID, provider event ID or nonce, lease fence, cancel generation, provider request fingerprint, and signature receipt. It stores the receipt before publishing output. If callback completion commits first, a later cancellation returns that terminal state without alteration. If cancellation commits first, its generation increment wins; the callback becomes `quarantined` and its output cannot be published. Reconciliation records the provider evidence and posts any charge once per provider request fingerprint before a classified retry can be scheduled.

## Transactional outbox

Each state, artifact, review, or invalidation transaction writes a content-minimal outbox event in the same database transaction. Required fields are event ID, aggregate type/ID, aggregate state version, event type, payload binding/digest, permitted destination/audience, availability time, delivery attempts, delivery receipt, and timestamps. Consumers deduplicate by event ID and aggregate version. The outbox contains no case text, prompt, answer, or raw evidence.

## Three editions and transport failover

**Edition 1: prompt-only MVP.** This edition has no external API, MCP server, custom connector, or backend. Copilot may demonstrate static instructions and synthetic, non-authoritative examples. It cannot perform F01-F10, save a candidate, retrieve case material, calculate quality status, or claim service enforcement.

**Edition 2: full connected.** The confirmed design target is a Standard-harness Copilot agent in Teams. Its MCP-primary profile calls the Streamable HTTP MCP adapter; its API-only profile calls the same dispatcher through authenticated HTTPS. HTTPS also supplies narrow read fallback for the MCP profile. Both profiles use the same operation envelope, policy, records, and response shape. Tenant import, Teams authentication, trusted Topic-adapter token injection, tool invocation, and published-channel behavior remain untested.

**Edition 3: full prompt workflow.** This separate manual-completion pack can take approved source/graph material as bounded text and guide a witness profile, packet, script, review, revision, and final package through manual human custody. It has no API, MCP, custom connector, backend, or automatic retrieval/persistence claim. SharePoint may be used as a human-selected file location in any edition, but no broad case folder is Copilot Knowledge.

Automatic fallback applies only to declared safe reads: job status, operation lookup, and bounded graph/span/artifact retrieval. It may occur after MCP produces no semantic response because of connection, DNS, session-reset, timeout, or unavailable 502/503/504-equivalent failure. Certificate validation failure, invalid TLS, or an untrusted redirect is a hard stop, never a fallback trigger. The HTTPS read repeats the exact operation ID, snapshot/cursor, and principal scope; a mismatched snapshot or policy digest is rejected. There is no fallback after an authentication/authorization failure, semantic absence, validation error, revision conflict, rate/budget/quality denial, cancellation, or any response that establishes business meaning.

In the MCP-primary connected profile, mutations have no **automatic** HTTPS fallback. A trusted Topic adapter, not model prose, creates a server-issued command authorization token bound to one operation, principal, tool, expiry, and canonical parameter digest; the service resolves its hidden operation ID/key. When a response is lost after send, the adapter performs only read-only `LookupOperation` with that same stored identity and digest. It must not submit an HTTPS mutation or create a new key. Only a ledger result proving the primary request was not accepted permits retrying the same MCP request. An operator may deliberately change the configuration to API-only after reconciliation, but submits the exact stored identity to the same dispatcher. While uncertain, the visible state is `provider_outcome_unknown` or `reconciling`, never success.

## Acceptance cases

`FL-01` proves a generation job ends at review-ready and H05 creates a separate export job. `FL-02` proves human reject/request-changes outcomes. `FL-03` proves pre-lease stale, budget, and cancellation outcomes. `AR-01` proves exact-hash H05 approval and `AR-02` proves stale download denial. `CB-01`, `CB-02`, and `CA-01` prove callback, reconciliation, and cancel races. `DB-01` proves state plus outbox atomicity and consumer deduplication. `TR-01` through `TR-04` prove common operation identity, read fallback, denied fallback classes, and mutation reconciliation.
