#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path


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

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

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

def layer_bucket(row):
    l=str(row.get('layer',''))
    if l=='0': return 'L0 early raw feature / geometry / PID readers'
    if l=='1': return 'L1 middle learned-neighborhood / route-composition heads'
    if l=='2': return 'L2 late aggregation / class-evidence heads'
    return 'other'

def compact_row(r):
    return {
        'head_id':r.get('head_id'),
        'layer':r.get('layer'),
        'group':r.get('group'),
        'channels':r.get('channels'),
        'acc_drop':fnum(r.get('acc_drop')),
        'base_acc':fnum(r.get('base_acc')),
        'patch_acc':fnum(r.get('patch_acc')),
        'delta_pred_logit':fnum(r.get('delta_pred_logit')),
        'kl':fnum(r.get('kl')),
        'role':r.get('role'),
        'question':r.get('question'),
        'semantic_hint':r.get('semantic_hint'),
        'confidence':r.get('confidence'),
        'composite_lens':r.get('composite_lens'),
        'top_weight_projection_evidence':r.get('top_weight_projection_evidence'),
        'top_class_effects':r.get('top_class_effects'),
        'next_test':r.get('next_test'),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',default='reports/latest/tables/head_projection_question_map.csv')
    ap.add_argument('--out-md',default='reports/latest/ALL_HEAD_QUESTIONS_AND_ANALYSIS.md')
    ap.add_argument('--out-json',default='manifests/latest/all_head_questions_and_analysis.json')
    args=ap.parse_args()
    rows=[compact_row(r) for r in readcsv(args.input)]
    rows=sorted(rows,key=lambda r:r['acc_drop'],reverse=True)
    buckets={}
    for r in rows:
        buckets.setdefault(layer_bucket(r),[]).append(r)
    strongest=rows[0] if rows else {}
    data={
        'schema':'all_head_questions_and_analysis.v1',
        'source':args.input,
        'n_heads':len(rows),
        'strongest_head':strongest,
        'heads':rows,
        'by_layer':{k:v for k,v in buckets.items()},
        'how_to_read':{
            'question':'best current natural-language question for this pseudo-head',
            'semantic_hint':'weak interpretation from weight projections + class effects, not proof',
            'composite_lens':'what to combine next to make the projection logically strong',
            'next_test':'the next causal/projection test to validate the interpretation'
        }
    }
    wjson(args.out_json,data)
    md=['# ALL HEAD QUESTIONS AND ANALYSIS\n\n',
        'This is the explicit file for all current ParticleNet pseudo-head questions and analysis. It is generated from `reports/latest/tables/head_projection_question_map.csv`.\n\n',
        '## What this file contains\n\n',
        '- every current EdgeConv pseudo-head group;\n',
        '- its causal effect;\n',
        '- the natural-language question it appears to ask;\n',
        '- semantic hint from weight projections and class effects;\n',
        '- composite projection lens to test next;\n',
        '- next validation test.\n\n']
    if strongest:
        md += ['## Strongest current head\n\n',
               f"**Head:** `{strongest.get('head_id')}`\n\n",
               f"**Effect:** accuracy `{fmt(strongest.get('base_acc'))} -> {fmt(strongest.get('patch_acc'))}`, acc_drop `{fmt(strongest.get('acc_drop'))}`, delta_logit `{fmt(strongest.get('delta_pred_logit'))}`.\n\n",
               f"**Role:** {strongest.get('role')}\n\n",
               f"**Question:** {strongest.get('question')}\n\n",
               f"**Semantic hint:** {strongest.get('semantic_hint')}\n\n",
               f"**Composite lens:** `{strongest.get('composite_lens')}`\n\n",
               f"**Weight evidence:** {strongest.get('top_weight_projection_evidence')}\n\n",
               f"**Class effects:** {strongest.get('top_class_effects')}\n\n",
               f"**Next test:** {strongest.get('next_test')}\n\n"]
    for b,rs in buckets.items():
        md += [f'## {b}\n\n', md_table(['head','acc_drop','role','question','semantic_hint','confidence','next_test'],[[r.get('head_id'),fmt(r.get('acc_drop')),r.get('role'),r.get('question'),r.get('semantic_hint'),r.get('confidence'),r.get('next_test')] for r in rs]), '\n']
    md += ['## Full JSON\n\nMachine-readable full version: `manifests/latest/all_head_questions_and_analysis.json`.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'n_heads':len(rows),'out_md':args.out_md,'out_json':args.out_json,'strongest':strongest.get('head_id')},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
