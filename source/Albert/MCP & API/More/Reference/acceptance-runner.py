"""Run protocol reference cases or a separately implemented isolated real-service adapter.
No network calls are made by this runner itself. Missing service adapter exits 2.
"""
from pathlib import Path
import argparse, importlib.util, json, hashlib, copy, sys
BASE=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['reference','service'],required=True)
    p.add_argument('--adapter',type=Path)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    adapter=args.adapter if args.mode=='service' else BASE/'reference_rules.py'
    if adapter is None or not adapter.is_file():
        print(json.dumps({'status':'blocked','reason':'Real service adapter is not supplied; no product checks ran.'}));return 2
    spec=importlib.util.spec_from_file_location('albert_acceptance_adapter',adapter)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    catalog_path=BASE/'acceptance-catalog.json';catalog=json.loads(catalog_path.read_text(encoding='utf-8'))
    results=[]
    for order in ['forward','reverse']:
        fixtures=catalog['fixtures'] if order=='forward' else list(reversed(catalog['fixtures']))
        for fixture in fixtures:
            # The adapter gets neither expected outcomes nor fixture IDs. Each call must be isolated.
            clean=mod.run_fixture(copy.deepcopy(catalog['clean_state']))
            actual=mod.run_fixture(copy.deepcopy(fixture['state']))
            delta=[x for x in actual['findings'] if x not in clean['findings']]
            passed=(clean=={'findings':[],'primary':None} and actual['findings']==fixture['expected_findings'] and actual['primary']==fixture['expected_primary'] and delta==fixture['expected_delta_from_clean'])
            results.append({'id':fixture['id'],'order':order,'passed':passed,'clean':clean,'actual':actual,'delta':delta})
    report={'mode':args.mode,'status':'passed_selected_cases' if all(x['passed'] for x in results) else 'failed','production_qualified':False,'scope':'Reference rules only; no backend, auth, tenant, provider or semantic quality tested.' if args.mode=='reference' else 'Selected adapter cases only. Tenant/manual/race/harness qualification still required.','catalog_sha256':sha(catalog_path),'adapter_sha256':sha(adapter),'results':results,'manual_cases_run':0}
    encoded=json.dumps(report,indent=2)
    if args.output:args.output.write_text(encoded+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='results'}));print(f"{sum(x['passed'] for x in results)}/{len(results)} checks passed")
    return 0 if all(x['passed'] for x in results) else 1
if __name__=='__main__':sys.exit(main())
