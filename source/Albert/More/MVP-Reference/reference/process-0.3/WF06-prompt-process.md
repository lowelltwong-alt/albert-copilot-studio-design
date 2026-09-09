# WF06 · Run the shared prompt-only improvement process

Process core0.3.0 candidate. This adds explicit handoff/payoff/check records to the unchanged P06/P01/P03/A02/A01 workflow. It is a local development revision pending the bound test report, not a tenant deployment or universal qualification. Ordinary production retains WF05's one bounded repair. A separately declared development study may use P09's conditional second loop; that exception does not silently change ordinary case operation.

Use one `CASE-WITNESS` prefix and immutable `REV` per assembly. The following names are output conventions; input prompt files use their P/A/T IDs. Save/open every output before handing it to the next role.

| Step / core node | Exact instruction | Required handoff → saved result |
|---|---|---|
| W01–W04 SOURCE | Existing intake; P01 | Approved raw Markdown, distinct semantic exhibit boundaries, provenance IDs and conflict endpoints → source index and graph/chunk tables. No OCR service required here. |
| W05 WITNESS / CLAIMS | P07 + P06 | Source index + existing permission authority → `CASE-WITNESS-W05-HANDOFF-REV.md`, permitted view and separate author ledger. Resolve permission unit explicitly. |
| W08 PLAN | P06 + T06 | Permitted source + method KB + reference functions → `CASE-WITNESS-W08-PLAN-REV.md` and draft `CASE-WITNESS-KC10-REV.md`. Plan supported pressure payoffs, both host roles, retrieval and earned duration. |
| W06 PLAN_REVIEW | Independent P01 + P07 | Complete plan/card/view + actual raw spans → `CASE-WITNESS-W06-PLAN-REV.md`. Resolve material premises before full draft; no old-case answers in a from-scratch run. |
| W08 DRAFT | P06 + T06 | Checked plan, permitted sources and function-only style fingerprint → `CASE-WITNESS-W08-SCRIPT-REV.md`, `...W08-CLAIMS-REV.md`, final `...KC10-REV.md`, `...W05-AUTHOR-REV.md`, as-built T06. |
| W06 SOURCE_REVIEW / CRAFT_REVIEW | Separate independent P01 and A02 + T06 | Complete identical frozen assembly, hash-bound `CASE-WITNESS-T06-REV.md` and required-input read receipts → separate `...W06-SOURCE-REV.md` and `...W06-CRAFT-REV.md`. Critic hypotheses need raw verification; neither reviewer authors its candidate. |
| W07 QUALITY_GATE / REPAIR | P09; if needed exact imported P02 + P06 + P08 | Verified findings and receipt recording P02 revision/digest specified in P08, P06, P08, source/view and prior assembly → accept, hold, or at most five craft actions plus evidence repairs. Save a new complete revision and `...CHANGE-RECEIPT-REV.md`; retain prior bytes. Missing required prompt holds repair. No blind shortening. |
| W06 FINAL_REVIEW | Fresh independent P03 and A02 | Previous/current exact assemblies + accepted findings + sources → new full checks. Distinguish fixed, preserved, not fixed and not assessed. Stop unresolved failures. |
| W09 EXPORT | P09 operator | Accepted current assembly → `...W09-REV-SPEAKERS.txt`, `...W09-REV-SPOKEN.txt`, `...W09-REV-TIMING.md`, KC card and source map. All instructions/citations nonspoken; words and pauses measured separately. Reopen and verify. |
| A01_AUDIT / LEDGER | Triggered A01 + P05 | Instructions, actual outputs, findings and runtime receipts → case-local audit and a privacy-safe generic candidate. No automatic prompt edit or model promotion. |
| DECISION / REVISION | Authorized owner; P09 | Exact proposal, checks and limits → a new shared revision only after its declared test. Freeze before fresh authors; transfer after fresh tests. Late observations remain candidates until another test. |

Minimal mesh: one planner/writer, independent evidence reviewer, independent craft reviewer, an editor only when needed, fresh full check. A01 is triggered by a real disagreement/failure, with one bounded evaluator challenge. No recursive reviewers. With one chat tool, the operator performs these handoffs sequentially in distinct chats where possible; record weaker independence honestly. No API or MCP is required to perform any prompt role.

NotebookLlama's public source-preparation→writing→conversational-rewrite pattern informs staging. We use verified optional rewriting because an additional pass can lose depth or introduce error. This is not NotebookLM's private prompt, copied model code, audio implementation or a promise of the same sound. The reference fingerprint supplies observed functions, never case facts or copied distinctive language.

## Same process, three storage/execution adapters

| Profile | Configuration | Durable state |
|---|---|---|
| MVP prompt-only | Authorized model chat; manual prompt/file handoffs; selected source/view; two teaching hosts; duration/mode; current model capability and exact prompt revision recorded. | Ordinary authorized case files: sources, author-only, permitted, drafts, reviews, exports. Markdown IDs/tables form the small graph. Save/open manually; context retention is not storage. |
| Full manual without API/MCP | Same prompts and IDs plus full case ledger, conflicts/chunks and human-controlled multi-witness joins. | Owner-managed files or approved SharePoint library with explicit access, version and retention configuration. SharePoint is optional, not assumed. |
| Full connected | Same artifacts and gates through separately configured/validated retrieval and persistence bindings. Record tenant/environment/authentication, allowed effects and fallback owner before activation. | Approved case store and receipts. Generic asset MCP retrieves exact prompt assets; it does not by itself store the case graph, execute models or spawn agents. Tenant/backend tests remain separately required. |

Changing a provider/model/runtime, source/view, tool permission, prompt or adapter invalidates affected evidence. Keep the old revision for rollback. Capability roles are stable; exact model names live in runtime receipts and must be checked in the actual environment. This local test does not certify Copilot Studio model availability or deployment.

## Keep every diagram synchronized

This is a post-local-test integration gate, not a requirement for running prompts in a chat. When supplied, the versioned shared core JSON is the single workflow definition. An integration receipt must name the exact core JSON, generator, renderer, commands, tests and resulting preview hashes. Prompt bindings and node/edge changes are reviewed by exact identity/digest, then regenerated into the common Mermaid and all three profile views. Do not hand-edit a generated diagram. Run the named generator write/check and affected tests, render all four sources and bind previews to the core digest. Without those assets, diagram integration remains pending while local prompt-only testing may proceed. The included CI installation is a template until installed and required in the target repository. Manual maintenance is explicit; no live watcher is implied.
