#!/usr/bin/env python3
import argparse, json
from pathlib import Path


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

def fnum(x, default=0.0):
    try: return float(x)
    except Exception: return default

def match(ev,args):
    text=' '.join([
        str(ev.get('event_type','')),
        str(ev.get('title','')),
        str(ev.get('summary','')),
        ' '.join(str(t) for t in ev.get('tags',[])),
        json.dumps(ev.get('payload',{}),ensure_ascii=False),
    ]).lower()
    if args.event_type and ev.get('event_type') != args.event_type:
        return False
    if args.query and args.query.lower() not in text:
        return False
    if args.head and args.head.lower() not in text:
        return False
    if args.class_label and args.class_label.lower() not in text:
        return False
    if args.hypothesis and args.hypothesis.lower() not in text:
        return False
    if args.tag and args.tag.lower() not in [str(t).lower() for t in ev.get('tags',[])]:
        return False
    return True

def main():
    ap=argparse.ArgumentParser(description='Query research stream events.')
    ap.add_argument('--events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--query',default='')
    ap.add_argument('--head',default='')
    ap.add_argument('--class-label',default='')
    ap.add_argument('--hypothesis',default='')
    ap.add_argument('--event-type',default='')
    ap.add_argument('--tag',default='')
    ap.add_argument('--top',type=int,default=25)
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    rows=[ev for ev in load_jsonl(args.events) if match(ev,args)]
    rows=sorted(rows,key=lambda e:fnum(e.get('score')),reverse=True)[:args.top]
    if args.json:
        print(json.dumps(rows,indent=2,ensure_ascii=False))
        return
    print(f'found={len(rows)}')
    for i,e in enumerate(rows,1):
        print(f"\n[{i}] {e.get('event_type')} score={e.get('score'):.4f} run={e.get('run_index')}")
        print(f"title: {e.get('title')}")
        print(f"tags: {', '.join(str(t) for t in e.get('tags',[]))}")
        if e.get('summary'):
            print(f"summary: {e.get('summary')}")
        payload=e.get('payload') or {}
        # Compact useful payload keys.
        keys=['head_id','gate_abs_grad','gate_grad','patch_acc_drop','role','question','semantic_hint','next_test','pred_label','particle_idx','super_score','pt','energy','deltaR_from_axis','charge','status','title']
        compact={k:payload.get(k) for k in keys if k in payload and payload.get(k) not in (None,'')}
        if compact:
            print('payload:', json.dumps(compact,ensure_ascii=False))

if __name__=='__main__':
    main()
