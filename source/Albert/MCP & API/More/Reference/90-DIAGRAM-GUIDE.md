# Diagram guide

Use D01 to follow the workflow or system boundary, then the remaining diagram(s) for setup and quality detail. Each card names its exact prompt or configuration file. Open that file and follow its input/output handoff. `10-CONFIGURATION-AND-PLACEMENT.md` and `workflow-map.json` are the complete placement index.

| Diagram | Preview | Editable sources |
|---|---|---|
| Connected implementation • placement and authority boundary | [PNG](D01-IMPLEMENTATION-CONTEXT.png) / [SVG](D01-IMPLEMENTATION-CONTEXT.svg) | [draw.io](D01-IMPLEMENTATION-CONTEXT.drawio) / [Mermaid](D01-IMPLEMENTATION-CONTEXT.mmd) |
| Connected implementation • F01–F10, P/H/S alignment | [PNG](D02-IMPLEMENTATION-FLOWS.png) / [SVG](D02-IMPLEMENTATION-FLOWS.svg) | [draw.io](D02-IMPLEMENTATION-FLOWS.drawio) / [Mermaid](D02-IMPLEMENTATION-FLOWS.mmd) |
| Connected implementation • separate packet and script revision loops | [PNG](D03-IMPLEMENTATION-QUALITY.png) / [SVG](D03-IMPLEMENTATION-QUALITY.svg) | [draw.io](D03-IMPLEMENTATION-QUALITY.drawio) / [Mermaid](D03-IMPLEMENTATION-QUALITY.mmd) |

Yellow cards identify human steps; blue prompts; green workflow gates; purple storage/services; red unresolved stops. Labels name what crosses each arrow. Different prompt editions retain their own M/C namespaces; connected P, F, H and S IDs identify different component types.

Diagram invocation suffixes P and S mean packet and script runs of the SAME checker prompt (for example C06P and C06S both use C06-independent-review.md). R, RPKT and RSCR identify revision invocations of the named writer prompt. They are not missing prompt files. A grouped range such as P01–P07 expands through the placement index; its card links to that index. Save/reload nodes refer to the per-case storage guide.

SVG and PNG share node/routing geometry. Use the SVG for zooming; PNG for previews. Mermaid and draw.io are editable sources. XML and references were checked; draw.io GUI import and Mermaid application rendering were not tested. These diagrams are documentation, not an executable BPMN process or proof of a deployed tenant.

For both full editions, packet and podcast have separate review/revision loops: at least two material accepted changes, at most five attempts, then an explicit unresolved stop. A packet gate means human-reviewed diagnostic status in the prompt edition when the category map is unresolved; formal connected qualification remains blocked. Every early prompt-stage transition requires the setup guide's human passage review even when the overview compresses the human step into an arrow label.
