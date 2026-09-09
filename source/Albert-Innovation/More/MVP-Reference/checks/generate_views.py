"""Generate starter views from workflow.json. Optional maintainer tool, no runtime dependency."""
from pathlib import Path
import argparse, hashlib, json, os

ROOT=Path(__file__).resolve().parents[1]
def expected():
    wf=json.loads((ROOT/'workflow.json').read_text())
    roles=json.loads((ROOT/'roles/ROLE-MAP.json').read_text())['roles']
    sha=hashlib.sha256((ROOT/'workflow.json').read_bytes()).hexdigest()
    ids={n['id'] for n in wf['nodes']}
    if len(ids)!=11 or any(a not in ids or b not in ids for a,b,_ in wf['edges']):raise ValueError('Invalid workflow node/edge identities')
    colors=['  classDef work fill:#eaf2ff,stroke:#315f96,color:#123047','  classDef review fill:#fff4d9,stroke:#ad7515,color:#493500','  classDef human fill:#e5f3e9,stroke:#387850,color:#143522','  classDef stop fill:#fcebec,stroke:#aa4755,color:#59212c']
    a=['flowchart TD',f'  %% Generated from workflow.json SHA-256 {sha}',*colors]
    for n in wf['nodes']:
        style='review' if n['role'] in ['EVIDENCE','CONVERSATION','NON_AUTHOR_REVIEWER'] else 'work'
        title=n['file'].split('/')[-1].split('.',1)[0].replace(n['id']+'-','').replace('-',' ').title()
        a.append('  '+n['id'].replace('-','')+'["'+n['id']+' · '+title+'<br/>'+n['role'].title().replace('_',' ')+'"]:::'+style)
    for f,t,label in wf['edges']:
        # Display the manifest's acceptance edge through its human owner once.
        if (f,t)==('RUN-07','RUN-10'):continue
        a.append(f'  {f.replace("-","")} -->|"{label}"| {t.replace("-","")}')
    a += ['  HOLD["HOLD<br/>Keep evidence and next input"]:::stop','  RUN07 -->|"unresolved after one repair / missing gate"| HOLD','  OWNER["Human operator<br/>Accept exact internal-use candidate"]:::human','  RUN07 -->|"candidate recommendation"| OWNER','  OWNER -->|"actual acceptance recorded"| RUN10','  RUN11 -.->|"propose next tested revision; no auto adoption"| OWNER']
    b=['flowchart LR',f'  %% Roles from ROLE-MAP; workflow SHA-256 {sha}',*colors,
       '  RAW["Authorized source files"]:::work','  ANALYST["Albert Case Analyst<br/>Source + typed graph"]:::work','  HUMAN["Operator checks scope<br/>Saves and reopens VIEW"]:::human','  VIEW["Permitted view + raw spans<br/>Actual grant and intended use"]:::work','  WRITER["Albert Writer<br/>Plan → chapters → full assembly"]:::work','  EVIDENCE["Albert Evidence Reviewer<br/>Complete raw-source check"]:::review','  CRAFT["Albert Conversation Reviewer<br/>Full listening / practice check"]:::review','  FILES["Operator-owned files<br/>Graph · scripts · reviews · revisions"]:::human','  AUTHOR["Separate author-only ledger<br/>Not sent to Writer/Craft"]:::stop','  CHILD["Optional Source Trace Helper<br/>Shares analyst parent context"]:::work',
       '  RAW --> ANALYST','  ANALYST --> HUMAN','  HUMAN --> VIEW','  ANALYST --> AUTHOR','  VIEW --> WRITER','  VIEW --> EVIDENCE','  RAW -->|"authorized evidence scope"| EVIDENCE','  VIEW --> CRAFT','  WRITER -->|"same frozen full assembly"| EVIDENCE','  WRITER -->|"same frozen full assembly"| CRAFT','  EVIDENCE --> FILES','  CRAFT --> FILES','  WRITER -->|"operator copies outputs"| FILES','  FILES -.->|"reopen current packet"| HUMAN','  ANALYST -.->|"optional TRACE / same scope"| CHILD','  CHILD -.->|"bounded evidence packet"| ANALYST']
    for role,label in [('ANALYST','Albert Case Analyst'),('WRITER','Albert Writer'),('EVIDENCE','Albert Evidence Reviewer'),('CONVERSATION','Albert Conversation Reviewer')]:
        b=[line.replace(label,roles[role]['name']) for line in b]
    c=['flowchart LR',f'  %% Graph contract projection; workflow SHA-256 {sha}',*colors,
       '  S["SOURCE<br/>Raw file + revision"]:::work','  SP["SPAN<br/>Exact anchors + qualifiers"]:::work','  EX["ITEM<br/>Distinct exhibit / attachment"]:::work','  C1["CLAIM A<br/>Attributed meaning + time"]:::work','  C2["CLAIM B<br/>Different attributed account"]:::work','  CF["CONFLICT<br/>Question; no truth winner"]:::review','  PG["OWNER GRANT<br/>Unit + use + witness + time"]:::human','  AR["ARTIFACT<br/>Plan / script / card / T06"]:::work','  RV["REVIEW + DECISION<br/>Exact assembly + full read"]:::review','  NX["NEXT REVISION<br/>Old results retained / stale"]:::stop',
       '  S -->|"CONTAINS exactly one parent"| SP','  SP -->|"IDENTIFIES_ITEM"| EX','  SP -->|"ATTRIBUTES"| C1','  CF -->|"HAS_SIDE_A"| C1','  CF -->|"HAS_SIDE_B; distinct"| C2','  PG -->|"PERMITS span unit"| SP','  PG -->|"or proposition unit"| C1','  AR -->|"USES permitted claims / sources"| C1','  AR -->|"USES applicable grant"| PG','  AR -->|"USES both permitted endpoints"| CF','  RV -->|"ASSESSES exact revision"| AR','  AR -.->|"changed dependency marks descendants stale"| NX']
    return {'diagrams/D01-WORKFLOW.mmd':'\n'.join(a)+'\n','diagrams/D02-SETUP.mmd':'\n'.join(b)+'\n','diagrams/D03-GRAPH.mmd':'\n'.join(c)+'\n'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
    results=[]
    for name,text in expected().items():
        target=ROOT/name
        if args.write:
            target.parent.mkdir(parents=True,exist_ok=True)
            # Explicit regeneration of derived views, not mutation of the source manifest.
            before=target.read_bytes() if target.exists() else None
            pending=target.with_suffix(target.suffix+'.pending')
            with pending.open('x',encoding='utf-8',newline='\n') as h:h.write(text)
            current=target.read_bytes() if target.exists() else None
            if current!=before:raise SystemExit('Concurrent view edit; retained '+str(pending))
            os.replace(pending,target)
        elif not target.is_file() or target.read_text(encoding='utf-8')!=text:raise SystemExit('VIEW_DRIFT: '+name)
        results.append(name)
    print(json.dumps({'generated_or_checked':results}))
