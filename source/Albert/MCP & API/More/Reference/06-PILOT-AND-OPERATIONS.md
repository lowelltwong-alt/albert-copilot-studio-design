# Pilot and operations

## Pilot boundary

This pilot is proposed. It has not imported a tenant solution, connected authentication, invoked a connector, published a channel, or called an OCR/generation provider. Start with a synthetic premises fixture containing a two-page exhibit with an ambiguous continuation, an attributed contrary statement, and one human-played witness. It is a wiring and custody demonstration, not a legal conclusion, learning study, or qualification claim.

## Gates before each expansion

| Gate | Required evidence | Stop condition |
|---|---|---|
| Source and code license | owner-confirmed rights for source, reusable component, and test fixture | unclear reuse rights or a restriction incompatible with the pilot |
| Tenant and channel | environment, region, DLP, authentication, Standard harness, Teams installation, tool invocation, card/deep-link, and published-channel feature probes | missing approved tenant/Teams configuration or a failed channel control |
| Provider and spend | approved processor, data classes, operations, retention, budget, and region | expired/revoked approval or unavailable budget |
| Data movement | H01 exact-scope decision and egress policy | unapproved content class or processor |
| Service controls | schema/adapters, transaction behavior, grants, state, and audit checks | any case, grant, callback, or stale-artifact control failure |
| Pilot fixture | synthetic input, expected discriminating results, and no production case material | fixture cannot demonstrate the required failure mode |

No gate is satisfied by a prompt claim or a successful chat response.

## Mode selection

Edition 1, prompt-only MVP, is a separate demonstration: it uses only Copilot instructions and synthetic static content. It contains no external API, MCP server, custom connector, backend, job state, source retrieval, or candidate persistence. It must label outputs as non-authoritative examples.

Edition 2, full connected, has MCP-primary and API-only profiles against the same dispatcher. The confirmed MCP-primary target uses a Standard Copilot harness in Teams and a Streamable HTTP MCP adapter. Teams import, authentication, trusted Topic-adapter command-token injection, invocation, and published-channel tests are pending; no connected profile is represented as deployed by these documents.

Edition 3, full prompt workflow, is a separate manual-completion pack. It can guide approved bounded text through source/graph review, witness profile, packet, script, independent human review, revision, and final package without API, MCP, custom connector, or backend. SharePoint is optional as a human-selected location in all three editions; it is never broad case-folder Knowledge.

## Operational controls

The dispatcher starts immutable attempts from a validated job and lease. It records provider request fingerprints and usage before retrying, requires a live lease fence and current cancellation generation before publishing, and writes state plus outbox in one transaction. Operational telemetry is content-minimal. Sensitive prompts, answers, and detailed findings remain case-scoped evidence, not global monitoring records.

Retries use bounded backoff and jitter only for classified retryable service or transport failures. A provider timeout, session reset after send, or missing callback is `provider_outcome_unknown`: the attempt enters reconciliation, the provider fingerprint is checked, and no duplicate charged request is sent until a reconciled receipt permits it. Cancellation is not deletion or retention management.

## Transport operating procedure

MCP is primary for Copilot. A response-free MCP failure may use HTTPS only for an allowlisted safe read: GetJob, LookupOperation, ReadGraph, ReadArtifact, or bounded source span retrieval. The read repeats the operation ID, verified principal scope, snapshot/cursor, and request digest. A returned policy or snapshot mismatch is rejected.

Automatic HTTPS fallback is prohibited for 401/403, semantic 404, validation/422, revision conflict, rate or budget rejection, quality denial, cancellation, and any semantic server result. StartJob, CancelJob, SaveCandidate, RequestEvaluation, and RecordHumanDecision never fall back automatically as mutations. On a lost mutation response, LookupOperation reconciles the same operation ID and idempotency key; only proof that the original was never accepted permits retry on the primary path. A deliberate move to API-only after reconciliation retains the same operation identity and dispatcher.

## Pilot runs

1. Validate the complete contract vocabulary and new transport request schemas against synthetic records.
2. Run intake through H01/H02 and prove ambiguous continuation blocks chunking.
3. Run graph/profile/H03 and prove a witness cannot retrieve a counsel-only intermediate node or hidden count.
4. Run separate A0, A1, and A2 packet and script cycles with independent evaluation; packet remains diagnostic-only until category membership is resolved.
5. Inject duplicate request, lost response, timed-out provider, callback replay, cancel race, expired grant, and dependency change.
6. Run F08 only on current exact artifacts, then have H05 create a separate export job. No external delivery is required for the pilot.

## Operations acceptance evidence

Record the fixture ID, contract/policy/grant/artifact hashes, safe test outcome, and timestamp in case-scoped receipts. Do not record source text or prompts in a general operations log. Required evidence includes `OP-01` idempotent start, `OP-02` unknown-outcome reconciliation, `OP-03` late callback quarantine, `OP-04` stale dependency download denial, `OP-05` fallback read digest match, and `OP-06` forbidden mutation fallback.

## Unresolved operational decisions

The owner must choose the approved tenant/environment/channel, authentication and authorization implementation, persistence technology, provider adapter, retention/restore process, budget enforcement source, and final incident/support ownership. Packet category membership remains unresolved and blocks packet convergence qualification. No deployment or production readiness conclusion follows from this pilot plan.
