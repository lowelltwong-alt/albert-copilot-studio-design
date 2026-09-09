# Albert delivery guide

Send the packages separately so the recipient can start with the smallest pilot. For the first delivery, use the send-ready MVP pack:

1. `Albert-MVP-Send-Ready-1.1.zip` — extract and open `START-HERE.md`. Create the four standard Copilot Studio agents, paste each ROLE file into **Overview → Instructions**, choose one of the three included case folders, add its original PDF and paired OCR Markdown, and run the numbered prompts in the Test agent chat. No MCP/API or SharePoint is required.
2. `Albert-MVP-Prompts-1.0.zip` — the clean prompt-only package without private case PDFs, useful when the recipient supplies its own licensed case files.
3. `Albert-No-MCP-or-API-1.0.zip` — the expanded manual workflow when the MVP is useful.
4. `Albert-MCP-and-API-1.0.zip` — the connected design after the manual workflow is understood. Its full case-processing backend still needs implementation.
5. `Albert-Digital-Assets-1.0.zip` — the independent searchable digital-assets service. Open `AI_FRONT_DOOR.md` first, then run its local tests before any Azure connection.

The [Albert-Upgrades-From-MVP-1.0.zip](Albert-Upgrades-From-MVP-1.0.zip) bundles the three upgrade archives above plus the migration map, additive stage mapping, full digital-assets MCP notes and a ready-to-send email. It is the handoff to use after the prompt-only MVP pilot; it does not rebuild the MVP.

The workflow packages include Mermaid sources, SVG/PNG previews and editable Visio XML Drawing files. Visio XML and connector references were checked; native desktop Visio was unavailable for an opening test.

The digital-assets package has a real local MCP stdio endpoint and an API-key guarded Streamable HTTP/API adapter. Its DAD-like learning path is explicit and candidate-only: the calling AI must report a privacy-safe candidate; exact duplicates do not add evidence; unsafe packets are quarantined; a recurrence after a claimed fix reopens verification; human review is required before promotion. It does not watch other AIs or infer importance from frequency/model confidence.

Use the package's own provenance and licensing files before copying content. Albert-authored material is proposed under CC BY 4.0 where rights permit. DAD-derived material is separately restricted pending the owner's final license decision. Do not publish the mixed-rights material as one blanket license.

The local checks are evidence of package behavior only. Record actual tenant URL, secret references, model labels, Copilot Studio/Foundry MCP calls, DLP settings, storage mount, and human review receipts in a private deployment record. No external send, Azure deployment, Teams publication or public GitHub push has occurred here.
