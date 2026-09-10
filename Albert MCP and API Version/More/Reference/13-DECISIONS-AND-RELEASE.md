# Architecture decisions and deployment handoff

These are proposed implementation decisions bound to this pack revision. They become operational only after implementation and acceptance. Their purpose is to prevent makers from having to infer configuration from a diagram.

| Decision | Choice and reason | Owner / condition to revisit |
|---|---|---|
| ADR01 Editions | Three independent setup guides: short MVP, full connected, full prompt-only. Same source/truthful-practice principles; explicit different persistence and assurance capabilities. | Product owner; revisit if automatic write-back is requested for prompt editions |
| ADR02 Integration | Standard harness + Teams; Streamable HTTP MCP and API-only share one backend. Read-only automatic failover and reconciled mutations prevent duplicate logical work. | Platform/backend leads; tenant injection/auth probes are mandatory |
| ADR03 Persistence | Proposed Azure Blob for source/artifact bodies and Azure SQL for transactional case/graph/conflict/job/review records. Graph relationships use typed adjacency tables with case constraints. | Backend lead; benchmark actual data before adding another graph/vector service |
| ADR04 Knowledge | General approved guidance separate from case evidence. SharePoint optional. Native knowledge uploads may help manually reload scoped prompt-only cases but cannot provide witness-grant enforcement. | Source custodian; revisit sharing/authentication model before multi-user case use |
| ADR05 Models | User-reported GPT-5.5 is simplest default; Sonnet 4.6 optional author. Record exact selector/harness/provider and evaluate before switching to the newer reported models. | Model/pilot owner; recheck after model or harness changes |
| ADR06 Quality | Podcast-first evaluation; separate packet/script revision histories; exact source/pair checks and human review. No inferred gold equivalence. | QA/rubric owner; actual approved reference and packet category decision required |
| ADR07 Configuration | Prompt/component IDs are stable. Nonsecret deployment values are separated from definitions; connection references hold managed authentication bindings. | Platform owner; review versioned configuration diff before promotion |

## Implementation package versus deployable solution

This pack supplies blueprints and connector templates. The implementation team must create/export a real Power Platform solution and actual backend deployment artifacts after WP21. Do not rename this ZIP as a solution ZIP or claim that uploading the diagram/configuration JSON installs an agent.

After building the real solution, use solution environment variables and connection references for the target environment. The supplied `deployment-settings.example.json` shows the documented deployment-settings envelope with placeholder IDs only; generate the final settings from the actual solution and validate its schema names. Keep development/test/production values private and separate. A backend configuration mapping must connect the case store, processor and trusted operation-envelope adapter to the service; a filled worksheet alone is insufficient.

## Release handoff record

Record release ID; prompt/workflow/schema/service/connector/solution versions; environment and channel; authenticated identity mapping; selected model labels; approved processor/region/data classes; configuration digest; required tests and actual outcomes; open findings; owner and rollback revision. Re-import/run read probes and scoped mutation probes in the destination environment before approving use. Restore procedures must cover both artifact bodies and their ledgers.

For later public Git publication, build from an explicit allowlist. Exclude tenant-specific settings, private sources, actual source passages, source paths, credentials, internal work logs and hidden study material. Confirm referenced-code and gold-reference licenses. Review the exact archive and hashes before publishing; this pack performs no public release.
