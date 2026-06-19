#!/usr/bin/env python3
import argparse,csv,json,re,sys
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def loadjson(p):
    p=Path(p)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fnum(x,d=0.0):
    try: return float(x) if x not in ('',None) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def parse_head(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None
def select_events(args,B):
    out=[]
    if args.event_indices.strip():
        for t in args.event_indices.split(','):
            t=t.strip()
            if t.isdigit() and int(t)<B: out.append(int(t))
    for p in [args.inner_events,args.residual_events]:
        for r in readcsv(p):
            ei=int(fnum(r.get('event_index'),-1))
            if 0<=ei<B and ei not in out: out.append(ei)
            if len(out)>=args.top_events: return out
    return out[:args.top_events]
def select_heads(args):
    heads=[]
    for r in readcsv(args.rankings):
        h=r.get('head_id','')
        if h and h not in heads: heads.append(h)
        if len(heads)>=args.top_heads: break
    return heads
def explain_tag(pred,true,active):
    txt=json.dumps(active,ensure_ascii=False)
    if pred=='label_Tbl' and true=='label_Hqql': return 'Hqql activates Tbl-like core route'
    if pred=='label_Tbl': return 'Tbl-like core-neighborhood route'
    if pred=='label_QCD': return 'QCD/background attractor route'
    if 'L2_ch224:256' in txt or 'L2_ch128:160' in txt: return 'late L2 core-readout route'
    return 'mixed route explanation'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--top-events',type=int,default=20)
    ap.add_argument('--top-heads',type=int,default=10)
    ap.add_argument('--event-indices',default='')
    ap.add_argument('--rankings',default='reports/latest/tables/question_driven_head_rankings.csv')
    ap.add_argument('--pseudo-v3',default='reports/latest/tables/pseudocode_operation_database_v3.csv')
    ap.add_argument('--inner-events',default='reports/latest/tables/edgeconv_inner_trace_v2_events.csv')
    ap.add_argument('--residual-events',default='reports/latest/tables/known_observable_residual_top_events.csv')
    ap.add_argument('--residual-json',default='manifests/latest/known_observable_residual_v1.json')
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-events',default='reports/latest/tables/event_forecast_explanations.csv')
    ap.add_argument('--out-routes',default='reports/latest/tables/event_forecast_active_routes.csv')
    ap.add_argument('--out-json',default='manifests/latest/event_forecast_explainer_v1.json')
    ap.add_argument('--out-md',default='reports/latest/EVENT_FORECAST_EXPLAINER_V1.md')
    a=ap.parse_args(); pseudo={r.get('head_id'):r for r in readcsv(a.pseudo_v3)}; heads=select_heads(a)
    model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    B=int(batch['y'].shape[0]); events=select_events(a,B)
    layers=sorted(set(parse_head(h)[0] for h in heads if parse_head(h))); caps={}; hooks=[]
    for li in layers:
        def hk(mod,inp,out,li=li): caps[li]=out.detach().cpu()
        hooks.append(model.edge_convs[li].register_forward_hook(hk))
    with torch.no_grad(): logits=model(batch['points'],batch['features'],batch['mask']).detach().cpu()
    [h.remove() for h in hooks]
    prob=torch.softmax(logits.float(),dim=1); pred=logits.argmax(1); y=batch['y'].detach().cpu(); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); lead=pt.masked_fill(~mask,-1e30).argmax(1)
    from weaver.nn.model.ParticleNet import knn
    k=int(getattr(model.edge_convs[0],'k',16)); knn_idx=knn(batch['points'],k).detach().cpu()
    residual=loadjson(a.residual_json)
    erows=[]; rrows=[]
    for ei in events:
        active=[]
        for h in heads:
            p=parse_head(h)
            if not p: continue
            li,c0,c1=p
            if li not in caps: continue
            z=caps[li][ei,c0:c1,:].abs().mean(0).masked_fill(~mask[ei],0)
            top=int(z.argmax()); score=float(z.max()); nb=[int(x) for x in knn_idx[ei,top].tolist()]
            active.append({'head_id':h,'layer':li,'score':score,'top_particle':top,'top_is_particle0':int(top==0),'top_is_leading':int(top==int(lead[ei])),'knn_contains_particle0':int(0 in nb),'knn_contains_leading':int(int(lead[ei]) in nb),'route_role':pseudo.get(h,{}).get('route_role',''),'route_code':pseudo.get(h,{}).get('route_aware_pseudocode','')[:240]})
        active=sorted(active,key=lambda x:x['score'],reverse=True)[:a.top_heads]
        true_lbl=LABELS[int(y[ei])]; pred_lbl=LABELS[int(pred[ei])]
        tag=explain_tag(pred_lbl,true_lbl,active)
        top3=torch.topk(prob[ei],min(3,prob.shape[1]))
        erows.append({'event_index':ei,'true_label':true_lbl,'pred_label':pred_lbl,'confidence':float(prob[ei,int(pred[ei])]),'top3':json.dumps([(LABELS[int(i)],float(v)) for v,i in zip(top3.values,top3.indices)],ensure_ascii=False),'leading_pt_particle':int(lead[ei]),'leading_pt':float(pt[ei,int(lead[ei])]),'active_heads':', '.join(x['head_id'] for x in active[:5]),'hypothesis_tag':tag,'residual_status':residual.get('status',''),'forecast_explanation':f"Model predicts {pred_lbl} because active route heads {', '.join(x['head_id'] for x in active[:3])} write evidence through particles {[x['top_particle'] for x in active[:3]]}; tag={tag}."})
        for rank,x in enumerate(active,1):
            r=dict(x); r.update({'event_index':ei,'rank':rank,'true_label':true_lbl,'pred_label':pred_lbl}); rrows.append(r)
    wcsv(a.out_events,erows); wcsv(a.out_routes,rrows); wjson(a.out_json,{'ok':True,'events':len(erows),'routes':len(rrows),'heads':heads,'residual_status':residual.get('status'),'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# Event Forecast Explainer v1\n\nEvent-level mechanistic forecasts: prediction, active routes, particles, and route-aware pseudocode context.\n\n','## Forecasts\n',mdtab(['event','true','pred','conf','active_heads','tag','explanation'],[[r['event_index'],r['true_label'],r['pred_label'],fmt(r['confidence']),r['active_heads'],r['hypothesis_tag'],r['forecast_explanation']] for r in erows]),'\n## Active routes\n',mdtab(['event','rank','head','score','top_particle','p0','lead','knn_p0','knn_lead','role'],[[r['event_index'],r['rank'],r['head_id'],fmt(r['score']),r['top_particle'],r['top_is_particle0'],r['top_is_leading'],r['knn_contains_particle0'],r['knn_contains_leading'],r['route_role']] for r in rrows[:120]]),'\n## Next\n\nUse this report to choose events for route-specific patching and richer residual validation.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(erows),'routes':len(rrows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
