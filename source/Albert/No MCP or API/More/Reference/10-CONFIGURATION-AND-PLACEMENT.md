# Configuration and exact placement

Use the diagram's node ID to find the same ID in `workflow-map.json` and this table. The filename is the exact prompt source. Keep that ID when naming the Copilot component: `Albert PROMPT-FULL {ID} — {role}`. Do not rename only the diagram or only the prompt. `M` identifies MVP stages, `C` identifies full prompt-only stages, and `P` identifies connected agent roles. In the connected edition `F` is a service workflow, `H` is a human review screen, `S` is a backend service, and `T` is a tool group. These namespaces describe different components; F06 and P06 are not interchangeable.

`configuration.example.json` is a worksheet with deliberately unset tenant values. It is NOT imported into Copilot Studio and does not activate anything. `workflow-map.json` is a machine-readable placement index, also not an importable solution. The setup document tells the maker what to paste; only the labeled instruction section goes into Instructions. Markdown guide headings, configuration records and diagrams are documentation, not case knowledge.

## Component map

| ID | Exact prompt file | Copilot placement | Trigger / gate | Required input | Produced output |
|---|---|---|---|---|---|
| C00 | [00-ALL-IN-ONE-PROMPT.md](00-ALL-IN-ONE-PROMPT.md) | Parent Instructions | route only; paste stage procedure next | case manifest + next stage | current stage and checkpoint |
| C01 | [C01-intake.md](C01-intake.md) | Stage message or Intake Instructions | H01 rights/scope | CASE-00-manifest.md + original source descriptions | CASE-00-manifest.md |
| C02 | [C02-source-exhibit-review.md](C02-source-exhibit-review.md) | Stage message or Source Review Instructions | H02 source/span review | source originals + exact transcribed passages | CASE-01-source-register.csv; CASE-02-chunks.csv |
| C03 | [C03-evidence-ledger.md](C03-evidence-ledger.md) | Stage message or Evidence Ledger Instructions | review evidence relationships | reviewed CASE-02-chunks.csv | CASE-03-graph-nodes.csv; CASE-04-graph-edges.csv; CASE-05-conflicts.csv |
| C04 | [C04-case-witness-profile.md](C04-case-witness-profile.md) | Stage message or Profile Instructions | H03 scope and knowledge limits | current ledgers + rules + exact relevant spans | CASE-06-witness-profile.md |
| C05 | [C05-full-witness-packet.md](C05-full-witness-packet.md) | Stage message or Packet Author Instructions | packet baseline | approved profile + scoped ledgers + exact spans | CASE-PACKET-A{n}.md |
| C06 | [C06-independent-review.md](C06-independent-review.md) | Fresh reviewer conversation or human review | H04 evidence and score review | one exact packet/script + sources + rubric + prior findings | CASE-{PACKET-or-PODCAST}-E{n}.md |
| C07 | [C07-material-revision.md](C07-material-revision.md) | Stage message or Revision Instructions | apply substantive findings | frozen A{n} + E{n} + approved findings + source spans | CASE-{PACKET-or-PODCAST}-A{n+1}.md; review log |
| C08 | [C08-full-chaptered-script.md](C08-full-chaptered-script.md) | Stage message or Script Author Instructions | podcast chapters + independent review loop | current reviewed packet + ledgers + exact spans + chapter plan | CASE-PODCAST-PC{01..08}-A{n}.md; CASE-PODCAST-A{n}.md |
| C09 | [C09-pair-consistency-final-package.md](C09-pair-consistency-final-package.md) | Stage message or Consistency Instructions | H05 exact text + H07 manual package | current exact packet/script + E{n} + ledgers | CASE-09-final-review.md; CASE-FINAL-PACKAGE-INDEX.md |
| C10 | [C10-truthful-rehearsal.md](C10-truthful-rehearsal.md) | Stage message or Rehearsal Instructions | optional truthful practice | approved materials + permitted practice question | CASE-PRACTICE-NOTES.md |

## Configuration register

| ID | Setting | Required value / owner | Where configured | Proof before use |
|---|---|---|---|---|
| CFG01 | Harness/channel | Standard + Teams, confirmed design target | Agent creation/settings and publishing | Actual test-chat and Teams test, not yet run |
| CFG02 | Tenant/environment/region | Tenant admin supplies exact IDs and approved region | Microsoft Entra / Power Platform environment | Record selected directory and environment |
| CFG03 | Models | GPT-5.5 as user-reported simplest default; Sonnet 4.6 optional author | Primary agent model selector; separate agent for separately selectable checker | Record exact selector label, release stage and successful pilot |
| CFG04 | Inputs/authority | Approved synthetic sources initially; rights, cloud processing and budget reviewed before real sources | Operator intake / H01 | Exact source, permitted audience and processor decision |
| CFG05 | MCP/API endpoint | Connected edition only, deployed HTTPS host | Tool connection / custom connector | Discover/invoke/denial tests on release revision |
| CFG06 | OAuth/connection | Connected edition only, issuer/audience/scopes and user mapping | Managed connection + backend verifier | Two-principal tenant test; no maker privilege leak |
| CFG07 | Persistent service | Connected edition only, approved storage and job workers | Backend deployment settings | Restore, idempotency, cancellation and stale-access tests |
| CFG08 | Trusted envelope | Connected edition only, non-model ID/token persistence | Trusted Topic/portal integration adapter | Lost-response test cannot create fresh logical work |
| CFG09 | Manual checkpoints | Prompt editions, local case folder; optional manually uploaded knowledge snapshot | Operator save/reload; Knowledge → Add knowledge if approved | Start fresh chat and recover exact current source and artifact versions |
| CFG10 | SharePoint | Optional, disabled by default | Approved document-source adapter or native Knowledge configuration | Audience/permissions and freshness tests if enabled |

## How configuration is handed to implementers

The package separates stable prompt/workflow definitions from environment-specific values, includes an explicit dependency/placement table, records design decisions, and binds test evidence to the exact release revision. Store tenant values in a private deployment worksheet; commit only blank examples. Credentials live in managed connections or the approved secret store.

For a connected Power Platform solution, create solution-owned environment variables for nonsecret URLs/IDs and connection references for authenticated connections; export the actual tenant solution after implementation. Microsoft's [environment-variable guidance](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables) and [deployment-settings guidance](https://learn.microsoft.com/en-us/power-platform/alm/conn-ref-env-variables-build-tools) document this separation. Prompt-only editions do not require solution automation, connection references or an external server.

Keep development, test and production values separate. Before a promotion record the prompt/config/connector/service versions, review the configuration diff, run the relevant acceptance tests, name the operator and retain rollback instructions. No environment exists because a worksheet has a value.

## Setup order

1. Read START HERE, the edition's setup guide and D01 diagram; choose this edition deliberately.
2. Fill CFG01–CFG04 and the edition's required settings. Leave unused settings explicitly not applicable.
3. Paste the exact instruction files from the table; bind the listed inputs and inspect outputs after each stage.
4. Use the source/save/reload method in `11-CASE-STORAGE.md`. Do not let old revisions or another witness's notes enter the current context.
5. Run the synthetic walkthrough and acceptance checklist. Publish to Teams only after the authorized pilot's checks pass.
6. Keep the completed configuration and run receipt with the case/release. Store reviewed artifacts independently of chat history.
