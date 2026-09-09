# Reuse and decisions

## Reuse boundary

Existing Albert components are reuse candidates only. This implementation pack does not identify, change, or certify a source file, service, or repository component. Before reuse, an owner must map the candidate's input/output contract, authorization behavior, source and revision semantics, error behavior, dependency invalidation, test evidence, license, and operating owner. A compatibility adapter and synthetic contract tests are required where the candidate differs from the proposed record vocabulary.

Likely reuse categories are immutable source storage, layout/OCR adapters, normalization/chunking, typed graph/query semantics, artifact rendering, and deterministic validators. New code is expected for the authenticated dispatcher, grants, execution assignments, job/idempotency ledger, lease/cancellation/reconciliation logic, outbox, artifact approval ledger, dependency invalidation, cross-artifact gate, transport adapters, and review UIs. This classification is a design decision, not an implementation inventory.

## Decision register

| Decision | Proposed direction | Owner decision still needed |
|---|---|---|
| Core authority | S03-S05 service controls remain authoritative; Copilot routes and presents status | persistence and policy engine choices |
| Agent execution | Topic-led bounded child calls or separately approved generator adapter; no assumed undocumented background-child API | which mode is authorized for unattended long work |
| Transport | one canonical dispatcher, MCP primary for Copilot, API-only equivalence for other clients | tenant authentication and connector/adapter configuration |
| Data location | local, hybrid, and cloud are distinct approved modes | tenant, region, processor, retention, and egress decision |
| Downloads | audience-scoped, expiring service links after H05 | storage/signing implementation |
| Human study | disabled by default and separately custodied | protocol, consent, custodian, and question custody |
| Packet quality | cannot converge until category membership is pinned | category taxonomy and map approval |

## Required compatibility decisions

The primary operations are StartJob, GetJob, CancelJob, LookupOperation, ReadGraph, ReadArtifact, SaveCandidate, RequestEvaluation, and RecordHumanDecision. Each must have an operation contract independent of both MCP and HTTPS. OCR, chunking, graph extraction, generation, evaluation, and export are backend dispatcher work; a Copilot agent does not become their system of record.

StartJob must create the server job ID atomically with its operation ledger record. GetJob and LookupOperation are safe reads. CancelJob has expected state version and changes cancellation generation only when an active attempt exists. SaveCandidate can create immutable assigned candidate kinds only. RequestEvaluation creates an independent checker assignment and frozen evaluation input. RecordHumanDecision is limited to the screen-specific authority and can never be a generic workflow completion action.

## Reuse acceptance criteria

`RE-01` proves source byte/revision compatibility; `RE-02` proves original-page and normalized-anchor behavior; `RE-03` proves typed graph queries cannot traverse unauthorized intermediate records; `RE-04` proves a reused generator adapter obeys attempt, grant, and cancellation checks; `RE-05` proves any reused renderer preserves exact approved artifact bindings. A failed compatibility check retains the candidate as unapproved and routes the capability to new, separately reviewed implementation.

## Open decisions

Owner resolution is required for the source inventory, component owners, licensing, database, policy implementation, identity provider mapping, tenant region/DLP, provider selection, export formats, retention/deletion, and handoff ownership. The reviewed record vocabulary is normative for adapters; altering it requires a versioned compatibility plan. These documents do not make those decisions or authorize a production integration.
