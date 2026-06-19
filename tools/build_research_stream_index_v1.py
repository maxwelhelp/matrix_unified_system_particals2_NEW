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

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def wjsonl(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')

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
        if g: items.append((fp,g))
    latest=loadjson(latest_path)
    if latest and (not items or items[-1][1].get('generated_at_utc') != latest.get('generated_at_utc')):
        items.append((latest_path,latest))
    return items

def add_event(events,event_type,run_index,source_path,title,score=0.0,tags=None,summary='',payload=None):
    ev={
        'event_type':event_type,
        'run_index':run_index,
        'source_path':source_path,
        'title':title,
        'score':float(score or 0.0),
        'tags':tags or [],
        'summary':summary,
        'payload':payload or {}
    }
    events.append(ev)
    return ev

def build_stream(graphs):
    events=[]
    for idx,(path,g) in enumerate(graphs):
        summary=g.get('summary') or {}
        add_event(events,'RUN_SUMMARY',idx,path,
                  f"Run {idx}: acc={fmt(summary.get('baseline_acc'))}, events={summary.get('n_events')}",
                  score=fnum(summary.get('baseline_acc')),
                  tags=['run','summary'],summary='Evidence graph snapshot summary.',payload=summary)
        # Heads
        heads=sorted(g.get('head_vectors') or [],key=lambda h:fnum(h.get('gate_abs_grad')),reverse=True)
        for rank,h in enumerate(heads,1):
            hid=h.get('head_id')
            tags=['head','gate',str(h.get('layer')),hid or '']
            if rank<=5: tags.append('top5_head')
            if fnum(h.get('gate_grad'))<0: tags.append('negative_gate')
            add_event(events,'HEAD_GATE',idx,path,
                      f"{hid} rank {rank} gate_abs={fmt(h.get('gate_abs_grad'))}",
                      score=fnum(h.get('gate_abs_grad')),tags=tags,
                      summary=h.get('question',''),payload=dict(h,head_rank=rank))
            if h.get('question') or h.get('semantic_hint'):
                add_event(events,'HEAD_QUESTION',idx,path,
                          f"{hid}: {h.get('role','head question')}",
                          score=fnum(h.get('gate_abs_grad')),tags=['head','question',hid or ''],
                          summary=(h.get('question','')+' | '+h.get('semantic_hint','')).strip(),payload=h)
        # Events and particles
        for n in g.get('nodes',[]):
            if n.get('type')=='event':
                add_event(events,'MODEL_EVENT',idx,path,
                          f"event {n.get('event_idx')} pred={n.get('pred_label')} score={fmt(n.get('super_max_particle_score'))}",
                          score=fnum(n.get('super_max_particle_score')),tags=['event',n.get('pred_label','')],summary='Top model event in evidence graph.',payload=n)
        particles=sorted(g.get('particle_vectors') or [],key=lambda p:fnum(p.get('super_score')),reverse=True)
        for p in particles[:300]:
            tags=['particle',p.get('pred_label',''),f"particle_{p.get('particle_idx')}"]
            if str(p.get('particle_idx'))=='0': tags.append('particle0')
            if fnum(p.get('deltaR_from_axis'))>0.5: tags.append('wide')
            if fnum(p.get('pt'))>50: tags.append('core_high_pt')
            if abs(fnum(p.get('charge')))>0.5: tags.append('charged')
            add_event(events,'PARTICLE_TOP',idx,path,
                      f"event {p.get('event_idx')} particle {p.get('particle_idx')} {p.get('pred_label')} score={fmt(p.get('super_score'))}",
                      score=fnum(p.get('super_score')),tags=tags,
                      summary=f"pt={fmt(p.get('pt'))} dR={fmt(p.get('deltaR_from_axis'))} charge={fmt(p.get('charge'))}",payload=p)
        # Hypotheses
        for n in g.get('nodes',[]):
            if n.get('type')!='hypothesis': continue
            hid=n.get('hypothesis_id') or n.get('id')
            add_event(events,'HYPOTHESIS_UPDATE',idx,path,
                      f"{hid}: {n.get('title')}",score=fnum(n.get('score')),tags=['hypothesis',hid or '',n.get('status','')],
                      summary=f"status={n.get('status')} next={n.get('next_test')}",payload=n)
    return events

def summarize(events):
    latest_run=max([e['run_index'] for e in events], default=-1)
    latest=[e for e in events if e['run_index']==latest_run]
    top_heads=sorted([e for e in latest if e['event_type']=='HEAD_GATE'],key=lambda e:e['score'],reverse=True)[:10]
    top_particles=sorted([e for e in latest if e['event_type']=='PARTICLE_TOP'],key=lambda e:e['score'],reverse=True)[:20]
    hyps=[e for e in latest if e['event_type']=='HYPOTHESIS_UPDATE']
    alerts=[]
    # Alert: particle0 dominance in top particles.
    if top_particles:
        p0=sum(1 for e in top_particles if 'particle0' in e.get('tags',[]))/len(top_particles)
        if p0>0.4:
            alerts.append({'severity':'HIGH','title':'particle0/core dominance in top particle stream','score':p0,'next_action':'run particle0 removal / top-k controls','tags':['AH1','particle0','control']})
    # Alert: negative gate heads.
    neg=sorted([e for e in latest if e['event_type']=='HEAD_GATE' and 'negative_gate' in e.get('tags',[])],key=lambda e:e['score'],reverse=True)[:5]
    if neg:
        alerts.append({'severity':'MEDIUM','title':'negative/suppressive head gates exist','score':len(neg),'next_action':'compare positive vs negative gates; add suppressive-head analysis','tags':['head','negative_gate']})
    # Alert: not enough snapshots.
    runs=sorted(set(e['run_index'] for e in events))
    if len(runs)<3:
        alerts.append({'severity':'LOW','title':'need more distinct snapshots for real stream dynamics','score':len(runs),'next_action':'run distinct SAMPLES_PER_FILE / controls with HISTORY_COPY=1','tags':['dynamics','snapshots']})
    cards=[]
    cards.append({'card_id':'stream_state','title':'Stream state','value':f'{len(runs)} snapshots, {len(events)} events','priority':'P0','drilldown':'manifests/latest/research_stream_index_v1.json'})
    if top_heads:
        cards.append({'card_id':'top_head','title':'Top current all-head gate','value':top_heads[0]['title'],'priority':'P0','drilldown':'python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 10'})
    if top_particles:
        cards.append({'card_id':'top_particle','title':'Top current particle evidence','value':top_particles[0]['title'],'priority':'P0','drilldown':'python tools/query_research_stream_v1.py --event-type PARTICLE_TOP --top 20'})
    for a in alerts:
        cards.append({'card_id':'alert:'+a['title'][:24],'title':a['title'],'value':a['next_action'],'priority':'P0' if a['severity']=='HIGH' else 'P1','drilldown':'reports/latest/tables/research_stream_alerts.csv'})
    next_actions=[
        'Run particle0/top-k controls and rebuild stream index.',
        'Run class-specific all-head gradients for Hqql/Tbl/Tbqq/Wqq/Zqq.',
        'Run route-neighbor trace for top all-head particles.',
        'Create more distinct snapshots with HISTORY_COPY=1 for real dynamics.',
        'Move large stream history to SQLite/DuckDB when Git files get too large.'
    ]
    return latest_run,top_heads,top_particles,hyps,alerts,cards,next_actions

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--history-glob',default='manifests/history/research_evidence_graph_*.json')
    ap.add_argument('--latest',default='manifests/latest/research_evidence_graph_v1.json')
    ap.add_argument('--out-json',default='manifests/latest/research_stream_index_v1.json')
    ap.add_argument('--out-md',default='reports/latest/RESEARCH_STREAM_INDEX_V1.md')
    ap.add_argument('--out-events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--out-cards',default='reports/latest/tables/research_stream_cards.csv')
    ap.add_argument('--out-alerts',default='reports/latest/tables/research_stream_alerts.csv')
    args=ap.parse_args()
    graphs=collect_graphs(args.history_glob,args.latest)
    events=build_stream(graphs)
    latest_run,top_heads,top_particles,hyps,alerts,cards,next_actions=summarize(events)
    index={
        'schema':'research_stream_index.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'n_snapshots':len(graphs),
        'n_stream_events':len(events),
        'latest_run_index':latest_run,
        'main_cards':cards,
        'alerts':alerts,
        'top_heads':[e for e in top_heads[:10]],
        'top_particles':[e for e in top_particles[:20]],
        'top_hypotheses':hyps[:20],
        'next_actions':next_actions,
        'available_drilldowns':{
            'head':'python tools/query_research_stream_v1.py --head L1_ch112:128',
            'class':'python tools/query_research_stream_v1.py --class-label label_Hqql',
            'hypothesis':'python tools/query_research_stream_v1.py --hypothesis AH1',
            'particle0':'python tools/query_research_stream_v1.py --query particle0',
            'event_type':'python tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20'
        },
        'source_files':[p for p,_ in graphs]
    }
    wjson(args.out_json,index)
    wjsonl(args.out_events,events)
    wcsv(args.out_cards,cards)
    wcsv(args.out_alerts,alerts)
    md=['# Research Stream Index v1\n\n',
        'This is the first thing to read before deep logs. It converts evidence graphs into queryable stream events.\n\n',
        f"- Snapshots: **{len(graphs)}**\n",
        f"- Stream events: **{len(events)}**\n",
        f"- Latest run index: **{latest_run}**\n\n",
        '## Main cards\n',
        md_table(['priority','title','value','drilldown'],[[c.get('priority'),c.get('title'),c.get('value'),c.get('drilldown')] for c in cards]),
        '\n## Alerts\n',
        md_table(['severity','title','score','next_action'],[[a.get('severity'),a.get('title'),fmt(a.get('score')),a.get('next_action')] for a in alerts]),
        '\n## Top current heads\n',
        md_table(['rank','title','score','summary'],[[i+1,e.get('title'),fmt(e.get('score')),e.get('summary')] for i,e in enumerate(top_heads[:10])]),
        '\n## Top current particles\n',
        md_table(['rank','title','score','summary','tags'],[[i+1,e.get('title'),fmt(e.get('score')),e.get('summary'),','.join(e.get('tags',[])[:6])] for i,e in enumerate(top_particles[:15])]),
        '\n## Next actions\n']
    for a in next_actions:
        md.append(f'- {a}\n')
    md += ['\n## Drilldown examples\n\n```bash\npython tools/query_research_stream_v1.py --query particle0 --top 20\npython tools/query_research_stream_v1.py --head L1_ch112:128\npython tools/query_research_stream_v1.py --class-label label_Hqql\npython tools/query_research_stream_v1.py --hypothesis AH1\npython tools/query_research_stream_v1.py --event-type HEAD_GATE --top 20\n```\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'snapshots':len(graphs),'events':len(events),'alerts':len(alerts),'out_json':args.out_json},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
