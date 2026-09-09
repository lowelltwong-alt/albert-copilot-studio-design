# Private repository scope

This repository is the current release surface for the Albert Copilot Studio design. It intentionally tracks the neutral current source and release archives rather than every intermediate artifact in the build workspace.

Tracked:

- The current prompt-only MVP and its send-ready private fixture archive.
- The additive no-MCP/no-API and MCP/API upgrade archives.
- The separate DAD-style digital-assets archive.
- The browsable neutral source tree and delivery/validation documents.
- The small deterministic build helpers used for the release archives.

Excluded:

- `work/`, which is a dependency/runtime cache and contains disposable test material.
- `outputs/` as a whole, which contains duplicate packages, historical drafts, and old CINO/CIO filenames. The current neutral artifacts are copied into this repository under `source/`, `packages/`, and `docs/`.
- Tenant secrets, client data, and unreviewed third-party material.

The private GitHub boundary is deliberate. The send-ready archive contains mock-trial PDFs whose redistribution rights have not been established for public publication.
