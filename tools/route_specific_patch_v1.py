#!/usr/bin/env python3
import argparse,csv,json,re,sys,random
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
def clone_batch(b): return {k:(v.clone() if torch.is_tensor(v) else v) for k,v in b.items()}
def patch_indices(batch, ei, inds):
    b=clone_batch(batch)
    inds=sorted(set(int(i) for i in inds if int(i)>=0 and int(i)<b['mask'].shape[-1]))
    if not inds: return b,[]
    idx=torch.tensor(inds,device=b['mask'].device,dtype=torch.long)
    b['mask'][ei:ei+1,:,idx]=0
    for k in ['features','points','vectors']:
        if k in b and torch.is_tensor(b[k]) and b[k].dim()==3:
            b[k][ei:ei+1,:,idx]=0
    return b,inds
def select_events(path,B,limit,manual):
    out=[]
    for t in str(manual).split(','):
        t=t.strip()
        if t.isdigit() and int(t)<B: out.append(int(t))
    for r in readcsv(path):
        ei=int(fnum(r.get('event_index'),-1))
        if 0<=ei<B and ei not in out: out.append(ei)
        if len(out)>=limit: break
    return out[:limit]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--events-csv',default='reports/latest/tables/event_forecast_explanations.csv')
    ap.add_argument('--event-indices',default='')
    ap.add_argument('--max-events',type=int,default=12)
    ap.add_argument('--heads',default='L2_ch224:256,L2_ch128:160,L2_ch32:64,L2_ch0:32')
    ap.add_argument('--random-seed',type=int,default=123)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-csv',default='reports/latest/tables/route_specific_patch_results.csv')
    ap.add_argument('--out-json',default='manifests/latest/route_specific_patch_v1.json')
    ap.add_argument('--out-md',default='reports/latest/ROUTE_SPECIFIC_PATCH_V1.md')
    a=ap.parse_args(); rng=random.Random(a.random_seed)
    model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    B=int(batch['y'].shape[0]); events=select_events(a.events_csv,B,a.max_events,a.event_indices); heads=[h.strip() for h in a.heads.split(',') if h.strip()]
    layers=sorted(set(parse_head(h)[0] for h in heads if parse_head(h))); caps={}; hooks=[]
    for li in layers:
        def hk(mod,inp,out,li=li): caps[li]=out.detach().cpu()
        hooks.append(model.edge_convs[li].register_forward_hook(hk))
    with torch.no_grad(): base=model(batch['points'],batch['features'],batch['mask']).detach().cpu()
    [h.remove() for h in hooks]
    prob=torch.softmax(base.float(),1); pred=base.argmax(1); y=batch['y'].detach().cpu(); mask=real_mask(batch).detach().cpu(); pt=pt_values(batch).detach().cpu(); lead=pt.masked_fill(~mask,-1e30).argmax(1)
    from weaver.nn.model.ParticleNet import knn
    k=int(getattr(model.edge_convs[0],'k',16)); knn_idx=knn(batch['points'],k).detach().cpu()
    rows=[]
    for ei in events:
        valid=[int(i) for i in torch.where(mask[ei])[0].tolist()]
        for h in heads:
            p=parse_head(h)
            if not p or p[0] not in caps: continue
            li,c0,c1=p; z=caps[li][ei,c0:c1,:].abs().mean(0).masked_fill(~mask[ei],0); top=int(z.argmax()); nb=[int(x) for x in knn_idx[ei,top].tolist()]
            patches={'remove_top_particle':[top],'remove_knn_neighbors':nb,'remove_top_plus_knn':[top]+nb}
            same_count=len(set([top]+nb)); pool=[x for x in valid if x not in set([top]+nb)] or valid; patches['random_same_count']=rng.sample(pool,min(same_count,len(pool)))
            for mode,inds in patches.items():
                pb,used=patch_indices(batch,ei,inds)
                with torch.no_grad(): out=model(pb['points'],pb['features'],pb['mask']).detach().cpu()
                bpred=int(pred[ei]); ppred=int(out[ei].argmax()); true=int(y[ei])
                rows.append({'event_index':ei,'true_label':LABELS[true],'baseline_pred':LABELS[bpred],'patched_pred':LABELS[ppred],'head_id':h,'patch_mode':mode,'patched_indices':json.dumps(used),'route_top_particle':top,'route_top_is_particle0':int(top==0),'route_top_is_leading':int(top==int(lead[ei])),'route_knn_contains_particle0':int(0 in nb),'route_knn_contains_leading':int(int(lead[ei]) in nb),'baseline_conf':float(prob[ei,bpred]),'patched_conf_for_baseline_pred':float(torch.softmax(out[ei].float(),0)[bpred]),'delta_baseline_pred_logit':float(out[ei,bpred]-base[ei,bpred]),'delta_true_logit':float(out[ei,true]-base[ei,true]),'flipped':int(ppred!=bpred)})
    wcsv(a.out_csv,rows); wjson(a.out_json,{'ok':True,'events':len(events),'rows':len(rows),'heads':heads,'patch_modes':['remove_top_particle','remove_knn_neighbors','remove_top_plus_knn','random_same_count'],'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    # compact summary
    by={}
    for r in rows:
        key=(r['head_id'],r['patch_mode']); by.setdefault(key,[]).append(r)
    summ=[]
    for (h,m),xs in by.items():
        summ.append([h,m,len(xs),fmt(sum(fnum(x['flipped']) for x in xs)/len(xs)),fmt(sum(fnum(x['delta_baseline_pred_logit']) for x in xs)/len(xs)),fmt(sum(fnum(x['patched_conf_for_baseline_pred']) for x in xs)/len(xs))])
    md=['# Route Specific Patch v1\n\nCausal patch test for event-level active L2/core routes.\n\n','## Summary by head/mode\n',mdtab(['head','mode','n','flip_rate','mean_delta_base_logit','mean_patched_conf'],summ),'\n## Rows\n',mdtab(['event','true','base','patched','head','mode','flip','d_base_logit','indices'],[[r['event_index'],r['true_label'],r['baseline_pred'],r['patched_pred'],r['head_id'],r['patch_mode'],r['flipped'],fmt(r['delta_baseline_pred_logit']),r['patched_indices']] for r in rows[:160]]),'\n## Interpretation\n\nCompare targeted remove_top/knn/top_plus_knn against random_same_count. Strong support means targeted route patch flips or reduces baseline logit more than random.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(events),'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
