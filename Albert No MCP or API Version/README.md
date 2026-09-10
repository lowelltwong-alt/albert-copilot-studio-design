# Albert — full workflow, no MCP or API

Create one unpublished standard Copilot Studio agent. Proposed pilot model: **GPT-5.5**, if present in the approved selector; this is a user-reported label, not a verified binding. Paste [the parent/router prompt](PROMPTS/00-ALL-IN-ONE-PROMPT.md) into **Overview → Instructions**. Paste the C01–C10 stage files into **Test agent chat** with the named source/ledger inputs. The router does not contain the ten full procedures.

Use [the wiring diagram](WORKFLOWS/README.md). Run intake → source/exhibits → ledger → witness profile → packet → review/repair → script → consistency → rehearsal. Save/reopen outputs manually; no tools, connectors or automatic persistence are required. A separate fresh checker conversation is needed for review; one conversation is not independent evaluation.

This is the earlier expanded manual design. Its original cycle counts remain in the preserved prompts; do not silently mix them with the newer shared podcast adapter. Read the version note under More before adopting that adapter. Detailed setup is [here](More/Reference/01-SETUP-AND-RUN-SEQUENCE.md).

## Prompts

- [00-ALL-IN-ONE-PROMPT.md](PROMPTS/00-ALL-IN-ONE-PROMPT.md)
- [C01-intake.md](PROMPTS/C01-intake.md)
- [C02-source-exhibit-review.md](PROMPTS/C02-source-exhibit-review.md)
- [C03-evidence-ledger.md](PROMPTS/C03-evidence-ledger.md)
- [C04-case-witness-profile.md](PROMPTS/C04-case-witness-profile.md)
- [C05-full-witness-packet.md](PROMPTS/C05-full-witness-packet.md)
- [C06-independent-review.md](PROMPTS/C06-independent-review.md)
- [C07-material-revision.md](PROMPTS/C07-material-revision.md)
- [C08-full-chaptered-script.md](PROMPTS/C08-full-chaptered-script.md)
- [C09-pair-consistency-final-package.md](PROMPTS/C09-pair-consistency-final-package.md)
- [C10-truthful-rehearsal.md](PROMPTS/C10-truthful-rehearsal.md)

[More](More/README.md) contains the complete supporting files.

## Build on the MVP

Retain the original source files, source and graph IDs, witness scope, conflict ledger, accepted plan/script and review history. Copy them into a new revision before adopting this upgrade. Map each existing artifact to the matching stage and validate one known case before changing operating mode. These older designs have different fixed-cycle language; reconcile it explicitly with the MVP review/repair/stop policy. Migration is a design path, not a verified automatic conversion.

## AI assistance

Give your AI this folder and ask: "Read README.md, then follow the prompt, workflow and supporting contract files. State what you read, what remains unverified and the next setup action. Do not execute or deploy without authorization." In the full repository, AI_FRONT_DOOR.md and AI-TOC.md map all four packages.

Rights: [Albert license](LICENSE.md) · [DAD-derived restrictions](LICENSE-DAD-DERIVED.md).
