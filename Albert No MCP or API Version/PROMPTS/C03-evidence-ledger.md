# C03 — Evidence ledger and graph-as-text

Input: H02-reviewed spans and operator ledger.

Create rows for SOURCE, INFERENCE, UNKNOWN and METHOD. Represent graph-as-text as `NODE`, `EDGE`, `ASSERTION`, `CONFLICT`, `GAP`, each linked to exact source IDs and attribution. Preserve competing accounts and temporal uncertainty. Ask for an actual span whenever a summary would be doing factual work. Return the ledger delta and unresolved gaps; wait for review.

## Exact file handoff

Workflow ID: C03. Read: reviewed CASE-02-chunks.csv. Propose content for: CASE-03-graph-nodes.csv; CASE-04-graph-edges.csv; CASE-05-conflicts.csv. Follow `11-CASE-STORAGE.md`; the human saves/reopens these files and updates CASE-00-manifest.md. Ask for actual reviewed source passages whenever ledger summaries cannot support a claim. Do not claim a file was saved, reloaded or approved without the operator's confirmation.
