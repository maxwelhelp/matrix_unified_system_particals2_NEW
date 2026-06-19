#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from datetime import datetime, timezone


def fnum(x, default=0.0):
    try:
        if x is None or x == '': return default
        return float(x)
    except Exception:
        return default

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
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})

def wjsonl(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def exists_any(paths):
    return any(Path(p).exists() for p in paths)

def best(rows, pred):
    xs=[r for r in rows if pred(r)]
    return sorted(xs,key=lambda r:fnum(r.get('relation_signal')),reverse=True)[0] if xs else {}

def add(rows,cid,claim,support,contradiction,missing,risk,next_exp,status,priority,label,evidence=None):
    rows.append({
        'comparison_id':cid,
        'claim':claim,
        'support_signal':support,
        'contradiction_signal':contradiction,
        'missing_control':missing,
        'risk':risk,
        'recommended_next_experiment':next_exp,
        'status':status,
        'priority':priority,
        'training_label':label,
        'evidence_json':json.dumps(evidence or {},ensure_ascii=False),
    })

def infer_n_events_from_dynamics(dyn_runs):
    vals=[]
    for r in dyn_runs:
        n=fnum(r.get('n_events'), None)
        if n is not None and n>0:
            vals.append(int(n))
    return sorted(set(vals))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--v1-json',default='manifests/latest/automatic_comparison_engine_v1.json')
    ap.add_argument('--relation-edges',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--watcher',default='manifests/latest/stream_task_watcher_v1.json')
    ap.add_argument('--dynamics',default='manifests/latest/research_dynamics_v1.json')
    ap.add_argument('--dynamics-heads',default='reports/latest/tables/dynamics_head_ranks.csv')
    ap.add_argument('--stream-index',default='manifests/latest/research_stream_index_v1.json')
    ap.add_argument('--head-vectors',default='reports/latest/tables/evidence_head_vectors.csv')
    ap.add_argument('--out-json',default='manifests/latest/automatic_comparison_engine_v2.json')
    ap.add_argument('--out-md',default='reports/latest/AUTOMATIC_COMPARISON_ENGINE_V2.md')
    ap.add_argument('--out-csv',default='reports/latest/tables/automatic_comparison_rows_v2.csv')
    ap.add_argument('--out-dataset',default='reports/latest/tables/automatic_comparison_training_dataset_v2.jsonl')
    args=ap.parse_args()

    v1=loadjson(args.v1_json)
    edges=readcsv(args.relation_edges)
    watcher=loadjson(args.watcher)
    dynamics=loadjson(args.dynamics)
    dyn_heads=readcsv(args.dynamics_heads)
    stream=loadjson(args.stream_index)
    head_vectors=readcsv(args.head_vectors)

    rows=[]
    # Carry v1 comparisons if available.
    for r in v1.get('comparisons',[]):
        rr=dict(r); rr['source']='v1'; rows.append(rr)

    # C7 sample-size scaling.
    n_events=infer_n_events_from_dynamics(dynamics.get('run_rows',[]))
    distinct_sizes=len(n_events)
    add(rows,'C7_SAMPLE_SIZE_SCALING',
        'signals must scale from small snapshots to larger streams',
        f'distinct_n_events={n_events} snapshots={dynamics.get("n_graph_snapshots")}',
        'same repeated snapshot can fake stability' if distinct_sizes<3 else 'multiple event scales available',
        'more distinct sample sizes 64/256/512/1024' if distinct_sizes<3 else '',
        'large stream can amplify shortcuts if controls are missing',
        'run stream cycles at SAMPLES_PER_FILE=64,256,512,1024 with HISTORY_COPY=1 and compare ranks/signals',
        'NEEDS_MORE_LARGE_RUNS' if distinct_sizes<3 else 'SCALING_PARTIAL',
        'P0','sample_size_scaling_required',{'n_events':n_events,'dynamics':dynamics.get('run_rows',[])[:10]})

    # C8 class concentration.
    hqql=next((t for t in watcher.get('task_scores',[]) if 'HQQL_TBL' in t.get('task_id','')),{})
    add(rows,'C8_CLASS_CONCENTRATION_VS_IMBALANCE',
        'Hqql/Tbl dominance may be real class signature or sampling bias',
        f'watcher_score={hqql.get("score","n/a")} state={hqql.get("state","n/a")}',
        'class-balanced/natural-distribution comparison missing',
        'balanced-vs-natural stream comparison',
        'balanced tiny subset can overstate class signatures; natural distribution can hide rare patterns',
        'run one balanced stream and one natural/random-file stream, compare class signatures',
        'NEEDS_CLASS_DISTRIBUTION_CHECK',
        'P0','class_distribution_check_required',hqql)

    # C9 correct-vs-wrong split.
    error_atlas=exists_any(['reports/latest/ERROR_ATLAS_V1.md','manifests/latest/error_atlas_v1.json','reports/latest/tables/error_route_head_atlas.csv'])
    add(rows,'C9_CORRECT_VS_WRONG_SPLIT',
        'mechanisms should be compared on correct predictions vs errors',
        'current stream stores pred/true but no dedicated error-head atlas',
        'no contradiction yet; missing error analysis' if not error_atlas else 'error atlas available',
        '' if error_atlas else 'error atlas / false-class route analysis',
        'heads on wrong examples may support predicted class rather than true class',
        'build error atlas: correct vs wrong head gates, particles, classes, and hypotheses',
        'NEEDS_ERROR_ATLAS' if not error_atlas else 'SUPPORTED_BY_MULTIPLE_SIGNALS',
        'P1','error_atlas_required')

    # C10 known observable residual.
    residual=exists_any(['reports/latest/KNOWN_OBSERVABLE_RESIDUAL_V1.md','manifests/latest/known_observable_residual_v1.json','reports/latest/tables/known_observable_residual.csv'])
    add(rows,'C10_KNOWN_OBSERVABLE_RESIDUAL',
        'discovery-relevant signals must survive known-observable baselines',
        'current signals use particles/heads but not residual after mass/tau/nparticles/pt',
        'no residual baseline yet' if not residual else 'residual baseline available',
        '' if residual else 'known-observable residual analysis',
        'particle0/core may be explained by pt/mass/nparticles/tau variables',
        'fit known observables then test whether head/particle signals explain residual errors or logits',
        'MISSING_RESIDUAL_TEST' if not residual else 'RESIDUAL_PARTIAL',
        'P0','known_observable_residual_required')

    # C11 head pair synergy.
    pair=exists_any(['reports/latest/HEAD_PAIR_SYNERGY_V1.md','manifests/latest/head_pair_synergy_v1.json','reports/latest/tables/head_pair_synergy.csv'])
    div_heads=[]
    for h in head_vectors:
        if fnum(h.get('gate_abs_grad'))>0.2 and fnum(h.get('patch_acc_drop'))<1e-6:
            div_heads.append(h.get('head_id'))
    add(rows,'C11_HEAD_PAIR_SYNERGY',
        'distributed computation requires pair/group head tests, not only single-head patch',
        f'divergent_gate_strong_patch_weak_heads={div_heads[:8]} count={len(div_heads)}',
        'pair patch report missing' if not pair else 'pair synergy report available',
        '' if pair else 'head-pair/multi-head patch synergy',
        'single-head tests can miss redundancy, compensation, and synergy',
        'patch top head pairs/groups and classify additive/synergistic/redundant effects',
        'NEEDS_HEAD_PAIR_SYNERGY' if not pair else 'SUPPORTED_BY_MULTIPLE_SIGNALS',
        'P1','head_pair_synergy_required',{'divergent_heads':div_heads[:20]})

    # C12 cross-model/checkpoint agreement.
    cross=exists_any(['reports/latest/CROSS_MODEL_AGREEMENT_V1.md','manifests/latest/cross_model_agreement_v1.json','reports/latest/tables/cross_model_agreement.csv'])
    add(rows,'C12_CROSS_MODEL_CHECKPOINT_AGREEMENT',
        'physics-like patterns should be checked across checkpoints/features/architectures',
        'current main stream is ParticleNet_kinpid-focused',
        'no cross-model agreement report yet' if not cross else 'cross-model report available',
        '' if cross else 'cross-model/checkpoint stream: ParticleNet kin/kinpid/full and ParT kinpid/full',
        'architecture-specific artifact can look like physics in one model',
        'run same watcher/relation/comparison stack on kin, kinpid, full and ParT where possible',
        'NEEDS_CROSS_MODEL_TEST' if not cross else 'CROSS_MODEL_PARTIAL',
        'P1','cross_model_agreement_required')

    # C13 per-file heldout.
    heldout=exists_any(['reports/latest/PER_FILE_HELDOUT_STABILITY_V1.md','manifests/latest/per_file_heldout_stability_v1.json','reports/latest/tables/per_file_heldout_stability.csv'])
    add(rows,'C13_PER_FILE_HELDOUT_STABILITY',
        'relations should survive different ROOT files and tar parts',
        f'snapshots={stream.get("n_snapshots")} but no per-file heldout breakdown',
        'per-file heldout missing' if not heldout else 'per-file heldout available',
        '' if heldout else 'per-file/per-tar-part stability report',
        'same extracted tiny files can fake stable patterns',
        'run stream over more ROOT files and compare head/rule signals per file and per class',
        'NEEDS_HELDOUT' if not heldout else 'HELDOUT_PARTIAL',
        'P0','per_file_heldout_required')

    # C14 ordering vs physical coordinate.
    order_control=exists_any(['reports/latest/PARTICLE_ORDER_CONTROL_V1.md','manifests/latest/particle_order_control_v1.json','reports/latest/tables/particle_order_control.csv'])
    p0_edge=best(edges,lambda e:e.get('src')=='pattern:particle0')
    add(rows,'C14_ORDERING_VS_PHYSICAL_COORDINATE',
        'particle0 dominance must be separated from particle ordering/sorting',
        f'particle0_edge_signal={p0_edge.get("relation_signal","n/a")} support={p0_edge.get("support","n/a")}',
        'order/shuffle control missing' if not order_control else 'order control available',
        '' if order_control else 'particle-order shuffle / coordinate-only comparison',
        'particle index can encode sorting by pt, not a physical interaction',
        'run particle order shuffle and compare index-based vs pt/deltaR-based signals',
        'NEEDS_ORDER_CONTROL' if not order_control else 'ORDER_CONTROL_PARTIAL',
        'P0','particle_order_control_required',p0_edge)

    # C15 discovery readiness.
    mandatory_missing=[r for r in rows if r.get('priority')=='P0' and str(r.get('status','')).startswith(('NEEDS','MISSING','CANDIDATE'))]
    readiness='method_debug'
    if not mandatory_missing:
        readiness='residual_candidate_ready_for_anomaly_test'
    add(rows,'C15_DISCOVERY_READINESS_SCORE',
        'a hypothesis is discovery-relevant only after controls, heldout, residual, and cross-model tests',
        f'p0_missing_count={len(mandatory_missing)} readiness={readiness}',
        'many P0 controls missing' if mandatory_missing else 'P0 controls satisfied',
        ', '.join(r['comparison_id'] for r in mandatory_missing[:8]),
        'correlation-only relation is not a discovery claim',
        'complete P0 controls before claiming physics/discovery relevance',
        'METHOD_DEBUG_NOT_DISCOVERY_READY' if mandatory_missing else 'RESIDUAL_CANDIDATE_READY',
        'P0','discovery_readiness_gate',{'missing_p0':[r['comparison_id'] for r in mandatory_missing]})

    # C16 big stream readiness.
    ready_for_big = not any(r['comparison_id'] in {'C1_STREAM_RELATION_VS_MISSING_CONTROL','C14_ORDERING_VS_PHYSICAL_COORDINATE'} and r['missing_control'] for r in rows)
    add(rows,'C16_BIG_STREAM_READINESS',
        'large stream should run with summaries and known P0 controls tracked',
        f'current_snapshots={stream.get("n_snapshots")} stream_events={stream.get("n_stream_events")}',
        'large stream without particle0/order controls may only amplify shortcut evidence',
        'run sampled large stream plus immediately run controls',
        'big data can make wrong shortcut look very confident',
        'run staged large stream: 64 smoke -> 256 -> 512/1024, then particle0/top-k controls',
        'READY_FOR_SAMPLED_LARGE_STREAM_WITH_CONTROLS' if ready_for_big else 'RUN_SAMPLED_LARGE_STREAM_BUT_PRIORITIZE_CONTROLS',
        'P0','big_stream_staged_run',{'snapshots':stream.get('n_snapshots'),'events':stream.get('n_stream_events')})

    prio={'P0':0,'P1':1,'P2':2}
    rows=sorted(rows,key=lambda r:(prio.get(r.get('priority'),9), r.get('comparison_id','')))
    dataset=[]
    for r in rows:
        dataset.append({'schema':'automatic_comparison_training_row.v2','input':{k:r[k] for k in ['comparison_id','claim','support_signal','contradiction_signal','missing_control','risk','evidence_json'] if k in r},'target':{k:r[k] for k in ['status','priority','training_label','recommended_next_experiment'] if k in r}})
    wcsv(args.out_csv,rows)
    wjsonl(args.out_dataset,dataset)
    out={'schema':'automatic_comparison_engine.v2','generated_at_utc':datetime.now(timezone.utc).isoformat(),'comparisons':rows,'p0':[r for r in rows if r.get('priority')=='P0'],'next_big_stream_policy':'staged_sampled_large_stream_with_controls'}
    wjson(args.out_json,out)
    md=['# Automatic Comparison Engine v2\n\n',
        'v2 adds big-stream and discovery-readiness comparisons on top of v1.\n\n',
        '## P0 comparisons\n',
        md_table(['status','comparison','claim','missing','next'],[[r['status'],r['comparison_id'],r['claim'],r.get('missing_control',''),r['recommended_next_experiment']] for r in rows if r.get('priority')=='P0']),
        '\n## All comparisons\n',
        md_table(['priority','status','comparison','support','risk'],[[r.get('priority'),r.get('status'),r.get('comparison_id'),r.get('support_signal'),r.get('risk')] for r in rows]),
        '\n## Big-stream policy\n\n',
        'Run a staged large stream, not the whole downloaded dataset blindly:\n\n',
        '1. smoke: SAMPLES_PER_FILE=64;\n',
        '2. medium: SAMPLES_PER_FILE=256;\n',
        '3. large sampled: SAMPLES_PER_FILE=512 or 1024 with MICRO_BATCH=16;\n',
        '4. immediately run particle0/top-k controls and class-specific gradients;\n',
        '5. only then expand to more ROOT files / tar parts.\n\n',
        '## Files\n\n',
        f'- JSON: `{args.out_json}`\n',
        f'- CSV: `{args.out_csv}`\n',
        f'- Training rows: `{args.out_dataset}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'comparisons':len(rows),'p0':len([r for r in rows if r.get('priority')=='P0']),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
