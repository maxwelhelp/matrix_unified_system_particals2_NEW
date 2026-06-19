#!/usr/bin/env python3
import argparse, csv, json, math, sys
from pathlib import Path
from collections import defaultdict
import torch
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import pt_values, real_mask

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def wjson(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fnum(x,d=0.0):
    try:
        v=float(x); return v if math.isfinite(v) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']
    out += ['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rows]
    return '\n'.join(out)+'\n'
def dist(a,b): return float(torch.sqrt(((a-b)**2).sum()+1e-9))
def is_had_role(role):
    return role in {'hard_hadron','hardest_hadron','nearest_hadron_to_best_lepton','hadron_neighbor'}
def summarize(rows):
    by=defaultdict(list)
    for r in rows: by[(r['group'],r['particle_role'])].append(r)
    out=[]
    for (g,role),xs in sorted(by.items()):
        n=len(xs)
        out.append({'group':g,'particle_role':role,'n':n,
            'mean_deltaR_to_best_lepton':sum(fnum(x['deltaR_to_best_lepton']) for x in xs)/max(1,n),
            'in_best_lepton_knn_rate':sum(int(x['is_in_best_lepton_knn']) for x in xs)/max(1,n),
            'mean_best_lepton_knn_rank':sum(fnum(x['best_lepton_knn_rank'],99) for x in xs)/max(1,n),
            'mean_particle_pt':sum(fnum(x['particle_pt']) for x in xs)/max(1,n),
            'l2_same_particle_top3_rate':sum(int(x['same_particle_in_L2_ch128_top3']) for x in xs)/max(1,n),
            'mean_l1_activation_norm':sum(fnum(x['l1_activation_norm']) for x in xs)/max(1,n),
            'mean_l2_activation_norm_if_top3':sum(fnum(x['l2_activation_norm_if_top3']) for x in xs)/max(1,n)})
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--annotated-top-particles',default='reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=4096)
    ap.add_argument('--max-files',type=int,default=1000)
    ap.add_argument('--focus-head',default='L1_ch80:96')
    ap.add_argument('--l2-head',default='L2_ch128:160')
    ap.add_argument('--knn-k',type=int,default=16)
    ap.add_argument('--device',default='cpu')
    ap.add_argument('--out-md',default='reports/latest/HARD_HADRON_GEOMETRY_PROBE_V1.md')
    ap.add_argument('--out-rows',default='reports/latest/tables/hard_hadron_geometry_probe_v1_rows.csv')
    ap.add_argument('--out-summary',default='reports/latest/tables/hard_hadron_geometry_probe_v1_summary.csv')
    ap.add_argument('--out-json',default='manifests/latest/hard_hadron_geometry_probe_v1.json')
    a=ap.parse_args()
    top=readcsv(a.annotated_top_particles)
    if not top: raise RuntimeError('Missing annotated top particles. Run INTERNAL_ACTIVATION_CONTRAST_V2_1 first.')
    batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    pts=batch['points'].detach().cpu(); pt=pt_values(batch).detach().cpu()
    from weaver.nn.model.ParticleNet import knn
    l2={(int(fnum(r.get('event_idx'),-1)),int(fnum(r.get('particle_idx'),-1))):r for r in top if r.get('head_id')==a.l2_head}
    rows=[]; cache={}
    for r in top:
        if r.get('head_id')!=a.focus_head or not is_had_role(r.get('particle_role','')): continue
        ei=int(fnum(r.get('event_idx'),-1)); pi=int(fnum(r.get('particle_idx'),-1)); best=int(fnum(r.get('best_lepton_idx'),-1))
        if ei<0 or pi<0 or best<0 or ei>=pts.shape[0]: continue
        if ei not in cache:
            with torch.no_grad(): cache[ei]=knn(pts[ei:ei+1],a.knn_k).detach().cpu()
        nb=[int(x) for x in cache[ei][0,best].tolist() if int(x)!=best]
        is_in=int(pi in nb); rank=(nb.index(pi)+1) if pi in nb else 99
        dr=dist(pts[ei,:,pi].float(),pts[ei,:,best].float())
        l2r=l2.get((ei,pi))
        rows.append({'event_idx':ei,'group':r.get('group'),'focus_head':a.focus_head,'particle_idx':pi,
            'particle_role':r.get('particle_role'),'pid':r.get('pid'),'particle_pt':r.get('pt'),
            'l1_rank':r.get('rank'),'l1_activation_norm':r.get('particle_activation_norm'),
            'best_lepton_idx':best,'deltaR_to_best_lepton':dr,'is_in_best_lepton_knn':is_in,
            'best_lepton_knn_rank':rank,'same_particle_in_L2_ch128_top3':int(l2r is not None),
            'l2_rank_if_top3':'' if l2r is None else l2r.get('rank',''),
            'l2_activation_norm_if_top3':0.0 if l2r is None else fnum(l2r.get('particle_activation_norm'))})
    summ=summarize(rows); wcsv(a.out_rows,rows); wcsv(a.out_summary,summ)
    wjson(a.out_json,{'ok':True,'rows':len(rows),'focus_head':a.focus_head,'l2_head':a.l2_head,'summary':summ})
    md=['# HARD_HADRON_GEOMETRY_PROBE_V1\n\n',
        'Checks whether hard-hadron top activators of L1_ch80:96 enter best-lepton KNN, how close they are to the lepton, and whether the same particles also reach L2_ch128:160 top3.\n\n',
        '## Summary\n',mdtab(['group','role','n','deltaR_lep','in_lep_KNN','knn_rank','pt','L2_same_top3','L1_act','L2_act_if_top3'],[[s['group'],s['particle_role'],s['n'],fmt(s['mean_deltaR_to_best_lepton']),fmt(s['in_best_lepton_knn_rate']),fmt(s['mean_best_lepton_knn_rank']),fmt(s['mean_particle_pt']),fmt(s['l2_same_particle_top3_rate']),fmt(s['mean_l1_activation_norm']),fmt(s['mean_l2_activation_norm_if_top3'])] for s in summ]),
        '\n## Interpretation\n\nIf B_confused hard hadrons have lower deltaR to best_lepton and higher in_lep_KNN rate than A, then L1_ch80:96 is driven by lepton-neighborhood hadronic contamination. If the same particles do not appear in L2_ch128:160 top activations, L2 does not recover Hqql evidence from that context.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
