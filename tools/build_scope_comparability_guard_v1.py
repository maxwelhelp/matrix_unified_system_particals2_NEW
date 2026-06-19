#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
from datetime import datetime, timezone


def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def wcsv(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k:r.get(k,'') for k in keys})

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream-index',default='manifests/latest/research_stream_index_v1.json')
    ap.add_argument('--dynamics',default='manifests/latest/research_dynamics_v1.json')
    ap.add_argument('--controls',default='manifests/latest/particle0_topk_controls_v2.json')
    ap.add_argument('--embeddings',default='manifests/latest/stream_feature_embeddings_v1.json')
    ap.add_argument('--comparison',default='manifests/latest/automatic_comparison_engine_v2.json')
    ap.add_argument('--out-json',default='manifests/latest/scope_comparability_guard_v1.json')
    ap.add_argument('--out-md',default='reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md')
    ap.add_argument('--out-checks',default='reports/latest/tables/scope_comparability_checks.csv')
    ap.add_argument('--out-manifest',default='reports/latest/tables/scoped_feature_manifest.csv')
    args=ap.parse_args()

    stream=loadjson(args.stream_index)
    dynamics=loadjson(args.dynamics)
    controls=loadjson(args.controls)
    emb=loadjson(args.embeddings)
    comp=loadjson(args.comparison)

    checks=[]
    manifest=[]
    def check(name, status, severity, meaning, allowed, forbidden):
        checks.append({'check':name,'status':status,'severity':severity,'meaning':meaning,'allowed_comparison':allowed,'forbidden_comparison':forbidden})

    # Data sources and scope classes.
    manifest.append({'artifact':'research_stream_events.jsonl','scope_class':'history_stream','scope_key':'run_index/snapshot','directly_comparable_to':'other stream snapshots with same schema','not_directly_comparable_to':'local control deltas','rule':'use for trends/stability, not local causal deltas'})
    manifest.append({'artifact':'research_stream_index_v1.json','scope_class':'latest_stream_summary','scope_key':'latest_run_index','directly_comparable_to':'latest relation/task summaries','not_directly_comparable_to':'control-run baseline unless linked as evidence type','rule':'use as current dashboard'})
    manifest.append({'artifact':'particle0_topk_controls_v2.json','scope_class':'control_run_local','scope_key':'same control batch baseline','directly_comparable_to':'baseline/random controls inside same run','not_directly_comparable_to':'global stream history numeric deltas','rule':'use for causal control evidence only inside run'})
    manifest.append({'artifact':'relation_signal_edges.csv','scope_class':'latest_relation_meta','scope_key':'latest stream relations','directly_comparable_to':'latest stream and task watcher','not_directly_comparable_to':'causal controls without explicit bridge','rule':'prioritization signal, not causal proof'})
    manifest.append({'artifact':'automatic_comparison_rows_v2.csv','scope_class':'comparison_meta','scope_key':'evidence bridge','directly_comparable_to':'mixed evidence only with explicit status/risk','not_directly_comparable_to':'raw numeric training without scope flags','rule':'safe bridge layer'})
    manifest.append({'artifact':'all_feature_embeddings.jsonl','scope_class':'mixed_embedding_pool','scope_key':'source field + id','directly_comparable_to':'same source/scope first','not_directly_comparable_to':'all rows as one homogeneous dataset','rule':'train with source/scope features or split by source'})

    has_controls=bool(controls.get('ok'))
    has_stream=bool(stream.get('n_stream_events'))
    has_dynamics=bool(dynamics.get('n_graph_snapshots'))
    has_embeddings=bool((emb.get('counts') or {}).get('all'))
    c1_status=''
    for r in comp.get('comparisons',[]):
        if r.get('comparison_id')=='C1_STREAM_RELATION_VS_MISSING_CONTROL':
            c1_status=r.get('status','')
    check('control_is_local_not_global_stream_delta','PASS' if has_controls else 'WARN','HIGH','particle0/top-k controls are local causal controls against same-run baseline/random','remove_particle0 vs baseline/random_remove1 inside same control run','treat remove_particle0 acc_drop as a stream-history delta')
    check('stream_history_available','PASS' if has_stream and has_dynamics else 'WARN','MEDIUM','stream/dynamics track repeated snapshots','head rank stability / stream signal stability','causal claim from stream relation alone')
    check('comparison_bridge_status','PASS' if 'SUPPORTED_BY_TARGETED_CONTROL' in c1_status else 'WARN','HIGH','comparison engine should bridge stream relation + local control with explicit remaining risks','stream suggested particle0; local control supports causality; still needs order/residual','claim discovery or global stream-wide causality without remaining controls')
    check('embedding_pool_is_mixed','WARN' if has_embeddings else 'WARN','HIGH','feature embeddings contain mixed sources/scopes','train with source/scope splits and flags','train one model treating all embedding rows as homogeneous facts')
    check('remaining_required_controls','WARN','HIGH','order/residual/class-specific/heldout are still required','next tests: order control, residual, class gradients, heldout','physics discovery claim')

    summary={'schema':'scope_comparability_guard.v1','generated_at_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_WITH_WARNINGS','checks':checks,'manifest':manifest,'counts':{'stream_events':stream.get('n_stream_events'),'snapshots':stream.get('n_snapshots'),'control_events':controls.get('n_events'),'embedding_rows':(emb.get('counts') or {}).get('all')},'core_rule':'local control deltas are compared only to same-run baseline/random; stream history is used for stability/trends; comparison engine is the explicit bridge.'}
    wjson(args.out_json,summary)
    wcsv(args.out_checks,checks)
    wcsv(args.out_manifest,manifest)
    md=['# Scope Comparability Guard v1\n\n',
        'This report prevents a methodology bug: comparing a one-batch/local control delta as if it were a whole-stream trend.\n\n',
        f"- Status: **{summary['status']}**\n",
        f"- Stream events: **{summary['counts'].get('stream_events')}**\n",
        f"- Stream snapshots: **{summary['counts'].get('snapshots')}**\n",
        f"- Control-run events: **{summary['counts'].get('control_events')}**\n",
        f"- Embedding rows: **{summary['counts'].get('embedding_rows')}**\n\n",
        '## Checks\n',
        md_table(['status','severity','check','allowed','forbidden'],[[c['status'],c['severity'],c['check'],c['allowed_comparison'],c['forbidden_comparison']] for c in checks]),
        '\n## Scope manifest\n',
        md_table(['artifact','scope','directly comparable to','not directly comparable to','rule'],[[m['artifact'],m['scope_class'],m['directly_comparable_to'],m['not_directly_comparable_to'],m['rule']] for m in manifest]),
        '\n## Short answer\n\n',
        'Yes, there is a real risk if we train/analyze the mixed embedding pool blindly. The fix is to keep scope labels and compare only within valid scope.\n\n',
        'The current particle0 control conclusion is valid as a **local causal control**: `remove_particle0` is compared against the same-run baseline and random same-count controls. It is not a global stream-history delta.\n\n',
        'The comparison engine is allowed to bridge evidence types, but only with explicit status and remaining risks: order control, residual, class-specific gradients, and heldout.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'status':summary['status'],'checks':len(checks),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
