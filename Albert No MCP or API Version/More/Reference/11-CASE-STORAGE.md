# Per-case storage and context recovery

## Full prompt-only case workspace

The operator creates one local folder per case using the layout below and saves every reviewed stage output there. The supplied CASE files are blank templates. These CSV files represent the knowledge graph as explicit node/edge/conflict tables; they are ordinary reviewed documents, not a running graph database. No separate database, SharePoint, custom API or MCP setup is required.

The agent proposes file contents; it does not silently write the operator's disk. The operator copies/saves the content using the exact filename, reopens it and checks it before updating the current manifest. At the next stage or in a new conversation, paste the current manifest, relevant ledger rows AND exact source passages. Large cases require bounded source-by-source processing and a human coverage check; retrieval or a summary alone cannot certify complete evidence coverage.

C02 proposes source/chunk rows; C03 proposes graph/conflict rows; C04 produces the witness profile; C05 creates the packet; C06/C07 review and revise each artifact separately; C08 produces podcast chapters; C09 verifies the pair and final package. Follow the precise input/output map in `10-CONFIGURATION-AND-PLACEMENT.md`. Never overwrite A0/A1/A2 or old source revisions; save a new version and update the manifest after review. A changed source or packet requires reviewing affected graph, conflicts, profile and podcast passages again.


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
