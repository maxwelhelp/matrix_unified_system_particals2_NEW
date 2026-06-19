#!/usr/bin/env python3
import argparse, csv, json, re
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

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'

def parse_ch(s):
    m=re.search(r'(\d+)\s*:\s*(\d+)', str(s))
    if not m: return None
    return int(m.group(1)), int(m.group(2))

def overlap(a,b):
    if a is None or b is None: return 0.0
    lo=max(a[0],b[0]); hi=min(a[1],b[1])
    inter=max(0,hi-lo)
    union=max(a[1],b[1])-min(a[0],b[0])
    return inter/max(1,union)

def related_weight_rows(weight_rows, layer, ch_range, max_rows=8):
    rel=[]
    for r in weight_rows:
        comp=r.get('component','')
        if f'edge_convs.{layer}' not in comp:
            continue
        # Prefer rows with matching output group / physical / block interaction.
        out=parse_ch(r.get('out_channels','') or r.get('answer',''))
        ov=overlap(ch_range,out) if out else 0.0
        lens=r.get('lens','')
        score=fnum(r.get('score'))
        keep=False
        if ov>0: keep=True
        if 'physical feature' in lens: keep=True
        if 'input/source' in lens and score>0.25: keep=True
        if 'block interaction' in lens and ov>0: keep=True
        if 'output pseudo-head' in lens and ov>0: keep=True
        if keep:
            rr=dict(r); rr['_overlap']=ov; rr['_rank']=score + 0.5*ov
            rel.append(rr)
    return sorted(rel,key=lambda x:fnum(x.get('_rank')),reverse=True)[:max_rows]

def strongest_classes(per_class_rows, layer, group, n=5):
    rows=[]
    for r in per_class_rows:
        if str(r.get('layer'))==str(layer) and str(r.get('group'))==str(group):
            rows.append(r)
    return sorted(rows,key=lambda r:abs(fnum(r.get('pred_logit_drop'))),reverse=True)[:n]

def infer_question(layer, group, causal, rel_rows, cls_rows):
    layer=int(layer)
    patch_acc=fnum(causal.get('patch_acc'))
    base_acc=fnum(causal.get('base_acc'))
    effect=base_acc-patch_acc
    rel_text='; '.join([r.get('lens','')+': '+r.get('answer','') for r in rel_rows[:3]])
    classes=', '.join([r.get('class_label','') for r in cls_rows[:3]])
    # Layer role.
    if layer==0:
        role='early feature/geometry/PID reader'
        base_q='Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?'
    elif layer==1:
        role='middle learned-neighborhood / route-composition head'
        base_q='Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?'
    else:
        role='late aggregation / class-evidence head'
        base_q='Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?'
    # Add specificity from related rows.
    tags=[]
    text=(rel_text+' '+classes).lower()
    if 'pid' in text or 'muon' in text or 'charged' in text: tags.append('PID/charge')
    if 'kin' in text or 'pt' in text or 'energy' in text or 'log' in text: tags.append('kinematic/energy')
    if 'coord' in text or 'deta' in text or 'dphi' in text or 'deltar' in text: tags.append('geometry/route-width')
    if classes: tags.append('class-specific: '+classes)
    tag_text=', '.join(tags) if tags else 'hidden source groups not yet semantically resolved'
    # Confidence.
    if effect>0.20: conf='HIGH causal, MEDIUM semantic'
    elif effect>0.08: conf='MEDIUM causal, LOW/MEDIUM semantic'
    else: conf='LOW causal, exploratory semantic'
    composite=[]
    composite.append(f'Patch lens: zero EdgeConv L{layer} {group}')
    composite.append(f'Weight lens: source/input blocks -> output {group}')
    if layer==1: composite.append('Route lens: compact/wide KNN route stats -> this pseudo-head')
    if layer==0: composite.append('Physical feature lens: raw kin/PID/geometry -> this pseudo-head')
    if layer==2: composite.append('Class direction lens: this pseudo-head -> classifier class/contrast direction')
    if cls_rows: composite.append('Class lens: strongest affected classes = '+classes)
    next_test='Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions.'
    if layer==1:
        next_test='Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 '+group+' -> class contrast.'
    return {
        'role':role,
        'question':base_q,
        'semantic_hint':tag_text,
        'confidence':conf,
        'composite_lens':' | '.join(composite),
        'next_test':next_test,
        'effect':effect
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-dir',default='runs/particlenet_head_projection_composer_v2')
    args=ap.parse_args(); out=Path(args.out_dir); (out/'tables').mkdir(parents=True,exist_ok=True)
    causal=readcsv('reports/latest/tables/research_edge_channel_heads.csv')
    weights=readcsv('reports/latest/tables/weight_projection_questions.csv')
    per_cls=readcsv('reports/latest/tables/research_edge_channel_heads_per_class.csv')
    rows=[]
    for c in causal:
        layer=c.get('layer'); group=c.get('group'); ch=parse_ch(group)
        rel=related_weight_rows(weights,layer,ch,max_rows=8)
        cls=strongest_classes(per_cls,layer,group,n=5)
        inf=infer_question(layer,group,c,rel,cls)
        rows.append({
            'head_id':f"L{layer}_{group}",
            'layer':layer,
            'group':group,
            'channels':c.get('channels'),
            'delta_pred_logit':c.get('delta_pred_logit'),
            'kl':c.get('kl'),
            'base_acc':c.get('base_acc'),
            'patch_acc':c.get('patch_acc'),
            'acc_drop':inf['effect'],
            'role':inf['role'],
            'question':inf['question'],
            'semantic_hint':inf['semantic_hint'],
            'confidence':inf['confidence'],
            'composite_lens':inf['composite_lens'],
            'top_weight_projection_evidence':' || '.join([r.get('lens','')+': '+r.get('answer','') for r in rel[:4]]),
            'top_class_effects':' || '.join([r.get('class_label','')+': drop='+fmt(r.get('pred_logit_drop'))+', acc='+fmt(r.get('patch_acc')) for r in cls[:5]]),
            'next_test':inf['next_test'],
        })
    rows=sorted(rows,key=lambda r:fnum(r.get('acc_drop')),reverse=True)
    wcsv(out/'tables/head_projection_question_map.csv',rows)
    summary={'ok':True,'n_heads':len(rows),'strongest_heads':rows[:8]}
    wjson(out/'particlenet_head_projection_composer_v2_summary.json',summary)
    # Manual deep note for the strongest head.
    top=rows[0] if rows else None
    md=['# ParticleNet Head Projection Composer v2\n\n',
        'This report combines causal pseudo-head patches with weight-projection questions. It is the head-aligned version of the projection-lens idea: not only which weight blocks are strong, but what logical question each pseudo-head may ask.\n\n']
    if top:
        md += ['## Manual-style interpretation of strongest head\n\n',
               f"**Head:** `{top['head_id']}`\n\n",
               f"**Causal effect:** accuracy `{fmt(top['base_acc'])} -> {fmt(top['patch_acc'])}`, delta logit `{fmt(top['delta_pred_logit'])}`.\n\n",
               f"**Likely role:** {top['role']}.\n\n",
               f"**Question:** {top['question']}\n\n",
               f"**Semantic hint:** {top['semantic_hint']}\n\n",
               f"**Composite projection lens:** `{top['composite_lens']}`\n\n",
               f"**Weight evidence:** {top['top_weight_projection_evidence']}\n\n",
               f"**Class effects:** {top['top_class_effects']}\n\n",
               f"**My current opinion:** this is not just a single feature detector. It is probably a middle learned-neighborhood composer: earlier feature/route evidence is compressed into a head-like channel group, then reused by the classifier. To make the projection logically strong, combine at least two elements: source hidden group -> this output head, then this head -> class/contrast or route-width lens.\n\n"]
    md += ['## All pseudo-head question map\n',
           md_table(['head','acc drop','role','question','semantic hint','confidence','next test'],[[r['head_id'],fmt(r['acc_drop']),r['role'],r['question'],r['semantic_hint'],r['confidence'],r['next_test']] for r in rows]),
           '\n## How to read this\n\n',
           '- `question` is the best current natural-language question for this pseudo-head.\n',
           '- `semantic_hint` is weaker: it is inferred from weight projections and class effects, not proven.\n',
           '- `composite_lens` tells what to combine next to make the projection stronger.\n',
           '- Strong claims require weight projection + activation/route + causal patch + random/heldout controls.\n\n',
           '## Output files\n\n- `reports/latest/tables/head_projection_question_map.csv`\n- `manifests/latest/particlenet_head_projection_composer_v2_summary.json`\n']
    (out/'PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
