from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from io import BytesIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs" / "Albert-MVP-Prompts-1.0"
SOURCE_ZIP = ROOT / "outputs" / "Albert-MVP-Prompts-1.0.zip"
DEST = ROOT / "outputs" / "Albert-MVP-Send-Ready-1.1"
ARCHIVE = ROOT / "outputs" / "Albert-MVP-Send-Ready-1.1.zip"
MVP_HASH = hashlib.sha256(SOURCE_ZIP.read_bytes()).hexdigest()
CASE_SOURCE = ROOT / "work" / "mvp_case_fixture_source"
CASE_FIXTURES = {
    "MSIMOTO": {
        "label": "Msimoto Fire",
        "slug": "msimoto-fire",
        "pdf": CASE_SOURCE / "MSIMOTO-original.pdf",
        "ocr": CASE_SOURCE / "MSIMOTO-ocr.md",
        "description": "fire-insurance mock-trial case",
    },
    "KEMPER": {
        "label": "Kemper v. Nita City Cubs",
        "slug": "kemper-city-cubs",
        "pdf": CASE_SOURCE / "KEMPER-original.pdf",
        "ocr": CASE_SOURCE / "KEMPER-ocr.md",
        "description": "baseball stadium bat-injury mock-trial case",
    },
    "EVANS": {
        "label": "Evans v. Nita State University",
        "slug": "evans-professor",
        "pdf": CASE_SOURCE / "EVANS-original.pdf",
        "ocr": CASE_SOURCE / "EVANS-ocr.md",
        "description": "university cyberbullying case involving an adjunct professor",
    },
}

QUICK_START = f'''# Albert MVP — send-ready quick start

This pack contains the prompt-only MVP. Start with the extracted `MVP/START-HERE.md`. The MVP is independent of MCP, API, SharePoint, the Digital Assets package and the two future upgrade packages.

## First run

1. In standard Copilot Studio, create four unpublished agents.
2. In each agent's **Overview → Instructions**, paste the exact ROLE file listed below. Select the proposed model only if it is available in your tenant; record the actual model if the label differs.
3. Open `MVP/WORKFLOWS/README.md` and `MVP/PROMPTS/00-PLACEMENT.md`.
4. Run the numbered RUN prompts in the Test agent chat. The operator saves, reopens and copies the complete Markdown packet between roles.
5. Choose one of the three included case fixtures in `CASE-FIXTURE/`: Msimoto Fire, the City Cubs baseball-bat case, or Evans v. Nita State University (the professor case). Keep the selected PDF as source authority and its paired OCR Markdown as a convenience working copy.

## First case-file run after setup

1. Open the selected fixture's `README.md` and confirm the rights and source-authority note.
2. Add both files from that fixture folder to the case input. If the tenant supports file upload, attach its original PDF and paired OCR Markdown. If it supports only one file, use the PDF first and paste or upload the OCR Markdown in a second source step.
3. Send the exact text in that fixture's `CASE-START-PROMPT.md` to the Case Analyst Test agent. It tells the Analyst to compare the two representations, preserve page/exhibit boundaries and hold OCR uncertainty instead of silently repairing it.
4. Run `RUN-01` through `RUN-11` in the order in `MVP/More/02-RUN-GUIDE.md`, saving the complete Markdown packet after each handoff. The first run is a pilot exercise; review its source, conflict, podcast and witness-preparation outputs before using a live case.
5. If the agent cannot ingest the PDF, keep it beside the run as the visual authority and use that fixture's OCR Markdown as the text input. Record that limitation in the source ledger and do not call the result gold-standard.

| Agent | Exact Instructions file | Proposed pilot model | Test-chat prompts |
|---|---|---|---|
| Case Analyst | `MVP/PROMPTS/ROLE-ANALYST.md` | GPT-5.5 | RUN-01 |
| Writer | `MVP/PROMPTS/ROLE-WRITER.md` | Claude Sonnet 4.6 | RUN-02, RUN-04, RUN-08, RUN-10 |
| Evidence Reviewer | `MVP/PROMPTS/ROLE-EVIDENCE.md` | GPT-5.5 | RUN-03, RUN-05, RUN-07, RUN-09 |
| Conversation Reviewer | `MVP/PROMPTS/ROLE-CONVERSATION.md` | GPT-5.5 | RUN-06 |

Run RUN-11 only as a separate non-author audit. Do not let a reviewer audit its own work.

## What to save

Keep the complete graph/view, source ledger, witness packet, plan, evidence review, conversation review, final two-host script, timing sheet and witness preparation card. Preserve the input and output Markdown exactly at each handoff. The MVP has no automatic file storage; the operator is the state manager.

## Acceptance check

Before treating a run as useful, verify that claims are source-linked or held, conflicts remain visible, unproved identity/details are not invented, both speakers contribute naturally, examination lessons are taught, and the independent reviewer can explain every repair. The bundled synthetic example is a held development candidate, not a gold-standard or tenant-acceptance result.

The included case files are a private test fixture. Do not publish the PDF or redistribute it outside the rights held by the recipient. The PDF is authoritative; the OCR Markdown is generated working text and may contain recognition errors.

## Package identity

Standalone MVP ZIP SHA-256: `{MVP_HASH}`

'''

EMAIL = f'''# Email to send with the MVP

**Subject:** Albert MVP — prompt-only Copilot Studio pilot

Hello,

I’m sending the first Albert package as a prompt-only Copilot Studio pilot. It is intentionally self-contained: no MCP server, API, SharePoint connection or database is required. The purpose of this first run is to see whether the source-grounded workflow produces a useful podcast transcript and witness-preparation work product before connecting the later versions.

Please extract the pack and open `MVP/START-HERE.md`. The short setup is:

1. Create four unpublished agents in standard Copilot Studio.
2. Paste each exact ROLE file into the agent’s **Overview → Instructions** field.
3. Select the proposed model if it is available, and record the actual model if your picker uses a different label.
4. Open `MVP/WORKFLOWS/README.md` and follow `MVP/PROMPTS/00-PLACEMENT.md`.
5. Run the numbered prompts in the Test agent chat, saving and reopening each complete Markdown packet before copying it to the next role.
6. Choose a folder under `CASE-FIXTURE/`, add its original PDF and paired OCR Markdown as the case inputs, and send that folder's exact `CASE-START-PROMPT.md` text to the Case Analyst. If file upload is unavailable, use the OCR Markdown as text input while retaining the PDF for source review.
7. Run `RUN-01` through `RUN-11` in order, saving each complete Markdown handoff. `MVP/More/02-RUN-GUIDE.md` explains what to paste, what to save and which reviewer must be independent.
8. Review the source, evidence, conversation quality, timing and witness-preparation outputs together. The synthetic case in `MVP/More/02-RUN-GUIDE.md` remains available as a smaller workflow check.

The expected work product is a source graph and ledger, witness profile and packet, evidence and conflict review, a two-host conversational script, a podcast-quality review, timing/export instructions and a witness-preparation card. It creates no audio. It should not be treated as approved legal advice, a gold-standard producer or a tenant-validated deployment until the team reviews the outputs.

The two future packages are included only as orientation in `FUTURE-PACKAGES.md`. **No MCP or API** is the expanded manual workflow after this pilot. **MCP and API** is the connected design, which still needs its full case-processing backend and tenant acceptance. **Digital Assets with MCP** is a separate optional DAD-style catalog and learning service; it is not required for this MVP.

The included case files are private test materials. Keep each PDF under the recipient's existing license and do not publish or redistribute it. Each PDF is source authority; its paired OCR Markdown is a generated convenience copy and must be checked against the PDF where the text, layout or exhibit boundary is uncertain.

Please record the actual model labels, run date, source packet, output files, held conflicts and any proposed repairs. Keep the original PDF private and use the OCR Markdown only as a convenience copy. The standalone MVP ZIP SHA-256 is `{MVP_HASH}` for version checking; the case fixture hashes are in `HANDOFF-RECEIPT.json`.

Best,

'''

CASE_README_TEMPLATE = '''# {label} case fixture

This folder is included so the first MVP pilot can start with a real, source-grounded test instead of an empty chat. It is the {description}.

## Files

- `{pdf_name}` — original case-file PDF. Treat this as the source authority.
- `{ocr_name}` — our existing OCR-derived Markdown snapshot. It is a working convenience copy, not source truth; preserve uncertainty and compare it to the PDF when the two differ.
- `CASE-START-PROMPT.md` — the exact first message to send after the Case Analyst agent is configured.

## Use and rights

This is a private test fixture for the recipient's licensed mock-trial work. Do not publish, commit to a public repository, or redistribute the PDF unless the recipient has the right to do so. The package contains no OCR engine; it only supplies the existing OCR snapshot so the prompt-only MVP can be exercised.

## Source boundary

The PDF is authoritative. The OCR Markdown may have recognition errors, missing layout, and imperfect exhibit boundaries. The Analyst must keep page anchors, semantic exhibit boundaries and conflicts visible, and must not turn an OCR guess into a fact. If the tenant cannot ingest the PDF, record that limitation in the source ledger and keep the PDF beside the run for human review.

## Integrity

- Original PDF SHA-256: `{pdf_hash}`
- OCR Markdown SHA-256: `{ocr_hash}`

'''

CASE_START_TEMPLATE = '''# Case Analyst — first run with the included {label} fixture

Use the two attached files as a paired source set:

1. `{pdf_name}` is the authority. Use it to resolve page layout, images, exhibits and any OCR ambiguity.
2. `{ocr_name}` is generated working text. Use it for searchable text, but do not promote an OCR guess to a fact.

Run the MVP source intake and produce the normal RUN-01 handoff. Preserve page anchors and semantic exhibit boundaries even where the document does not label an item "Exhibit." For every material statement, record source file, page or section anchor, speaker or document attribution, certainty, and whether the witness would know it. List OCR uncertainty and every PDF/OCR discrepancy for later review. Do not summarize beyond the supplied files, add outside facts, invent a speaker, or state that an image proves more than the source shows.

End with the complete Markdown packet required by RUN-01 and a short `INPUT-LIMITATIONS` section stating whether the PDF was directly readable in this tenant and which pages or exhibits need human visual review.
'''

FIXTURE_INDEX = '''# Included case fixtures

Choose one folder for the first run. Each folder contains an original PDF, its paired OCR Markdown working copy, a source-boundary README and an exact Case Analyst start prompt.

| Folder | Use it for |
|---|---|
| `msimoto-fire/` | Msimoto Fire insurance mock-trial case |
| `kemper-city-cubs/` | Nita City Cubs baseball-bat injury case |
| `evans-professor/` | Evans v. Nita State University, involving adjunct Professor Jamie Winstone |

For every folder, the PDF is source authority. The OCR Markdown is searchable convenience text and may contain recognition or layout errors. Keep these files private and confirm redistribution rights before publication.
'''


def case_metadata(key: str, spec: dict[str, object]) -> dict[str, object]:
    pdf = spec["pdf"]
    ocr = spec["ocr"]
    assert isinstance(pdf, Path) and isinstance(ocr, Path)
    return {
        "key": key,
        "label": spec["label"],
        "slug": spec["slug"],
        "description": spec["description"],
        "pdf": pdf,
        "ocr": ocr,
        "pdf_name": pdf.name,
        "ocr_name": ocr.name,
        "pdf_hash": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "ocr_hash": hashlib.sha256(ocr.read_bytes()).hexdigest(),
    }

FUTURE = '''# What the other packages are for

The MVP is the only package needed for the first Copilot Studio pilot. Keep the other packages separate until the MVP's source, evidence and conversation checks are useful.

## No MCP or API

`Albert-No-MCP-or-API-1.0.zip` expands the same source-grounded idea into a longer manual workflow. It gives one all-in-one prompt, explicit case/exhibit ledgers, storage templates, acceptance checklists and detailed diagrams. It still relies on human packet handoffs and does not need a server.

## MCP and API

`Albert-MCP-and-API-1.0.zip` describes the connected architecture, service contracts, API/MCP connector shapes and durable storage boundaries. It is an implementation design, not a completed full Albert case-processing backend. Do not present it as deployed until the backend, authentication, tenant and regression tests exist.

## Digital Assets with MCP

`Albert-Digital-Assets-1.0.zip` is an independent, reusable digital-assets service. It catalogs agents, workflows, skills, prompts and harnesses; exposes typed graph search and lifecycle checks; and accepts explicit privacy-safe lesson candidates. It does not observe another AI automatically, does not promote lessons, and is not required by the prompt-only MVP. Open its `AI_FRONT_DOOR.md` before connecting it.

'''


def deterministic_zip(name: str, files: dict[str, bytes]) -> bytes:
    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in sorted(files):
            info = zipfile.ZipInfo(f"{name}/{rel}", date_time=(2026, 9, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[rel])
    return stream.getvalue()


def main() -> None:
    assert SOURCE.is_dir() and SOURCE_ZIP.is_file()
    assert all(spec["pdf"].is_file() and spec["ocr"].is_file() for spec in CASE_FIXTURES.values())
    assert not DEST.exists() and not ARCHIVE.exists()
    DEST.mkdir(parents=True)
    (DEST / "MVP").mkdir()
    shutil.copytree(SOURCE, DEST / "MVP", dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "tests/tmp*"))
    (DEST / "CASE-FIXTURE").mkdir()
    (DEST / "CASE-FIXTURE" / "README.md").write_text(FIXTURE_INDEX, encoding="utf-8")
    fixture_receipts = []
    for key, spec in CASE_FIXTURES.items():
        meta = case_metadata(key, spec)
        folder = DEST / "CASE-FIXTURE" / str(meta["slug"])
        folder.mkdir()
        shutil.copy2(meta["pdf"], folder / str(meta["pdf_name"]))
        shutil.copy2(meta["ocr"], folder / str(meta["ocr_name"]))
        (folder / "README.md").write_text(CASE_README_TEMPLATE.format(**meta), encoding="utf-8")
        (folder / "CASE-START-PROMPT.md").write_text(CASE_START_TEMPLATE.format(**meta), encoding="utf-8")
        fixture_receipts.append({
            "key": meta["key"],
            "label": meta["label"],
            "folder": f"CASE-FIXTURE/{meta['slug']}/",
            "authority": f"CASE-FIXTURE/{meta['slug']}/{meta['pdf_name']}",
            "working_copy": f"CASE-FIXTURE/{meta['slug']}/{meta['ocr_name']}",
            "pdf_sha256": meta["pdf_hash"],
            "pdf_bytes": meta["pdf"].stat().st_size,
            "ocr_sha256": meta["ocr_hash"],
            "ocr_bytes": meta["ocr"].stat().st_size,
        })
    (DEST / "START-HERE.md").write_text(QUICK_START, encoding="utf-8")
    (DEST / "EMAIL-TO-RECIPIENT.md").write_text(EMAIL, encoding="utf-8")
    (DEST / "FUTURE-PACKAGES.md").write_text(FUTURE, encoding="utf-8")
    receipt = {
        "pack": "Albert-MVP-Send-Ready-1.1",
        "mvp_zip_sha256": MVP_HASH,
        "mvp_zip_bytes": SOURCE_ZIP.stat().st_size,
        "intended_consumer": "innovation implementation recipient",
        "intended_use": "first prompt-only Copilot Studio pilot",
        "contents": ["START-HERE.md", "EMAIL-TO-RECIPIENT.md", "FUTURE-PACKAGES.md", "CASE-FIXTURE/", "MVP/"],
        "case_fixtures": fixture_receipts,
        "rights_note": "Private test fixtures; recipient must confirm redistribution rights before any publication.",
        "mvp_local_status": "prompt packet, graph, link and local checks passed; synthetic example held",
        "unverified": ["tenant execution", "model picker availability", "audio generation", "gold-standard quality"],
        "delivery_state": "prepared; user sends through approved channel",
    }
    (DEST / "HANDOFF-RECEIPT.json").write_bytes((json.dumps(receipt, indent=2) + "\n").encode())
    files = {p.relative_to(DEST).as_posix(): p.read_bytes() for p in DEST.rglob("*") if p.is_file()}
    payload = deterministic_zip("Albert-MVP-Send-Ready-1.1", files)
    ARCHIVE.write_bytes(payload)
    with zipfile.ZipFile(ARCHIVE) as archive:
        assert archive.testzip() is None
    print(json.dumps({"pack": str(ARCHIVE), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(), "members": len(files)}))


if __name__ == "__main__":
    main()
