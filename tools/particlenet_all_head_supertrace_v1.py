#!/usr/bin/env python3
import argparse, csv, json, sys, gc
from pathlib import Path
import torch
import torch.nn.functional as F

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced, clean, unwrap
from data.jetclass_tiny_loader_v3_official import LABELS

FEATURE_NAMES={
 'kin':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_deta','part_dphi'],
 'kinpid':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_deta','part_dphi'],
 'full':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_d0','part_d0err','part_dz','part_dzerr','part_deta','part_dphi'],
}

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wjson(p,o): p=Path(p); mkdir(p.parent); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def wcsv(p,rows):
    p=Path(p); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def table(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rs])+'\n'

def make_model(checkpoint,mode,device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd,strict=False)
    return model,res,input_dims

def split_ranges(C,groups):
    out=[]
    for g in range(groups):
        a=(C*g)//groups; b=(C*(g+1))//groups
        if a<b: out.append((g,a,b))
    return out

def slice_batch(batch,s,e):
    out={}
    B=batch['y'].shape[0]
    for k,v in batch.items():
        if torch.is_tensor(v) and v.shape and v.shape[0]==B:
            out[k]=v[s:e]
        else:
            out[k]=v
    return out

def particle_row(batch,mode,ei,pi):
    names=FEATURE_NAMES[mode]
    vals=batch['features'][ei,:,pi].detach().cpu().float().tolist()
    row={n:float(v) for n,v in zip(names,vals)}
    vec=batch['vectors'][ei,:,pi].detach().cpu().float()
    px,py,pz,en=[float(x) for x in vec[:4]]
    pt=(px*px+py*py)**0.5
    deta=float(batch['points'][ei,0,pi].detach().cpu())
    dphi=float(batch['points'][ei,1,pi].detach().cpu())
    dr=(deta*deta+dphi*dphi)**0.5
    row.update({'px':px,'py':py,'pz':pz,'energy':en,'pt':pt,'deta':deta,'dphi':dphi,'deltaR_from_axis':dr})
    return row

def baseline_logits(model,batch):
    with torch.no_grad():
        return model(batch['points'],batch['features'],batch['mask']).detach()

def gated_forward(model,batch,groups):
    gate_tensors=[]
    meta_by_layer=[]
    captures=[]
    hooks=[]

    def make_hook(layer_id):
        def hook(m, inp, out):
            C=out.shape[1]
            if len(gate_tensors)<=layer_id:
                ranges=split_ranges(C,groups)
                gate=torch.ones(len(ranges),device=out.device,requires_grad=True)
                gate_tensors.append(gate)
                meta_by_layer.append([(layer_id,gi,a,b) for gi,a,b in ranges])
            parts=[]
            energies=[]
            last=0
            for idx,(ly,gi,a,b) in enumerate(meta_by_layer[layer_id]):
                if a>last:
                    parts.append(out[:,last:a,:])
                parts.append(out[:,a:b,:] * gate_tensors[layer_id][idx])
                energies.append(torch.sqrt((out[:,a:b,:].detach().float()**2).sum(dim=1)+1e-12))
                last=b
            if last<C:
                parts.append(out[:,last:C,:])
            captures.append({'layer':layer_id,'energies':energies,'shape':tuple(out.shape)})
            return torch.cat(parts,dim=1)
        return hook

    for i,conv in enumerate(model.edge_convs):
        hooks.append(conv.register_forward_hook(make_hook(i)))
    logits=model(batch['points'],batch['features'],batch['mask'])
    for h in hooks:
        h.remove()
    return logits,gate_tensors,meta_by_layer,captures

def capture_energies(model,batch,groups):
    captures=[]; hooks=[]
    def make_hook(layer_id):
        def hook(m,inp,out):
            C=out.shape[1]
            ranges=split_ranges(C,groups)
            energies=[]
            for gi,a,b in ranges:
                energies.append(torch.sqrt((out[:,a:b,:].detach().float()**2).sum(dim=1)+1e-12))
            captures.append({'layer':layer_id,'energies':energies,'shape':tuple(out.shape)})
        return hook
    for i,conv in enumerate(model.edge_convs):
        hooks.append(conv.register_forward_hook(make_hook(i)))
    with torch.no_grad():
        _=model(batch['points'],batch['features'],batch['mask'])
    for h in hooks:
        h.remove()
    return captures

def collect_gate_grads(gate_tensors,meta_by_layer):
    grads=[]
    for layer_id,gate in enumerate(gate_tensors):
        gate_grad=gate.grad.detach().cpu() if gate.grad is not None else torch.zeros_like(gate.detach().cpu())
        for idx,(ly,gi,a,b) in enumerate(meta_by_layer[layer_id]):
            grad=float(gate_grad[idx])
            grads.append({'layer':ly,'group_id':gi,'channels':f'ch{a}:{b}','grad':grad,'abs_grad':abs(grad),'positive_grad':max(0.0,grad),'head_id':f'L{ly}_ch{a}:{b}'})
    return grads

def add_grad_accum(accum,grads,weight):
    for r in grads:
        key=(r['layer'],r['group_id'],r['channels'],r['head_id'])
        if key not in accum:
            accum[key]=0.0
        accum[key]+=float(r['grad'])*weight

def grad_rows_from_accum(accum):
    rows=[]
    for (ly,gi,ch,hid),grad in accum.items():
        rows.append({'layer':ly,'group_id':gi,'channels':ch,'grad':grad,'abs_grad':abs(grad),'positive_grad':max(0.0,grad),'head_id':hid})
    return sorted(rows,key=lambda r:r['abs_grad'],reverse=True)

def effective_n_from_captures(captures):
    ns=[]
    for cap in captures:
        for energy in cap.get('energies',[]):
            if energy.ndim==2:
                ns.append(int(energy.shape[1]))
    if not ns:
        return 0
    return max(ns)

def pad_or_crop_energy(en, n_eff):
    if en.shape[1] == n_eff:
        return en
    if en.shape[1] > n_eff:
        return en[:, :n_eff]
    pad = torch.zeros(en.shape[0], n_eff - en.shape[1], device=en.device, dtype=en.dtype)
    return torch.cat([en, pad], dim=1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--samples-per-file',type=int,default=64)
    ap.add_argument('--max-files',type=int,default=20)
    ap.add_argument('--head-groups',type=int,default=8)
    ap.add_argument('--micro-batch',type=int,default=64)
    ap.add_argument('--top-events',type=int,default=30)
    ap.add_argument('--top-particles',type=int,default=10)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_all_head_supertrace_v1')
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dims=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    B=int(batch['y'].shape[0])
    mb=max(1,int(args.micro_batch))

    # Pass 0: baseline predictions in micro-batches, no grad.
    base_chunks=[]
    for s in range(0,B,mb):
        e=min(B,s+mb)
        b=slice_batch(batch,s,e)
        base_chunks.append(baseline_logits(model,b).detach().cpu())
        if args.device.startswith('cuda'):
            torch.cuda.empty_cache()
    base_cpu=torch.cat(base_chunks,dim=0)
    pred_cpu=base_cpu.argmax(-1)
    y_cpu=batch['y'].detach().cpu()
    prob_cpu=F.softmax(base_cpu.float(),-1)
    baseline_acc=float((pred_cpu==y_cpu).float().mean())

    # Pass 1: micro-batched differentiable gates. Accumulate gradients for global mean objective.
    grad_accum={}
    obj_mean=0.0
    for s in range(0,B,mb):
        e=min(B,s+mb)
        b=slice_batch(batch,s,e)
        model.zero_grad(set_to_none=True)
        logits,gate_tensors,meta_by_layer,_captures=gated_forward(model,b,args.head_groups)
        pred_mb=pred_cpu[s:e].to(args.device)
        obj=logits.gather(1,pred_mb[:,None]).mean()
        obj.backward()
        grads=collect_gate_grads(gate_tensors,meta_by_layer)
        weight=(e-s)/B
        add_grad_accum(grad_accum,grads,weight)
        obj_mean += float(obj.detach().cpu())*weight
        del logits,gate_tensors,meta_by_layer,_captures,obj
        gc.collect()
        if args.device.startswith('cuda'):
            torch.cuda.empty_cache()
    grads_sorted=grad_rows_from_accum(grad_accum)
    weight_by=(lambda r:r['positive_grad'])
    if sum(weight_by(r) for r in grads_sorted)<1e-12:
        weight_by=lambda r:r['abs_grad']
    grad_lookup={(r['layer'],r['group_id']):weight_by(r) for r in grads_sorted}

    # Pass 2: no-grad head energies and all-head particle scores in micro-batches.
    event_rows_all=[]
    particle_rows_all=[]
    class_score_sum={}; class_score_vals={}; class_n={}; class_correct={}
    for s in range(0,B,mb):
        e=min(B,s+mb)
        b=slice_batch(batch,s,e)
        captures=capture_energies(model,b,args.head_groups)
        n_eff=effective_n_from_captures(captures)
        if n_eff <= 0:
            continue
        # ParticleNet's SequenceTrimmer can shorten N inside EdgeConv. Use the actual
        # effective length from EdgeConv outputs, not the padded input length.
        super_score=torch.zeros(e-s,n_eff,device=args.device)
        for cap in captures:
            ly=cap['layer']
            for gi,energy in enumerate(cap['energies']):
                w=grad_lookup.get((ly,gi),0.0)
                if w==0: continue
                en=energy.detach().float()
                en=en/(en.amax(dim=1,keepdim=True)+1e-9)
                en=pad_or_crop_energy(en,n_eff)
                super_score += w*en
        real_mask=b['mask'][:,0,:n_eff].detach().bool()
        if real_mask.shape[1] < n_eff:
            pad=torch.zeros(real_mask.shape[0], n_eff-real_mask.shape[1], device=real_mask.device, dtype=torch.bool)
            real_mask=torch.cat([real_mask,pad],dim=1)
        super_score=super_score.masked_fill(~real_mask,-1)
        event_score=super_score.max(dim=1).values.detach().cpu()
        for local_i in range(e-s):
            global_i=s+local_i
            pred=int(pred_cpu[global_i]); true=int(y_cpu[global_i])
            lbl=LABELS[pred]
            class_n[pred]=class_n.get(pred,0)+1
            class_correct[pred]=class_correct.get(pred,0)+(1 if pred==true else 0)
            class_score_sum[pred]=class_score_sum.get(pred,0.0)+float(event_score[local_i])
            class_score_vals.setdefault(pred,[]).append(float(event_score[local_i]))
            real_n=max(1,int(real_mask[local_i].sum().detach().cpu()))
            pe=super_score[local_i]
            k=min(args.top_particles, real_n, int(pe.numel()))
            idx=torch.topk(pe,k).indices.detach().cpu().tolist()
            event_rows_all.append({'event_idx':global_i,'true':true,'true_label':LABELS[true],'pred':pred,'pred_label':lbl,'conf':float(prob_cpu[global_i,pred]),'pred_logit':float(base_cpu[global_i,pred]),'super_max_particle_score':float(event_score[local_i]),'real_particles':real_n,'effective_particles':n_eff,'top_particle_indices':json.dumps(idx)})
            for rank,pi in enumerate(idx,1):
                pr=particle_row(b,args.mode,local_i,pi)
                row={'event_idx':global_i,'rank':rank,'particle_idx':pi,'super_score':float(super_score[local_i,pi].detach().cpu()),'true_label':LABELS[true],'pred_label':lbl,'conf':float(prob_cpu[global_i,pred])}
                row.update(pr); particle_rows_all.append(row)
        del captures,super_score
        gc.collect()
        if args.device.startswith('cuda'):
            torch.cuda.empty_cache()

    event_rows_all=sorted(event_rows_all,key=lambda r:float(r['super_max_particle_score']),reverse=True)
    top_event_ids=set(r['event_idx'] for r in event_rows_all[:args.top_events])
    event_rows=event_rows_all[:args.top_events]
    particle_rows=[r for r in particle_rows_all if r['event_idx'] in top_event_ids]
    particle_rows=sorted(particle_rows,key=lambda r:(r['event_idx'],r['rank']))
    class_rows=[]
    for c,lbl in enumerate(LABELS):
        if class_n.get(c,0)==0: continue
        vals=torch.tensor(class_score_vals[c],dtype=torch.float32)
        class_rows.append({'pred_label':lbl,'n_pred':class_n[c],'super_score_mean':class_score_sum[c]/class_n[c],'super_score_p90':float(torch.quantile(vals,0.9)),'acc_within_pred':class_correct[c]/class_n[c]})

    wcsv(out/'tables/all_head_gate_gradients.csv',grads_sorted)
    wcsv(out/'tables/all_head_supertrace_events.csv',event_rows)
    wcsv(out/'tables/all_head_supertrace_particles.csv',particle_rows)
    wcsv(out/'tables/all_head_supertrace_class_summary.csv',class_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'n_events':B,'micro_batch':mb,'baseline_acc':baseline_acc,'objective_pred_logit_mean':obj_mean,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'top_heads_by_abs_grad':grads_sorted[:20],'top_events':event_rows[:10],'class_summary':class_rows}
    wjson(out/'all_head_supertrace_summary.json',summary)
    md=['# ParticleNet All-Head Differentiable Supertrace v1\n\n',
        f"n_events={summary['n_events']} micro_batch={mb} baseline_acc={fmt(summary['baseline_acc'])} objective_pred_logit_mean={fmt(summary['objective_pred_logit_mean'])}\n\n",
        'This treats all EdgeConv pseudo-head groups as differentiable gates and backpropagates the predicted-class logit through them. It is the all-head analogue of token/particle tracing. This version uses micro-batches and the effective trimmed particle length to avoid CUDA OOM / shape mismatch.\n\n',
        '## Top differentiable head gates\n',
        table(['rank','head','grad','abs_grad','channels'],[[i+1,r['head_id'],fmt(r['grad']),fmt(r['abs_grad']),r['channels']] for i,r in enumerate(grads_sorted[:30])]),
        '\n## Class summary by predicted class\n',
        table(['pred_label','n_pred','super_mean','super_p90','acc_within_pred'],[[r['pred_label'],r['n_pred'],fmt(r['super_score_mean']),fmt(r['super_score_p90']),fmt(r['acc_within_pred'])] for r in class_rows]),
        '\n## Top events by all-head super-score\n',
        table(['event','true','pred','conf','super_max','real_particles','effective_particles','top_particle_indices'],[[r['event_idx'],r['true_label'],r['pred_label'],fmt(r['conf']),fmt(r['super_max_particle_score']),r['real_particles'],r.get('effective_particles',''),r['top_particle_indices']] for r in event_rows[:80]]),
        '\n## Top particles inside top events\n',
        table(['event','rank','particle','super_score','pt','energy','deta','dphi','deltaR','charge','pred'],[[r['event_idx'],r['rank'],r['particle_idx'],fmt(r['super_score']),fmt(r.get('pt')),fmt(r.get('energy')),fmt(r.get('deta')),fmt(r.get('dphi')),fmt(r.get('deltaR_from_axis')),fmt(r.get('part_charge','')),r['pred_label']] for r in particle_rows[:200]]),
        '\nFull CSV tables:\n- `reports/latest/tables/all_head_gate_gradients.csv`\n- `reports/latest/tables/all_head_supertrace_events.csv`\n- `reports/latest/tables/all_head_supertrace_particles.csv`\n- `reports/latest/tables/all_head_supertrace_class_summary.csv`\n']
    (out/'PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False)[:20000])

if __name__=='__main__': main()
