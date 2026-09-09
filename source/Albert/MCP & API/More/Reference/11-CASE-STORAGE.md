# Per-case storage and context recovery

## Proposed connected Azure persistence

The reference deployment uses Azure Blob Storage for immutable originals, page renders, extraction derivatives and artifact bodies; Azure SQL Database for case-scoped sources/chunks, graph nodes/edges, attributed assertions, conflicts, grants, versions, jobs, attempts, evaluations, human decisions and outbox rows. This is a proposed adapter choice, not a deployed service or evidence that existing Albert already uses these products. WP02/WP04/WP09 implement and test adapters before migration. The logical contracts remain provider-neutral.

Use composite `(case_id, record_id, revision)` keys and same-case foreign keys for graph edges, chunks and citations. Store current pointers separately from immutable versions. Enforce role and witness-view access before traversal, including counts/summaries. A relational adjacency model supports this bounded pilot without a separate graph service. Chunk text can live in versioned rows with its exact original-span binding; large content is referenced to immutable Blob objects. Graph/conflict tables preserve allegations and competing accounts, never a single unqualified truth field.

Candidate persistence commits metadata and an artifact-body reference only after verified body storage; publish visibility through a transaction plus outbox. Garbage collection cannot remove an object referenced by current or retained audit state. Backups cover BOTH objects and relational dependencies. A restore must reconcile current pointers, grants, pending jobs and charge receipts before resumed execution.

General reference knowledge (approved technique/rule guides) is separate from case evidence. Search/vector indexes, if added after measurement, are derived caches, not the authoritative case graph. A missing index cannot erase source history. `ReadGraph` resolves current case/witness scope before returning grounded spans for the podcast writer/checker.

Microsoft's [document-processing architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/automate-document-processing-azure-ai-document-intelligence) illustrates separating source/artifact object storage from processing records. The Azure SQL choice here is an Albert pilot design decision, not Microsoft's prescribed database for that reference architecture.


```text
CASE-{case-id}/
  CASE-00-manifest.md
  originals/                         unmodified source files
  evidence/                          CASE-01 through CASE-05, versioned copies
  witnesses/{witness-id}/             CASE-06 profile and scoped excerpts
  packet/                            CASE-PACKET-A0.md, A1.md, A2.md and E0/E1/E2
  podcast/                           CASE-PODCAST-PC01-A0.md ... PC08-A0.md
                                     assembled CASE-PODCAST-A0.md, A1/A2 and E0/E1/E2
  reviews/                           CASE-07 / CASE-08 logs, CASE-09 final review
  gold-reference/                    owner-approved reference and rights record, if supplied
  delivery/                          approved exact packet, script, citation/production notes
```

## Optional persistent knowledge without a custom integration

Copilot Studio can retain manually uploaded knowledge files in Dataverse. This is retrieval storage, not automatic write-back of generated drafts. See [Microsoft file upload](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload).

1. Manually save and review the case snapshot. For a maker-controlled pilot, use a dedicated case agent with only material every intended user of that agent may see.
2. Open Knowledge → Add knowledge, upload the selected current files, give each its case/version/scope description, and wait for readiness. Keep originals locally or in the approved custody store.
3. For a changed file, manually replace/update the selected knowledge entry using the tenant's supported UI and confirm the active version; do not leave old/current versions indistinguishable.
4. Test a fresh conversation with a known fact and its exact source passage. If the needed span is missing, stale or uncertain, paste that reviewed span explicitly. Do not assume the whole file is in context or every conflict was retrieved.
5. Preserve authoritative drafts and review records outside chat. Knowledge retrieval may help reload context; it does not approve an artifact, count revisions or enforce witness knowledge limits.

SharePoint is optional. It may be an organization-managed document source when approved, but a SharePoint folder, Microsoft Graph and an Albert litigation knowledge graph are different things. Native file permissions do not by themselves encode which facts a role-play witness is allowed to know. Do not attach a whole multi-case or coach-only library to a shared witness-facing agent. Keep the prompt-only pilot under an authorized operator with deliberately scoped inputs; use the connected service for enforced per-witness access.
