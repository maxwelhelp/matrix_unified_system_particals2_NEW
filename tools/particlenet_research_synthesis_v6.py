#!/usr/bin/env python3
import csv, json, argparse
from pathlib import Path

LABELS=['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']

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

def writecsv(path, rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def load_json(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def top(rows, key, n=5, reverse=True):
    return sorted(rows,key=lambda r:fnum(r.get(key)),reverse=reverse)[:n]

def score_hypothesis(evidence, controls=0, stability=0, risk_penalty=0):
    # 0..100 heuristic: evidence strongest, then controls/stability, minus risks.
    return max(0, min(100, int(55*evidence + 20*controls + 20*stability - 15*risk_penalty)))

def build_hypotheses(edge_heads, features_pc, route_rows, particle_rows, contrasts, obs_rows, baseline):
    hyps=[]
    acc=fnum(baseline.get('acc')) if baseline else 0.0
    valid=acc>0.6
    # H1 edgeconv global
    if edge_heads:
        best=edge_heads[0]
        patch_acc=fnum(best.get('patch_acc'))
        evidence=min(1.0, max(0.0, (acc-patch_acc)/max(1e-6,acc))) if valid else 0.0
        hyps.append({
            'id':'H1','title':'EdgeConv learned-neighborhood separator','status':'CAUSAL_PATCHED' if evidence>0.2 else 'OBSERVED','priority':'P0','score':score_hypothesis(evidence,controls=0.7,stability=0.2,risk_penalty=0.2),
            'core_evidence':f"Best EdgeConv pseudo-head {best.get('layer')}:{best.get('group')} drops acc {fmt(acc)}->{fmt(patch_acc)}; full EdgeConv layers also previously dropped accuracy near random.",
            'risk':'Channel-head groups are fixed slices, not learned clusters yet.',
            'next_test':'Cluster EdgeConv activations and patch learned clusters; run heldout stability.'
        })
    # H2 pseudo-head specialization
    strong_heads=[r for r in edge_heads if fnum(r.get('delta_pred_logit'))>2 or fnum(r.get('patch_acc'))<0.65]
    if strong_heads:
        names=', '.join([f"L{r.get('layer')}:{r.get('group')}" for r in strong_heads[:5]])
        hyps.append({'id':'H2','title':'EdgeConv pseudo-head specialization','status':'CAUSAL_PATCHED','priority':'P0','score':78,'core_evidence':f'Strong internal pseudo-head groups: {names}.','risk':'Equal channel slicing may hide or split real functional groups.','next_test':'Add activation-cluster pseudo-heads and random channel-group controls.'})
    # H3 route width
    w=[]; t=[]
    for r in route_rows:
        if r.get('class_label')=='label_Wqq': w.append(fnum(r.get('neighbor_dr_mean')))
        if r.get('class_label')=='label_Tbqq': t.append(fnum(r.get('neighbor_dr_mean')))
    if w and t:
        gap=sum(t)/len(t)-sum(w)/len(w)
        hyps.append({'id':'H3','title':'Wqq compact route vs Tbqq wide route','status':'OBSERVED','priority':'P1','score':score_hypothesis(min(1,gap/0.1),controls=0.3,stability=0.4,risk_penalty=0.35),'core_evidence':f'Mean neighbor ΔR gap Tbqq-Wqq ≈ {gap:.4f} across route layers.','risk':'Route stats are descriptive; may be explained by mass/multiplicity.','next_test':'Causal route-group patch: compact vs wide edges; regress against jet mass and nparticles.'})
    # H4 leading particle
    pr={r.get('group'):r for r in particle_rows}
    if 'top_pt' in pr and 'random_control' in pr:
        top_acc=fnum(pr['top_pt'].get('patch_acc')); rnd=fnum(pr['random_control'].get('patch_acc'))
        gap=rnd-top_acc
        hyps.append({'id':'H4','title':'Leading-particle core hypothesis','status':'CAUSAL_PATCHED','priority':'P0','score':score_hypothesis(min(1,gap/0.25),controls=0.8,stability=0.2,risk_penalty=0.15),'core_evidence':f'top_pt ablation acc={fmt(top_acc)} vs random={fmt(rnd)}; gap={fmt(gap)}.','risk':'top_pt and top_energy highly overlap; need top-k sweep.','next_test':'Run k sweep k=1,2,4,8,16 and per-class particle ablation.'})
    # H5 features per class
    strong_feat=[]
    for r in features_pc:
        if abs(fnum(r.get('pred_logit_drop')))>5 or fnum(r.get('acc_drop'))>0.4:
            strong_feat.append(r)
    if strong_feat:
        by_cls={}
        for r in strong_feat:
            cls=r.get('class_label')
            cur=by_cls.get(cls)
            if cur is None or abs(fnum(r.get('pred_logit_drop')))>abs(fnum(cur.get('pred_logit_drop'))): by_cls[cls]=r
        examples=', '.join([f"{c}->{r.get('group')}" for c,r in list(by_cls.items())[:8]])
        hyps.append({'id':'H5','title':'Explicit feature-channel class codes','status':'CAUSAL_PATCHED','priority':'P1','score':74,'core_evidence':examples,'risk':'Zeroing feature channels may be out-of-distribution.','next_test':'Permutation/noise controls and class contrast reports.'})
    # H6 known-observable alignment
    if contrasts:
        tb=[r for r in contrasts if r.get('contrast')=='label_Tbqq_vs_label_Tbl']
        if tb:
            r=tb[0]
            hyps.append({'id':'H6','title':'Known-observable alignment','status':'OBSERVED','priority':'P1','score':66,'core_evidence':f"Tbqq-vs-Tbl: route ΔR gap L1={fmt(r.get('layer1_neighbor_dr_mean_delta_A_minus_B'))}, sdmass gap={fmt(r.get('jet_sdmass_mean_delta_A_minus_B'))}, nparticles gap={fmt(r.get('jet_nparticles_mean_delta_A_minus_B'))}.",'risk':'May be explained by known mass/multiplicity only.','next_test':'Residual analysis after controlling for sdmass/nparticles/tau variables.'})
    # H7 error atlas todo
    hyps.append({'id':'H7','title':'Error-route hypothesis','status':'TODO','priority':'P2','score':35,'core_evidence':'Not tested yet: wrong predictions may share route/feature pattern with predicted class.','risk':'Needs confusion-pair analysis.','next_test':'Build error atlas true->pred pairs with route stats and signed competing logits.'})
    # H8 attention model todo
    hyps.append({'id':'H8','title':'Transformer attention route hypothesis','status':'PAUSED','priority':'P2','score':20,'core_evidence':'ParT attention cannot be claimed until ParT accuracy is fixed.','risk':'Current ParT checkpoint invocation is invalid for claims.','next_test':'Find/train valid ParT checkpoint, then extract attention heads / pair bias.'})
    return sorted(hyps,key=lambda r:(r['priority'], -int(r['score'])))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-dir',default='runs/particlenet_research_synthesis_v6')
    args=ap.parse_args()
    out=Path(args.out_dir); (out/'tables').mkdir(parents=True,exist_ok=True)
    v5=load_json('manifests/latest/particlenet_research_compass_v5_summary.json')
    v4=load_json('manifests/latest/particlenet_discovery_atlas_v4_summary.json')
    baseline=(v5.get('baseline') or v4.get('baseline') or {})
    edge_heads=readcsv('reports/latest/tables/research_edge_channel_heads.csv')
    features_pc=readcsv('reports/latest/tables/research_feature_channels_per_class.csv')
    route_rows=readcsv('reports/latest/tables/discovery_route_knn_stats.csv')
    particle_rows=readcsv('reports/latest/tables/discovery_particle_controls.csv')
    contrasts=readcsv('reports/latest/tables/research_class_contrasts.csv')
    obs=readcsv('reports/latest/tables/research_known_observables_by_class.csv')
    hyps=build_hypotheses(edge_heads,features_pc,route_rows,particle_rows,contrasts,obs,baseline)
    writecsv(out/'tables/research_hypothesis_board.csv',hyps)
    summary={'ok':True,'baseline':baseline,'n_edge_heads':len(edge_heads),'n_feature_class_rows':len(features_pc),'n_route_rows':len(route_rows),'n_particle_rows':len(particle_rows),'n_contrasts':len(contrasts),'hypotheses':hyps}
    wjson(out/'particlenet_research_synthesis_v6_summary.json',summary)
    p0=[h for h in hyps if h['priority']=='P0']; p1=[h for h in hyps if h['priority']=='P1']; p2=[h for h in hyps if h['priority']=='P2']
    md=['# ParticleNet Research Synthesis v6\n\n',
        'This report consolidates v3/v4/v5 outputs into a research board. It does not run the model; it reads latest CSV/JSON outputs and turns them into prioritized hypotheses.\n\n',
        '## Baseline / validity\n\n```json\n',json.dumps(baseline,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Hypothesis board\n',
        md_table(['id','priority','status','score','title','core evidence','risk','next test'],[[h['id'],h['priority'],h['status'],h['score'],h['title'],h['core_evidence'],h['risk'],h['next_test']] for h in hyps]),
        '\n## P0 immediate tests\n']
    for h in p0:
        md.append(f"- **{h['id']} {h['title']}**: {h['next_test']}\n")
    md += ['\n## P1 research tests\n']
    for h in p1:
        md.append(f"- **{h['id']} {h['title']}**: {h['next_test']}\n")
    md += ['\n## P2 backlog\n']
    for h in p2:
        md.append(f"- **{h['id']} {h['title']}**: {h['next_test']}\n")
    # compact facts
    md += ['\n## Current strongest facts\n']
    if edge_heads:
        md.append(f"- Strongest EdgeConv pseudo-head: L{edge_heads[0].get('layer')} {edge_heads[0].get('group')} drops acc to {fmt(edge_heads[0].get('patch_acc'))}.\n")
    pr={r.get('group'):r for r in particle_rows}
    if 'top_pt' in pr and 'random_control' in pr:
        md.append(f"- Top-pT particle ablation acc={fmt(pr['top_pt'].get('patch_acc'))}; random control acc={fmt(pr['random_control'].get('patch_acc'))}.\n")
    # known issue notes
    md += ['\n## Known weaknesses to fix\n',
           '- Edge pseudo-heads are currently equal channel slices; replace with activation clusters.\n',
           '- Route stats are descriptive; add route-group causal patch.\n',
           '- Need heldout stability across more ROOT files.\n',
           '- Need error atlas for wrong predictions and competing logits.\n',
           '- ParT attention is paused until valid accuracy is recovered.\n',
           '\n## Output files\n\n- `reports/latest/tables/research_hypothesis_board.csv`\n- `manifests/latest/particlenet_research_synthesis_v6_summary.json`\n']
    (out/'PARTICLENET_RESEARCH_SYNTHESIS_V6.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
