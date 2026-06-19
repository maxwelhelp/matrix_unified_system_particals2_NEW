#!/usr/bin/env python3
import argparse,csv,json,re,sys
from pathlib import Path
import numpy as np, torch
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
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def parse(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None
def corr(a,b):
    a=np.asarray(a); b=np.asarray(b)
    if a.std()<1e-9 or b.std()<1e-9: return 0.0
    return float(np.corrcoef(a,b)[0,1])
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pseudocode',default='reports/latest/tables/pseudocode_operation_database.csv')
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid'); ap.add_argument('--samples-per-file',type=int,default=128); ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-csv',default='reports/latest/tables/head_output_trace.csv'); ap.add_argument('--out-events',default='reports/latest/tables/head_output_top_events.csv'); ap.add_argument('--out-json',default='manifests/latest/head_output_trace_v1.json'); ap.add_argument('--out-md',default='reports/latest/HEAD_OUTPUT_TRACE_V1.md')
    a=ap.parse_args(); pseudo=readcsv(a.pseudocode); model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    outs={}; hooks=[]
    for li in [0,1,2]:
        def hk(mod,inp,out,li=li): outs[li]=out.detach().cpu()
        hooks.append(model.edge_convs[li].register_forward_hook(hk))
    with torch.no_grad(): logits=model(batch['points'],batch['features'],batch['mask']).detach().cpu()
    [h.remove() for h in hooks]
    y=batch['y'].detach().cpu().numpy(); pred=logits.argmax(1).numpy(); logn=logits.numpy(); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); lead_pt_idx=pt.masked_fill(~mask,-1e30).argmax(1).numpy()
    rows=[]; evrows=[]
    for r in pseudo:
        h=r.get('head_id',''); p=parse(h)
        if not p: continue
        li,c0,c1=p
        if li not in outs: continue
        z=outs[li][:,c0:c1,:].abs()   # [B,C,N]
        per_particle=z.mean(1)        # [B,N]
        per_particle=per_particle.masked_fill(~mask,0)
        event_score=per_particle.max(1).values.numpy()
        top_idx=per_particle.argmax(1).numpy()
        particle0_top=float((top_idx==0).mean())
        lead_match=float((top_idx==lead_pt_idx).mean())
        mean_abs=float(z.mean().item()); max_abs=float(z.max().item()); sparsity=float((z<1e-6).float().mean().item())
        class_means=[]
        for c,lbl in enumerate(LABELS):
            m=(y==c)
            if m.sum(): class_means.append((lbl,float(event_score[m].mean())))
        class_means=sorted(class_means,key=lambda x:x[1],reverse=True)
        top_class,top_class_score=class_means[0] if class_means else ('',0.0)
        base_score=np.mean([x[1] for x in class_means[1:]]) if len(class_means)>1 else 0.0
        contrast=top_class_score-base_score
        logit_corrs=[(LABELS[c],corr(event_score,logn[:,c])) for c in range(len(LABELS))]
        logit_corrs=sorted(logit_corrs,key=lambda x:abs(x[1]),reverse=True)
        interp=f"writes strongest output for {top_class}; top activation particle matches leading-pT {lead_match:.2f}, particle0 {particle0_top:.2f}"
        rows.append({'head_id':h,'layer':li,'channels':f'{c0}:{c1}','output_shape':list(outs[li].shape),'activation_mean_abs':mean_abs,'activation_max_abs':max_abs,'sparsity_like':sparsity,'particle0_top_rate':particle0_top,'top_activation_matches_leading_pt_rate':lead_match,'top_activation_class':top_class,'class_activation_contrast':contrast,'top_logit_corr_class':logit_corrs[0][0],'top_logit_corr':logit_corrs[0][1],'output_interpretation':interp,'semantic_axis':r.get('class_axis',''),'semantic_pseudocode':r.get('pseudocode','')})
        top_events=np.argsort(-event_score)[:5]
        for rank,ei in enumerate(top_events,1):
            evrows.append({'head_id':h,'rank':rank,'event_index':int(ei),'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'event_score':float(event_score[ei]),'top_particle_index':int(top_idx[ei]),'leading_pt_index':int(lead_pt_idx[ei]),'top_is_particle0':int(top_idx[ei]==0),'top_is_leading_pt':int(top_idx[ei]==lead_pt_idx[ei])})
    rows=sorted(rows,key=lambda r:(r['layer'],-r['activation_mean_abs']))
    wcsv(a.out_csv,rows); wcsv(a.out_events,evrows); wjson(a.out_json,{'ok':True,'rows':len(rows),'events':len(evrows),'n_events':len(y),'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# Head Output Trace v1\n\nActual pseudo-head output statistics from EdgeConvBlock outputs. This answers what each pseudo-head writes, not only what its gradient suggests.\n\n','## Summary\n',mdtab(['head','layer','mean_abs','top_class','contrast','particle0_top','lead_pt_match','logit_corr'],[[r['head_id'],r['layer'],fmt(r['activation_mean_abs']),r['top_activation_class'],fmt(r['class_activation_contrast']),fmt(r['particle0_top_rate']),fmt(r['top_activation_matches_leading_pt_rate']),r['top_logit_corr_class']+':'+fmt(r['top_logit_corr'])] for r in rows[:80]]),'\n## Interpretation\n\nIf `lead_pt_match` is high, this pseudo-head output is core/leading-particle aligned. If class contrast and logit correlation are high, it writes class-relevant evidence. Next: route-neighbor trace for exact neighbor sources.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
