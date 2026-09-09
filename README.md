# Albert Copilot Studio workflow

This is the private, reviewable handoff repository for the Albert witness-preparation and podcast workflow. It contains the prompt-only MVP, the additive no-MCP/no-API workflow, the MCP/API design, and the separate DAD-style digital-assets package.

## Start here

1. Open [`docs/SEND-TO-INNOVATION-2026-09-09.md`](docs/SEND-TO-INNOVATION-2026-09-09.md) for the delivery order and setup boundary.
2. For the first Copilot Studio pilot, use [`packages/Albert-MVP-Send-Ready-1.1.zip`](packages/Albert-MVP-Send-Ready-1.1.zip), then open its `START-HERE.md` after extraction.
3. For the inspectable neutral source tree, open [`source/Albert/START-HERE.md`](source/Albert/START-HERE.md).
4. Use [`packages/Albert-Upgrades-From-MVP-1.0.zip`](packages/Albert-Upgrades-From-MVP-1.0.zip) only after the MVP works; it preserves the MVP and adds the two upgrade paths plus digital assets.

## Repository map

- `packages/` — integrity-checked release archives.
- `source/Albert/` — browsable neutral workflow source, diagrams, prompts, and configuration guidance.
- `docs/` — handoff notes and validation receipt.
- `tools/` — deterministic repack/build helpers used to make the handoff archives.

The MVP is prompt-only and needs no MCP, API, database, or SharePoint connection. The MCP/API package is an implementation design with a working digital-assets MCP component; its tenant-specific Albert backend still needs deployment and acceptance in Azure/Copilot Studio/Foundry.

## Verification boundary

Local checks cover prompt graph integrity, negative cases, timing estimates, ZIP integrity, source hashes, the local digital-assets MCP stdio server, and the authenticated HTTP adapter. They do not claim a live Azure tenant deployment, Teams publication, model-picker binding, or gold-standard audio quality.

## Private fixture boundary

`Albert-MVP-Send-Ready-1.1.zip` contains licensed mock-trial PDFs and paired OCR Markdown for private testing. Keep this repository private and confirm rights before copying those fixtures elsewhere. Do not publish the fixture archive or its extracted contents without a separate rights review.

## Licensing

See [`LICENSE.md`](LICENSE.md) and the package-specific notices. Albert-authored material is proposed under CC BY 4.0 where the owner has rights to grant it. DAD-derived material remains separately restricted pending a final license decision; it is not relicensed by this repository.
