"""Allowlisted fresh public tree; never copies private Git history or fixture archives."""
from pathlib import Path
import shutil, hashlib, json
R=Path(__file__).resolve().parents[1]
D=R/'public-release'
if D.exists():
    raise SystemExit('Refusing to overwrite existing release directory')
files=['README.md','AI_FRONT_DOOR.md','AI-TOC.md','LICENSE','LICENSE.md','CONTRIBUTING.md']
folders=['Albert Prompt Only Version','Albert MCP and API Version','Albert No MCP or API Version','Extras']
D.mkdir()
for f in files: shutil.copyfile(R/f,D/f)
for folder in folders:
    for p in (R/folder).rglob('*'):
        if not p.is_file() or any(x in {'__pycache__','.pytest_cache','state'} or x.startswith('tmp') for x in p.relative_to(R/folder).parts): continue
        if p.suffix.lower() in {'.zip','.pdf','.pyc','.pfx','.pem','.key'}: raise SystemExit(f'Forbidden public artifact: {p.name}')
        q=D/p.relative_to(R);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
(D/'SECURITY.md').write_text('# Security\n\nDo not submit credentials, client records, or licensed case files. Report sensitive issues privately to the owner. Mini DAD requires tenant authentication and deployment acceptance before production use.\n',encoding='utf-8')
(D/'.gitignore').write_text('__pycache__/\n.pytest_cache/\n.venv/\n.env\n.env.*\n**/state/\n**/tests/tmp*/\nprivate/\n',encoding='utf-8')
(D/'.gitattributes').write_text('* -text\n',encoding='utf-8')
manifest={p.relative_to(D).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(D.rglob('*')) if p.is_file()}
(D/'RELEASE-CONTENTS.json').write_text(json.dumps({'edition':'public-2026-09-10','files':manifest},indent=2)+'\n',encoding='utf-8')
print(f'{len(manifest)} allowlisted files prepared; no prior Git history')
