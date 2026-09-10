# Albert — full connected implementation package

Edition 2 of 3 • revision 2 • Standard Copilot Studio harness + Teams • implementation specification, not deployed software

This package gives the Innovation's team an assignable design for the complete case-to-podcast workflow. MCP is the primary connection and HTTPS API is an alternate profile over the same services. Automatic failover is limited to safe reads; uncertain mutations are reconciled in the common operation ledger. The separate MVP and full prompt-only packs require neither backend transport.

## Reading and implementation order

1. Open `D01-IMPLEMENTATION-CONTEXT.png`, then D02 for workflow and D03 for the two separate artifact revision loops. SVG, Mermaid and draw.io copies are editable design sources.
2. Use `10-CONFIGURATION-AND-PLACEMENT.md` and `workflow-map.json` to match every Pxx prompt to its exact component/inputs/outputs. `configuration.example.json` is a blank private-setup worksheet, not an import file.
3. Read `11-CASE-STORAGE.md`: proposed Azure Blob objects plus Azure SQL case/chunk/graph/conflict/job/review records. SharePoint is optional; a chat transcript or search index is not the authoritative case store.
4. Assign `01-IMPLEMENTATION-BACKLOG.md` / `.json`: 28 owner/dependency/effort/deliverable work packages. Use `02-FLOWS-AND-STATE.md` and `04-ADMIN-SCREENS.md` to implement F01–F10 and H01–H07.
5. Implement `03-MCP-AND-API.md` with canonical OpenAPI, the separate full JSON Schema transport contract, MCP tools, and the Swagger 2 connector templates. Deploy and test the trusted non-model operation-envelope provider before mutations go live.
6. Follow `08-QUALITY-CONTRACT.md` and `12-PODCAST-QUALITY.md`. The podcast is the highest-priority output; packet and script each need two material independently evaluated revisions, up to five attempts.
7. Run the supplied reference demonstration, then implement the real-service acceptance adapter and execute `05-ACCEPTANCE-PLAN.md`. Inspect `VERIFICATION.md` for what was actually checked in this package.
8. Close the pilot and operations handoff through `06-PILOT-AND-OPERATIONS.md`. Resolve the specific decisions in `07-REUSE-AND-DECISIONS.md` and `13-DECISIONS-AND-RELEASE.md`.

## Readiness and remaining decisions

The decomposition and candidate configuration/interface artifacts are prepared for engineering implementation and review. No backend, MCP server, actual Power Platform solution or tenant connection is delivered by these design files. Tenant ID/environment/region, identity configuration, trusted token injection, licensing/data approval and real tests remain implementation tasks. No 100% tenant compatibility certification is claimed.

One synthetic premises case is the first pilot, followed by medical-handoff, cold-chain and unfamiliar-rule fixtures. Target a complete source-bound witness packet and chaptered 8,000–12,000 spoken-word script when the approved source/scope supports it. Do not inflate facts to hit length. Audio generation is a separate approved downstream step.

Packet rubric category membership remains unresolved; diagnostic building can proceed, but formal packet convergence and the connected qualified-export gate cannot pass until the owner pins it. Human acceptance, reference/panel gold qualification and learning evidence are separate from machine checks.

Prepared for Lowell's Innovation handoff; not sent to the Innovation or published to Git. Referenced Albert implementation code is not bundled. Source/code licenses and authorized implementation-lane readiness must be checked before reuse.
