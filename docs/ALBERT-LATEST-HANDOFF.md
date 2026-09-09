# Albert — current handoff

Use the standalone packages in this order:

The concise [delivery guide](SEND-TO-INNOVATION-2026-09-09.md) gives the extraction and setup order.

The additive [upgrade bundle](Albert-Upgrades-From-MVP-1.0.zip) contains the no-MCP workflow, MCP/API workflow design and full digital-assets MCP package with migration instructions. It preserves the MVP as the base instead of rebuilding it.

The [delivery receipt](ALBERT-DELIVERY-RECEIPT-2026-09-09.json) records package hashes and validation boundaries.

1. [Albert-MVP-Prompts-1.0.zip](Albert-MVP-Prompts-1.0.zip) — prompt-only Copilot Studio pilot. It needs no MCP, API, database or SharePoint connection.
   - [Albert-MVP-Send-Ready-1.1.zip](Albert-MVP-Send-Ready-1.1.zip) — same MVP plus a ready-to-run private fixture pack: Msimoto, the City Cubs baseball-bat case, and the Evans professor case, each with original PDF, paired OCR Markdown, README and exact first-run prompt.
2. [Albert-No-MCP-or-API-1.0.zip](Albert-No-MCP-or-API-1.0.zip) — expanded manual workflow with the same source-grounded stages and human packet handoffs.
3. [Albert-MCP-and-API-1.0.zip](Albert-MCP-and-API-1.0.zip) — connected workflow design with MCP/API contracts; its full Albert case-processing backend still needs implementation and tenant acceptance.
4. [Albert-Digital-Assets-1.0.zip](Albert-Digital-Assets-1.0.zip) — separate lightweight DAD-style digital asset catalog with a working local MCP server, authenticated API adapter, typed graph, lifecycle checks and explicit cross-instance learning intake.

Open `START-HERE.md` in the first three packages. Open `AI_FRONT_DOOR.md` in the digital-assets package before evaluating or connecting it. That front door maps every endpoint, tool, graph field, learning disposition, test and Azure/Copilot Studio/Foundry boundary.

The workflow diagrams are supplied as Mermaid, SVG, PNG and editable Visio XML Drawing files. XML structure and connector references were checked. Native Visio opening was not tested because no Visio desktop installation is available in this environment; use the SVG/PNG backups if needed.

Local validation covers prompt packet reconstruction, graph integrity, links, lifecycle/cycle checks, MCP stdio initialize/list/call, authenticated HTTP MCP/API parity, input bounds, duplicate handling, and candidate/review gates. Model labels are proposed pilot settings reported by the owner, not verified tenant bindings. No audio, tenant deployment, Teams publication, or gold-standard quality certification is claimed.

The digital-assets package records DAD-derived provenance separately. Albert-authored material is proposed under CC BY 4.0 where the owner has rights to grant it; DAD-derived and third-party material are excluded pending their separate terms. Public GitHub publication remains a later, explicit rights and privacy review.

No external message, public publication, tenant deployment, donor checkout mutation or global installation occurred during this handoff.
