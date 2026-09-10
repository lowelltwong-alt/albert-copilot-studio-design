# Albert — MCP & API

**This is an implementation design, not a complete running Albert server.** It supplies tool/API contracts, connector templates and a backlog. The separate toolkit server retrieves reusable assets; it does not implement full case processing.

Use [the wiring diagram](WORKFLOWS/README.md). Put [P00](PROMPTS/P00-parent.md) in the standard Copilot Studio parent agent's **Instructions**. Proposed parent model: **GPT-5.5**, if the approved selector provides the user-reported label. P01–P05/P07 are scoped worker instruction contracts; P06 is a separately assigned evaluator worker. Model assignment and worker isolation require the implementation described under More. Do not assume native child agents have separate model selectors or independent parent context.

The intended connection is Studio → authenticated MCP (primary), or configured HTTPS API → the same authoritative dispatcher/storage. Safe-read fallback and uncertain mutation reconciliation have different rules. A deployed server URL, authentication, scope enforcement and real tenant tests are still needed before these prompts can call the full workflow.

[Exact placement and tool boundaries](More/Reference/09-COPILOT-PLACEMENT.md) · [MCP/API contracts and server requirements](More/Reference/03-MCP-AND-API.md). The older fixed-cycle prompt language needs an explicit service-policy adaptation and tests before using the newer shared podcast loop.

## Prompts

- [P00-parent.md](PROMPTS/P00-parent.md)
- [P01-source-review.md](PROMPTS/P01-source-review.md)
- [P02-case-profile.md](PROMPTS/P02-case-profile.md)
- [P03-witness-planner.md](PROMPTS/P03-witness-planner.md)
- [P04-packet-writer.md](PROMPTS/P04-packet-writer.md)
- [P05-script-writer.md](PROMPTS/P05-script-writer.md)
- [P06-independent-evaluator.md](PROMPTS/P06-independent-evaluator.md)
- [P07-truthful-rehearsal.md](PROMPTS/P07-truthful-rehearsal.md)

[More](More/README.md) contains the complete supporting files.
