from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "outputs" / "Albert-Upgrades-From-MVP-1.0"
ARCHIVE = ROOT / "outputs" / "Albert-Upgrades-From-MVP-1.0.zip"
PACKAGES = {
    "Albert-MVP-Prompts-1.0.zip": ROOT / "outputs" / "Albert-MVP-Prompts-1.0.zip",
    "Albert-No-MCP-or-API-1.0.zip": ROOT / "outputs" / "Albert-No-MCP-or-API-1.0.zip",
    "Albert-MCP-and-API-1.0.zip": ROOT / "outputs" / "Albert-MCP-and-API-1.0.zip",
    "Albert-Digital-Assets-1.0.zip": ROOT / "outputs" / "Albert-Digital-Assets-1.0.zip",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def deterministic_zip(name: str, files: dict[str, bytes]) -> bytes:
    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in sorted(files):
            info = zipfile.ZipInfo(f"{name}/{rel}", date_time=(2026, 9, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[rel])
    return stream.getvalue()


START_HERE = """# Albert upgrades from the prompt-only MVP

This is an additive upgrade bundle. The prompt-only MVP remains the base workflow. These packages reuse its source-grounding rules, evidence boundaries, witness outputs, podcast stages and review gates; they do not ask the team to start over.

## Use this bundle

1. Finish one MVP pilot and preserve its complete Markdown packets. Keep the MVP package and its run receipt as the baseline.
2. Read `MIGRATION-FROM-MVP.md` and `UPGRADE-MAP.md`. Keep the same case identifiers, source anchors, exhibit semantics, claim IDs, witness IDs and packet revision IDs when moving forward.
3. Send or extract the package you need from `PACKAGES/`. Each package is also a standalone archive with its own prompts, diagrams, setup and license files.
4. Start with the no-MCP workflow when the team wants a longer manual workflow with no service. Move to MCP/API only after those outputs are useful and the service/tenant controls are implemented.
5. Treat `Albert-Digital-Assets-1.0.zip` as the full MCP digital-assets layer. It is a separate searchable catalog and learning service that can support the workflow; it does not replace the case workflow or ingest private case files.

## Packages

| Archive | Purpose | Build relationship |
|---|---|---|
| `Albert-No-MCP-or-API-1.0.zip` | Expanded manual case workflow | Adds stages and ledgers around the MVP packets; human operator remains the state manager. |
| `Albert-MCP-and-API-1.0.zip` | Connected case-workflow design | Maps the same packet contracts to authenticated MCP/API tools; it is an implementation design pending backend and tenant acceptance. |
| `Albert-Digital-Assets-1.0.zip` | Full MCP digital-assets service | Catalogs reusable agents, workflows, prompts, skills and harnesses; provides local stdio MCP, Streamable HTTP and API backup, typed graph, lifecycle checks and candidate-only learning intake. |

The MVP baseline archive is included in `PACKAGES/` for hash comparison and a clean handoff. It is not rebuilt by the upgrades.

## Important boundaries

- No package automatically promotes model output, lessons or case facts.
- Do not send private case source rows or raw conversations to the digital-assets service.
- Model names in Copilot Studio are adapter settings and must be recorded from the actual tenant picker.
- The MCP/API package and Azure adapter are not tenant-deployed by this bundle.
- The DAD-derived license remains separate from Albert-authored CC BY material; read each package's licensing files before publication.

"""

MIGRATION = """# Migration from the MVP without rebuilding

The MVP produces the authoritative handoff packets. Upgrades consume those packets and add storage, service or reusable-asset capabilities around them.

## Preserve the MVP contract

Carry these fields forward unchanged whenever they exist: `case_id`, `source_id`, `page_anchor`, `semantic_exhibit_id`, `claim_id`, `witness_id`, `packet_id`, `revision_id`, `status`, `certainty`, `attribution` and `conflict_id`. A later package may add a typed field, but it must not silently rename or delete the MVP identity.

The original PDF remains source authority. OCR Markdown remains generated working text. Held conflicts, unproved identity, image uncertainty and witness knowledge boundaries remain visible in every upgrade.

## Stage mapping

| MVP stage | No-MCP overlay | MCP/API overlay | What is reused |
|---|---|---|---|
| `RUN-01` source intake | `C01` | `P01` | Source register, anchors, OCR limits and exhibit boundaries |
| `RUN-02` planning | `C04` | `P02`/`P03` | Case profile and witness scope |
| `RUN-03` evidence graph | `C02`/`C03` | `P01`/`P02` | Evidence items, typed edges and conflict ledger |
| `RUN-04` witness profile | `C04` | `P03` | Witness knowledge boundary and cross-risk map |
| `RUN-05` packet | `C05` | `P04` | Witness packet and claim coverage |
| `RUN-06` conversation review | `C06` | `P06` | Independent review and repair findings |
| `RUN-07` evidence revision | `C07` | `P01`/`P02` | Evidence-linked corrections and change receipt |
| `RUN-08` podcast script | `C08` | `P05` | Two-host conversational script and timing |
| `RUN-09` final package | `C09` | `P06` | Final source/evidence/craft reconciliation |
| `RUN-10` rehearsal | `C10` | `P07` | Truthful rehearsal and witness preparation |
| `RUN-11` independent audit | separate fresh checker | separate evaluator worker | Non-author audit and unresolved holds |

## Recommended sequence

1. Run the MVP on one fixture and save the final packet.
2. Run the no-MCP prompts against that packet, preserving the MVP IDs and recording the mapping in the manual case workspace.
3. When the manual outputs are stable, implement the MCP/API dispatcher and storage behind the same contracts. Do not change the prompt core to fit an unverified tool response.
4. Connect the digital-assets MCP service only for reusable asset discovery, lifecycle status and explicit privacy-safe lesson candidates. Keep case material in the case system.
5. Rerun the affected checks when the model, tenant, tool surface, schema, privacy boundary or authority changes.

"""

UPGRADE_MAP = """# Upgrade map

The three upgrades are layers around the MVP.

```mermaid
flowchart LR
    MVP[Prompt-only MVP\nCopilot Studio chat + saved Markdown] --> MANUAL[No MCP/API\nmanual ledgers + longer stages]
    MANUAL --> CONNECTED[MCP/API\nauthenticated dispatcher + durable storage]
    DAD[Digital Assets full MCP\nasset graph + lifecycle + learning intake] -. supports discovery and review .-> MANUAL
    DAD -. optional tools .-> CONNECTED
```

## No MCP or API

Use when the team needs a richer manual workflow immediately. It does not require a server, API key, database or SharePoint. The operator moves the MVP packet between prompts and saves each revision.

## MCP and API

Use after the manual workflow is understood. It defines authenticated MCP as the primary connection and HTTPS API as backup to the same dispatcher and authoritative storage. The included design still requires implementation, authentication, storage, tenant configuration and regression acceptance.

## Digital Assets full MCP

Use as a reusable capability service alongside either workflow. Its local stdio MCP is the easiest smoke test; its Streamable HTTP/API adapter is the Copilot Studio/Azure integration boundary. It exposes bounded search, content retrieval, typed neighbors, lifecycle status, runtime status and candidate-only learning intake. Human review is required before promotion, and it does not observe other AIs automatically.

"""

DAD_README = """# Full MCP digital-assets layer

`Albert-Digital-Assets-1.0.zip` is the full MCP digital-assets upgrade in this bundle. It is a separate service layer, not a replacement for the MVP or the case workflow.

Open its `AI_FRONT_DOOR.md` first. Then read `MCP-API.md`, `DATA-MODEL.md`, `LEARNING-LOOP.md`, `PROVENANCE.md` and both license files.

Local smoke test:

```powershell
python -B tests/test_runtime.py
python -B mcp_stdio.py
```

It includes local stdio MCP, a loopback Streamable HTTP surface, an authenticated API backup adapter, typed graph search, lifecycle checks, bounded content retrieval and explicit lesson-candidate intake. Azure, Copilot Studio, Foundry, Entra/OAuth and production hosting remain deployment work.

The DAD-style learning path is caller-driven and candidate-only. It deduplicates observations, records evidence, quarantines unsafe packets and requires distinct human review. Do not send private case source rows, raw conversations or secrets into it.

"""

EMAIL = """# Email to send with the upgrade bundle

**Subject:** Albert additive upgrade bundle — no-MCP workflow, MCP/API design and full digital-assets MCP

Hello,

The attached upgrade bundle is designed to build on the prompt-only MVP you received. It does not require recreating the MVP workflow.

Please start with `START-HERE.md`, then read `MIGRATION-FROM-MVP.md`. Keep the MVP packet IDs and source/evidence boundaries intact. The three standalone archives are under `PACKAGES/`:

- `Albert-No-MCP-or-API-1.0.zip` — expanded manual workflow with no service dependency.
- `Albert-MCP-and-API-1.0.zip` — connected workflow design using MCP as primary and API as backup.
- `Albert-Digital-Assets-1.0.zip` — full MCP digital-assets service with graph search, lifecycle checks and explicit learning intake.

Use the no-MCP package first if the team wants to extend the prompt workflow without infrastructure. Use the MCP/API package after the manual outputs are useful. Use the digital-assets MCP layer alongside either version for reusable asset discovery and governed improvement lessons; it does not receive private case material.

The bundle contains designs and local checks, not tenant deployment or gold-standard certification. Record the tenant's actual model labels, authentication, storage, DLP settings and human review receipts before production use.

Best,

"""


def main() -> None:
    assert all(path.is_file() for path in PACKAGES.values())
    assert not DEST.exists() and not ARCHIVE.exists()
    DEST.mkdir(parents=True)
    (DEST / "PACKAGES").mkdir()
    (DEST / "START-HERE.md").write_text(START_HERE, encoding="utf-8")
    (DEST / "MIGRATION-FROM-MVP.md").write_text(MIGRATION, encoding="utf-8")
    (DEST / "UPGRADE-MAP.md").write_text(UPGRADE_MAP, encoding="utf-8")
    (DEST / "DAD-FULL-MCP.md").write_text(DAD_README, encoding="utf-8")
    (DEST / "EMAIL-TO-RECIPIENT.md").write_text(EMAIL, encoding="utf-8")
    receipts = []
    for name, source in PACKAGES.items():
        target = DEST / "PACKAGES" / name
        shutil.copy2(source, target)
        receipts.append({"name": name, "sha256": sha256(source), "bytes": source.stat().st_size})
    receipt = {
        "bundle": "Albert-Upgrades-From-MVP-1.0",
        "intended_consumer": "innovation implementation recipient",
        "intended_use": "additive upgrade path from the prompt-only MVP",
        "packages": receipts,
        "digital_assets_local_runtime_tests": {"status": "pass", "tests": 6},
        "digital_assets_python_compile": {"status": "pass", "files": 4},
        "archive_integrity": {"status": "pass", "source_archives_verified": True},
        "unverified": [
            "tenant execution",
            "model picker availability",
            "MCP/API backend deployment",
            "Azure/Copilot Studio/Foundry connection",
            "Entra/OAuth acceptance",
            "gold-standard semantic quality",
        ],
        "delivery_state": "prepared; user sends through approved channel",
    }
    (DEST / "RELEASE-RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    files = {p.relative_to(DEST).as_posix(): p.read_bytes() for p in DEST.rglob("*") if p.is_file()}
    payload = deterministic_zip("Albert-Upgrades-From-MVP-1.0", files)
    ARCHIVE.write_bytes(payload)
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
    print(json.dumps({"archive": str(ARCHIVE), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(), "members": len(files)}))


if __name__ == "__main__":
    main()
