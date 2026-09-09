# Albert Innovation full prompt workflow v2

This recipient-facing package completes the full manual deliverable workflow using Copilot Studio built-in agent instructions and ordinary copy/paste. It uses no MCP, API, custom connector, backend, database, Power Automate, or automatic case processing. The operator keeps custody of the approved source ledger and review record in an approved Word/text workspace.

Run C01–C10 in order. Stop for human review after every stage. The deliverables are a diagnostic witness packet and a full chaptered script planned for 8,000–12,000 spoken words when the approved evidence supports that length. The 243-word synthetic seed in `03-SYNTHETIC-WALKTHROUGH.md` is intentionally too small to support an 8,000-word fact-rich script; the prompts must use method exercises and controlled repetition, never invented facts or stretched source claims.

Formal packet convergence remains blocked until the packet category map is pinned. A complete human-reviewed diagnostic packet can still be delivered and must be labeled diagnostic. No output from this package is gold, a signed artifact, a server-verified state, or proof of learning.

Start with `01-SETUP-AND-RUN-SEQUENCE.md`, select a tenant-approved model from `02-MODELS.md`, prepare `03-OPERATOR-LEDGER-TEMPLATE.md`, then use the stage files. `00-ALL-IN-ONE-PROMPT.md` is the compact one-agent alternative.


## Diagram, prompt and file placement

Open this pack's D01 workflow diagram and D02 setup diagram. Use `10-CONFIGURATION-AND-PLACEMENT.md` / `workflow-map.json` to match node IDs to exact prompt files and expected inputs/outputs. `configuration.example.json` is a human setup worksheet, not a Copilot import file. Read `11-CASE-STORAGE.md` for manual save/reload and optional native knowledge uploads; SharePoint is optional. `12-PODCAST-QUALITY.md` describes the podcast-first review target. `VERIFICATION.md` distinguishes file checks from actual tenant/model testing.
