# Albert — prompts only

1. Create four unpublished agents in Copilot Studio's **standard** experience. In each agent's **Overview → Instructions**, paste its ROLE file below. Set the model in the agent's model selector.
2. Open [the wiring diagram](WORKFLOWS/README.md). Run the numbered RUN prompts in each agent's **Test agent chat**, supplying their named inputs. The operator copies the saved packets between roles; this MVP does not require tools or automatic child-agent wiring.
3. Follow [the exact prompt order](PROMPTS/00-PLACEMENT.md). Save/reopen each output before the next handoff. The detailed [first-run instructions](More/02-RUN-GUIDE.md) include a short synthetic case.

| Studio agent | Paste into Instructions | Proposed pilot model | RUN prompts in its test chat |
|---|---|---|---|
| Albert Case Analyst | [ROLE-ANALYST](PROMPTS/ROLE-ANALYST.md) | GPT-5.5 | 01 |
| Albert Writer | [ROLE-WRITER](PROMPTS/ROLE-WRITER.md) | Claude Sonnet 4.6 | 02, 04, 08, 10 |
| Albert Evidence Reviewer | [ROLE-EVIDENCE](PROMPTS/ROLE-EVIDENCE.md) | GPT-5.5 | 03, 05, 07, 09 |
| Albert Conversation Reviewer | [ROLE-CONVERSATION](PROMPTS/ROLE-CONVERSATION.md) | GPT-5.5 | 06 |

RUN-11 is a triggered audit by a non-author reviewer. Do not let a reviewer audit its own work.

These model names come from the labels you reported. They are proposed pilot settings, not verified tenant bindings or a performance claim. If a label is absent, record the actual available approved model and treat that run as a new configuration. Keep tools and knowledge sources empty; disable web/general-knowledge controls where exposed. No API key, MCP, database or SharePoint setup is required.

Separate upgrades are supplied as Albert-No-MCP-or-API and Albert-MCP-and-API. Digital Assets with MCP is an independent optional package.

[More](More/README.md) holds setup details, templates, examples, reviews, tests, credits. The example remains held with documented improvements; Studio tenant testing is pending.
