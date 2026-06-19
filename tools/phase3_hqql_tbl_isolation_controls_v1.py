#!/usr/bin/env python3
import argparse,csv,json,sys,random,math
from pathlib import Path
from collections import defaultdict
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model, pt_values, real_mask
from data.jetclass_tiny_loader_v3_official import LABELS
HQQL=LABELS.index('label_Hqql'); TBL=LABELS.index('label_Tbl'); QCD=LABELS.index('label_QCD') if 'label_QCD' in LABELS else 0

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
def isolation_bins(events):
    bins=[(0.0,0.10),(0.10,0.15),(0.15,0.20),(0.20,0.30),(0.30,999.0)]
    rows=[]
    for lo,hi in bins:
        xs=[r for r in events if r.get('true_label')=='label_Hqql' and lo<=fnum(r.get('particle0_iso_pt_ratio'))<hi]
        conf=[r for r in xs if r.get('group')=='Hqql_to_Tbl']
        rows.append({'bin':f'{lo:.2f}-{hi:.2f}' if hi<999 else f'{lo:.2f}+','lo':lo,'hi':hi,'n_hqql':len(xs),'n_hqql_to_tbl':len(conf),'confusion_rate':len(conf)/len(xs) if xs else 0.0,'p0_lepton_rate':sum(fnum(r.get('particle0_is_lepton')) for r in xs)/len(xs) if xs else 0.0,'mean_missing_pt':sum(fnum(r.get('missing_pt_proxy')) for r in xs)/len(xs) if xs else 0.0})
    # simple monotonic score: count adjacent increases
    inc=sum(1 for a,b in zip(rows,rows[1:]) if fnum(b['confusion_rate'])>=fnum(a['confusion_rate']))
    return rows,inc

def slice_batch(batch,s,e): return {k:(v[s:e] if torch.is_tensor(v) and v.shape[0]>=e else v) for k,v in batch.items()}
def forward_micro(model,batch,mb,device):
    B=int(batch['y'].shape[0]); out=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e); out.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if str(device).startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(out,0)
def one(batch,ei): return {k:(v[ei:ei+1].clone() if torch.is_tensor(v) and v.shape[0]>ei else v) for k,v in batch.items()}
def copy_particle(dst,di,src,si):
    for k in ['points','features','vectors']:
        if k in dst and k in src and torch.is_tensor(dst[k]) and dst[k].dim()==3: dst[k][0,:,di]=src[k][0,:,si]
    if 'mask' in dst and torch.is_tensor(dst['mask']): dst['mask'][0,:,di]=1
def single(model,b):
    with torch.no_grad(): return model(b['points'],b['features'],b['mask']).detach().cpu()[0]
def is_had(feat,ei,idx): return feat.shape[1]>=8 and bool((feat[ei,6,idx]>0.5) or (feat[ei,7,idx]>0.5))
def pid(feat,ei,idx):
    if feat.shape[1]<11: return 'no_pid'
    vals={'charged_hadron':float(feat[ei,6,idx]),'neutral_hadron':float(feat[ei,7,idx]),'photon':float(feat[ei,8,idx]),'electron':float(feat[ei,9,idx]),'muon':float(feat[ei,10,idx])}
    return max(vals.items(),key=lambda kv:kv[1])[0]
def group(y,p):
    if int(y)==HQQL and int(p)==HQQL: return 'Hqql_correct'
    if int(y)==HQQL and int(p)==TBL: return 'Hqql_to_Tbl'
    if int(y)==QCD: return 'QCD'
    return ''
def match_event(cands,target_pt,pt):
    best=None; bd=1e30
    for ei in cands:
        d=abs(math.log((float(pt[ei,0])+1e-6)/(target_pt+1e-6)))
        if d<bd: best=ei; bd=d
    return best
def hadrons(feat,pt,ei):
    xs=[j for j in range(pt.shape[1]) if is_had(feat,ei,j)]
    return sorted(xs,key=lambda j:float(pt[ei,j]),reverse=True)
def loginfo(base,out):
    bpred=int(base.argmax()); ppred=int(out.argmax()); bm=float(base[HQQL]-base[TBL]); pm=float(out[HQQL]-out[TBL])
    return bpred,ppred,bm,pm,pm-bm

def run_patches(args):
    rng=random.Random(args.seed); model,res=make_model(args.checkpoint,args.mode,args.device); batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    logits=forward_micro(model,batch,max(1,args.micro_batch),args.device); pred=logits.argmax(1); y=batch['y'].detach().cpu(); pt=pt_values(batch).detach().cpu(); feat=batch['features'].detach().cpu(); mask=real_mask(batch).detach().cpu()
    from weaver.nn.model.ParticleNet import knn
    chunks=[]
    with torch.no_grad():
        for s in range(0,batch['points'].shape[0],max(1,args.knn_micro_batch)):
            e=min(batch['points'].shape[0],s+max(1,args.knn_micro_batch)); chunks.append(knn(batch['points'][s:e],int(getattr(model.edge_convs[0],'k',16))).detach().cpu())
    knn_idx=torch.cat(chunks,0)
    gs=defaultdict(list)
    for ei in range(len(y)):
        g=group(y[ei],pred[ei])
        if g: gs[g].append(ei)
    target=gs['Hqql_to_Tbl'][:args.max_targets]
    rows=[]; sweeps=[]
    for ei in target:
        base=logits[ei]; nb=[int(x) for x in knn_idx[ei,0].tolist() if int(x)!=0][:args.patch_k]
        donors={'3A_real_hqql_hadron':match_event(gs['Hqql_correct'],float(pt[ei,0]),pt),'3A_control_qcd_hadron':match_event(gs['QCD'],float(pt[ei,0]),pt)}
        for test,de in donors.items():
            if de is None: continue
            tb=one(batch,ei); db=one(batch,de); hs=hadrons(feat,pt,de)[:len(nb)]
            for di,si in zip(nb,hs): copy_particle(tb,di,db,si)
            out=single(model,tb); bpred,ppred,bm,pm,dm=loginfo(base,out)
            rows.append({'test':test,'event':ei,'donor':de,'n_patch':len(hs),'baseline_pred':LABELS[bpred],'patched_pred':LABELS[ppred],'success_to_Hqql':int(ppred==HQQL),'flip':int(ppred!=bpred),'delta_margin':dm,'target_p0_pid':pid(feat,ei,0),'donor_p0_pid':pid(feat,de,0)})
        # 3B sweep uses Hqql_correct donor
        de=donors['3A_real_hqql_hadron']
        if de is not None:
            hs=hadrons(feat,pt,de)[:len(nb)]
            for frac in [0.0,0.2,0.4,0.6,0.8,1.0]:
                tb=one(batch,ei); db=one(batch,de); n=int(round(frac*len(nb)))
                for di,si in zip(nb[:n],hs[:n]): copy_particle(tb,di,db,si)
                out=base if n==0 else single(model,tb); bpred,ppred,bm,pm,dm=loginfo(base,out)
                sweeps.append({'event':ei,'donor':de,'fraction':frac,'n_patch':n,'baseline_pred':LABELS[bpred],'patched_pred':LABELS[ppred],'success_to_Hqql':int(ppred==HQQL),'flip':int(ppred!=bpred),'delta_margin':dm,'target_p0_pid':pid(feat,ei,0),'donor_p0_pid':pid(feat,de,0)})
    return rows,sweeps,{'groups':{k:len(v) for k,v in gs.items()},'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)}
def summarize(rows,keys):
    by=defaultdict(list)
    for r in rows: by[tuple(r[k] for k in keys)].append(r)
    out=[]
    for key,xs in by.items():
        row={k:v for k,v in zip(keys,key)}; n=len(xs); row.update({'n':n,'success_to_Hqql_rate':sum(fnum(x['success_to_Hqql']) for x in xs)/n,'flip_rate':sum(fnum(x['flip']) for x in xs)/n,'mean_delta_margin':sum(fnum(x['delta_margin']) for x in xs)/n}); out.append(row)
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--phase1-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv'); ap.add_argument('--run-patches',action='store_true')
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt'); ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced')); ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=1024); ap.add_argument('--max-files',type=int,default=100); ap.add_argument('--micro-batch',type=int,default=64); ap.add_argument('--knn-micro-batch',type=int,default=128); ap.add_argument('--max-targets',type=int,default=100); ap.add_argument('--patch-k',type=int,default=8); ap.add_argument('--seed',type=int,default=123); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-bins',default='reports/latest/tables/phase3_hqql_tbl_isolation_bins.csv'); ap.add_argument('--out-controls',default='reports/latest/tables/phase3_hqql_tbl_matched_controls.csv'); ap.add_argument('--out-control-summary',default='reports/latest/tables/phase3_hqql_tbl_matched_controls_summary.csv'); ap.add_argument('--out-sweep',default='reports/latest/tables/phase3_hqql_tbl_sweep.csv'); ap.add_argument('--out-sweep-summary',default='reports/latest/tables/phase3_hqql_tbl_sweep_summary.csv'); ap.add_argument('--out-json',default='manifests/latest/phase3_hqql_tbl_isolation_controls_v1.json'); ap.add_argument('--out-md',default='reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md')
    a=ap.parse_args(); ev=readcsv(a.phase1_events); bins,inc=isolation_bins(ev); wcsv(a.out_bins,bins); controls=[]; sweeps=[]; extra={}
    if a.run_patches: controls,sweeps,extra=run_patches(a); wcsv(a.out_controls,controls); wcsv(a.out_control_summary,summarize(controls,['test'])); wcsv(a.out_sweep,sweeps); wcsv(a.out_sweep_summary,summarize(sweeps,['fraction']))
    wjson(a.out_json,{'ok':True,'phase1_events':len(ev),'isolation_bins':len(bins),'monotonic_adjacent_increases':inc,'patches_run':bool(a.run_patches),'control_rows':len(controls),'sweep_rows':len(sweeps),**extra})
    md=['# Phase 3 Hqql/Tbl Isolation Controls v1\n\n','## 3C Isolation bins\n',mdtab(['bin','n_hqql','n_hqql_to_tbl','confusion_rate','p0_lepton','missing_pt'],[[r['bin'],r['n_hqql'],r['n_hqql_to_tbl'],fmt(r['confusion_rate']),fmt(r['p0_lepton_rate']),fmt(r['mean_missing_pt'])] for r in bins])]
    if a.run_patches:
        cs=summarize(controls,['test']); ss=summarize(sweeps,['fraction'])
        md += ['\n## 3A matched controls\n',mdtab(['test','n','success','flip','delta_margin'],[[r['test'],r['n'],fmt(r['success_to_Hqql_rate']),fmt(r['flip_rate']),fmt(r['mean_delta_margin'])] for r in cs]),'\n## 3B hadron fraction sweep\n',mdtab(['fraction','n','success','flip','delta_margin'],[[r['fraction'],r['n'],fmt(r['success_to_Hqql_rate']),fmt(r['flip_rate']),fmt(r['mean_delta_margin'])] for r in ss])]
    md += ['\n## Interpretation\n\n3C is the cleanest observable test. If confusion_rate increases with isolation, isolation is a real physical discriminator. 3A checks whether Hqql-specific hadronic context beats QCD-matched hadrons. 3B checks whether the effect has a monotonic density curve.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'bins':len(bins),'patches_run':a.run_patches,'controls':len(controls),'sweeps':len(sweeps),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
