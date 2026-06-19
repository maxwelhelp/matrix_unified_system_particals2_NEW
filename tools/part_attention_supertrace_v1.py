#!/usr/bin/env python3
import argparse, csv, importlib.util, json, math, os, sys
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

import awkward as ak
import numpy as np
import torch
import torch.nn.functional as F
import uproot

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
SRC='label_Hqql'; TGT='label_Tbl'
BRANCHES = ['part_px','part_py','part_pz','part_energy','part_deta','part_dphi','part_charge',
 'part_isChargedHadron','part_isNeutralHadron','part_isPhoton','part_isElectron','part_isMuon',
 'part_d0val','part_d0err','part_dzval','part_dzerr','jet_pt','jet_energy']


def wcsv(path, rows):
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with path.open('w', encoding='utf-8', newline='') as f:
        wr=csv.DictWriter(f, fieldnames=keys); wr.writeheader(); wr.writerows(rows)

def wjson(path, obj):
    path=Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

def mdtab(h, rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'


def read_manifest(path):
    mp={}
    p=Path(path)
    if p.exists():
        for line in p.read_text(encoding='utf-8').splitlines():
            if ':' in line:
                g,f=line.split(':',1); mp[g]=f
    return mp

def group_from_output_name(path):
    n=Path(path).name
    if n.startswith('part_weaver_predict_smoke_v3_') and n.endswith('.root'):
        return n[len('part_weaver_predict_smoke_v3_'):-5]
    return Path(path).stem

def find_tree(rf):
    for k in rf.keys():
        o=rf[k]
        if hasattr(o,'arrays') and hasattr(o,'keys'): return o
    raise RuntimeError('no tree found')

def score_branches(keys):
    out=[]
    for lab in LABELS:
        for c in [f'score_{lab}', f'score_{lab.replace("label_","")}']:
            if c in keys: out.append(c); break
        else: return []
    return out

def build_groups_from_outputs(root_glob, manifest_path, max_a, max_b, max_c, max_d):
    manifest=read_manifest(manifest_path); rows=[]
    for f in sorted(Path('.').glob(root_glob)):
        g=group_from_output_name(f)
        with uproot.open(f) as rf:
            t=find_tree(rf); keys=list(t.keys()); scores=score_branches(keys)
            arr=t.arrays(LABELS+scores, library='np')
            y=np.stack([arr[x] for x in LABELS],1).argmax(1)
            s=np.stack([arr[x] for x in scores],1); pred=s.argmax(1)
            for i in range(len(y)):
                tl,pl=LABELS[int(y[i])],LABELS[int(pred[i])]
                group=None
                if g=='HToWW2Q1L' and tl==SRC and pl==SRC: group='A_Hqql_correct'
                elif g=='HToWW2Q1L' and tl==SRC and pl==TGT: group='B_Hqql_to_Tbl'
                elif g=='TTBarLep' and tl==TGT and pl==TGT: group='C_Tbl_correct'
                elif g=='TTBarLep' and tl==TGT and pl==SRC: group='D_Tbl_to_Hqql'
                if group:
                    rows.append({'analysis_group':group,'source_group':g,'source_root':manifest.get(g,''),'entry_idx':i,
                        'true_label':tl,'pred_label':pl,'score_Hqql':float(s[i,LABELS.index(SRC)]),'score_Tbl':float(s[i,LABELS.index(TGT)]),
                        'margin_Tbl_minus_Hqql':float(s[i,LABELS.index(TGT)]-s[i,LABELS.index(SRC)]),
                        'margin_Hqql_minus_Tbl':float(s[i,LABELS.index(SRC)]-s[i,LABELS.index(TGT)])})
    def pick(group, n):
        xs=[r for r in rows if r['analysis_group']==group]
        key='margin_Tbl_minus_Hqql' if group.startswith(('B','C')) else 'margin_Hqql_minus_Tbl'
        return sorted(xs, key=lambda r:r[key], reverse=True)[:n], len(xs)
    out=[]; counts={}
    for g,n in [('A_Hqql_correct',max_a),('B_Hqql_to_Tbl',max_b),('C_Tbl_correct',max_c),('D_Tbl_to_Hqql',max_d)]:
        xs,c=pick(g,n); out+=xs; counts[g]=c
    return out, counts

def load_groups(path, root_glob, manifest, max_a, max_b, max_c, max_d):
    if path and Path(path).exists():
        rows=[]
        with open(path, newline='', encoding='utf-8') as f:
            for r in csv.DictReader(f):
                r['entry_idx']=int(r['entry_idx']); rows.append(r)
        return rows, {g:sum(1 for r in rows if r.get('analysis_group')==g) for g in sorted(set(r.get('analysis_group') for r in rows))}
    return build_groups_from_outputs(root_glob, manifest, max_a, max_b, max_c, max_d)


def pad_wrap(x, length=128, value=0.0):
    x=np.asarray(x, dtype=np.float32)
    n=len(x)
    if n>=length: return x[:length], min(n,length)
    if n==0: return np.full(length,value,np.float32), 0
    reps=int(math.ceil(length/n)); y=np.tile(x,reps)[:length]
    return y.astype(np.float32), n

def transform(x, center=None, scale=1.0, lo=-5, hi=5):
    y=np.asarray(x, dtype=np.float32)
    if center is not None: y=(y-center)*scale
    return np.clip(y, lo, hi).astype(np.float32)

def pid_role(ev, i):
    if ev['part_isElectron'][i]>0.5: return 'electron'
    if ev['part_isMuon'][i]>0.5: return 'muon'
    if ev['part_isPhoton'][i]>0.5: return 'photon'
    if ev['part_isChargedHadron'][i]>0.5: return 'charged_hadron'
    if ev['part_isNeutralHadron'][i]>0.5: return 'neutral_hadron'
    return 'other'

def event_to_arrays(arr, idx):
    ev={k:np.asarray(arr[k][idx]) for k in BRANCHES if k not in ('jet_pt','jet_energy')}
    ev['jet_pt']=float(arr['jet_pt'][idx]); ev['jet_energy']=float(arr['jet_energy'][idx])
    px,py,pz,e=ev['part_px'],ev['part_py'],ev['part_pz'],ev['part_energy']
    pt=np.hypot(px,py).clip(min=1e-8); ee=e.clip(min=1e-8)
    d0=np.tanh(ev['part_d0val']); dz=np.tanh(ev['part_dzval'])
    deltaR=np.hypot(ev['part_deta'],ev['part_dphi'])
    feat=[transform(np.log(pt),1.7,0.7), transform(np.log(ee),2.0,0.7), transform(np.log(pt/max(ev['jet_pt'],1e-8)),-4.7,0.7),
          transform(np.log(ee/max(ev['jet_energy'],1e-8)),-4.7,0.7), transform(deltaR,0.2,4.0),
          ev['part_charge'].astype(np.float32), ev['part_isChargedHadron'].astype(np.float32), ev['part_isNeutralHadron'].astype(np.float32),
          ev['part_isPhoton'].astype(np.float32), ev['part_isElectron'].astype(np.float32), ev['part_isMuon'].astype(np.float32),
          d0.astype(np.float32), transform(ev['part_d0err'],0,1,0,1), dz.astype(np.float32), transform(ev['part_dzerr'],0,1,0,1),
          ev['part_deta'].astype(np.float32), ev['part_dphi'].astype(np.float32)]
    cols=[]
    for f in feat: cols.append(pad_wrap(f)[0])
    points=np.stack([pad_wrap(ev['part_deta'])[0], pad_wrap(ev['part_dphi'])[0]],0)
    features=np.stack(cols,0)
    vectors=np.stack([pad_wrap(px)[0],pad_wrap(py)[0],pad_wrap(pz)[0],pad_wrap(e)[0]],0)
    real=min(len(px),128); mask=np.zeros((1,128),np.float32); mask[0,:real]=1
    roles=[]; pts=[]; detas=[]; dphis=[]
    for i in range(128):
        j=i % max(len(px),1) if len(px)>0 else 0
        roles.append(pid_role(ev,j) if i<real and len(px)>0 else 'pad')
        pts.append(float(pt[j]) if i<real and len(px)>0 else 0.0)
        detas.append(float(ev['part_deta'][j]) if i<real and len(px)>0 else 0.0)
        dphis.append(float(ev['part_dphi'][j]) if i<real and len(px)>0 else 0.0)
    return points,features,vectors,mask,{'roles':roles,'pt':pts,'deta':detas,'dphi':dphis,'n_real':real}

def build_batch(rows, device):
    byfile=defaultdict(list)
    for n,r in enumerate(rows): byfile[r['source_root']].append((n,r))
    out=[None]*len(rows); meta=[None]*len(rows)
    for f,items in byfile.items():
        if not f or not Path(f).exists(): raise RuntimeError(f'missing source_root: {f}')
        with uproot.open(f) as rf:
            t=find_tree(rf); arr=t.arrays(BRANCHES, library='ak')
        for n,r in items:
            p,x,v,m,mm=event_to_arrays(arr, int(r['entry_idx']))
            out[n]=(p,x,v,m); meta[n]={**r, **mm}
    pts=torch.tensor(np.stack([o[0] for o in out]),device=device)
    fts=torch.tensor(np.stack([o[1] for o in out]),device=device)
    vec=torch.tensor(np.stack([o[2] for o in out]),device=device)
    msk=torch.tensor(np.stack([o[3] for o in out]),device=device)
    return pts,fts,vec,msk,meta


def load_model(network_file, checkpoint, device):
    spec=importlib.util.spec_from_file_location('part_net', network_file); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    dc=SimpleNamespace(input_names=['pf_points','pf_features','pf_vectors','pf_mask'], input_dicts={'pf_features':[str(i) for i in range(17)]}, label_value=list(range(10)), input_shapes={})
    model,_=mod.get_model(dc); model.to(device); sd=torch.load(checkpoint,map_location=device); model.load_state_dict(sd, strict=True); model.eval(); return model

class AttentionTap:
    def __init__(self, topk=8): self.topk=topk; self.records=[]; self.handles=[]
    def hook(self, name):
        def fn(module, args, kwargs):
            q=args[0]; k=args[1]; v=args[2]
            kpm=kwargs.get('key_padding_mask', None); am=kwargs.get('attn_mask', None)
            b,t,_=q.shape; s=k.shape[1]; nh=module.num_heads; hd=module.head_dim
            qq,kk,_=F._in_projection_packed(q,k,v,module.in_proj.weight,module.in_proj.bias)
            qq=module.q_norm(qq.view(b,t,nh,hd)).transpose(1,2)*math.sqrt(1.0/hd)
            kk=module.k_norm(kk.view(b,s,nh,hd)).transpose(1,2)
            w=qq @ kk.transpose(-2,-1)
            if am is not None: w=w+am
            if kpm is not None:
                w=w.masked_fill(kpm.view(b,1,1,s).bool(), float('-inf'))
            a=torch.softmax(w, dim=-1).detach()
            flat=a.reshape(b,nh,-1); val,idx=torch.topk(flat, k=min(self.topk, flat.shape[-1]), dim=-1)
            self.records.append({'name':name,'tgt':t,'src':s,'val':val.cpu(),'idx':idx.cpu()})
        return fn
    def attach(self, model):
        for name,m in model.named_modules():
            if hasattr(m,'in_proj') and hasattr(m,'num_heads') and hasattr(m,'head_dim'):
                self.handles.append(m.register_forward_pre_hook(self.hook(name), with_kwargs=True))
    def clear(self): self.records=[]
    def close(self):
        for h in self.handles: h.remove()

def pair_dist(meta,q,k):
    if q<0 or k<0: return 0.0
    return float(math.hypot(meta['deta'][q]-meta['deta'][k], meta['dphi'][q]-meta['dphi'][k]))

def process_records(records, meta_batch, rows_out):
    for rec in records:
        name=rec['name']; is_cls=(rec['tgt']==1)
        for bi,meta in enumerate(meta_batch):
            for h in range(rec['val'].shape[1]):
                for kk in range(rec['val'].shape[2]):
                    flat=int(rec['idx'][bi,h,kk]); w=float(rec['val'][bi,h,kk])
                    q=flat//rec['src']; k=flat%rec['src']
                    qi=-1 if is_cls else q; ki=k-1 if is_cls and rec['src']==129 else k
                    qr='CLS' if qi<0 else meta['roles'][qi]; kr='CLS' if ki<0 else meta['roles'][ki]
                    rows_out.append({'group':meta['analysis_group'],'source_group':meta['source_group'],'entry_idx':meta['entry_idx'],
                        'module':name,'head':h,'query_idx':qi,'key_idx':ki,'query_role':qr,'key_role':kr,'pair_role':qr+'<-'+kr,
                        'attn_weight':w,'deltaR':pair_dist(meta,qi,ki),'query_pt':0 if qi<0 else round(meta['pt'][qi],5),'key_pt':0 if ki<0 else round(meta['pt'][ki],5)})

def aggregate(rows):
    d=defaultdict(lambda: defaultdict(list))
    for r in rows:
        key=(r['module'],r['head'],r['pair_role'])
        d[key][r['group']].append(float(r['attn_weight']))
    out=[]
    for (m,h,p),g in d.items():
        A=np.mean(g.get('A_Hqql_correct',[0])); B=np.mean(g.get('B_Hqql_to_Tbl',[0])); C=np.mean(g.get('C_Tbl_correct',[0])); D=np.mean(g.get('D_Tbl_to_Hqql',[0]))
        out.append({'module':m,'head':h,'pair_role':p,'A':A,'B':B,'C':C,'D':D,'trigger_B_minus_A':B-A,'loss_A_minus_B':A-B,'tbl_like_B_close_C':B-abs(B-C),'anomaly_B_not_A_not_C':abs(B-A)*abs(B-C),'n':sum(len(v) for v in g.values())})
    return sorted(out, key=lambda r:abs(r['trigger_B_minus_A']), reverse=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--groups-csv', default='reports/latest/tables/part_hqql_tbl_groups_v1.csv')
    ap.add_argument('--root-glob', default='reports/latest/part_weaver_predict_smoke_v3_*.root')
    ap.add_argument('--manifest', default='manifests/latest/part_weaver_predict_smoke_v3_args.txt')
    ap.add_argument('--network-file', default='external/particle_transformer/networks/example_ParticleTransformer.py')
    ap.add_argument('--checkpoint', default='external/particle_transformer/models/ParT_full.pt')
    ap.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--batch-size', type=int, default=16); ap.add_argument('--topk', type=int, default=8)
    ap.add_argument('--max-a', type=int, default=5000); ap.add_argument('--max-b', type=int, default=2000); ap.add_argument('--max-c', type=int, default=5000); ap.add_argument('--max-d', type=int, default=2000)
    ap.add_argument('--out-md', default='reports/latest/PART_ATTENTION_SUPERTRACE_V1.md')
    ap.add_argument('--out-pairs', default='reports/latest/tables/part_attention_pair_flows_v1.csv')
    ap.add_argument('--out-summary', default='reports/latest/tables/part_attention_path_summary_v1.csv')
    ap.add_argument('--out-json', default='manifests/latest/part_attention_supertrace_v1.json')
    a=ap.parse_args(); device=torch.device(a.device)
    groups,counts=load_groups(a.groups_csv,a.root_glob,a.manifest,a.max_a,a.max_b,a.max_c,a.max_d)
    model=load_model(a.network_file,a.checkpoint,device); tap=AttentionTap(a.topk); tap.attach(model)
    pair_rows=[]
    with torch.no_grad():
        for s in range(0,len(groups),a.batch_size):
            sub=groups[s:s+a.batch_size]; pts,fts,vec,msk,meta=build_batch(sub,device)
            tap.clear(); _=model(pts,fts,vec,msk); process_records(tap.records,meta,pair_rows)
    tap.close(); summary=aggregate(pair_rows)
    wcsv(a.out_pairs,pair_rows); wcsv(a.out_summary,summary); wjson(a.out_json,{'ok':True,'events':len(groups),'counts':counts,'pair_rows':len(pair_rows),'summary_rows':len(summary)})
    top_tr=sorted(summary,key=lambda r:r['trigger_B_minus_A'],reverse=True)[:20]
    top_loss=sorted(summary,key=lambda r:r['loss_A_minus_B'],reverse=True)[:20]
    top_anom=sorted(summary,key=lambda r:r['anomaly_B_not_A_not_C'],reverse=True)[:20]
    md='# PART_ATTENTION_SUPERTRACE_V1\n\nFull ParT top-K attention-pair supertrace over A/B/C/D groups. Saves top-K pairs per attention module/head/event, then ranks trigger/loss/anomaly paths.\n\n'
    md+=f'- events traced: **{len(groups)}**\n- pair rows: **{len(pair_rows)}**\n- summary rows: **{len(summary)}**\n- topk per head: **{a.topk}**\n\n'
    md+='## Input counts\n'+mdtab(['group','available/selected'], [[k,v] for k,v in counts.items()])
    md+='\n## Top B>A trigger paths\n'+mdtab(['module','head','pair_role','A','B','C','B-A'], [[r['module'],r['head'],r['pair_role'],round(r['A'],5),round(r['B'],5),round(r['C'],5),round(r['trigger_B_minus_A'],5)] for r in top_tr])
    md+='\n## Top A>B Hqql-loss paths\n'+mdtab(['module','head','pair_role','A','B','C','A-B'], [[r['module'],r['head'],r['pair_role'],round(r['A'],5),round(r['B'],5),round(r['C'],5),round(r['loss_A_minus_B'],5)] for r in top_loss])
    md+='\n## Top anomaly paths B!=A and B!=C\n'+mdtab(['module','head','pair_role','A','B','C','score'], [[r['module'],r['head'],r['pair_role'],round(r['A'],5),round(r['B'],5),round(r['C'],5),round(r['anomaly_B_not_A_not_C'],5)] for r in top_anom])
    md+='\n## Next\nUse `part_attention_path_summary_v1.csv` for automatic physics-regime interpretation and ParticleNet-vs-ParT comparison.\n'
    Path(a.out_md).parent.mkdir(parents=True, exist_ok=True); Path(a.out_md).write_text(md,encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(groups),'pair_rows':len(pair_rows),'out_md':a.out_md}, indent=2))
if __name__=='__main__': main()
