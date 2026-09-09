# Copilot placement

## Proposed placement for edition 2

Edition 2's confirmed design target is the Standard Copilot harness in Teams. P00 is the parent router. P01 source review, P02 case profile, P03 witness planner, P04 packet writer, P05 script writer, P06 independent evaluator, and P07 truthful rehearsal are proposed child/connected-worker roles. Their output is a reference and safe status, never conversational proof that work is complete. Public technique material and the user guide may be knowledge content; bulk case folders and coach-only material are not knowledge attachments. Edition 1 is prompt-only MVP; edition 3 is the separate manual full-prompt workflow pack and does not use these tools.

This placement is design-compatible only. Tenant import, Teams installation, identity configuration, tool invocation, MCP authentication, published-channel behavior, callback behavior, and harness labels have not been tested. Tenant details remain pending.

## Tools and boundaries

In full MCP-primary mode, the tool adapter is Streamable HTTP MCP. A Swagger 2 custom-connector fallback/alternative is proposed with `x-ms-agentic-protocol: mcp-streamable-1.0` and a POST `/mcp` operation. The configuration is not evidence of a created connector or working channel. API-only mode calls the equivalent authenticated service operations without claiming a Copilot tool installation.

The eight agent operations are StartJob, GetJob, CancelJob, LookupOperation, ReadGraph, ReadArtifact, SaveCandidate and RequestEvaluation. RecordHumanDecision is a ninth canonical API operation available only to the human portal; it is absent from both agent connectors. The client receives compact references and state only. It cannot submit arbitrary query language, filesystem paths, principal identities, bulk source material, generic state completion, or human-review authority.

| Role or flow | Allowed operation | Prohibited authority |
|---|---|---|
| P00 | safe routing, GetJob, LookupOperation, approved reads | candidate writing, approval, quality/state mutation |
| P01/P02 | assigned SaveCandidate | witness artifacts, source/review mutation |
| P03 | permitted ReadGraph and assigned candidate | broad case traversal or export |
| P04 | ReadGraph/ReadArtifact within grant; packet SaveCandidate | scripts, grants, quality decision |
| P05 | permitted reads; script/chapter SaveCandidate | packets, grants, quality decision |
| P06 | Internal service-assigned worker reads frozen inputs and returns Evaluation for service validation/persistence | self-assignment, recursive evaluation requests, candidate/source/review mutation |
| H01-H07 UIs | RecordHumanDecision within screen authority | generic job completion |

The trusted Topic adapter invokes StartJob, CancelJob and RequestEvaluation after the configured user action/authorization. P00 may request that route but cannot fabricate command tokens or decide state. The worker adapter invokes P06 with its issued assignment; RequestEvaluation is the enqueue boundary, not a tool P06 calls to evaluate itself.

## Topics and conditions

Create explicit topics for Start intake, Review sources, Review witness, Prepare packet, Prepare script, Check job, Cancel job, and Review/export. These route to F01-F09; F10 is a separate custodial path. Before and after a tool call, the Topic checks only the server response for authorization, current input digest, expected state version, budget, and cancellation. Missing security input fails closed. A Topic should never decide that a long-running job completed because a child wrote prose.

Long work is handled in S04. Topic-led bounded child calls are resumable when each assigned candidate is persisted before the next interaction. An unattended generator path requires a separately approved backend adapter; no undocumented background child-agent invocation is assumed. Asynchronous callback behavior, if later enabled, is notification only and never replaces GetJob or LookupOperation.

## Transport behavior in Copilot

The MCP client is primary. A trusted Topic adapter, not the model, injects the server-issued command authorization token and retains the resulting operation identity. If MCP has no semantic response for an allowlisted read, the adapter may call the HTTPS equivalent with identical operation/snapshot/principal bindings. It must not switch transports automatically after authorization, validation, conflict, budget, cancellation, or quality results. For a mutation with lost response, P00 reports the pending/reconciling state and the adapter calls LookupOperation; it must not call the HTTPS mutation or make up another idempotency key. An operator-directed API-only configuration may retry only after reconciliation and with the same retained operation identity. The injection path is unimplemented and a tenant go-live blocker.

## Placement acceptance cases

`CP-01` proves child role capabilities are isolated; `CP-02` proves an unbound child output cannot set job success; `CP-03` proves MCP and API requests map to the same operation ledger; `CP-04` proves read fallback retains digest/snapshot scope; `CP-05` proves lost mutation response follows lookup rather than fallback mutation; and `CP-06` proves a long script remains reference-based rather than being returned in one tool response.
