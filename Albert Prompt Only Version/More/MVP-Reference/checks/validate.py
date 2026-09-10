"""Optional local functional validation. Not a model, legal, tenant, or DAD assurance certification."""
from pathlib import Path
from urllib.parse import unquote
import argparse, hashlib, importlib.util, json, re

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load_json(p):
    def unique(pairs):
        result={}
        for k,v in pairs:
            if k in result:raise ValueError('duplicate key '+k)
            result[k]=v
        return result
    return json.loads(p.read_text(encoding='utf-8'),object_pairs_hook=unique)

def graph_findings(text):
    findings=[]
    def flag(rule,identity):findings.append({'rule':rule,'identity':identity})
    tables={};section=None
    for line in text.splitlines():
        if line.startswith('## '):section=line[3:].strip().lower();tables.setdefault(section,[])
        elif line.startswith('| ') and section:
            cells=[s.strip() for s in line.strip().strip('|').split('|')]
            if cells[0]=='id' or all(set(x)<=set('-: ') for x in cells):continue
            tables[section].append(cells)
    for required in ['sources','spans','items','claims','grants','conflicts','edges']:
        if required not in tables:flag('MISSING_SECTION',required)
    for required in ['sources','spans','claims','grants','edges']:
        if required in tables and not tables[required]:flag('EMPTY_SECTION',required)
    kinds={'sources':'SOURCE','spans':'SPAN','items':'ITEM','claims':'CLAIM','grants':'GRANT','conflicts':'CONFLICT'}
    nodes={};rows={}
    widths={'sources':5,'spans':6,'items':5,'claims':7,'grants':8,'conflicts':6,'edges':5}
    for section,width in widths.items():
        for row in tables.get(section,[]):
            if len(row)!=width:flag('ROW_SHAPE',section+':'+row[0]);continue
            if section!='edges':
                if row[0] in nodes:flag('DUPLICATE_NODE',row[0])
                else:nodes[row[0]]=kinds[section];rows[row[0]]=row
    edges=tables.get('edges',[])
    seen=set();allowed={'CONTAINS':('SOURCE',{'SPAN'}),'IDENTIFIES_ITEM':('SPAN',{'ITEM'}),'ATTRIBUTES':('SPAN',{'CLAIM'}),'HAS_SIDE_A':('CONFLICT',{'CLAIM'}),'HAS_SIDE_B':('CONFLICT',{'CLAIM'}),'PERMITS':('GRANT',{'SPAN','CLAIM'})}
    for e in edges:
        if len(e)!=5:continue
        eid,a,rel,b,rev=e
        if eid in seen:flag('DUPLICATE_EDGE',eid)
        seen.add(eid)
        if a not in nodes or b not in nodes:flag('DANGLING_EDGE',eid);continue
        if rel not in allowed or nodes[a]!=allowed[rel][0] or nodes[b] not in allowed[rel][1]:flag('EDGE_TYPE',eid)
        if rev!='R01':flag('EDGE_REVISION',eid)
    for nid,kind in nodes.items():
        row=rows[nid]
        if kind=='SPAN':
            parents=[e[1] for e in edges if len(e)==5 and e[2]=='CONTAINS' and e[3]==nid]
            if parents!=[row[1]]:flag('SPAN_PARENT',nid)
            if not row[2].startswith(row[1]+':') or not row[3].startswith(row[1]+':'):flag('SPAN_ANCHOR',nid)
        elif kind=='CLAIM':
            supports=[e[1] for e in edges if len(e)==5 and e[2]=='ATTRIBUTES' and e[3]==nid]
            expected=[s.strip() for s in row[6].split(',')]
            if sorted(supports)!=sorted(expected):flag('CLAIM_SUPPORT_PATH',nid)
        elif kind=='CONFLICT':
            aa=[e[3] for e in edges if len(e)==5 and e[1]==nid and e[2]=='HAS_SIDE_A']
            bb=[e[3] for e in edges if len(e)==5 and e[1]==nid and e[2]=='HAS_SIDE_B']
            if aa!=[row[2]] or bb!=[row[3]] or row[2]==row[3]:flag('CONFLICT_ENDPOINTS',nid)
            if row[5]!='unresolved':flag('CONFLICT_TRUTH_UPGRADE',nid)
        elif kind=='GRANT':
            target_type={'span':'SPAN','proposition':'CLAIM'}.get(row[3])
            targets=[s.strip() for s in row[4].split(',')]
            if not target_type or any(nodes.get(t)!=target_type for t in targets):flag('GRANT_UNIT',nid)
            actual=[e[3] for e in edges if len(e)==5 and e[1]==nid and e[2]=='PERMITS']
            if sorted(actual)!=sorted(targets):flag('GRANT_TARGETS',nid)
    return findings

def validate(graph_path=None,final=False):
    findings=[]
    def flag(rule,identity):findings.append({'rule':rule,'identity':identity})
    imports=load_json(ROOT/'IMPORTS.json')['files']
    for name,entry in imports.items():
        if not (ROOT/name).is_file() or sha(ROOT/name)!=entry['sha256']:flag('IMPORT_DRIFT',name)
    roles=load_json(ROOT/'roles/ROLE-MAP.json')['roles']
    for role,data in roles.items():
        content=(ROOT/data['instruction_file']).read_text(encoding='utf-8')
        if len(content)>8000 or len(data['name'])>42 or len(data['description'])>1024:flag('STUDIO_FIELD_LIMIT',role)
        if len(content)!=data['instructions_characters']:flag('ROLE_LENGTH_RECORD',role)
    wf=load_json(ROOT/'workflow.json');ids=[n['id'] for n in wf['nodes']]
    if len(set(ids))!=len(ids):flag('WORKFLOW_DUPLICATE_ID','nodes')
    for a,b,_ in wf['edges']:
        if a not in ids or b not in ids:flag('WORKFLOW_EDGE_TARGET',a+'->'+b)
    for n in wf['nodes']:
        placement=(ROOT/'07-PROMPT-PLACEMENT.md').read_text(encoding='utf-8')
        expected_row=f"| {n['id']} | {n['role']} | [{n['file']}]({n['file']}) | {n['inputs']} | {n['outputs']} |"
        if expected_row not in placement:flag('PLACEMENT_DRIFT',n['id'])
        expected_parts='| '+n['id']+' | '+', '.join('['+p+']('+p+')' for p in n['paste_parts'])+' |'
        if expected_parts not in placement:flag('PLACEMENT_PARTS_DRIFT',n['id'])
        text=(ROOT/n['file']).read_text(encoding='utf-8')
        for mod in n['modules']:
            source=(ROOT/mod['file']).read_text(encoding='utf-8-sig').strip()
            if sha(ROOT/mod['file'])!=mod['sha256']:flag('MODULE_DIGEST',n['id']+':'+mod['id'])
            marker='<!-- BEGIN CORE '+mod['id']+' -->\n```text\n'+source+'\n```\n<!-- END CORE '+mod['id']+' -->'
            if marker not in text:flag('MODULE_BODY',n['id']+':'+mod['id'])
        parts=[]
        for part in n['paste_parts']:
            p=(ROOT/part).read_text(encoding='utf-8')
            if len(p)>5000:flag('PASTE_PART_LIMIT',part)
            chunk=p.split('BEGIN_PART\n',1)[1].rsplit('\nEND_PART',1)[0]
            parts.append(chunk)
        if ''.join(parts).strip()!=text.strip():flag('PASTE_RECONSTRUCTION',n['id'])
    spec=importlib.util.spec_from_file_location('views',ROOT/'checks/generate_views.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    for name,text in module.expected().items():
        if not (ROOT/name).is_file() or (ROOT/name).read_text(encoding='utf-8')!=text:flag('VIEW_DRIFT',name)
    render_path=ROOT/'diagrams/RENDER-RECEIPT.json'
    if render_path.is_file():
        rendered=load_json(render_path)
        if rendered['workflow_sha256']!=sha(ROOT/'workflow.json') or rendered['generator_sha256']!=sha(ROOT/'checks/generate_views.py'):flag('RENDER_INPUT_DRIFT','receipt')
        for rendered_file in rendered['files']:
            for suffix,key in [('mmd','source_sha256'),('svg','svg_sha256'),('png','png_sha256')]:
                view=ROOT/'diagrams'/(rendered_file['name']+'.'+suffix)
                if not view.is_file() or sha(view)!=rendered_file[key]:flag('RENDER_OUTPUT_DRIFT',view.name)
    elif final:flag('RENDER_RECEIPT_MISSING','diagrams')
    allowed_pending={'QA.md','diagrams/D01-WORKFLOW.svg','diagrams/D02-SETUP.svg','diagrams/D03-GRAPH.svg','checks/NEGATIVE-RESULTS.json','checks/DEMO-MEASUREMENTS.json'} if not final else set()
    links=0
    for file in ROOT.rglob('*.md'):
        text=re.sub(r'```.*?```','',file.read_text(encoding='utf-8-sig'),flags=re.S)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
            if target.startswith(('https://','http://','#')):continue
            rel=unquote(target.split('#',1)[0]);p=(file.parent/rel).resolve()
            if not p.is_relative_to(ROOT.resolve()):flag('LINK_ESCAPE',str(file.relative_to(ROOT))+':'+target);continue
            if not p.is_file() and p.relative_to(ROOT).as_posix() not in allowed_pending:flag('BROKEN_LINK',str(file.relative_to(ROOT))+':'+target)
            links+=1
    selected=(ROOT/(graph_path or 'demo/WORKED-GRAPH.md')).resolve()
    if not selected.is_relative_to(ROOT.resolve()):flag('GRAPH_ESCAPE',str(graph_path))
    else:findings.extend(graph_findings(selected.read_text(encoding='utf-8')))
    return {'status':'PASS' if not findings else 'FAIL','scope':'local functional packaging/graph checks; no semantic-source, model, tenant or formal DAD assurance qualification','graph':str(selected.relative_to(ROOT)),'graph_sha256':sha(selected),'links_checked':links,'findings':findings}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--graph');p.add_argument('--final',action='store_true');a=p.parse_args()
    result=validate(a.graph,a.final);print(json.dumps(result,indent=2));raise SystemExit(0 if result['status']=='PASS' else 1)
