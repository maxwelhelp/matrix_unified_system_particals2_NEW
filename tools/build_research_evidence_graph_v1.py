#!/usr/bin/env python3
import argparse, csv, json, hashlib
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

def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}

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

def stable_id(prefix, payload):
    s=json.dumps(payload,sort_keys=True,ensure_ascii=False)
    return prefix+':'+hashlib.sha1(s.encode('utf-8')).hexdigest()[:12]

def node(nodes, typ, id_, **attrs):
    if id_ not in nodes:
        nodes[id_]={'id':id_,'type':typ}
    nodes[id_].update(attrs)
    return id_

def edge(edges, src, dst, typ, **attrs):
    e={'src':src,'dst':dst,'type':typ}
    e.update(attrs); edges.append(e)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-json',default='manifests/latest/research_evidence_graph_v1.json')
    ap.add_argument('--out-heads',default='reports/latest/tables/evidence_head_vectors.csv')
    ap.add_argument('--out-particles',default='reports/latest/tables/evidence_particle_vectors.csv')
    ap.add_argument('--out-edges',default='reports/latest/tables/evidence_edges.csv')
    ap.add_argument('--out-md',default='reports/latest/RESEARCH_EVIDENCE_GRAPH_V1.md')
    ap.add_argument('--history-copy',action='store_true')
    args=ap.parse_args()

    super_summary=loadjson('manifests/latest/all_head_supertrace_summary.json')
    dashboard=loadjson('manifests/latest/research_dashboard_latest.json')
    head_grads=readcsv('reports/latest/tables/all_head_gate_gradients.csv')
    head_questions=readcsv('reports/latest/tables/head_projection_question_map.csv')
    patch_heads=readcsv('reports/latest/tables/research_edge_channel_heads.csv')
    particles=readcsv('reports/latest/tables/all_head_supertrace_particles.csv')
    events=readcsv('reports/latest/tables/all_head_supertrace_events.csv')
    hypo_board=readcsv('reports/latest/tables/research_hypothesis_board.csv')
    feature_map=readcsv('reports/latest/tables/research_feature_channels_per_class.csv')
    route_rows=readcsv('reports/latest/tables/discovery_route_knn_stats.csv')

    run_id='run:all_head_supertrace:v1:latest'
    generated_at=datetime.now(timezone.utc).isoformat()
    nodes={}; edges=[]
    node(nodes,'run',run_id,
         generated_at_utc=generated_at,
         n_events=super_summary.get('n_events'),
         baseline_acc=super_summary.get('baseline_acc'),
         objective_pred_logit_mean=super_summary.get('objective_pred_logit_mean'),
         micro_batch=super_summary.get('micro_batch'),
         model=super_summary.get('checkpoint','ParticleNet_kinpid.pt'))

    # Index auxiliary head data.
    q_by_head={r.get('head_id'):r for r in head_questions}
    patch_by_head={}
    for r in patch_heads:
        hid=f"L{r.get('layer')}_{r.get('group')}"
        patch_by_head[hid]=r

    head_vectors=[]
    for r in head_grads:
        hid=r.get('head_id')
        if not hid: continue
        q=q_by_head.get(hid,{})
        p=patch_by_head.get(hid,{})
        hv={
            'head_id':hid,
            'layer':r.get('layer'),
            'group_id':r.get('group_id'),
            'channels':r.get('channels'),
            'gate_grad':fnum(r.get('grad')),
            'gate_abs_grad':fnum(r.get('abs_grad')),
            'gate_positive_grad':fnum(r.get('positive_grad')),
            'patch_acc_drop':fnum(p.get('acc_drop')) if p else '',
            'patch_acc':fnum(p.get('patch_acc')) if p else '',
            'patch_delta_pred_logit':fnum(p.get('delta_pred_logit')) if p else '',
            'role':q.get('role',''),
            'question':q.get('question',''),
            'semantic_hint':q.get('semantic_hint',''),
            'confidence':q.get('confidence',''),
            'next_test':q.get('next_test',''),
        }
        head_vectors.append(hv)
        hnode=node(nodes,'head','head:'+hid,**hv)
        edge(edges,run_id,hnode,'run_has_head',gate_abs_grad=hv['gate_abs_grad'],patch_acc_drop=hv['patch_acc_drop'])

    # Events.
    for r in events:
        eid='event:'+str(r.get('event_idx'))
        node(nodes,'event',eid,
             event_idx=r.get('event_idx'),
             true_label=r.get('true_label'),
             pred_label=r.get('pred_label'),
             conf=fnum(r.get('conf')),
             pred_logit=fnum(r.get('pred_logit')),
             super_max_particle_score=fnum(r.get('super_max_particle_score')),
             real_particles=r.get('real_particles'),
             effective_particles=r.get('effective_particles'))
        edge(edges,run_id,eid,'run_has_event',super_max_particle_score=fnum(r.get('super_max_particle_score')))
        cnode=node(nodes,'class','class:'+str(r.get('pred_label')),label=r.get('pred_label'))
        edge(edges,eid,cnode,'event_predicted_as',conf=fnum(r.get('conf')))

    # Particles.
    particle_vectors=[]
    for r in particles:
        eid='event:'+str(r.get('event_idx'))
        pid=f"particle:{r.get('event_idx')}:{r.get('particle_idx')}"
        pv={
            'particle_node':pid,
            'event_idx':r.get('event_idx'),
            'rank':r.get('rank'),
            'particle_idx':r.get('particle_idx'),
            'true_label':r.get('true_label'),
            'pred_label':r.get('pred_label'),
            'conf':fnum(r.get('conf')),
            'super_score':fnum(r.get('super_score')),
            'pt':fnum(r.get('pt')),
            'energy':fnum(r.get('energy')),
            'deltaR_from_axis':fnum(r.get('deltaR_from_axis')),
            'deta':fnum(r.get('deta')),
            'dphi':fnum(r.get('dphi')),
            'charge':fnum(r.get('part_charge')),
            'is_charged_hadron':fnum(r.get('part_isChargedHadron')),
            'is_neutral_hadron':fnum(r.get('part_isNeutralHadron')),
            'is_photon':fnum(r.get('part_isPhoton')),
            'is_electron':fnum(r.get('part_isElectron')),
            'is_muon':fnum(r.get('part_isMuon')),
        }
        particle_vectors.append(pv)
        pnode=node(nodes,'particle',pid,**pv)
        edge(edges,eid,pnode,'event_has_top_particle',rank=r.get('rank'),super_score=pv['super_score'])

    # Hypotheses from board and updated AH hypotheses.
    for r in hypo_board:
        hid='hypothesis:'+str(r.get('id'))
        node(nodes,'hypothesis',hid,
             hypothesis_id=r.get('id'),
             title=r.get('title'),
             priority=r.get('priority'),
             status=r.get('status'),
             score=fnum(r.get('score')),
             evidence=r.get('core evidence') or r.get('core_evidence'),
             risk=r.get('risk'),
             next_test=r.get('next test') or r.get('next_test'))
        edge(edges,run_id,hid,'run_updates_hypothesis',score=fnum(r.get('score')))

    # Add explicit AH nodes after supertrace.
    ah = [
        ('AH1','Distributed core-anchor + secondary-context mechanism','OBSERVED_NEEDS_CONTROL','particle0_removal_topk_controls'),
        ('AH2','Hqql/Tbl high-confidence head-system signature','OBSERVED','class_specific_all_head_gradients'),
        ('AH3','Single-head and all-head evidence differ','METHOD_FINDING','patch_rank_vs_gate_rank'),
        ('AH4','Head-system mixture across L0/L1/L2','OBSERVED','multi_head_patch_and_class_contrast'),
    ]
    for hid,title,status,next_test in ah:
        n=node(nodes,'hypothesis','hypothesis:'+hid,hypothesis_id=hid,title=title,status=status,next_test=next_test,source='ALL_HEAD_SUPERTRACE_FINDINGS_v1')
        edge(edges,run_id,n,'run_updates_hypothesis')

    # Link top positive heads to AH4/AH3.
    for hv in sorted(head_vectors,key=lambda x:x.get('gate_abs_grad') or 0,reverse=True)[:10]:
        edge(edges,'head:'+hv['head_id'],'hypothesis:AH4','head_supports_hypothesis',gate_abs_grad=hv.get('gate_abs_grad'))
        edge(edges,'head:'+hv['head_id'],'hypothesis:AH3','head_in_method_comparison',gate_abs_grad=hv.get('gate_abs_grad'),patch_acc_drop=hv.get('patch_acc_drop'))

    # Link top particles to AH1.
    for pv in sorted(particle_vectors,key=lambda x:x.get('super_score') or 0,reverse=True)[:80]:
        edge(edges,pv['particle_node'],'hypothesis:AH1','particle_supports_hypothesis',super_score=pv.get('super_score'),pt=pv.get('pt'),deltaR=pv.get('deltaR_from_axis'))

    graph={
        'schema':'research_evidence_graph.v1',
        'generated_at_utc':generated_at,
        'run_id':run_id,
        'summary':{
            'n_nodes':len(nodes),
            'n_edges':len(edges),
            'n_head_vectors':len(head_vectors),
            'n_particle_vectors':len(particle_vectors),
            'baseline_acc':super_summary.get('baseline_acc'),
            'n_events':super_summary.get('n_events'),
        },
        'nodes':list(nodes.values()),
        'edges':edges,
        'head_vectors':head_vectors,
        'particle_vectors':particle_vectors,
        'source_files':[
            'manifests/latest/all_head_supertrace_summary.json',
            'reports/latest/tables/all_head_gate_gradients.csv',
            'reports/latest/tables/all_head_supertrace_events.csv',
            'reports/latest/tables/all_head_supertrace_particles.csv',
            'reports/latest/tables/head_projection_question_map.csv',
            'reports/latest/tables/research_hypothesis_board.csv'
        ]
    }
    wjson(args.out_json,graph)
    wcsv(args.out_heads,head_vectors)
    wcsv(args.out_particles,particle_vectors)
    wcsv(args.out_edges,edges)

    if args.history_copy:
        stamp=datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
        wjson(f'manifests/history/research_evidence_graph_{stamp}.json',graph)

    md=['# Research Evidence Graph v1\n\n',
        'This is the compact structured evidence graph for agent/neural analysis.\n\n',
        f"- Nodes: **{len(nodes)}**\n",
        f"- Edges: **{len(edges)}**\n",
        f"- Head vectors: **{len(head_vectors)}**\n",
        f"- Particle vectors: **{len(particle_vectors)}**\n",
        f"- Baseline acc: **{super_summary.get('baseline_acc')}**\n\n",
        '## Main updated hypotheses\n\n',
        '- AH1: distributed core-anchor + secondary-context mechanism.\n',
        '- AH2: Hqql/Tbl high-confidence head-system signature.\n',
        '- AH3: single-head and all-head evidence differ.\n',
        '- AH4: head-system mixture across L0/L1/L2.\n\n',
        '## Files\n\n',
        f'- JSON graph: `{args.out_json}`\n',
        f'- Head vectors: `{args.out_heads}`\n',
        f'- Particle vectors: `{args.out_particles}`\n',
        f'- Edges: `{args.out_edges}`\n\n',
        '## Next use\n\n',
        'This graph can be loaded by an agent, a notebook, Redis cache, SQLite/DuckDB, or a future neural hypothesis generator.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'nodes':len(nodes),'edges':len(edges),'heads':len(head_vectors),'particles':len(particle_vectors),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
