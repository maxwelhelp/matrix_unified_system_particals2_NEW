#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path


def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def fnum(x):
    try: return float(x)
    except Exception: return 0.0

def match(row,args):
    text=' '.join(str(row.get(k,'')) for k in row).lower()
    if args.query and args.query.lower() not in text: return False
    if args.src and args.src.lower() not in str(row.get('src','')).lower(): return False
    if args.dst and args.dst.lower() not in str(row.get('dst','')).lower(): return False
    if args.relation and args.relation.lower() not in str(row.get('relation_type','')).lower(): return False
    if args.confidence and args.confidence.lower() != str(row.get('confidence','')).lower(): return False
    return True

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--edges',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--query',default='')
    ap.add_argument('--src',default='')
    ap.add_argument('--dst',default='')
    ap.add_argument('--relation',default='')
    ap.add_argument('--confidence',default='')
    ap.add_argument('--top',type=int,default=25)
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    rows=[r for r in readcsv(args.edges) if match(r,args)]
    rows=sorted(rows,key=lambda r:fnum(r.get('relation_signal')),reverse=True)[:args.top]
    if args.json:
        print(json.dumps(rows,indent=2,ensure_ascii=False)); return
    print(f'found={len(rows)}')
    for i,r in enumerate(rows,1):
        print(f"\n[{i}] signal={r.get('relation_signal')} support={r.get('support')} confidence={r.get('confidence')}")
        print(f"{r.get('src')} --{r.get('relation_type')}--> {r.get('dst')}")
        print(f"strength={r.get('mean_strength')} lift={r.get('lift_like')}")
        if r.get('risk'): print('risk:',r.get('risk'))
        if r.get('next_control'): print('next:',r.get('next_control'))
        if r.get('evidence'): print('evidence:',r.get('evidence'))

if __name__=='__main__': main()
