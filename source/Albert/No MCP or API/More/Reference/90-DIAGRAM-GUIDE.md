# Diagram guide

Use D01 to follow the workflow or system boundary, then the remaining diagram(s) for setup and quality detail. Each card names its exact prompt or configuration file. Open that file and follow its input/output handoff. `10-CONFIGURATION-AND-PLACEMENT.md` and `workflow-map.json` are the complete placement index.

| Diagram | Preview | Editable sources |
|---|---|---|
| Full prompt workflow • evidence, revision and final approval | [PNG](D01-FULL-END-TO-END.png) / [SVG](D01-FULL-END-TO-END.svg) | [draw.io](D01-FULL-END-TO-END.drawio) / [Mermaid](D01-FULL-END-TO-END.mmd) |
| Full prompt workflow • placement and case recovery | [PNG](D02-FULL-SETUP-PLACEMENT.png) / [SVG](D02-FULL-SETUP-PLACEMENT.svg) | [draw.io](D02-FULL-SETUP-PLACEMENT.drawio) / [Mermaid](D02-FULL-SETUP-PLACEMENT.mmd) |

Yellow cards identify human steps; blue prompts; green workflow gates; purple storage/services; red unresolved stops. Labels name what crosses each arrow. Different prompt editions retain their own M/C namespaces; connected P, F, H and S IDs identify different component types.

Diagram invocation suffixes P and S mean packet and script runs of the SAME checker prompt (for example C06P and C06S both use C06-independent-review.md). R, RPKT and RSCR identify revision invocations of the named writer prompt. They are not missing prompt files. A grouped range such as P01–P07 expands through the placement index; its card links to that index. Save/reload nodes refer to the per-case storage guide.

SVG and PNG share node/routing geometry. Use the SVG for zooming; PNG for previews. Mermaid and draw.io are editable sources. XML and references were checked; draw.io GUI import and Mermaid application rendering were not tested. These diagrams are documentation, not an executable BPMN process or proof of a deployed tenant.

For both full editions, packet and podcast have separate review/revision loops: at least two material accepted changes, at most five attempts, then an explicit unresolved stop. A packet gate means human-reviewed diagnostic status in the prompt edition when the category map is unresolved; formal connected qualification remains blocked. Every early prompt-stage transition requires the setup guide's human passage review even when the overview compresses the human step into an arrow label.
