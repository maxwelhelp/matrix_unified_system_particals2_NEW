#!/usr/bin/env python3
import argparse, csv, json
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

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'

def pick_baseline():
    for p in [
        'manifests/latest/particlenet_research_synthesis_v6_summary.json',
        'manifests/latest/particlenet_research_compass_v5_summary.json',
        'manifests/latest/particlenet_hypothesis_atlas_summary.json',
    ]:
        j=loadjson(p)
        b=j.get('baseline') or {}
        if b:
            return b,p
    return {},''

def top_hypotheses(board, n=8):
    pri={'P0':0,'P1':1,'P2':2}
    out=[]
    for r in sorted(board,key=lambda x:(pri.get(x.get('priority','P9'),9), -fnum(x.get('score'))))[:n]:
        out.append({
            'id':r.get('id'), 'priority':r.get('priority'), 'status':r.get('status'),
            'score':fnum(r.get('score')), 'title':r.get('title'),
            'evidence':r.get('core evidence') or r.get('core_evidence'),
            'risk':r.get('risk'), 'next_test':r.get('next test') or r.get('next_test')
        })
    return out

def top_heads(heads, n=12):
    out=[]
    for r in sorted(heads,key=lambda x:fnum(x.get('acc_drop')),reverse=True)[:n]:
        out.append({
            'head_id':r.get('head_id'), 'layer':r.get('layer'), 'group':r.get('group'),
            'acc_drop':fnum(r.get('acc_drop')), 'patch_acc':fnum(r.get('patch_acc')),
            'delta_pred_logit':fnum(r.get('delta_pred_logit')),
            'role':r.get('role'), 'question':r.get('question'),
            'semantic_hint':r.get('semantic_hint'), 'confidence':r.get('confidence'),
            'composite_lens':r.get('composite_lens'),
            'top_class_effects':r.get('top_class_effects'),
            'next_test':r.get('next_test')
        })
    return out

def weight_question_buckets(rows):
    buckets={'physical_feature_projection':[], 'block_interaction':[], 'class_contrast':[], 'output_pseudo_head':[], 'weight_energy':[]}
    for r in rows:
        lens=(r.get('lens') or '').lower()
        item={
            'component':r.get('component'), 'lens':r.get('lens'), 'question':r.get('question'),
            'answer':r.get('answer'), 'score':fnum(r.get('score')), 'risk':r.get('risk'),
            'next_lens':r.get('next_lens')
        }
        if 'physical feature' in lens: buckets['physical_feature_projection'].append(item)
        elif 'block interaction' in lens: buckets['block_interaction'].append(item)
        elif 'class contrast' in lens: buckets['class_contrast'].append(item)
        elif 'output pseudo-head' in lens: buckets['output_pseudo_head'].append(item)
        elif 'weight-energy' in lens or 'weight energy' in lens: buckets['weight_energy'].append(item)
    for k in buckets:
        buckets[k]=sorted(buckets[k],key=lambda x:x['score'],reverse=True)[:8]
    return buckets

def route_particle_summary(route_rows, particle_rows):
    # Route width summary by layer: min/max mean neighbor DR.
    layers={}
    for r in route_rows:
        layers.setdefault(str(r.get('layer')),[]).append(r)
    route=[]
    for layer,rs in sorted(layers.items()):
        vals=[r for r in rs if r.get('neighbor_dr_mean') not in (None,'')]
        if not vals: continue
        lo=min(vals,key=lambda x:fnum(x.get('neighbor_dr_mean')))
        hi=max(vals,key=lambda x:fnum(x.get('neighbor_dr_mean')))
        route.append({
            'layer':layer,
            'compact_class':lo.get('class_label'), 'compact_dr_mean':fnum(lo.get('neighbor_dr_mean')),
            'wide_class':hi.get('class_label'), 'wide_dr_mean':fnum(hi.get('neighbor_dr_mean')),
            'gap':fnum(hi.get('neighbor_dr_mean'))-fnum(lo.get('neighbor_dr_mean'))
        })
    particle=[]
    for r in sorted(particle_rows,key=lambda x:fnum(x.get('delta_pred_logit')),reverse=True):
        particle.append({
            'group':r.get('group'), 'patch_acc':fnum(r.get('patch_acc')),
            'base_acc':fnum(r.get('base_acc')), 'delta_pred_logit':fnum(r.get('delta_pred_logit')),
            'top1_match':fnum(r.get('top1_match')), 'jaccard_with_top_pt':fnum(r.get('mean_jaccard_with_top_pt')),
        })
    return {'route_width_by_layer':route, 'particle_controls':particle[:8]}

def class_feature_map(rows):
    by={}
    for r in rows:
        cls=r.get('class_label')
        if not cls: continue
        cur=by.get(cls)
        if cur is None or abs(fnum(r.get('pred_logit_drop')))>abs(fnum(cur.get('pred_logit_drop'))):
            by[cls]=r
    return [{
        'class_label':cls,
        'feature':r.get('group'),
        'pred_logit_drop':fnum(r.get('pred_logit_drop')),
        'acc_drop':fnum(r.get('acc_drop')),
        'patch_acc':fnum(r.get('patch_acc')),
    } for cls,r in sorted(by.items())]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-dir',default='runs/research_dashboard_latest')
    args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    baseline,baseline_src=pick_baseline()
    board=readcsv('reports/latest/tables/research_hypothesis_board.csv')
    heads=readcsv('reports/latest/tables/head_projection_question_map.csv')
    wq=readcsv('reports/latest/tables/weight_projection_questions.csv')
    route=readcsv('reports/latest/tables/discovery_route_knn_stats.csv')
    particles=readcsv('reports/latest/tables/discovery_particle_controls.csv')
    features=readcsv('reports/latest/tables/research_feature_channels_per_class.csv')
    question_map=readcsv('reports/latest/tables/network_question_map.csv')

    acc=fnum(baseline.get('acc'))
    top_h=top_heads(heads,12)
    top_hyps=top_hypotheses(board,10)
    w_buckets=weight_question_buckets(wq)
    rp=route_particle_summary(route,particles)
    cf=class_feature_map(features)

    dashboard={
        'schema':'research_dashboard_latest.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'metadata':{
            'repo':'maxwelhelp/matrix_unified_system_particals',
            'model':'ParticleNet_kinpid.pt',
            'mode':'kinpid',
            'baseline':baseline,
            'baseline_source':baseline_src,
            'valid_model':acc>0.6,
        },
        'executive_summary':[
            f'Validated ParticleNet baseline acc={fmt(acc)} on current balanced subset.' if acc else 'Baseline not found.',
            f'Strongest current pseudo-head: {top_h[0]["head_id"]} acc_drop={fmt(top_h[0]["acc_drop"])}; role={top_h[0]["role"]}.' if top_h else 'Head projection map not found.',
            'Weight-projection scan found physical-feature, block-interaction, and class-contrast questions.' if wq else 'Weight projection questions not found.',
            'Current strongest research direction: triangulate weight projection + route/activation + causal patch for EdgeConv pseudo-heads.',
        ],
        'top_hypotheses':top_hyps,
        'top_heads':top_h,
        'weight_projection_questions':w_buckets,
        'route_and_particle_findings':rp,
        'class_feature_map':cf,
        'question_map_sample':question_map[:20],
        'risks':[
            'EdgeConv pseudo-heads are equal channel slices, not learned activation clusters yet.',
            'Weight projections are not causal by themselves.',
            'Route-width results are descriptive until route-group causal patch is implemented.',
            'Need heldout stability across more ROOT files.',
            'ParT attention claims are paused until a valid ParT checkpoint/invocation is found.',
        ],
        'next_actions_ranked':[
            'Run activation-cluster pseudo-head lens and compare against random channel groups.',
            'Run route-group causal patch: compact/wide/top-pT/random neighbor routes.',
            'Run top-k particle sweep k=1,2,4,8,16 with per-class effects.',
            'Project pseudo-head activations into class contrast directions Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc/Hgg.',
            'Build error-route atlas for wrong predictions true->pred.',
            'Find/train valid ParT checkpoint before attention-head claims.',
        ],
        'source_files':{
            'main_md':'reports/latest/RESEARCH_DASHBOARD_LATEST.md',
            'head_projection':'reports/latest/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md',
            'weight_projection':'reports/latest/PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md',
            'synthesis':'reports/latest/PARTICLENET_RESEARCH_SYNTHESIS_V6.md',
            'question_atlas':'reports/latest/PARTICLENET_QUESTION_ATLAS_V1.md',
            'tables':[
                'reports/latest/tables/head_projection_question_map.csv',
                'reports/latest/tables/weight_projection_questions.csv',
                'reports/latest/tables/research_hypothesis_board.csv',
                'reports/latest/tables/research_feature_channels_per_class.csv',
                'reports/latest/tables/discovery_route_knn_stats.csv',
                'reports/latest/tables/discovery_particle_controls.csv',
            ]
        }
    }
    wjson(out/'research_dashboard_latest.json',dashboard)
    # Markdown compact summary.
    md=['# Research Dashboard Latest\n\n',
        'This is the compact dashboard for quick analysis before opening full logs.\n\n',
        '## Executive summary\n']
    for b in dashboard['executive_summary']:
        md.append(f'- {b}\n')
    md += ['\n## Top hypotheses\n',
           md_table(['id','priority','status','score','title','next test'],[[h['id'],h['priority'],h['status'],fmt(h['score']),h['title'],h['next_test']] for h in top_hyps]),
           '\n## Top heads / pseudo-head questions\n',
           md_table(['head','acc_drop','role','question','semantic_hint','next'],[[h['head_id'],fmt(h['acc_drop']),h['role'],h['question'],h['semantic_hint'],h['next_test']] for h in top_h[:12]]),
           '\n## Top weight projection buckets\n']
    for k,items in w_buckets.items():
        md.append(f'\n### {k}\n')
        md.append(md_table(['component','score','question','answer'],[[i['component'],fmt(i['score']),i['question'],i['answer']] for i in items[:6]]))
    md += ['\n## Route / particle findings\n',
           md_table(['layer','compact','wide','gap'],[[r['layer'],f"{r['compact_class']} {fmt(r['compact_dr_mean'])}",f"{r['wide_class']} {fmt(r['wide_dr_mean'])}",fmt(r['gap'])] for r in rp['route_width_by_layer']]),
           '\n## Next actions\n']
    for a in dashboard['next_actions_ranked']:
        md.append(f'- {a}\n')
    md += ['\n## JSON\n\nMain machine-readable file: `manifests/latest/research_dashboard_latest.json`.\n']
    (out/'RESEARCH_DASHBOARD_LATEST.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'dashboard':'research_dashboard_latest.json','top_heads':len(top_h),'top_hypotheses':len(top_hyps)},indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
