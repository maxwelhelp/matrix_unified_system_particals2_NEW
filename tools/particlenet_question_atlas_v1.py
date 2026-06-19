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

def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def writecsv(path,rows):
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

def confidence(effect, status=''):
    s=status.upper()
    if 'CAUSAL' in s and effect>0.25: return 'HIGH'
    if effect>0.15: return 'MEDIUM'
    if effect>0.05: return 'LOW'
    return 'WEAK'

def build_questions(edge_heads, features_pc, route_rows, particle_rows, board, baseline):
    acc=fnum(baseline.get('acc'))
    rows=[]
    # Edge pseudo-heads as internal questions.
    for i,r in enumerate(edge_heads[:20]):
        patch_acc=fnum(r.get('patch_acc'))
        effect=max(0, acc-patch_acc)
        rows.append({
            'component_id':f"edgeconv_L{r.get('layer')}_{r.get('group')}",
            'component_type':'EdgeConv pseudo-head',
            'lens':'L2 EdgeConv pseudo-head lens',
            'question':f"Does EdgeConv layer {r.get('layer')} channel group {r.get('group')} detect/support a class-separating particle-neighborhood pattern?",
            'answer':f"Patching it changes logits; accuracy {fmt(acc)} -> {fmt(patch_acc)}; delta_logit={fmt(r.get('delta_pred_logit'))}.",
            'evidence':'research_edge_channel_heads.csv',
            'confidence':confidence(effect,'CAUSAL_PATCHED'),
            'risk':'Equal channel slice; may not match learned functional cluster.',
            'next_lens':'L3 activation-cluster pseudo-head lens + random channel controls.'
        })
    # Feature-channel questions.
    best_by_class={}
    for r in features_pc:
        cls=r.get('class_label')
        cur=best_by_class.get(cls)
        if cur is None or abs(fnum(r.get('pred_logit_drop')))>abs(fnum(cur.get('pred_logit_drop'))):
            best_by_class[cls]=r
    for cls,r in best_by_class.items():
        effect=abs(fnum(r.get('pred_logit_drop')))
        rows.append({
            'component_id':f"feature_{r.get('group')}_{cls}",
            'component_type':'Input feature channel',
            'lens':'L7 Feature-channel lens',
            'question':f"Does {cls} rely on explicit particle feature `{r.get('group')}`?",
            'answer':f"Zeroing `{r.get('group')}` gives logit_drop={fmt(r.get('pred_logit_drop'))}; class accuracy {fmt(r.get('base_acc'))}->{fmt(r.get('patch_acc'))}.",
            'evidence':'research_feature_channels_per_class.csv',
            'confidence':'HIGH' if effect>7 else 'MEDIUM' if effect>4 else 'LOW',
            'risk':'Feature zeroing may be out-of-distribution.',
            'next_lens':'Permutation/noise controls for this feature channel.'
        })
    # Route width question.
    by_layer={}
    for r in route_rows:
        by_layer.setdefault(str(r.get('layer')),[]).append(r)
    for layer,rs in by_layer.items():
        if not rs: continue
        lo=min(rs,key=lambda x:fnum(x.get('neighbor_dr_mean')))
        hi=max(rs,key=lambda x:fnum(x.get('neighbor_dr_mean')))
        gap=fnum(hi.get('neighbor_dr_mean'))-fnum(lo.get('neighbor_dr_mean'))
        rows.append({
            'component_id':f"route_width_L{layer}",
            'component_type':'KNN / EdgeConv route',
            'lens':'L5 Particle route-width lens',
            'question':f"Does EdgeConv layer {layer} ask compact-neighborhood vs wide-neighborhood questions differently by class?",
            'answer':f"Lowest mean neighbor ΔR: {lo.get('class_label')}={fmt(lo.get('neighbor_dr_mean'))}; highest: {hi.get('class_label')}={fmt(hi.get('neighbor_dr_mean'))}; gap={fmt(gap)}.",
            'evidence':'discovery_route_knn_stats.csv',
            'confidence':'MEDIUM' if gap>0.08 else 'LOW',
            'risk':'Descriptive only; may be explained by mass/multiplicity.',
            'next_lens':'L6 compact/wide route causal lens.'
        })
    # Particle subset question.
    pr={r.get('group'):r for r in particle_rows}
    if 'top_pt' in pr and 'random_control' in pr:
        top_acc=fnum(pr['top_pt'].get('patch_acc'))
        rnd_acc=fnum(pr['random_control'].get('patch_acc'))
        rows.append({
            'component_id':'particle_subset_top_pt',
            'component_type':'Particle subset',
            'lens':'L4 Leading-particle lens',
            'question':'Does the model rely on leading high-pT particles more than random particles?',
            'answer':f"top_pt ablation accuracy={fmt(top_acc)}; random_control accuracy={fmt(rnd_acc)}; gap={fmt(rnd_acc-top_acc)}.",
            'evidence':'discovery_particle_controls.csv',
            'confidence':'HIGH' if (rnd_acc-top_acc)>0.2 else 'MEDIUM',
            'risk':'top_pt and top_energy overlap; needs top-k sweep.',
            'next_lens':'Top-k sweep k=1,2,4,8,16 and per-class particle ablation.'
        })
    # Research board hypotheses as meta-questions.
    for h in board:
        rows.append({
            'component_id':h.get('id'),
            'component_type':'Research hypothesis',
            'lens':'Research synthesis board',
            'question':h.get('title'),
            'answer':h.get('core evidence'),
            'evidence':'research_hypothesis_board.csv',
            'confidence':h.get('status'),
            'risk':h.get('risk'),
            'next_lens':h.get('next test')
        })
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-dir',default='runs/particlenet_question_atlas_v1')
    args=ap.parse_args()
    out=Path(args.out_dir); (out/'tables').mkdir(parents=True,exist_ok=True)
    v5=loadjson('manifests/latest/particlenet_research_compass_v5_summary.json')
    v6=loadjson('manifests/latest/particlenet_research_synthesis_v6_summary.json')
    baseline=v6.get('baseline') or v5.get('baseline') or {}
    edge_heads=readcsv('reports/latest/tables/research_edge_channel_heads.csv')
    features_pc=readcsv('reports/latest/tables/research_feature_channels_per_class.csv')
    route_rows=readcsv('reports/latest/tables/discovery_route_knn_stats.csv')
    particle_rows=readcsv('reports/latest/tables/discovery_particle_controls.csv')
    board=readcsv('reports/latest/tables/research_hypothesis_board.csv')
    questions=build_questions(edge_heads,features_pc,route_rows,particle_rows,board,baseline)
    writecsv(out/'tables/network_question_map.csv',questions)
    summary={'ok':True,'baseline':baseline,'n_questions':len(questions),'counts_by_type':{}}
    for q in questions:
        summary['counts_by_type'][q['component_type']]=summary['counts_by_type'].get(q['component_type'],0)+1
    wjson(out/'particlenet_question_atlas_v1_summary.json',summary)
    # rank display: high/medium first, causal board first.
    priority={'HIGH':0,'CAUSAL_PATCHED':1,'MEDIUM':2,'OBSERVED':3,'LOW':4,'TODO':5,'PAUSED':6,'WEAK':7}
    disp=sorted(questions,key=lambda q:priority.get(str(q.get('confidence','')).upper(),9))
    md=['# ParticleNet Question Atlas v1\n\n',
        'This report turns components/lenses into a map of questions the network appears to ask and answers/effects it produces.\n\n',
        '## Baseline\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Question map\n',
        md_table(['component','type','lens','question','answer','confidence','risk','next lens'],[[q['component_id'],q['component_type'],q['lens'],q['question'],q['answer'],q['confidence'],q['risk'],q['next_lens']] for q in disp[:80]]),
        '\n## How to use this map\n\n',
        '- Treat each row as a hypothesis about one internal question.\n',
        '- Do not promote a row to a physics claim until it has causal evidence, controls, and heldout stability.\n',
        '- Add new lenses when a question is still too vague.\n',
        '- For ParticleNet, EdgeConv pseudo-heads are the current analogue of attention heads.\n',
        '- For Transformer/ParT, only build attention-head question maps after a valid checkpoint is found.\n\n',
        '## Output files\n\n- `reports/latest/tables/network_question_map.csv`\n- `manifests/latest/particlenet_question_atlas_v1_summary.json`\n']
    (out/'PARTICLENET_QUESTION_ATLAS_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
