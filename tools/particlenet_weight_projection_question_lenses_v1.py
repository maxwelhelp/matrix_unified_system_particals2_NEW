#!/usr/bin/env python3
import argparse, csv, json, sys
from pathlib import Path
import torch
import torch.nn as nn

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import clean, unwrap
from data.jetclass_tiny_loader_v3_official import LABELS

FEATURE_NAMES={
 'kin':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_deta','part_dphi'],
 'kinpid':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_deta','part_dphi'],
 'full':['part_pt_log','part_e_log','part_logptrel','part_logerel','part_deltaR','part_charge','part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon','part_d0','part_d0err','part_dz','part_dzerr','part_deta','part_dphi'],
}
FEATURE_GROUPS={
 'kin_logs_0_4':[0,1,2,3,4],
 'pid_charge_5_10':[5,6,7,8,9,10],
 'coords_last2':'last2',
}
CONTRASTS=[('label_Wqq','label_Zqq'),('label_Tbqq','label_Tbl'),('label_Hbb','label_Hcc'),('label_Hbb','label_Hgg'),('label_H4q','label_Hqql'),('label_QCD','label_Wqq'),('label_QCD','label_Tbqq')]

def mkdir(p): Path(p).mkdir(parents=True,exist_ok=True)
def wcsv(path,rows):
    p=Path(path); mkdir(p.parent); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def wjson(path,obj):
    p=Path(path); mkdir(p.parent); p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'
def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows: out.append('| '+' | '.join(str(x) for x in r)+' |')
    return '\n'.join(out)+'\n'

def make_model(checkpoint,mode,device):
    from weaver.nn.model.ParticleNet import ParticleNet
    input_dims={'kin':7,'kinpid':13,'full':17}[mode]
    model=ParticleNet(input_dims=input_dims,num_classes=10,conv_params=[(16,(64,64,64)),(16,(128,128,128)),(16,(256,256,256))],fc_params=[(256,0.1)],use_fusion=False,use_fts_bn=True,use_counts=True,trim=True,for_inference=False).to(device).eval()
    sd=clean(unwrap(torch.load(checkpoint,map_location='cpu')))
    res=model.load_state_dict(sd,strict=False)
    return model,res,input_dims

def as_matrix(w):
    # Convert Linear/Conv weights into [out, in_flat]
    W=w.detach().float().cpu()
    if W.ndim==1: return W.reshape(1,-1)
    return W.reshape(W.shape[0], -1)

def norm(x): return float(torch.linalg.vector_norm(x).item())
def energy_ratio(x,total): return norm(x)/(total+1e-12)
def group_ranges(n, groups):
    out=[]
    for g in range(groups):
        a=(n*g)//groups; b=(n*(g+1))//groups
        if a<b: out.append((g,a,b))
    return out

def feature_groups_for(mode,input_dim):
    names=FEATURE_NAMES[mode]
    groups=[]
    for i,n in enumerate(names): groups.append((n,[i]))
    groups.append(('kin_logs_0_4',[i for i in range(min(5,input_dim))]))
    if input_dim>=13: groups.append(('pid_charge_5_10',[5,6,7,8,9,10]))
    groups.append(('coords_last2',[input_dim-2,input_dim-1]))
    return [(n,[i for i in idxs if 0<=i<input_dim]) for n,idxs in groups]

def classify_module_name(name):
    if 'edge_convs.0' in name: return 'edge_conv_0'
    if 'edge_convs.1' in name: return 'edge_conv_1'
    if 'edge_convs.2' in name: return 'edge_conv_2'
    if name.startswith('fc') or '.fc' in name: return 'classifier_fc'
    if 'bn_fts' in name: return 'feature_norm'
    return 'other'

def question_row(component,lens,question,answer,score,score_type,evidence,risk,next_lens,**extra):
    row={'component':component,'lens':lens,'question':question,'answer':answer,'score':score,'score_type':score_type,'evidence':evidence,'risk':risk,'next_lens':next_lens}
    row.update(extra); return row

def scan_weights(model,mode,input_dim,out_groups=8,in_groups=8,topk=200):
    rows=[]
    for name,m in model.named_modules():
        if not isinstance(m,(nn.Linear,nn.Conv1d,nn.Conv2d)): continue
        if not hasattr(m,'weight') or m.weight is None: continue
        W=as_matrix(m.weight); total=norm(W)
        if total<=0: continue
        comp_type=classify_module_name(name)
        out_dim,in_flat=W.shape
        rows.append(question_row(name,'WL1 weight-energy',f'How much raw weight energy is stored in module `{name}`?',f'Module has ||W||={fmt(total)} with shape {tuple(m.weight.shape)}.',total,'weight_norm','model weights','Weight norm alone is not causal.','Compare with causal patch and activation evidence.',component_type=comp_type,rank_key=total))
        # Output pseudo-head groups: which output slices are high-energy.
        for g,a,b in group_ranges(out_dim,min(out_groups,out_dim)):
            er=energy_ratio(W[a:b,:],total)
            rows.append(question_row(name,'WL3 output pseudo-head projection',f'Does output channel group {a}:{b} behave like a strong internal question/head?',f'Output group {a}:{b} carries {fmt(er)} of module weight energy.',er,'output_group_energy','module weight block energy','High weight energy may not imply causal effect.','Patch this output group and compare to random channel groups.',component_type=comp_type,output_group=g,out_channels=f'{a}:{b}',rank_key=er))
        # Generic input groups.
        for g,a,b in group_ranges(in_flat,min(in_groups,in_flat)):
            er=energy_ratio(W[:,a:b],total)
            rows.append(question_row(name,'WL2 input/source projection',f'Does module `{name}` read source/input slice {a}:{b}?',f'Input slice {a}:{b} carries {fmt(er)} of module weight energy.',er,'input_group_energy','module input block energy','Flat input slice may mix physical channels after hidden layers.','Map this source slice to activation clusters or known feature channels.',component_type=comp_type,input_group=g,input_channels=f'{a}:{b}',rank_key=er))
        # Two-element block questions: input group -> output group.
        for og,oa,ob in group_ranges(out_dim,min(out_groups,out_dim)):
            for ig,ia,ib in group_ranges(in_flat,min(in_groups,in_flat)):
                er=energy_ratio(W[oa:ob,ia:ib],total)
                if er < 0.03: continue
                rows.append(question_row(name,'WL4 block interaction projection',f'Does source slice {ia}:{ib} feed output pseudo-head {oa}:{ob}?',f'Block {ia}:{ib}->{oa}:{ob} carries {fmt(er)} of module weight energy.',er,'block_energy','module block energy','Block energy is structural, not causal alone.','Patch corresponding activation source/output group; compare random blocks.',component_type=comp_type,input_group=ig,input_channels=f'{ia}:{ib}',output_group=og,out_channels=f'{oa}:{ob}',rank_key=er))
        # If first layer-ish and input dimension matches explicit features, add physical feature group questions.
        if in_flat>=input_dim and ('edge_convs.0' in name or 'bn_fts' in name or 'conv' in name):
            for fg,idxs in feature_groups_for(mode,input_dim):
                if not idxs: continue
                idx=torch.tensor([i for i in idxs if i<in_flat])
                if idx.numel()==0: continue
                er=energy_ratio(W[:,idx],total)
                rows.append(question_row(name,'WL2 physical feature projection',f'Does module `{name}` read physical feature group `{fg}`?',f'Feature group `{fg}` carries {fmt(er)} of module weight energy.',er,'feature_group_energy','physical input feature projection','Only valid when flat source dimension aligns with physical feature channels.','Confirm with feature-channel causal patch and activation lens.',component_type=comp_type,feature_group=fg,feature_indices=json.dumps(idxs),rank_key=er))
        # Classifier class and contrast questions.
        if isinstance(m,nn.Linear) and out_dim==10:
            for c,lbl in enumerate(LABELS):
                er=energy_ratio(W[c:c+1,:],total)
                rows.append(question_row(name,'WL5 class direction projection',f'Which hidden directions support class `{lbl}`?',f'Classifier row `{lbl}` carries {fmt(er)} of classifier weight energy.',er,'class_row_energy','classifier weight row','Class row norm is not same as logit attribution.','Project hidden activations onto this class row and patch supporting components.',component_type=comp_type,class_label=lbl,class_id=c,rank_key=er))
            for a,b in CONTRASTS:
                ia=LABELS.index(a); ib=LABELS.index(b)
                vec=W[ia]-W[ib]
                er=norm(vec)/(total+1e-12)
                rows.append(question_row(name,'WL6 class contrast projection',f'What hidden directions separate `{a}` from `{b}`?',f'Contrast row {a}-{b} has relative norm {fmt(er)}.',er,'class_contrast_norm','classifier contrast direction','Large contrast norm needs hidden activation alignment.','Project EdgeConv/FC activations onto this contrast direction.',component_type=comp_type,contrast=f'{a}_vs_{b}',rank_key=er))
    rows=sorted(rows,key=lambda r:float(r.get('rank_key',0)),reverse=True)
    return rows[:topk],rows

def synthesize(rows):
    hyps=[]
    blocks=[r for r in rows if r['lens'].startswith('WL4')][:10]
    if blocks:
        hyps.append('Strong two-element projection questions were found: source/input slices feeding output pseudo-head groups. These should be compared with causal output-group patches.')
    phys=[r for r in rows if r['lens'].startswith('WL2 physical')][:10]
    if phys:
        hyps.append('Physical feature projection questions exist in early modules; check whether these align with feature-channel causal patches from v5.')
    cls=[r for r in rows if r['lens'].startswith('WL6')][:5]
    if cls:
        hyps.append('Classifier contrast directions define class questions such as Wqq-vs-Zqq and Tbqq-vs-Tbl; next step is to project hidden activations/components into these contrast directions.')
    return hyps

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--mode',default='kinpid',choices=['kin','kinpid','full'])
    ap.add_argument('--device',default='cpu')
    ap.add_argument('--out-dir',default='runs/particlenet_weight_projection_questions_v1')
    ap.add_argument('--topk',type=int,default=250)
    args=ap.parse_args(); out=Path(args.out_dir); mkdir(out/'tables')
    model,res,input_dim=make_model(args.checkpoint,args.mode,args.device)
    top_rows,all_rows=scan_weights(model,args.mode,input_dim,topk=args.topk)
    wcsv(out/'tables/weight_projection_questions.csv',top_rows)
    summary={'ok':True,'checkpoint':args.checkpoint,'mode':args.mode,'missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys),'n_questions_total':len(all_rows),'n_questions_exported':len(top_rows),'hypotheses':synthesize(top_rows)}
    wjson(out/'particlenet_weight_projection_questions_v1_summary.json',summary)
    md=['# ParticleNet Weight Projection Questions v1\n\n',
        'This report scans model weights as projection questions. It asks which source/input groups feed which output pseudo-head groups, which classes/contrasts classifier weights encode, and which physical feature groups are visible in early weights.\n\n',
        '## Summary\n\n```json\n',json.dumps(summary,indent=2,ensure_ascii=False),'\n```\n\n',
        '## Candidate synthesis\n\n']
    for h in summary['hypotheses']: md.append(f'- {h}\n')
    md += ['\n## Top projection questions\n',
           md_table(['component','lens','question','answer','score','risk','next_lens'],[[r['component'],r['lens'],r['question'],r['answer'],fmt(r['score']),r['risk'],r['next_lens']] for r in top_rows[:80]]),
           '\n## Output files\n\n- `reports/latest/tables/weight_projection_questions.csv`\n- `manifests/latest/particlenet_weight_projection_questions_v1_summary.json`\n']
    (out/'PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md').write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
