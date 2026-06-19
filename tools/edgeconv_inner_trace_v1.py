#!/usr/bin/env python3
import argparse,csv,json,re,sys,inspect
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
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def fnum(x,d=0.0):
    try: return float(x) if x not in ('',None) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def parse_head(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None
def shape(x):
    if torch.is_tensor(x): return list(x.shape)
    if isinstance(x,(list,tuple)): return [shape(y) for y in x]
    return str(type(x).__name__)
def pick_heads(rankings, questions, topn):
    qs=set(q.strip() for q in questions.split(',') if q.strip())
    out=[]
    for r in rankings:
        if r.get('question_id') in qs and r.get('head_id') and r.get('head_id') not in out:
            out.append(r.get('head_id'))
            if len(out)>=topn: break
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
    ap.add_argument('--top-events-per-head',type=int,default=5)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-heads',default='reports/latest/tables/edgeconv_inner_trace_heads.csv')
    ap.add_argument('--out-events',default='reports/latest/tables/edgeconv_inner_trace_events.csv')
    ap.add_argument('--out-json',default='manifests/latest/edgeconv_inner_trace_v1.json')
    ap.add_argument('--out-md',default='reports/latest/EDGE_CONV_INNER_TRACE_V1.md')
    a=ap.parse_args(); rankings=readcsv(a.rankings); heads=pick_heads(rankings,a.questions,a.top_heads)
    model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device)
    caps={}; hooks=[]
    layers=sorted(set(parse_head(h)[0] for h in heads if parse_head(h)))
    for li in layers:
        block=model.edge_convs[li]
        def hblock(mod,inp,out,li=li): caps[f'L{li}.block_out']={'tensor':out.detach().cpu(),'input_shape':shape(inp),'output_shape':shape(out)}
        hooks.append(block.register_forward_hook(hblock))
        if hasattr(block,'convs'):
            for ci,cm in enumerate(block.convs):
                def hc(mod,inp,out,li=li,ci=ci): caps[f'L{li}.convs.{ci}']={'tensor':out.detach().cpu(),'input_shape':shape(inp),'output_shape':shape(out),'module_type':type(mod).__name__}
                hooks.append(cm.register_forward_hook(hc))
    with torch.no_grad(): logits=model(batch['points'],batch['features'],batch['mask']).detach().cpu()
    [h.remove() for h in hooks]
    y=batch['y'].detach().cpu(); pred=logits.argmax(1); pt=pt_values(batch).detach().cpu(); mask=real_mask(batch).detach().cpu(); lead=pt.masked_fill(~mask,-1e30).argmax(1)
    knn_idx=None
    try:
        from weaver.nn.model.ParticleNet import knn
        k=int(getattr(model.edge_convs[0],'k',16)); knn_idx=knn(batch['points'],k).detach().cpu()
    except Exception:
        knn_idx=None
    head_rows=[]; event_rows=[]
    for h in heads:
        p=parse_head(h)
        if not p: continue
        li,c0,c1=p; bt=caps.get(f'L{li}.block_out',{}).get('tensor')
        if bt is None: continue
        z=bt[:,c0:c1,:].abs(); per=z.mean(1).masked_fill(~mask,0); evscore=per.max(1).values; topp=per.argmax(1)
        part0=float((topp==0).float().mean()); leadm=float((topp==lead).float().mean())
        top_ev=torch.argsort(evscore,descending=True)[:a.top_events_per_head]
        conv_shapes='; '.join([f'{k}:{v.get("output_shape")}' for k,v in caps.items() if k.startswith(f'L{li}.convs.')])
        head_rows.append({'head_id':h,'layer':li,'channels':f'{c0}:{c1}','block_output_shape':json.dumps(caps.get(f'L{li}.block_out',{}).get('output_shape')), 'inner_conv_shapes':conv_shapes,'activation_mean_abs':float(z.mean()),'activation_max_abs':float(z.max()),'particle0_top_rate':part0,'leading_pt_match_rate':leadm,'trace_interpretation':('core-neighborhood readout' if li==2 and leadm>0.4 else 'context/feature builder or relay')})
        for rank,ei in enumerate(top_ev.tolist(),1):
            nb=[]
            if knn_idx is not None and int(topp[ei]) < knn_idx.shape[1]: nb=[int(x) for x in knn_idx[ei,int(topp[ei])].tolist()[:16]]
            event_rows.append({'head_id':h,'rank':rank,'event_index':int(ei),'true_label':LABELS[int(y[ei])],'pred_label':LABELS[int(pred[ei])],'top_particle':int(topp[ei]),'leading_pt_particle':int(lead[ei]),'top_is_particle0':int(topp[ei]==0),'top_is_leading_pt':int(topp[ei]==lead[ei]),'event_score':float(evscore[ei]),'top_particle_pt':float(pt[ei,int(topp[ei])]),'leading_pt':float(pt[ei,int(lead[ei])]),'knn_neighbors_of_top_particle':json.dumps(nb)})
    wcsv(a.out_heads,head_rows); wcsv(a.out_events,event_rows)
    wjson(a.out_json,{'ok':True,'heads':heads,'head_rows':len(head_rows),'event_rows':len(event_rows),'captured_keys':list(caps.keys()),'knn_available':knn_idx is not None,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
    md=['# EdgeConv Inner Trace v1\n\nQuestion-driven inner trace for selected pseudo-heads.\n\n','## Head summary\n',mdtab(['head','layer','shape','particle0','lead_match','interp'],[[r['head_id'],r['layer'],r['block_output_shape'],fmt(r['particle0_top_rate']),fmt(r['leading_pt_match_rate']),r['trace_interpretation']] for r in head_rows]),'\n## Top events\n',mdtab(['head','rank','event','true','pred','top_p','lead_p','score','knn'],[[r['head_id'],r['rank'],r['event_index'],r['true_label'],r['pred_label'],r['top_particle'],r['leading_pt_particle'],fmt(r['event_score']),r['knn_neighbors_of_top_particle']] for r in event_rows[:80]]),'\n## Next\n\nUse this to refine pseudocode into route-aware code: which KNN neighbors feed the activated particle and whether L2 core readouts depend on particle0 neighborhoods.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'heads':len(head_rows),'events':len(event_rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
