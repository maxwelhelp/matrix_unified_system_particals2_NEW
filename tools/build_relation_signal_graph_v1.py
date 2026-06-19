#!/usr/bin/env python3
import argparse, csv, json, math
from pathlib import Path
from collections import Counter, defaultdict
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

def load_jsonl(path):
    p=Path(path)
    if not p.exists(): return []
    rows=[]
    with p.open('r',encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if not line: continue
            try: rows.append(json.loads(line))
            except Exception: pass
    return rows

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

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def tags(ev):
    return [str(t) for t in ev.get('tags',[])]

def add_node(nodes,node_id,node_type,label='',score=0.0,**attrs):
    n=nodes.setdefault(node_id,{'node_id':node_id,'node_type':node_type,'label':label or node_id,'score':0.0})
    n['score']=max(fnum(n.get('score')), fnum(score))
    n.update(attrs)

def add_edge(edges,src,dst,rel_type,support=1,strength=0.0,lift_like=1.0,confidence='LOW',risk='',next_control='',evidence=''):
    key=(src,dst,rel_type)
    if key not in edges:
        edges[key]={'src':src,'dst':dst,'relation_type':rel_type,'support':0,'strength_sum':0.0,'max_strength':0.0,'lift_like':lift_like,'confidence':confidence,'risk':risk,'next_control':next_control,'evidence':evidence}
    e=edges[key]
    e['support'] += int(support)
    e['strength_sum'] += fnum(strength)
    e['max_strength'] = max(fnum(e.get('max_strength')), fnum(strength))
    e['lift_like'] = max(fnum(e.get('lift_like')), fnum(lift_like))
    # Keep stronger confidence.
    order={'LOW':0,'MEDIUM':1,'HIGH':2}
    if order.get(confidence,0) > order.get(e.get('confidence','LOW'),0):
        e['confidence']=confidence
    if risk and not e.get('risk'): e['risk']=risk
    if next_control and not e.get('next_control'): e['next_control']=next_control
    if evidence and not e.get('evidence'): e['evidence']=evidence

def finalize_edges(edges):
    rows=[]
    for e in edges.values():
        support=max(1,int(e['support']))
        e=dict(e)
        e['mean_strength']=e['strength_sum']/support
        # relation_signal combines support, max strength, and lift-like but keeps bounded.
        e['relation_signal']=min(1.0, math.log1p(support)/math.log(101) * 0.35 + min(1.0,e['max_strength']/5.0)*0.45 + min(2.0,e['lift_like'])/2.0*0.20)
        rows.append(e)
    return sorted(rows,key=lambda r:(fnum(r.get('relation_signal')),fnum(r.get('support'))),reverse=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream-index',default='manifests/latest/research_stream_index_v1.json')
    ap.add_argument('--watcher',default='manifests/latest/stream_task_watcher_v1.json')
    ap.add_argument('--events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--out-json',default='manifests/latest/relation_signal_graph_v1.json')
    ap.add_argument('--out-md',default='reports/latest/RELATION_SIGNAL_GRAPH_V1.md')
    ap.add_argument('--out-nodes',default='reports/latest/tables/relation_signal_nodes.csv')
    ap.add_argument('--out-edges',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--out-alerts',default='reports/latest/tables/relation_signal_alerts.csv')
    args=ap.parse_args()

    stream=loadjson(args.stream_index)
    watcher=loadjson(args.watcher)
    events=load_jsonl(args.events)
    latest_idx=int(stream.get('latest_run_index', max([int(e.get('run_index',0)) for e in events], default=0)))
    latest=[e for e in events if int(e.get('run_index',-1))==latest_idx]
    nodes={}; edges={}; alerts=[]

    add_node(nodes,'run:latest','run',f'latest run {latest_idx}',score=1.0)

    # Stream head nodes and head-hypothesis/method relations.
    for e in latest:
        if e.get('event_type')=='HEAD_GATE':
            p=e.get('payload') or {}
            hid=p.get('head_id') or e.get('title','').split()[0]
            hnode='head:'+hid
            add_node(nodes,hnode,'head',hid,score=e.get('score'),layer=p.get('layer'),channels=p.get('channels'),role=p.get('role'),question=p.get('question'))
            add_edge(edges,'run:latest',hnode,'run_has_head_signal',support=1,strength=e.get('score'),confidence='MEDIUM',risk='gradient signal is not causal patch proof',next_control='compare with patch and class-specific gradients',evidence=e.get('title'))
            if 'negative_gate' in tags(e):
                add_node(nodes,'hypothesis:NEGATIVE_GATES','hypothesis','negative/suppressive gates',score=e.get('score'))
                add_edge(edges,hnode,'hypothesis:NEGATIVE_GATES','head_supports_hypothesis',support=1,strength=e.get('score'),confidence='MEDIUM',risk='negative gradient may be local objective artifact',next_control='class-specific suppressive-head analysis',evidence=e.get('title'))
            # Method links.
            add_node(nodes,'hypothesis:AH4','hypothesis','head-system mixture across layers',score=e.get('score'))
            add_edge(edges,hnode,'hypothesis:AH4','head_supports_hypothesis',support=1,strength=e.get('score'),confidence='MEDIUM',risk='needs multi-head patch controls',next_control='multi-head patch combinations',evidence=e.get('title'))

    # Particle pattern to class relations.
    particle_events=[e for e in latest if e.get('event_type')=='PARTICLE_TOP']
    total_particles=max(1,len(particle_events))
    class_counts=Counter()
    pattern_counts=Counter()
    pair_counts=Counter()
    score_sums=defaultdict(float)
    for e in particle_events:
        ts=tags(e)
        cls=next((t for t in ts if t.startswith('label_')), 'label_unknown')
        patterns=[]
        if 'particle0' in ts: patterns.append('pattern:particle0')
        if 'core_high_pt' in ts: patterns.append('pattern:core_high_pt')
        if 'wide' in ts: patterns.append('pattern:wide')
        if 'charged' in ts: patterns.append('pattern:charged')
        if not patterns: patterns.append('pattern:other_particle')
        class_counts[cls]+=1
        add_node(nodes,'class:'+cls,'class',cls,score=class_counts[cls])
        for pat in patterns:
            pattern_counts[pat]+=1
            pair_counts[(pat,cls)]+=1
            score_sums[(pat,cls)] += fnum(e.get('score'))
            add_node(nodes,pat,'particle_pattern',pat.replace('pattern:',''),score=pattern_counts[pat])
    for (pat,cls),support in pair_counts.items():
        p_pair=support/total_particles
        p_pat=pattern_counts[pat]/total_particles
        p_cls=class_counts[cls]/total_particles
        lift=p_pair/max(1e-9,p_pat*p_cls)
        mean_score=score_sums[(pat,cls)]/max(1,support)
        conf='HIGH' if support>=20 and lift>1.2 else 'MEDIUM' if support>=5 else 'LOW'
        risk='co-occurrence only; can reflect sorting or class imbalance'
        next_control='particle0/top-k/random controls' if pat in ('pattern:particle0','pattern:core_high_pt') else 'route-neighbor trace and heldout stability'
        add_edge(edges,pat,'class:'+cls,'particle_pattern_associated_with_class',support=support,strength=mean_score,lift_like=lift,confidence=conf,risk=risk,next_control=next_control,evidence=f'{pat}->{cls} support={support}')
        # Link strong particle0/core to AH1.
        if pat in ('pattern:particle0','pattern:core_high_pt'):
            add_node(nodes,'hypothesis:AH1','hypothesis','distributed core-anchor + secondary context',score=mean_score)
            add_edge(edges,pat,'hypothesis:AH1','pattern_supports_hypothesis',support=support,strength=mean_score,lift_like=lift,confidence=conf,risk='may be leading-particle shortcut',next_control='remove particle0 / keep only particle0 / top-k controls',evidence=f'{pat} dominates top particle stream')
        if pat == 'pattern:wide':
            add_node(nodes,'hypothesis:T6_WIDE_SECONDARY_CONTEXT','hypothesis','wide secondary context',score=mean_score)
            add_edge(edges,pat,'hypothesis:T6_WIDE_SECONDARY_CONTEXT','pattern_supports_hypothesis',support=support,strength=mean_score,lift_like=lift,confidence=conf,risk='needs KNN neighbor and causal route controls',next_control='route-neighbor trace',evidence=f'wide particles support {cls}')

    # Task watcher relations.
    task_scores=watcher.get('task_scores') or []
    for t in task_scores:
        tid='task:'+t.get('task_id')
        score=fnum(t.get('score'))
        add_node(nodes,tid,'task',t.get('task_id'),score=score,priority=t.get('priority'),state=t.get('state'),question=t.get('question'))
        if 'PARTICLE0' in tid:
            dst='hypothesis:AH1'
        elif 'HEAD_RANK' in tid:
            dst='hypothesis:AH4'
        elif 'NEGATIVE' in tid:
            dst='hypothesis:NEGATIVE_GATES'
        elif 'HQQL_TBL' in tid:
            dst='hypothesis:AH2'
            add_node(nodes,dst,'hypothesis','Hqql/Tbl high-confidence signature',score=score)
        elif 'PATCH_VS_GRADIENT' in tid:
            dst='hypothesis:AH3'
            add_node(nodes,dst,'hypothesis','single-head and all-head evidence differ',score=score)
        elif 'WIDE_SECONDARY' in tid:
            dst='hypothesis:T6_WIDE_SECONDARY_CONTEXT'
        else:
            dst='hypothesis:UNKNOWN'
        add_edge(edges,tid,dst,'task_monitors_hypothesis',support=1,strength=score,confidence=t.get('state','LOW'),risk='task score is deterministic weak signal',next_control=t.get('next_action'),evidence=t.get('question'))
        if t.get('state') in ('HIGH','MEDIUM'):
            alerts.append({'severity':'HIGH' if t.get('state')=='HIGH' and t.get('priority')=='P0' else 'MEDIUM','relation':f'{tid}->{dst}','score':score,'next_control':t.get('next_action'),'reason':t.get('question')})

    edge_rows=finalize_edges(edges)
    node_rows=sorted(nodes.values(),key=lambda n:fnum(n.get('score')),reverse=True)
    # Add alerts from strongest uncontrolled candidate relations.
    for e in edge_rows[:30]:
        if e.get('confidence')=='HIGH' and e.get('next_control'):
            alerts.append({'severity':'HIGH','relation':f"{e['src']}->{e['dst']}",'score':e.get('relation_signal'),'next_control':e.get('next_control'),'reason':e.get('risk')})
    alerts=sorted(alerts,key=lambda a:fnum(a.get('score')),reverse=True)[:30]

    out={
        'schema':'relation_signal_graph.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'latest_run_index':latest_idx,
        'n_nodes':len(node_rows),
        'n_edges':len(edge_rows),
        'top_edges':edge_rows[:50],
        'alerts':alerts,
        'next_actions':[
            'Run particle0/top-k controls to validate AH1 core-anchor signal.',
            'Run class-specific all-head gradients to upgrade head-class relations.',
            'Run route-neighbor trace to validate wide/secondary context relations.',
            'Add causal_edge_score after controls are available.',
        ]
    }
    wjson(args.out_json,out)
    wcsv(args.out_nodes,node_rows)
    wcsv(args.out_edges,edge_rows)
    wcsv(args.out_alerts,alerts)

    md=['# Relation Signal Graph v1\n\n',
        'Automatic relationship mining over the stream/evidence graph. Signals are prioritization, not causal proof.\n\n',
        f"- Latest run index: **{latest_idx}**\n",
        f"- Nodes: **{len(node_rows)}**\n",
        f"- Edges: **{len(edge_rows)}**\n\n",
        '## Top relation signals\n',
        md_table(['signal','support','src','relation','dst','strength','lift','confidence','next_control'],[[fmt(e.get('relation_signal')),e.get('support'),e.get('src'),e.get('relation_type'),e.get('dst'),fmt(e.get('mean_strength')),fmt(e.get('lift_like')),e.get('confidence'),e.get('next_control')] for e in edge_rows[:25]]),
        '\n## Alerts / controls\n',
        md_table(['severity','relation','score','next_control','reason'],[[a.get('severity'),a.get('relation'),fmt(a.get('score')),a.get('next_control'),a.get('reason')] for a in alerts[:20]]),
        '\n## Interpretation\n\n',
        '- Strong particle0/core relations are currently candidates, not proof. They require particle0/top-k controls.\n',
        '- Head relations are mostly gradient/support relations until class-specific gradients and causal patches are added.\n',
        '- Wide/secondary relations need route-neighbor trace.\n\n',
        '## Files\n\n',
        f'- JSON: `{args.out_json}`\n',
        f'- Edges: `{args.out_edges}`\n',
        f'- Nodes: `{args.out_nodes}`\n',
        f'- Alerts: `{args.out_alerts}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'nodes':len(node_rows),'edges':len(edge_rows),'alerts':len(alerts),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
