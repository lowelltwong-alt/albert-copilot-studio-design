# 01 — Copilot Studio prompt-only setup

This starter uses four separate, unpublished standard-harness agents. A human operator manually moves each packet from one agent to the next. It needs no API, MCP, custom action, Power Automate, SharePoint, or knowledge-upload setup.

| Agent | Permanent instruction file | Job |
|---|---|---|
| Albert Case Analyst | `PROMPTS/ROLE-ANALYST.md` | Extract a bounded case profile from the supplied source. |
| Albert Writer | `PROMPTS/ROLE-WRITER.md` | Draft the requested artifact from the accepted packet. |
| Albert Evidence Reviewer | `PROMPTS/ROLE-EVIDENCE.md` | Check support, uncertainty, and overclaiming. |
| Albert Conversation Reviewer | `PROMPTS/ROLE-CONVERSATION.md` | Check clarity, tone, audience fit, and revision priorities. |

Each instruction file is designed to remain below Microsoft’s 8,000-character agent-instructions limit. The stage prompts in `prompts/RUN-01...` are pasted or attached to the Test agent chat for the current run; do not concatenate every stage prompt into permanent Instructions. Save outputs manually in an ordinary authorized folder. The model must not claim that it wrote files or computed hashes.

1. **Choose the standard experience.** Sign in to Copilot Studio and select the intended environment. If the interface offers a **New experience** switch, turn it off for this guide. The labels below describe the standard/classic flow; Microsoft documents that classic and new experiences can differ. See [Create and delete agents](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-first-bot).

2. **Create four blank agents.** Open **Agents**, choose **Create blank agent** (or the equivalent blank-agent command), and make one agent for each role in the table. Keep every agent unpublished. Select an actually available approved model and record its displayed label in the run record; do not assume GPT-5.5, Claude, or any other model is available.

3. **Set only the durable contract.** In each agent, open **Overview**, find **Instructions**, choose **Edit**, paste the matching file from `PROMPTS/`, and **Save**. Put role, scope, evidence rules, output contract, and refusal/uncertainty behavior here. Keep **Tools** and **Knowledge sources** empty for the first run. If Web search or “use general knowledge” controls appear, turn them off; a source-grounded prompt still requires review.

4. **Prepare the synthetic run.** Open [the first-run guide](02-RUN-GUIDE.md), [demo/SOURCE.md](More/MVP-Reference/demo/SOURCE.md) and [demo/OPERATOR-BRIEF.md](More/MVP-Reference/demo/OPERATOR-BRIEF.md). Start with [RUN-01](PROMPTS/RUN-01-GRAPH.md), supplying the named packet and templates. Paste text directly for the default route; attachment support may differ by tenant and channel. Keep all content synthetic or authorized.

5. **Run the analyst.** Open the first agent’s standard **Test agent** pane, paste the RUN-01 prompt and the source packet, and send it. Copy the response into the designated handoff Markdown file. Record the agent name, displayed model label, prompt/file identifiers, and the human revision identifier under `manual_revision`.

6. **Move packets by hand.** Open the next agent’s Test agent pane and provide the prior accepted packet plus its stage prompt. Repeat for Writer, Evidence Reviewer, and Conversation Reviewer. The four agents are separate manual surfaces; this is an operating workflow, not native child-agent orchestration.

7. **Save and compare.** The operator saves each accepted output in the authorized folder, reopens it, and compares exact content and IDs. `manual_revision` is the baseline identity mode. Optional hashes may be recorded later, but this is not canonical hash-verified P09 qualification.

8. **Keep it unpublished and improve deliberately.** Test several synthetic turns before any publication decision. Preview/test is for iteration; inspect unsupported claims, missing evidence, and reviewer disagreement. Change one instruction or stage prompt at a time and repeat the relevant stage.

## Troubleshooting

| Symptom | Recovery |
|---|---|
| New UI labels do not match | Turn **New experience** off if available; otherwise stop and record the tenant-specific labels before proceeding. |
| Instructions will not save | Check that only the matching ROLE file was pasted; each supplied file is under 3,300 characters. If a tenant constraint still prevents saving, record it before testing a smaller new revision; do not silently delete source/permission gates. |
| Agent invents support or current facts | Confirm Web search/general knowledge are off; provide the source packet and require “not found/uncertain” when unsupported. |
| Attachment or output seems missing | Reattach/paste the current packet in the same Test agent turn, then manually save the returned text. Do not claim automatic persistence or writeback. |

Microsoft documents the 8,000-character instruction limit in [Quotas and limits](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas), and the standard test surface in [Test your agent](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-test-bot).
