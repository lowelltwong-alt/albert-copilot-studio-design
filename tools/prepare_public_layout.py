"""Prepare self-contained human entry points from the frozen release packages."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    'Albert Prompt Only Version': 'Albert-MVP-Prompts-1.0.zip',
    'Albert MCP and API Version': 'Albert-MCP-and-API-1.0.zip',
    'Albert No MCP or API Version': 'Albert-No-MCP-or-API-1.0.zip',
    'Extras/Mini DAD': 'Albert-Digital-Assets-1.0.zip',
}
for dest, archive in PACKS.items():
    base = ROOT / dest
    if base.exists():
        raise SystemExit(f'Refusing to overwrite {dest}')
    with zipfile.ZipFile(ROOT / 'packages' / archive) as z:
        for member in z.infolist():
            rel = Path(*Path(member.filename).parts[1:])
            if not rel.parts or member.is_dir():
                continue
            if '..' in rel.parts or rel.is_absolute():
                raise ValueError('Unsafe archive path')
            # Original receipts are historical evidence, not new package manifests.
            if rel.as_posix() == 'CONTENTS.json':
                rel = Path('More/ORIGINAL-PACKAGE-CONTENTS.json')
            target = base / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(member))
    print(dest)
