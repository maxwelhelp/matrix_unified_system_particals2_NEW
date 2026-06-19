#!/usr/bin/env python3
import argparse, csv, json
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
        for r in rows:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')

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

def best_edge(edges, pred):
    rows=[e for e in edges if pred(e)]
    rows=sorted(rows,key=lambda e:fnum(e.get('relation_signal')),reverse=True)
    return rows[0] if rows else {}

def has_control_file(paths):
    return any(Path(p).exists() for p in paths)

def add(rows, cid, claim, support_signal, contradiction_signal, missing_control, risk, recommended, status, priority, training_label, evidence_json=None):
    rows.append({
        'comparison_id':cid,
        'claim':claim,
        'support_signal':support_signal,
        'contradiction_signal':contradiction_signal,
        'missing_control':missing_control,
        'risk':risk,
        'recommended_next_experiment':recommended,
        'status':status,
        'priority':priority,
        'training_label':training_label,
        'evidence_json':json.dumps(evidence_json or {},ensure_ascii=False),
    })

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--relation-edges',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--watcher',default='manifests/latest/stream_task_watcher_v1.json')
    ap.add_argument('--dynamics-heads',default='reports/latest/tables/dynamics_head_ranks.csv')
    ap.add_argument('--head-vectors',default='reports/latest/tables/evidence_head_vectors.csv')
    ap.add_argument('--out-json',default='manifests/latest/automatic_comparison_engine_v1.json')
    ap.add_argument('--out-md',default='reports/latest/AUTOMATIC_COMPARISON_ENGINE_V1.md')
    ap.add_argument('--out-csv',default='reports/latest/tables/automatic_comparison_rows.csv')
    ap.add_argument('--out-dataset',default='reports/latest/tables/automatic_comparison_training_dataset.jsonl')
    args=ap.parse_args()

    edges=readcsv(args.relation_edges)
    watcher=loadjson(args.watcher)
    dyn_heads=readcsv(args.dynamics_heads)
    head_vectors=readcsv(args.head_vectors)
    rows=[]

    particle0_edge=best_edge(edges,lambda e:e.get('src') in ('pattern:particle0','pattern:core_high_pt') and 'hypothesis:AH1' in e.get('dst',''))
    particle0_control=has_control_file([
        'reports/latest/PARTICLE0_TOPK_CONTROLS_V1.md',
        'manifests/latest/particle0_topk_controls_v1.json',
        'reports/latest/tables/particle0_topk_controls.csv'
    ])
    add(rows,'C1_STREAM_RELATION_VS_MISSING_CONTROL',
        'particle0/core_high_pt relation supports AH1 core-anchor hypothesis',
        f"relation_signal={particle0_edge.get('relation_signal','n/a')} support={particle0_edge.get('support','n/a')}",
        'none yet; controls not run' if not particle0_control else 'particle0 controls available',
        '' if particle0_control else 'particle0/top-k/random controls',
        'could be sorting shortcut or normal leading-particle bias',
        'run particle0 removal / keep-only particle0 / top-k removal / same-count random controls',
        'SUPPORTED_BY_MULTIPLE_SIGNALS' if particle0_control else 'CANDIDATE_STRONG_MISSING_CONTROL',
        'P0','particle0_topk_controls_required',particle0_edge)

    wide_edge=best_edge(edges,lambda e:e.get('src')=='pattern:wide')
    route_trace=has_control_file([
        'reports/latest/ROUTE_NEIGHBOR_TRACE_V1.md',
        'manifests/latest/route_neighbor_trace_v1.json'
    ])
    add(rows,'C2_WIDE_PATTERN_VS_ROUTE_TRACE',
        'wide particle pattern may be secondary context rather than noise',
        f"relation_signal={wide_edge.get('relation_signal','n/a')} support={wide_edge.get('support','n/a')} dst={wide_edge.get('dst','')}",
        'none yet; route-neighbor trace missing' if not route_trace else 'route-neighbor trace available',
        '' if route_trace else 'route-neighbor trace / causal route controls',
        'wide relation can be class imbalance, loose fragments, or sorting artifact',
        'run route-neighbor trace for top all-head particles and wide non-particle0 particles',
        'NEEDS_ROUTE_TRACE' if not route_trace else 'SUPPORTED_BY_MULTIPLE_SIGNALS',
        'P0','route_neighbor_trace_required',wide_edge)

    # Patch vs gradient divergence.
    divergences=[]
    for h in head_vectors:
        gate=fnum(h.get('gate_abs_grad'))
        patch=fnum(h.get('patch_acc_drop'))
        if gate>0.2 and patch<1e-6:
            divergences.append({'head_id':h.get('head_id'),'gate_abs_grad':gate,'patch_acc_drop':patch,'role':h.get('role')})
    divergences=sorted(divergences,key=lambda r:r['gate_abs_grad'],reverse=True)
    add(rows,'C3_PATCH_VS_GRADIENT_DIVERGENCE',
        'some heads are jointly supportive by gradient but not individually important by patch',
        f"divergent_heads={len(divergences)} top={divergences[:3]}",
        'no contradiction; this is method divergence',
        'multi-head patch combinations / patch-rank-vs-gate-rank table',
        'gradient support is local; patch may reveal redundancy or compensation',
        'build patch-rank vs gate-rank report and run multi-head patch combinations',
        'NEEDS_CLASS_SPECIFIC_TEST' if divergences else 'LOW_PRIORITY',
        'P1','patch_gradient_divergence_analysis',{'divergent_heads':divergences[:20]})

    # Head rank stability.
    latest_top=[r for r in dyn_heads if str(r.get('head_rank')) in {'1','2','3','4','5'}]
    stable_score=0.0
    known_delta=[]
    for r in latest_top:
        if r.get('delta_rank') not in ('',None):
            known_delta.append(abs(fnum(r.get('delta_rank'))))
    if known_delta:
        stable_score=max(0.0,1.0-sum(known_delta)/len(known_delta)/5.0)
    else:
        stable_score=0.5
    add(rows,'C4_HEAD_RANK_STABILITY_VS_RUN_CHANGES',
        'top all-head gates may be stable mechanism candidates',
        f"stability_score={fmt(stable_score)} top_heads={[r.get('head_id') for r in latest_top[:5]]}",
        'unknown if snapshots are not distinct enough',
        'more distinct snapshots / heldout files / controls',
        'repeated same data can fake stability',
        'run heldout subsets and controls with HISTORY_COPY=1, then compare head ranks',
        'NEEDS_HELDOUT' if stable_score>=0.7 else 'LOW_PRIORITY',
        'P1','heldout_stability_required',{'stable_score':stable_score,'top_heads':latest_top[:10]})

    # Class signature vs class-specific gradients.
    hqql_task=next((t for t in watcher.get('task_scores',[]) if 'HQQL_TBL' in t.get('task_id','')),{})
    class_grad=has_control_file([
        'reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md',
        'manifests/latest/class_specific_all_head_gradients_v1.json'
    ])
    add(rows,'C5_CLASS_SIGNATURE_VS_CLASS_SPECIFIC_GRADIENT',
        'Hqql/Tbl signature is strong in stream but global gradients are not class-specific',
        f"watcher_score={hqql_task.get('score','n/a')} state={hqql_task.get('state','n/a')}",
        'none yet; class-specific gradient missing' if not class_grad else 'class-specific gradients available',
        '' if class_grad else 'class-specific all-head gradients',
        'global all-head gradient can hide class-specific roles',
        'run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq',
        'NEEDS_CLASS_SPECIFIC_TEST' if not class_grad else 'SUPPORTED_BY_MULTIPLE_SIGNALS',
        'P0','class_specific_gradient_required',hqql_task)

    neg_task=next((t for t in watcher.get('task_scores',[]) if 'NEGATIVE' in t.get('task_id','')),{})
    add(rows,'C6_NEGATIVE_GATES_VS_SUPPRESSIVE_ROLE',
        'negative gate gradients may indicate suppressive heads',
        f"watcher_score={neg_task.get('score','n/a')} state={neg_task.get('state','n/a')}",
        'negative gradient can be local objective artifact',
        'class-specific negative gradients / suppressive patch analysis',
        'not causal until class-specific and patch tests agree',
        'add suppressive-head analysis and compare patch effects',
        'NEEDS_CLASS_SPECIFIC_TEST',
        'P1','negative_gate_suppressive_analysis',neg_task)

    # Sort by priority/status.
    prio={'P0':0,'P1':1,'P2':2}
    rows=sorted(rows,key=lambda r:(prio.get(r['priority'],9), r['status']))
    dataset=[]
    for r in rows:
        dataset.append({
            'schema':'automatic_comparison_training_row.v1',
            'input':{
                'comparison_id':r['comparison_id'],
                'claim':r['claim'],
                'support_signal':r['support_signal'],
                'contradiction_signal':r['contradiction_signal'],
                'missing_control':r['missing_control'],
                'risk':r['risk'],
                'evidence':json.loads(r['evidence_json'] or '{}'),
            },
            'target':{
                'status':r['status'],
                'priority':r['priority'],
                'training_label':r['training_label'],
                'recommended_next_experiment':r['recommended_next_experiment'],
            }
        })
    wcsv(args.out_csv,rows)
    wjsonl(args.out_dataset,dataset)
    out={'schema':'automatic_comparison_engine.v1','generated_at_utc':datetime.now(timezone.utc).isoformat(),'comparisons':rows,'top_p0':[r for r in rows if r['priority']=='P0']}
    wjson(args.out_json,out)
    md=['# Automatic Comparison Engine v1\n\n',
        'This report automates the specific comparisons the human analyst currently performs manually.\n\n',
        '## Comparison rows\n',
        md_table(['priority','status','comparison','claim','support','missing_control','next'],[[r['priority'],r['status'],r['comparison_id'],r['claim'],r['support_signal'],r['missing_control'],r['recommended_next_experiment']] for r in rows]),
        '\n## Main interpretation\n\n',
        '- Strong particle0/core signals are not enough. They must be compared against missing particle0/top-k controls.\n',
        '- Wide secondary signals are useful only after route-neighbor trace.\n',
        '- Head gradient and patch evidence must be compared, not merged blindly.\n',
        '- Hqql/Tbl stream dominance requires class-specific gradients.\n\n',
        '## Files\n\n',
        f'- JSON: `{args.out_json}`\n',
        f'- CSV: `{args.out_csv}`\n',
        f'- Training rows: `{args.out_dataset}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'comparisons':len(rows),'p0':len([r for r in rows if r['priority']=='P0']),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
