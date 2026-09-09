"""Run the aggregate validator in isolated subprocesses. No optional dependencies."""
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(graph):
    p=subprocess.run([sys.executable,'-B',str(ROOT/'checks/validate.py'),'--graph',graph],capture_output=True,text=True,encoding='utf-8',timeout=30)
    if p.returncode not in [0,1]:raise AssertionError('Validator crashed: '+p.stderr)
    data=json.loads(p.stdout)
    assert data['status']==('PASS' if p.returncode==0 else 'FAIL')
    return data
def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt');args=p.parse_args()
    catalog=json.loads((ROOT/'checks/FIXTURES.json').read_text(encoding='utf-8'))
    assert sha(ROOT/catalog['baseline'])==catalog['baseline_sha256'],'baseline drift'
    baseline=run(catalog['baseline']);assert baseline['findings']==[],'baseline has findings: '+str(baseline['findings'])
    receipts=[]
    for order,cases in [('forward',catalog['cases']),('reverse',list(reversed(catalog['cases'])))]:
        for case in cases:
            assert sha(ROOT/case['file'])==case['sha256'],'fixture drift'
            result=run(case['file'])
            assert result['findings']==case['expected_findings'],(case['file'],result['findings'])
            assert result['status']=='FAIL'
            receipts.append({'order':order,'graph':case['file'],'graph_sha256':case['sha256'],'first_guard':result['findings'][0]['rule'],'complete_findings':result['findings']})
    baseline_after=run(catalog['baseline']);assert baseline_after['findings']==[]
    result={'status':'PASS','scope':'local functional aggregate-validator tests; not semantic source checks or formal DAD assurance qualification','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline_before':baseline,'baseline_after':baseline_after,'validator_sha256':sha(ROOT/'checks/validate.py'),'runner_sha256':sha(Path(__file__)),'catalog_sha256':sha(ROOT/'checks/FIXTURES.json'),'negative_runs':receipts}
    if args.receipt:
        target=(ROOT/args.receipt).resolve();assert target.is_relative_to(ROOT.resolve())
        with target.open('x',encoding='utf-8',newline='\n') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':'PASS','negative_cases':len(catalog['cases']),'negative_runs':len(receipts),'clean_baselines':2}))
if __name__=='__main__':main()
