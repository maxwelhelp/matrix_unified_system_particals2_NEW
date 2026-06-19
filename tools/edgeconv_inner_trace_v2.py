#!/usr/bin/env python3
import argparse,csv,json,re,sys
from pathlib import Path
from collections import Counter
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def fnum(x,d=0.0):
    try: return float(x) if x not in ('',None) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def parse(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None
def pick_heads(rankings,questions,topn):
    qs=set(q.strip() for q in questions.split(',') if q.strip()); out=[]
    for r in rankings:
        if r.get('question_id') in qs and r.get('head_id') and r.get('head_id') not in out:
            out.append(r.get('head_id'))
            if len(out)>=topn: break
    return out
def pid_summary(features, idxs, ei):
    # features shape [B,C,N]. For kinpid: charge=5, PID flags 6..10 when available.
    C=features.shape[1]; out={}
    if C>5:
        charge=features[ei,5,idxs].float(); out['neighbor_charge_mean']=float(charge.mean()); out['neighbor_charge_abs_mean']=float(charge.abs().mean())
    names=['charged_hadron','neutral_hadron','photon','electron','muon']
    for j,nm in enumerate(names,6):
        if C>j: out['neighbor_pid_'+nm+'_frac']=float(features[ei,j,idxs].float().mean())
    return out
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rankings',default='reports/latest/tables/question_driven_head_rankings.csv')
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--questions',default='Q1_core_readout,Q3_residual_axis,Q4_trace_priority')
    ap.add_argument('--top-heads',type=int,default=10)
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--top-events-per-head',type=int,default=8)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-heads',default='reports/latest/tables/edgeconv_inner_trace_v2_heads.csv')
    ap.add_argument('--out-events',default='reports/latest/tables/edgeconv_inner_trace_v2_events.csv')
    ap.add_argument('--out-json',default='manifests/latest/edgeconv_inner_trace_v2.json')
    ap.add_argument('--out-md',default='reports/latest/EDGE_CONV_INNER_TRACE_V2.md')
    a=ap.parse_args(); rankings=readcsv(a.rankings); heads=pick_heads(rankings,a.questions,a.top_heads)
    model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    caps={}; hooks=[]; layers=sorted(set(parse(h)[0] for h in heads if parse(h)))
    for li in layers:
        def hk(mod,inp,out,li=li): caps[li]=out.detach().cpu()
        hooks.append(model.edge_convs[li].register_forward_hook(hk))
    with torch.no_grad(): logits=model(batch['points'],batch['features'],batch['mask']).detach().cpu()
    [h.remove() for h in hooks]
    y=batch['y'].detach().cpu(); pred=logits.argmax(1); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); features=batch['features'].detach().cpu(); points=batch['points'].detach().cpu()
    lead=pt.masked_fill(~mask,-1e30).argmax(1); pt_order=torch.argsort(pt.masked_fill(~mask,-1e30),dim=1,descending=True)
    rank_map=torch.empty_like(pt_order)
    for i in range(pt_order.shape[0]): rank_map[i,pt_order[i]]=torch.arange(pt_order.shape[1])
    from weaver.nn.model.ParticleNet import knn
    k=int(getattr(model.edge_convs[0],'k',16)); knn_idx=knn(batch['points'],k).detach().cpu()
    head_rows=[]; event_rows=[]
    for h in heads:
        p=parse(h)
        if not p: continue
        li,c0,c1=p; z=caps[li][:,c0:c1,:].abs(); per=z.mean(1).masked_fill(~mask,0); score=per.max(1).values; top=per.argmax(1)
        top_events=torch.argsort(score,descending=True)[:a.top_events_per_head]
        evs=[]
        for rank,ei in enumerate(top_events.tolist(),1):
            tp=int(top[ei]); nb=knn_idx[ei,tp].long(); nb_list=[int(x) for x in nb.tolist()]
            nb_pt=pt[ei,nb]; nb_rank=rank_map[ei,nb].float(); topk4=float((nb_rank<4).float().mean()); topk16=float((nb_rank<16).float().mean())
            deta=points[ei,0,nb]-points[ei,0,tp]; dphi=points[ei,1,nb]-points[ei,1,tp]; dr=torch.sqrt(deta*deta+dphi*dphi+1e-9)
            row={'head_id':h,'rank':rank,'event_index':int(ei),'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'top_particle':tp,'leading_pt_particle':int(lead[ei]),'top_is_particle0':int(tp==0),'top_is_leading_pt':int(tp==int(lead[ei])),'event_score':float(score[ei]),'top_particle_pt':float(pt[ei,tp]),'leading_pt':float(pt[ei,int(lead[ei])]),'knn_neighbors':json.dumps(nb_list),'knn_contains_particle0':int(0 in nb_list),'knn_contains_leading':int(int(lead[ei]) in nb_list),'neighbor_pt_mean':float(nb_pt.mean()),'neighbor_pt_max':float(nb_pt.max()),'neighbor_pt_rank_mean':float(nb_rank.mean()),'neighbor_top4_frac':topk4,'neighbor_top16_frac':topk16,'neighbor_deltaR_mean':float(dr.mean()),'neighbor_deltaR_max':float(dr.max())}
            row.update(pid_summary(features,nb,ei)); event_rows.append(row); evs.append(row)
        n=max(1,len(evs)); head_rows.append({'head_id':h,'layer':li,'channels':f'{c0}:{c1}','events':len(evs),'particle0_top_event_rate':sum(r['top_is_particle0'] for r in evs)/n,'leading_top_event_rate':sum(r['top_is_leading_pt'] for r in evs)/n,'knn_contains_particle0_rate':sum(r['knn_contains_particle0'] for r in evs)/n,'knn_contains_leading_rate':sum(r['knn_contains_leading'] for r in evs)/n,'neighbor_top4_frac_mean':sum(r['neighbor_top4_frac'] for r in evs)/n,'neighbor_top16_frac_mean':sum(r['neighbor_top16_frac'] for r in evs)/n,'neighbor_deltaR_mean':sum(r['neighbor_deltaR_mean'] for r in evs)/n,'route_pattern':('core particle + core-neighborhood route' if sum(r['top_is_particle0'] for r in evs)/n>0.6 else 'context/non-core route')})
    wcsv(a.out_heads,head_rows); wcsv(a.out_events,event_rows); wjson(a.out_json,{'ok':True,'heads':heads,'head_rows':len(head_rows),'event_rows':len(event_rows),'k':k,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# EdgeConv Inner Trace v2\n\nRicher KNN/neighbor route trace for question-ranked pseudo-heads.\n\n','## Head route summary\n',mdtab(['head','route','p0_top','lead_top','knn_p0','knn_lead','top4_nb','dR'],[[r['head_id'],r['route_pattern'],fmt(r['particle0_top_event_rate']),fmt(r['leading_top_event_rate']),fmt(r['knn_contains_particle0_rate']),fmt(r['knn_contains_leading_rate']),fmt(r['neighbor_top4_frac_mean']),fmt(r['neighbor_deltaR_mean'])] for r in head_rows]),'\n## Event route examples\n',mdtab(['head','rank','event','true','pred','top','lead','score','knn_p0','knn_lead','nb_top4','nb_dR'],[[r['head_id'],r['rank'],r['event_index'],r['true_label'],r['pred_label'],r['top_particle'],r['leading_pt_particle'],fmt(r['event_score']),r['knn_contains_particle0'],r['knn_contains_leading'],fmt(r['neighbor_top4_frac']),fmt(r['neighbor_deltaR_mean'])] for r in event_rows[:120]]),'\n## Interpretation\n\nUse `route_pattern` and neighbor statistics to refine pseudocode v3/v4. Core L2 readouts should have high top particle0/leading rates; context builders may have lower top particle0 but can still include core in KNN route.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'heads':len(head_rows),'events':len(event_rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
