# Exact prompt placement

This is the operator map. RUN IDs select tasks; P/A/T IDs name inherited instruction assets; W/PC/KC IDs identify saved work and episode sections. Permanent role Instructions stay short. The RUN files include the complete selected core instructions, so you need not hunt down dependencies while running a stage.

| Stage | Agent | Paste in Test agent chat | Required packet | Save output suffixes |
|---|---|---|---|---|
| RUN-01 | ANALYST | [prompts/RUN-01-GRAPH.md](prompts/RUN-01-GRAPH.md) | SOURCE, operator scope/permissions, case/witness/use, GRAPH template, state packet | W05-GRAPH, W05-VIEW, W05-AUTHOR, STATE |
| RUN-02 | WRITER | [prompts/RUN-02-PLAN.md](prompts/RUN-02-PLAN.md) | owner-reviewed W05-VIEW and permitted source spans, GRAPH permitted projection, method source, style-function brief, mode/duration, PACKET | W08-PLAN, draft KC10, planned T06 |
| RUN-03 | EVIDENCE | [prompts/RUN-03-PLAN-GATE.md](prompts/RUN-03-PLAN-GATE.md) | complete W08-PLAN/draft KC10/planned T06, W05-GRAPH/VIEW, actual raw spans and owner scope; for graph-first review the plan fields may be explicitly not_started | W06-PLAN (graph/view result and, when present, plan result) |
| RUN-04 | WRITER | [prompts/RUN-04-WRITE.md](prompts/RUN-04-WRITE.md) | complete reviewed PLAN, W06-PLAN, current VIEW/permitted raw spans, method/style brief, planned T06, operator acceptance of plan, chapter request | W08-SCRIPT, W08-CLAIMS, KC10, as-built T06; chapter files first if needed |
| RUN-05 | EVIDENCE | [prompts/RUN-05-SOURCE-REVIEW.md](prompts/RUN-05-SOURCE-REVIEW.md) | full frozen SCRIPT, CLAIMS, KC10, as-built T06, PLAN, current VIEW/GRAPH, actual permitted raw passages and required internal source access, STATE | W06-SOURCE |
| RUN-06 | CONVERSATION | [prompts/RUN-06-CRAFT-REVIEW.md](prompts/RUN-06-CRAFT-REVIEW.md) | same full frozen SCRIPT, CLAIMS, KC10, as-built T06, PLAN and permitted VIEW/source passages; style-function brief; original benchmark only if authorized and provided | W06-CRAFT |
| RUN-07 | EVIDENCE | [prompts/RUN-07-JOIN.md](prompts/RUN-07-JOIN.md) | complete current assembly identities, both current reviews, T06, STATE and operator read confirmations; any unresolved disagreement | W07-DECISION (recommendation for human) |
| RUN-08 | WRITER | [prompts/RUN-08-REPAIR.md](prompts/RUN-08-REPAIR.md) | exact complete before assembly, current raw/view, verified findings and join recommendation, prior source/craft reports, unchanged chapters and current STATE | new-revision full SCRIPT, CLAIMS, KC10, T06, CHANGE-RECEIPT |
| RUN-09 | EVIDENCE | [prompts/RUN-09-REPAIR-EVIDENCE.md](prompts/RUN-09-REPAIR-EVIDENCE.md) | complete before and after assemblies, verified original findings, CHANGE-RECEIPT, current raw/view and exact STATE identities | W06-SOURCE on the new revision, per-finding verification |
| RUN-10 | WRITER | [prompts/RUN-10-EXPORT.md](prompts/RUN-10-EXPORT.md) | human acceptance of exact manual_reviewed_candidate or actual hash-verified assembly, current SCRIPT/CLAIMS/KC10/T06/STATE/decision, intended internal audience | W09-SPEAKERS.txt, W09-SPOKEN.txt, W09-TIMING.md, copy of permitted KC10/CLAIMS |
| RUN-11 | NON_AUTHOR_REVIEWER | [prompts/RUN-11-AUDIT.md](prompts/RUN-11-AUDIT.md) | specific suspected worker/reviewer failure, exact instructions and inputs, actual output and reviews, source evidence within authorized scope, experiment record | A01-AUDIT, generic lesson candidate, proposed test or no-change |

## Loading a long prompt

Try the complete stage file first. If the UI rejects it, use the corresponding ordered files in paste/. Send each part separately; expect acknowledgment only. Then provide the named PACKET contents in numbered parts and send BEGIN RUN. If a role cannot accurately identify every part/source needed, split the task and hold the incomplete check. Part acknowledgments alone do not prove complete reading.

| RUN | Ordered smaller paste files |
|---|---|
| RUN-01 | [paste/RUN-01-part-01.txt](paste/RUN-01-part-01.txt), [paste/RUN-01-part-02.txt](paste/RUN-01-part-02.txt) |
| RUN-02 | [paste/RUN-02-part-01.txt](paste/RUN-02-part-01.txt), [paste/RUN-02-part-02.txt](paste/RUN-02-part-02.txt), [paste/RUN-02-part-03.txt](paste/RUN-02-part-03.txt) |
| RUN-03 | [paste/RUN-03-part-01.txt](paste/RUN-03-part-01.txt), [paste/RUN-03-part-02.txt](paste/RUN-03-part-02.txt) |
| RUN-04 | [paste/RUN-04-part-01.txt](paste/RUN-04-part-01.txt), [paste/RUN-04-part-02.txt](paste/RUN-04-part-02.txt), [paste/RUN-04-part-03.txt](paste/RUN-04-part-03.txt) |
| RUN-05 | [paste/RUN-05-part-01.txt](paste/RUN-05-part-01.txt), [paste/RUN-05-part-02.txt](paste/RUN-05-part-02.txt) |
| RUN-06 | [paste/RUN-06-part-01.txt](paste/RUN-06-part-01.txt), [paste/RUN-06-part-02.txt](paste/RUN-06-part-02.txt), [paste/RUN-06-part-03.txt](paste/RUN-06-part-03.txt) |
| RUN-07 | [paste/RUN-07-part-01.txt](paste/RUN-07-part-01.txt), [paste/RUN-07-part-02.txt](paste/RUN-07-part-02.txt) |
| RUN-08 | [paste/RUN-08-part-01.txt](paste/RUN-08-part-01.txt), [paste/RUN-08-part-02.txt](paste/RUN-08-part-02.txt), [paste/RUN-08-part-03.txt](paste/RUN-08-part-03.txt) |
| RUN-09 | [paste/RUN-09-part-01.txt](paste/RUN-09-part-01.txt), [paste/RUN-09-part-02.txt](paste/RUN-09-part-02.txt) |
| RUN-10 | [paste/RUN-10-part-01.txt](paste/RUN-10-part-01.txt), [paste/RUN-10-part-02.txt](paste/RUN-10-part-02.txt) |
| RUN-11 | [paste/RUN-11-part-01.txt](paste/RUN-11-part-01.txt), [paste/RUN-11-part-02.txt](paste/RUN-11-part-02.txt), [paste/RUN-11-part-03.txt](paste/RUN-11-part-03.txt) |

## Canonical mapping and updates

workflow.json owns this starter projection. Its core_nodes values map to the retained Core0.2 node identities; it does not modify that frozen core. Generated diagrams and this placement table must reflect the same manifest. Run the optional maintenance checker after changes; no persistent watcher is installed. A changed prompt or adapter is a new tested candidate, not a silent rewrite of a historical result.
