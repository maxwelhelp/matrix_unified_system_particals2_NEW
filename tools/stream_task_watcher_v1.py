#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
from datetime import datetime, timezone

TASKS = [
    {
        'task_id':'T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR',
        'priority':'P0',
        'question':'Is the all-head system over-dominated by particle0 / leading-core evidence?',
        'next_if_high':'Run particle0 removal / keep-only particle0 / top-k removal / same-count random controls.',
    },
    {
        'task_id':'T2_HEAD_RANK_STABILITY',
        'priority':'P0',
        'question':'Do the same heads stay important across snapshots?',
        'next_if_high':'Keep tracking; if unstable, split by class/sample size and run heldout stability.',
    },
    {
        'task_id':'T3_NEGATIVE_SUPPRESSIVE_GATES',
        'priority':'P1',
        'question':'Are there heads that suppress the current class logit?',
        'next_if_high':'Add suppressive-head analysis and class-specific negative gate gradients.',
    },
    {
        'task_id':'T4_HQQL_TBL_SIGNATURE',
        'priority':'P0',
        'question':'Is the current stream dominated by Hqql/Tbl high-confidence events?',
        'next_if_high':'Run class-specific all-head gradients: Hqql, Tbl, Tbqq, Wqq, Zqq.',
    },
    {
        'task_id':'T5_PATCH_VS_GRADIENT_DIVERGENCE',
        'priority':'P1',
        'question':'Which heads are patch-important but not gradient-important, or gradient-important but not patch-important?',
        'next_if_high':'Build patch-rank vs gate-rank report and run multi-head patch combinations.',
    },
    {
        'task_id':'T6_WIDE_SECONDARY_CONTEXT',
        'priority':'P1',
        'question':'Besides particle0/core, is there stable wide/secondary particle context?',
        'next_if_high':'Run route-neighbor trace for top all-head particles and wide secondary particles.',
    },
]

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

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def tag_has(ev, tag):
    return tag in [str(t) for t in ev.get('tags',[])]

def latest_events(events, latest_idx):
    return [e for e in events if int(e.get('run_index',-1)) == latest_idx]

def score_state(score):
    if score >= 0.80: return 'HIGH'
    if score >= 0.45: return 'MEDIUM'
    if score > 0.0: return 'LOW'
    return 'NONE'

def task_score_particle0(latest):
    parts=[e for e in latest if e.get('event_type')=='PARTICLE_TOP']
    top=sorted(parts,key=lambda e:fnum(e.get('score')),reverse=True)[:50]
    if not top:
        return 0.0, {'top_particles':0}
    p0=sum(1 for e in top if tag_has(e,'particle0'))/len(top)
    core=sum(1 for e in top if tag_has(e,'core_high_pt'))/len(top)
    score=max(p0,0.5*p0+0.5*core)
    return score, {'top_particles':len(top),'particle0_fraction_top50':p0,'core_high_pt_fraction_top50':core}

def task_score_head_stability(dyn_heads, stream_index):
    latest_heads=stream_index.get('top_heads') or []
    if not latest_heads:
        return 0.0, {'top_heads':0}
    # Stable if top heads have small absolute delta rank where available.
    top_titles=[e.get('payload',{}).get('head_id') or e.get('title','') for e in latest_heads[:5]]
    recent=[r for r in dyn_heads if str(r.get('head_rank')) in {'1','2','3','4','5'}]
    deltas=[]
    for r in recent:
        if r.get('delta_rank') not in ('',None):
            deltas.append(abs(fnum(r.get('delta_rank'))))
    if not deltas:
        return 0.5, {'top_heads':top_titles,'mean_abs_delta_rank':'unknown'}
    mean_delta=sum(deltas)/len(deltas)
    score=max(0.0, min(1.0, 1.0 - mean_delta/5.0))
    return score, {'top_heads':top_titles,'mean_abs_delta_rank':mean_delta}

def task_score_negative_gates(latest):
    heads=[e for e in latest if e.get('event_type')=='HEAD_GATE']
    neg=[e for e in heads if tag_has(e,'negative_gate')]
    score=min(1.0,len(neg)/5.0)
    return score, {'negative_gate_count':len(neg),'negative_heads':[e.get('payload',{}).get('head_id') for e in neg[:10]]}

def task_score_hqql_tbl(latest):
    parts=[e for e in latest if e.get('event_type')=='PARTICLE_TOP']
    top=sorted(parts,key=lambda e:fnum(e.get('score')),reverse=True)[:80]
    if not top:
        return 0.0, {'top_particles':0}
    n_hqql=sum(1 for e in top if 'label_Hqql' in e.get('tags',[]))
    n_tbl=sum(1 for e in top if 'label_Tbl' in e.get('tags',[]))
    frac=(n_hqql+n_tbl)/len(top)
    return frac, {'top_particles':len(top),'hqql_fraction':n_hqql/len(top),'tbl_fraction':n_tbl/len(top),'hqql_tbl_fraction':frac}

def task_score_patch_grad_divergence(latest):
    heads=[e for e in latest if e.get('event_type')=='HEAD_GATE']
    diffs=[]
    samples=[]
    for e in heads:
        p=e.get('payload') or {}
        gate=fnum(p.get('gate_abs_grad'))
        patch=fnum(p.get('patch_acc_drop'))
        # Divergence if strong gate with near-zero patch, or strong patch with weak gate.
        div = gate if patch < 1e-6 and gate > 0.2 else 0.0
        if div>0:
            samples.append({'head_id':p.get('head_id'), 'gate_abs_grad':gate, 'patch_acc_drop':patch})
        diffs.append(div)
    score=min(1.0, sum(diffs[:10]) / 3.0) if diffs else 0.0
    return score, {'divergent_heads':samples[:10]}

def task_score_wide_context(latest):
    parts=[e for e in latest if e.get('event_type')=='PARTICLE_TOP']
    top=sorted(parts,key=lambda e:fnum(e.get('score')),reverse=True)[:200]
    if not top:
        return 0.0, {'top_particles':0}
    wide=sum(1 for e in top if tag_has(e,'wide'))/len(top)
    nonp0_wide=sum(1 for e in top if tag_has(e,'wide') and not tag_has(e,'particle0'))/len(top)
    score=min(1.0, 0.5*wide + nonp0_wide)
    return score, {'top_particles':len(top),'wide_fraction':wide,'non_particle0_wide_fraction':nonp0_wide}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stream-index',default='manifests/latest/research_stream_index_v1.json')
    ap.add_argument('--events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--dynamics-heads',default='reports/latest/tables/dynamics_head_ranks.csv')
    ap.add_argument('--out-json',default='manifests/latest/stream_task_watcher_v1.json')
    ap.add_argument('--out-md',default='reports/latest/STREAM_TASK_WATCHER_V1.md')
    ap.add_argument('--out-scores',default='reports/latest/tables/stream_task_watcher_scores.csv')
    ap.add_argument('--out-dataset',default='reports/latest/tables/stream_task_training_dataset.jsonl')
    args=ap.parse_args()

    stream=loadjson(args.stream_index)
    events=load_jsonl(args.events)
    dyn_heads=readcsv(args.dynamics_heads)
    latest_idx=int(stream.get('latest_run_index', max([int(e.get('run_index',0)) for e in events], default=0)))
    latest=latest_events(events, latest_idx)

    scorers={
        'T1_PARTICLE0_SHORTCUT_OR_CORE_ANCHOR': lambda: task_score_particle0(latest),
        'T2_HEAD_RANK_STABILITY': lambda: task_score_head_stability(dyn_heads, stream),
        'T3_NEGATIVE_SUPPRESSIVE_GATES': lambda: task_score_negative_gates(latest),
        'T4_HQQL_TBL_SIGNATURE': lambda: task_score_hqql_tbl(latest),
        'T5_PATCH_VS_GRADIENT_DIVERGENCE': lambda: task_score_patch_grad_divergence(latest),
        'T6_WIDE_SECONDARY_CONTEXT': lambda: task_score_wide_context(latest),
    }
    rows=[]; dataset=[]
    for t in TASKS:
        score,features=scorers[t['task_id']]()
        state=score_state(score)
        row={
            'task_id':t['task_id'],
            'priority':t['priority'],
            'state':state,
            'score':score,
            'question':t['question'],
            'next_action':t['next_if_high'],
            'features_json':json.dumps(features,ensure_ascii=False),
        }
        rows.append(row)
        dataset.append({
            'schema':'stream_task_training_row.v1',
            'run_index':latest_idx,
            'task_id':t['task_id'],
            'question':t['question'],
            'features':features,
            'weak_label_state':state,
            'weak_label_score':score,
            'target_next_action':t['next_if_high'],
        })
    rows=sorted(rows,key=lambda r:({'P0':0,'P1':1,'P2':2}.get(r['priority'],9), -r['score']))
    wcsv(args.out_scores,rows)
    wjsonl(args.out_dataset,dataset)
    out={
        'schema':'stream_task_watcher.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'latest_run_index':latest_idx,
        'n_stream_events':len(events),
        'n_latest_events':len(latest),
        'task_scores':rows,
        'top_recommendations':[r for r in rows if r['state'] in ('HIGH','MEDIUM')][:5],
        'note':'v1 uses deterministic task features and weak labels. Later this becomes MLP/attention training data after enough snapshots/controls.'
    }
    wjson(args.out_json,out)
    md=['# Stream Task Watcher v1\n\n',
        'This is an automatic watcher over the research stream. It scores only predefined tasks/questions, not arbitrary interpretations.\n\n',
        f"- Latest run index: **{latest_idx}**\n",
        f"- Stream events: **{len(events)}**\n",
        f"- Latest-run events: **{len(latest)}**\n\n",
        '## Task scores\n',
        md_table(['priority','state','score','task','question','next_action'],[[r['priority'],r['state'],fmt(r['score']),r['task_id'],r['question'],r['next_action']] for r in rows]),
        '\n## What this means\n\n']
    for r in rows:
        if r['state'] in ('HIGH','MEDIUM'):
            md.append(f"- **{r['task_id']}** is `{r['state']}` ({fmt(r['score'])}). Next: {r['next_action']}\n")
    md += ['\n## Files\n\n',
           f'- JSON: `{args.out_json}`\n',
           f'- Scores: `{args.out_scores}`\n',
           f'- Weak training dataset: `{args.out_dataset}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'latest_run_index':latest_idx,'tasks':len(rows),'top':rows[:3]},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
