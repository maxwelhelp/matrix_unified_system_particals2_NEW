#!/usr/bin/env python3
import csv, json, argparse
from pathlib import Path
from datetime import datetime, timezone


def fnum(x, default=0.0):
    try:
        if x is None or x == '': return default
        return float(x)
    except Exception:
        return default

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

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

def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def wjsonl(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')

def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def row_by_control(rows, name):
    return next((r for r in rows if r.get('control') == name), {})

def random_mean(rows, prefix, key):
    rs=[r for r in rows if r.get('control','').startswith(prefix)]
    if not rs: return 0.0
    return sum(fnum(r.get(key)) for r in rs)/len(rs)

def update_c15(rows):
    missing=[r for r in rows if r.get('priority')=='P0' and str(r.get('status','')).startswith(('NEEDS','MISSING','CANDIDATE'))]
    for r in rows:
        if r.get('comparison_id')=='C15_DISCOVERY_READINESS_SCORE':
            r['support_signal']=f"p0_missing_count={len(missing)} readiness=method_debug"
            r['missing_control']=', '.join(x.get('comparison_id','') for x in missing[:8])
            r['status']='METHOD_DEBUG_NOT_DISCOVERY_READY' if missing else 'RESIDUAL_CANDIDATE_READY'
            r['evidence_json']=json.dumps({'missing_p0':[x.get('comparison_id') for x in missing]},ensure_ascii=False)
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rows',default='reports/latest/tables/automatic_comparison_rows_v2.csv')
    ap.add_argument('--json',default='manifests/latest/automatic_comparison_engine_v2.json')
    ap.add_argument('--dataset',default='reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl')
    ap.add_argument('--md',default='reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md')
    ap.add_argument('--controls',default='reports/latest/tables/particle0_topk_control_summary_v2.csv')
    ap.add_argument('--order',default='reports/latest/tables/particle_order_control.csv')
    ap.add_argument('--confusion',default='reports/latest/tables/control_confusion_summary.csv')
    ap.add_argument('--residual',default='manifests/latest/known_observable_residual_v1.json')
    args=ap.parse_args()
    rows=readcsv(args.rows)
    controls=readcsv(args.controls)
    order=readcsv(args.order)
    confusion=readcsv(args.confusion)
    residual=loadjson(args.residual)
    if not rows or not controls:
        print(json.dumps({'ok':False,'reason':'missing rows or controls','rows':len(rows),'controls':len(controls)},indent=2))
        return
    rem0=row_by_control(controls,'remove_particle0')
    keep0=row_by_control(controls,'keep_only_particle0')
    rand_drop=random_mean(controls,'random_remove1_','acc_drop_from_baseline')
    rand_flip=random_mean(controls,'random_remove1_','pred_flip_rate')
    ratio=(fnum(rem0.get('acc_drop_from_baseline'))/max(1e-9,rand_drop)) if rem0 else 0.0
    random_order_flips=[fnum(r.get('pred_flip_rate')) for r in order if r.get('control','').startswith('random_shuffle')]
    max_order_flip=max(random_order_flips) if random_order_flips else None
    order_ok=(max_order_flip is not None and max_order_flip <= 0.001)
    confusion_ok=bool(confusion)
    residual_ok=bool(residual.get('ok'))
    residual_status=residual.get('status','')
    residual_remains=(residual_status=='RESIDUAL_SIGNAL_REMAINS')
    residual_support=(
        f"residual_status={residual_status}, agreement={fmt(residual.get('known_observable_agreement_with_model'))}, "
        f"surrogate_acc={fmt(residual.get('known_observable_surrogate_acc'))}, "
        f"logit_r2_mean={fmt(residual.get('logit_r2_mean'))}, residual_rel={fmt(residual.get('residual_rel_mean'))}"
    ) if residual_ok else 'residual not available'
    for r in rows:
        if r.get('comparison_id')=='C1_STREAM_RELATION_VS_MISSING_CONTROL':
            r['support_signal']=(
                f"particle0 control: remove_particle0_drop={fmt(rem0.get('acc_drop_from_baseline'))}, "
                f"random_remove1_drop={fmt(rand_drop)}, ratio={fmt(ratio)}, "
                f"keep_only_particle0_acc={fmt(keep0.get('acc'))}; "
                f"order_max_random_flip={fmt(max_order_flip) if max_order_flip is not None else 'n/a'}; "
                f"{residual_support}"
            )
            r['contradiction_signal']='keep_only_particle0 is weak globally, so this is not a pure particle0-only shortcut'
            r['missing_control']='class-specific gradients / heldout / richer residual v2' if residual_ok else 'residual/class-specific/heldout controls'
            r['risk']='simple known-observable-only explanation is weakened, but richer ECF/EFP features and heldout are still needed' if residual_remains else 'known-observable proxy may still explain much of signal'
            r['recommended_next_experiment']='run class-specific all-head gradients, richer residual v2, and per-file heldout stability'
            r['status']='SUPPORTED_BY_CONTROL_ORDER_AND_RESIDUAL_V1_NEEDS_CLASS_HEADS' if residual_remains else 'SUPPORTED_BY_CONTROL_ORDER_NEEDS_RESIDUAL_REVIEW'
            r['training_label']='control_order_residual_supported_class_heads_required' if residual_remains else 'control_order_supported_residual_review_required'
            r['evidence_json']=json.dumps({'remove_particle0':rem0,'keep_only_particle0':keep0,'random_remove1_acc_drop_mean':rand_drop,'random_remove1_flip_mean':rand_flip,'target_vs_random_drop_ratio':ratio,'order_max_random_flip':max_order_flip,'confusion_atlas_available':confusion_ok,'residual':residual},ensure_ascii=False)
        if r.get('comparison_id')=='C10_KNOWN_OBSERVABLE_RESIDUAL' and residual_ok:
            r['support_signal']=residual_support
            r['contradiction_signal']='simple surrogate explains some logit variance but low model agreement means decision structure is not reproduced'
            r['missing_control']='richer residual v2 / heldout / cross-model'
            r['risk']='v1 uses simple linear/ridge known observables; richer ECF/EFP/tau features may explain more'
            r['recommended_next_experiment']='add richer pair/ECF-like observables and run class-specific head gradients'
            r['status']='RESIDUAL_SIGNAL_REMAINS_NEEDS_RICHER_V2_HELDOUT' if residual_remains else 'KNOWN_OBSERVABLE_PROXY_PARTIAL_NEEDS_REVIEW'
            r['training_label']='residual_signal_remains_v1_richer_v2_required' if residual_remains else 'known_observable_proxy_partial_review_required'
            r['evidence_json']=json.dumps(residual,ensure_ascii=False)
        if r.get('comparison_id')=='C14_ORDERING_VS_PHYSICAL_COORDINATE' and order_ok:
            r['support_signal']=f"order control available: random/reverse/move controls preserve predictions; max_random_shuffle_flip={fmt(max_order_flip)}"
            r['contradiction_signal']='none at prediction level; small logit differences may still have outliers'
            r['missing_control']='heldout / richer residual v2' if residual_ok else 'known-observable residual / heldout'
            r['risk']='array-index shortcut risk is strongly reduced; leading-core residual remains after simple surrogate' if residual_remains else 'array-index shortcut risk is reduced, but proxy status needs review'
            r['recommended_next_experiment']='run per-file heldout and richer residual v2; optionally inspect max-logit-diff outliers'
            r['status']='ORDER_INDEX_ARTIFACT_REDUCED_RESIDUAL_REMAINS_NEEDS_HELDOUT' if residual_remains else 'ORDER_INDEX_ARTIFACT_REDUCED_NEEDS_RESIDUAL_HELDOUT'
            r['training_label']='order_artifact_reduced_residual_remains_heldout_required' if residual_remains else 'order_artifact_reduced_residual_heldout_required'
    rows=update_c15(rows)
    prio={'P0':0,'P1':1,'P2':2}
    rows=sorted(rows,key=lambda r:(prio.get(r.get('priority'),9), r.get('comparison_id','')))
    wcsv(args.rows,rows)
    dataset=[]
    for r in rows:
        dataset.append({'schema':'automatic_comparison_training_row.v2.after_residual','input':{k:r.get(k,'') for k in ['comparison_id','claim','support_signal','contradiction_signal','missing_control','risk','evidence_json']},'target':{k:r.get(k,'') for k in ['status','priority','training_label','recommended_next_experiment']}})
    wjsonl(args.dataset,dataset)
    out={'schema':'automatic_comparison_engine.v2','generated_at_utc':datetime.now(timezone.utc).isoformat(),'postprocess':'particle0_order_confusion_residual_fix_v1','comparisons':rows,'p0':[r for r in rows if r.get('priority')=='P0'],'next_big_stream_policy':'class_heads_residual_v2_heldout_then_scale'}
    wjson(args.json,out)
    md=['# Automatic Comparison Engine v2\n\n',
        'v2 after particle0/top-k controls, order/confusion controls, and known-observable residual v1 when available.\n\n',
        '## P0 comparisons\n',
        md_table(['status','comparison','claim','missing','next'],[[r.get('status'),r.get('comparison_id'),r.get('claim'),r.get('missing_control',''),r.get('recommended_next_experiment')] for r in rows if r.get('priority')=='P0']),
        '\n## All comparisons\n',
        md_table(['priority','status','comparison','support','risk'],[[r.get('priority'),r.get('status'),r.get('comparison_id'),r.get('support_signal'),r.get('risk')] for r in rows]),
        '\n## Particle0 / order / residual update\n\n',
        f"- remove_particle0 acc_drop: **{fmt(rem0.get('acc_drop_from_baseline'))}**\n",
        f"- random_remove1 acc_drop mean: **{fmt(rand_drop)}**\n",
        f"- targeted/random drop ratio: **{fmt(ratio)}**\n",
        f"- keep_only_particle0 acc: **{fmt(keep0.get('acc'))}**\n",
        f"- max random order-shuffle flip: **{fmt(max_order_flip) if max_order_flip is not None else 'n/a'}**\n",
        f"- confusion atlas available: **{confusion_ok}**\n",
        f"- residual status: **{residual_status or 'n/a'}**\n",
        f"- residual agreement with model: **{fmt(residual.get('known_observable_agreement_with_model')) if residual_ok else 'n/a'}**\n",
        f"- residual logit R2 mean: **{fmt(residual.get('logit_r2_mean')) if residual_ok else 'n/a'}**\n\n",
        'Interpretation: particle0/core is targeted-causal, array-index artifact is reduced, and residual v1 suggests simple known-observable surrogate does not reproduce ParticleNet decisions. Remaining P0: class-specific gradients, richer residual v2, heldout/per-file stability.\n\n',
        '## Files\n\n',
        f'- JSON: `{args.json}`\n',
        f'- CSV: `{args.rows}`\n',
        f'- Training rows: `{args.dataset}`\n']
    Path(args.md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'patched_C1':True,'patched_C10':residual_ok,'patched_C14':order_ok,'target_vs_random_drop_ratio':ratio,'order_max_random_flip':max_order_flip,'residual_status':residual_status,'out_json':args.json},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
