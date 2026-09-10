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

## Setup complete: run your first case

# First run: Lantern Hall

Use this new synthetic case to learn the setup. The target is a useful short exercise, not a gold comparison or a 30-minute case product. Keep [SOURCE](More/MVP-Reference/demo/SOURCE.md) and [OPERATOR-BRIEF](More/MVP-Reference/demo/OPERATOR-BRIEF.md) unchanged while comparing attempts. The [worked example and actual review](More/MVP-Reference/demo/00-READ-THIS-EXAMPLE.md) and instructor-only probes are comparison aids, not inputs for a fresh Writer.

## Prepare once

Create an ordinary approved folder for this practice and copy the source, operator brief and [STATE](More/MVP-Reference/templates/STATE.md) template into it. Use `LANTERN-MINA` as the prefix and `R01` as the initial assembly revision. Open the four unpublished agents from [setup](More/01-SETUP.md). Record the actual model labels and context in the [configuration worksheet](More/MVP-Reference/templates/CONFIGURATION.md).

Paste the named complete RUN file into the stated role's Test agent chat, then paste the required content in a [PACKET](More/MVP-Reference/templates/PACKET.md). Send **BEGIN RUN** only when all required content has arrived. If the full RUN is rejected, use the ordered smaller paste files listed in [placement](PROMPTS/00-PLACEMENT.md). Do not substitute a filename for file content.

## Execute these handoffs

| Order | Where / prompt | Supply | Save and inspect |
|---|---|---|---|
| 1 | Analyst / [RUN-01](PROMPTS/RUN-01-GRAPH.md) | SOURCE, OPERATOR-BRIEF, GRAPH and STATE templates | `LANTERN-MINA-W05-GRAPH-R01.md`, `...W05-VIEW-R01.md`, separate `...W05-AUTHOR-R01.md`; inspect one TRACE and all grant scopes |
| 2 | Writer / [RUN-02](PROMPTS/RUN-02-PLAN.md) | Human-reviewed VIEW/permitted raw passages, methods/style brief, requested demo mode | `...W08-PLAN-R01.md`, draft `...KC10-R01.md`, planned `...T06-R01.md` |
| 3 | Evidence / [RUN-03](PROMPTS/RUN-03-PLAN-GATE.md) | GRAPH/VIEW, actual raw spans, complete plan/card/planned T06 | `...W06-PLAN-R01.md`; correct actual plan/source defects and repeat this plan check before drafting |
| 4 | Writer / [RUN-04](PROMPTS/RUN-04-WRITE.md) | Complete accepted plan and packet, request `PC01 only` | Save `...PC01-R01.md`. Repeat PC02 through PC08. Request ASSEMBLE only with every complete saved chapter |
| 5 | Writer assembly | Same RUN-04 and all saved chapters | Complete `...W08-SCRIPT-R01.md`, `...W08-CLAIMS-R01.md`, `...KC10-R01.md`, as-built `...T06-R01.md`; freeze these exact files |
| 6 | Evidence / [RUN-05](PROMPTS/RUN-05-SOURCE-REVIEW.md) | Full assembly and actual source/view/graph; not the writer's self-score | `...W06-SOURCE-R01.md` with coverage and source gate |
| 7 | Conversation / [RUN-06](PROMPTS/RUN-06-CRAFT-REVIEW.md) | Same full assembly, permitted packet and style-function brief | `...W06-CRAFT-R01.md`; no original supplied means matched reference comparison unavailable |
| 8 | Evidence / [RUN-07](PROMPTS/RUN-07-JOIN.md), then operator | Both exact reviews, STATE and actual saved/reopened comparison | `...W07-DECISION-R01.md`: manual candidate, one repair, or hold. A high craft score cannot clear a source/method/permission hold |
| 9, only if justified | Writer / [RUN-08](PROMPTS/RUN-08-REPAIR.md) | Whole R01, verified findings, source/view and change plan | Full R02 assembly and `...CHANGE-RECEIPT-R02.md`; preserve R01 |
| 10, after repair | Evidence / [RUN-09](PROMPTS/RUN-09-REPAIR-EVIDENCE.md), Conversation / RUN-06, then RUN-07 | Whole before/after and exact findings; both reviewers inspect all of R02 | New reports/decision on R02. Remaining material failure means HOLD; do not begin another production repair |
| 11, after human acceptance | Writer / [RUN-10](PROMPTS/RUN-10-EXPORT.md) | Exact accepted assembly and human acceptance for this internal exercise | `...W09-SPEAKERS-R01.txt`, `...W09-SPOKEN-R01.txt`, `...W09-TIMING-R01.md`, permitted card/map; use R02 if that was accepted |

At every row the operator saves, reopens and compares the complete output, records the role/model/revision and updates STATE. Models propose outputs; they do not persist them. If you edit any accepted text, give it a new revision and recheck the affected complete assembly before exporting it.

Copy this continuation only after your actual inspection:

```text
Operator checkpoint: I saved and reopened [exact files/revisions].
Required content is complete: [list]. Identity mode: manual_revision.
Comparison performed: [describe actual exact-text/ID check]. Digest: not_computed.
Permitted next stage: [RUN-ID]. Audience/use remains [named internal use].
Unresolved findings: [none or IDs; HOLD if material]. BEGIN RUN [RUN-ID].
```

Do not copy a prewritten acceptance as if it were a check you performed. If you have no authority, missing files or unresolved scope, say so and hold.

## What to look for

The clatter, a later observation and a collision are different propositions. Both approximate time accounts remain attributed. The two packet inserts remain distinct; an unchecked condition box is not a clean inspection; a schedule does not establish actual finishing time. Mina cannot authenticate Lee's signature from the supplied record. The hosts teach these distinctions before asking the listener to apply them.

The source should sustain ten distinct facts/limits, but a model must show their source support and actual teaching. Quality means a useful conversation and applied practice, not just ten numbered labels. Use the instructor-only probes after the baseline to test whether reviewers catch errors. Keep their expected findings out of fresh author context.

## When you return tomorrow

Open STATE and the listed saved files. Start a new appropriate role conversation, load the exact current RUN and required packet, and ask it to list received/missing IDs before continuing. Do not ask it to remember yesterday. If actual saved content is missing, rebuild only from authoritative inputs and label the new attempt.

For timing, copy speech-only text into an ordinary editor/word processor that reports word count, exclude cues/labels, and record how it was counted. The model's count is an estimate until verified. Pauses remain separate. No audio generation or paid audio service is needed for this exercise.

## Use your own case

Supply an authorized case PDF and/or Markdown, the target witness, intended duration, and the witness knowledge boundaries. Keep PDF pages and exhibit identifiers as source authority. Start RUN-01 with source text and the GRAPH, STATE and PACKET templates; preserve unknowns instead of filling gaps. Follow the same table above. Save the transcript, timing sheet, witness preparation card, claims ledger and independent reviews. No audio is generated. For a short case, request a short exercise rather than padding to 30 minutes.

## AI assistance

Give your AI this folder and ask: "Read README.md, then follow the prompt, workflow and supporting contract files. State what you read, what remains unverified and the next setup action. Do not execute or deploy without authorization." In the full repository, AI_FRONT_DOOR.md and AI-TOC.md map all four packages.

Rights: [Albert license](LICENSE.md) · [DAD-derived restrictions](LICENSE-DAD-DERIVED.md).
