# Run the reviewer architecture in your environment

The portable roles specify behavior; this document is a runtime adapter. Candidate 0.2.0. User priority: test the prompt-only MVP before propagating the podcast candidate to the full manual and connected Albert profiles. Those two profile implementations are unchanged.

| Setup | What to do | Actual responsibility |
|---|---|---|
| Prompt-only MVP / any chat | Open WF04 or WF05, paste its exact role prompt plus named inputs into saved separate conversations; save and reopen each output | Human or operator coordinates roles and owns persistence; no custom API or MCP |
| Host-native subagents | Assign planner/writer, evidence checker and conversation checker bounded read scopes; use one editor; bind actual model IDs and effort in T02 | Host runs agents; fresh context is recorded, not assumed independent |
| Asset MCP | SearchAssets, then GetAsset/GetNeighbors, then GetAssetContent for exact stable ID | Existing optional service retrieves generic instructions; host executes them separately |
| API backup | POST /api/tools/GetAssetContent with {"asset_id":"albert:agent:podcast-conversation-reviewer"} | Same verified bytes as MCP; no case input or model invocation in this endpoint |
| NotebookLM comparison / later audio | Select Deep Dive and the available Longer control, supply authorized permitted sources and the reviewed episode brief | Product generates its own output; it may rewrite the script, so new audio/transcript needs new source/style checks |

For the desired two-voice production, label HOST_A and HOST_B consistently. A male-presenting and female-presenting voice is an operator preference, not a required gender identity or expertise hierarchy. Record actual selected voice IDs only when producing audio. No voice/audio was generated in this package.

Select current economy capability for extraction/format checks; balanced capability with sufficient context for source-rich writing and review; stronger specialist for a named unresolved disagreement. Record actual model/runtime, prompt digest, input digests, output digest, visible reference/grade context, tools, elapsed time and known cost. Do not infer prices, provider diversity or identity. Existing user-reported model names are not verified tenant bindings.

Copilot Studio has not been imported or tested in the user's tenant. Team/operator saves case files in its approved storage and enforces permissions; generic MCP asset retrieval does not provide a case database or automatic agent scheduling. Manual prompt execution and saved Markdown are the lowest-setup path.

Stable retrieval IDs: `albert:agent:subagent-improver`, `albert:agent:podcast-conversation-reviewer`, `albert:prompt:conversational-podcast-writer`. Internal A01 role labels map to the first catalog ID; WF04 is the architecture. Instruction changes require new exact evidence. Adoption is owner-controlled and rollback retains the prior release.
