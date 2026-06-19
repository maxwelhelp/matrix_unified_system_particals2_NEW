#!/usr/bin/env python3
import argparse, csv, glob, json
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
    if not p.exists(): return None
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return None

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

def collect_graphs(history_glob, latest_path):
    items=[]
    for fp in sorted(glob.glob(history_glob)):
        g=loadjson(fp)
        if not g: continue
        items.append((fp,g))
    latest=loadjson(latest_path)
    if latest:
        # Avoid duplicate if latest has same generated_at as last history file.
        if not items or items[-1][1].get('generated_at_utc') != latest.get('generated_at_utc'):
            items.append((latest_path,latest))
    return items

def head_rows_for_graph(idx,path,g):
    rows=[]
    heads=g.get('head_vectors') or []
    heads=sorted(heads,key=lambda r:fnum(r.get('gate_abs_grad')),reverse=True)
    for rank,h in enumerate(heads,1):
        rows.append({
            'run_index':idx,
            'source_path':path,
            'generated_at_utc':g.get('generated_at_utc'),
            'run_id':g.get('run_id'),
            'head_rank':rank,
            'head_id':h.get('head_id'),
            'layer':h.get('layer'),
            'channels':h.get('channels'),
            'gate_grad':fnum(h.get('gate_grad')),
            'gate_abs_grad':fnum(h.get('gate_abs_grad')),
            'patch_acc_drop':fnum(h.get('patch_acc_drop')),
            'role':h.get('role'),
            'semantic_hint':h.get('semantic_hint'),
        })
    return rows

def particle_stats_for_graph(idx,path,g):
    parts=g.get('particle_vectors') or []
    if not parts:
        return []
    by_class={}
    for p in parts:
        cls=p.get('pred_label','unknown')
        by_class.setdefault(cls,[]).append(p)
    rows=[]
    for cls,ps in sorted(by_class.items()):
        n=len(ps)
        if n==0: continue
        particle0=sum(1 for p in ps if str(p.get('particle_idx'))=='0')/n
        rows.append({
            'run_index':idx,
            'source_path':path,
            'generated_at_utc':g.get('generated_at_utc'),
            'pred_label':cls,
            'n_particles':n,
            'mean_super_score':sum(fnum(p.get('super_score')) for p in ps)/n,
            'mean_pt':sum(fnum(p.get('pt')) for p in ps)/n,
            'mean_energy':sum(fnum(p.get('energy')) for p in ps)/n,
            'mean_deltaR':sum(fnum(p.get('deltaR_from_axis')) for p in ps)/n,
            'particle0_fraction':particle0,
            'charged_fraction':sum(1 for p in ps if abs(fnum(p.get('charge'))) > 0.5)/n,
        })
    return rows

def hypothesis_rows_for_graph(idx,path,g):
    rows=[]
    for n in g.get('nodes',[]):
        if n.get('type')!='hypothesis':
            continue
        rows.append({
            'run_index':idx,
            'source_path':path,
            'generated_at_utc':g.get('generated_at_utc'),
            'hypothesis_id':n.get('hypothesis_id') or n.get('id'),
            'title':n.get('title'),
            'status':n.get('status'),
            'priority':n.get('priority'),
            'score':fnum(n.get('score')),
            'next_test':n.get('next_test'),
        })
    return rows

def add_deltas(head_rows):
    prev_by_head={}
    out=[]
    for r in sorted(head_rows,key=lambda x:(int(x['run_index']), int(x['head_rank']))):
        hid=r['head_id']
        prev=prev_by_head.get(hid)
        rr=dict(r)
        if prev:
            rr['delta_gate_abs_grad']=rr['gate_abs_grad']-prev['gate_abs_grad']
            rr['delta_rank']=rr['head_rank']-prev['head_rank']
        else:
            rr['delta_gate_abs_grad']=''
            rr['delta_rank']=''
        prev_by_head[hid]=rr
        out.append(rr)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--history-glob',default='manifests/history/research_evidence_graph_*.json')
    ap.add_argument('--latest',default='manifests/latest/research_evidence_graph_v1.json')
    ap.add_argument('--out-json',default='manifests/latest/research_dynamics_v1.json')
    ap.add_argument('--out-md',default='reports/latest/RESEARCH_DYNAMICS_V1.md')
    ap.add_argument('--out-heads',default='reports/latest/tables/dynamics_head_ranks.csv')
    ap.add_argument('--out-particles',default='reports/latest/tables/dynamics_particle_patterns.csv')
    ap.add_argument('--out-hypotheses',default='reports/latest/tables/dynamics_hypotheses.csv')
    args=ap.parse_args()

    graphs=collect_graphs(args.history_glob,args.latest)
    head_rows=[]; particle_rows=[]; hypo_rows=[]; run_rows=[]
    for idx,(path,g) in enumerate(graphs):
        summary=g.get('summary') or {}
        run_rows.append({
            'run_index':idx,
            'source_path':path,
            'generated_at_utc':g.get('generated_at_utc'),
            'n_nodes':summary.get('n_nodes'),
            'n_edges':summary.get('n_edges'),
            'n_head_vectors':summary.get('n_head_vectors'),
            'n_particle_vectors':summary.get('n_particle_vectors'),
            'baseline_acc':summary.get('baseline_acc'),
            'n_events':summary.get('n_events'),
        })
        head_rows.extend(head_rows_for_graph(idx,path,g))
        particle_rows.extend(particle_stats_for_graph(idx,path,g))
        hypo_rows.extend(hypothesis_rows_for_graph(idx,path,g))
    head_rows=add_deltas(head_rows)
    wcsv(args.out_heads,head_rows)
    wcsv(args.out_particles,particle_rows)
    wcsv(args.out_hypotheses,hypo_rows)

    latest_heads=[r for r in head_rows if r.get('run_index') == (len(graphs)-1)]
    latest_heads=sorted(latest_heads,key=lambda r:fnum(r.get('gate_abs_grad')),reverse=True)[:10]
    latest_particles=[r for r in particle_rows if r.get('run_index') == (len(graphs)-1)]
    latest_particles=sorted(latest_particles,key=lambda r:fnum(r.get('mean_super_score')),reverse=True)[:10]

    dynamics={
        'schema':'research_dynamics.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'n_graph_snapshots':len(graphs),
        'run_rows':run_rows,
        'latest_top_heads':latest_heads,
        'latest_class_particle_patterns':latest_particles,
        'has_real_dynamics':len(graphs)>=2,
        'notes':[] if len(graphs)>=2 else ['Only one graph snapshot found. Run HISTORY_COPY=1 on future evidence graph builds to get real dynamics.'],
        'source_files':[p for p,_ in graphs],
    }
    wjson(args.out_json,dynamics)

    md=['# Research Dynamics v1\n\n',
        'This report compares evidence graph snapshots across runs.\n\n',
        f'- Graph snapshots: **{len(graphs)}**\n',
        f'- Real dynamics available: **{len(graphs)>=2}**\n\n']
    if len(graphs)<2:
        md += ['## Need more snapshots\n\n',
               'Only one evidence graph snapshot is available. After every meaningful run, use:\n\n',
               '```bash\nHISTORY_COPY=1 bash scripts/RUN_RESEARCH_EVIDENCE_GRAPH_V1.sh\nbash scripts/RUN_RESEARCH_DYNAMICS_V1.sh\n```\n\n']
    md += ['## Runs\n',
           md_table(['run','generated','baseline_acc','n_events','nodes','edges','heads','particles'],[[r['run_index'],r.get('generated_at_utc'),fmt(r.get('baseline_acc')),r.get('n_events'),r.get('n_nodes'),r.get('n_edges'),r.get('n_head_vectors'),r.get('n_particle_vectors')] for r in run_rows]),
           '\n## Latest top heads\n',
           md_table(['rank','head','gate_abs','delta_gate','delta_rank','patch_drop','role'],[[r.get('head_rank'),r.get('head_id'),fmt(r.get('gate_abs_grad')),fmt(r.get('delta_gate_abs_grad')),r.get('delta_rank'),fmt(r.get('patch_acc_drop')),r.get('role')] for r in latest_heads]),
           '\n## Latest class particle patterns\n',
           md_table(['class','n','mean_score','mean_pt','mean_deltaR','particle0_fraction','charged_fraction'],[[r.get('pred_label'),r.get('n_particles'),fmt(r.get('mean_super_score')),fmt(r.get('mean_pt')),fmt(r.get('mean_deltaR')),fmt(r.get('particle0_fraction')),fmt(r.get('charged_fraction'))] for r in latest_particles]),
           '\n## Output files\n\n',
           f'- JSON: `{args.out_json}`\n',
           f'- Head dynamics: `{args.out_heads}`\n',
           f'- Particle dynamics: `{args.out_particles}`\n',
           f'- Hypothesis dynamics: `{args.out_hypotheses}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'snapshots':len(graphs),'has_real_dynamics':len(graphs)>=2,'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
