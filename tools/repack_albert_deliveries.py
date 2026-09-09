from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def collect(folder: Path) -> dict[str, bytes]:
    excluded = {"__pycache__", ".git"}
    files: dict[str, bytes] = {}
    for path in folder.rglob("*"):
        if not path.is_file() or any(part in excluded for part in path.parts):
            continue
        rel = path.relative_to(folder).as_posix()
        if rel == "CONTENTS.json" or any(part.startswith("tmp") for part in path.relative_to(folder).parts):
            continue
        files[rel] = path.read_bytes()
    return files


def zip_bytes(name: str, files: dict[str, bytes]) -> bytes:
    from io import BytesIO

    stream = BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in sorted(files):
            info = zipfile.ZipInfo(f"{name}/{rel}", date_time=(2026, 9, 9, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[rel])
    with zipfile.ZipFile(BytesIO(stream.getvalue())) as archive:
        assert archive.testzip() is None
    return stream.getvalue()


def repack(folder_name: str) -> None:
    folder = OUT / folder_name
    files = collect(folder)
    receipt = {
        "package": folder_name,
        "status": "presentation package; local checks only",
        "files": {rel: {"sha256": sha(data), "bytes": len(data)} for rel, data in sorted(files.items())},
        "excludes": ["CONTENTS.json", "__pycache__", "tests/tmp*"],
        "native_visio_open": "unverified; desktop Visio unavailable",
        "tenant_execution": "unverified",
    }
    (folder / "CONTENTS.json").write_bytes(json_bytes(receipt))
    files["CONTENTS.json"] = json_bytes(receipt)
    payload = zip_bytes(folder_name, files)
    archive = OUT / f"{folder_name}.zip"
    archive.write_bytes(payload)
    with zipfile.ZipFile(archive) as check:
        assert check.testzip() is None
        assert not any("__pycache__" in n or "/tmp" in n for n in check.namelist())
    print(json.dumps({"package": folder_name, "members": len(files), "bytes": len(payload), "sha256": sha(payload)}))


if __name__ == "__main__":
    for package in ("Albert-MVP-Prompts-1.0", "Albert-No-MCP-or-API-1.0", "Albert-MCP-and-API-1.0", "Albert-Digital-Assets-1.0"):
        repack(package)
