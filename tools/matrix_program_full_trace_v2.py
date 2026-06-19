#!/usr/bin/env python3
import argparse,csv,json,math,sys
from pathlib import Path
from collections import defaultdict
import torch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model,pt_values,real_mask
from data.jetclass_tiny_loader_v3_official import LABELS
SRC='label_Hqql'; TGT='label_Tbl'; SRC_ID=LABELS.index(SRC); TGT_ID=LABELS.index(TGT)
def readcsv(p):
 p=Path(p); 
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
 try: v=float(x); return v if math.isfinite(v) else d
 except Exception: return d
def fmt(x):
 try: return f'{float(x):.4f}'
 except Exception: return 'n/a'
def mdtab(h,rows):
 if not rows: return '_No rows._\n'
 return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rows])+'\n'
def slice_batch(b,ids):
 idx=torch.as_tensor(ids,dtype=torch.long,device=b['y'].device); B=b['y'].shape[0]; o={}
 for k,v in b.items(): o[k]=v.index_select(0,idx) if torch.is_tensor(v) and v.shape and v.shape[0]==B else v
 return o
def forward_logits(model,b,mb=256):
 outs=[]; B=b['y'].shape[0]
 with torch.no_grad():
  for s in range(0,B,mb): outs.append(model(**{k:v for k,v in slice_batch(b,list(range(s,min(B,s+mb)))).items() if k in []}) if False else model(slice_batch(b,list(range(s,min(B,s+mb))))['points'],slice_batch(b,list(range(s,min(B,s+mb))))['features'],slice_batch(b,list(range(s,min(B,s+mb))))['mask']).detach().cpu())
 return torch.cat(outs,0)
def groups_from_phase(rows,thr):
 A=[]; B=[]
 for r in rows:
  if r.get('true_label')!=SRC or fnum(r.get('particle0_iso_pt_ratio'))<thr: continue
  ei=int(fnum(r.get('event_index'),-1))
  if r.get('group')=='Hqql_correct': A.append(ei)
  elif r.get('group')=='Hqql_to_Tbl': B.append(ei)
 return sorted(set(A)),sorted(set(B))
def select_C(b,logits,n):
 y=b['y'].detach().cpu().long(); p=logits.argmax(1).long(); return [i for i in range(len(y)) if int(y[i])==TGT_ID and int(p[i])==TGT_ID][:n]
def capture(model,b,layers):
 caps={}; hooks=[]
 def mk(li):
  def hook(m,inp,out):
   x=out[0] if isinstance(out,(tuple,list)) else out; caps[li]=x.detach().float().cpu()
  return hook
 for li in layers: hooks.append(model.edge_convs[li].register_forward_hook(mk(li)))
 with torch.no_grad(): logits=model(b['points'],b['features'],b['mask']).detach().cpu()
 [h.remove() for h in hooks]; return logits,caps
def zero_logits(model,b,h):
 li,s,e=h['layer'],h['start'],h['end']
 def hook(m,inp,out):
  if isinstance(out,(tuple,list)):
   x=out[0].clone(); x[:,s:e,:]=0; return (x,)+tuple(out[1:])
  x=out.clone(); x[:,s:e,:]=0; return x
 hk=model.edge_convs[li].register_forward_hook(hook)
 with torch.no_grad(): z=model(b['points'],b['features'],b['mask']).detach().cpu()
 hk.remove(); return z
def heads_from_caps(caps,step=32):
 hs=[]
 for li,act in sorted(caps.items()):
  C=act.shape[1]
  for s in range(0,C,step): hs.append({'head_id':f'L{li}_ch{s}:{min(C,s+step)}','layer':li,'start':s,'end':min(C,s+step)})
 return hs
def convs(m): return [(n,x) for n,x in m.named_modules() if isinstance(x,(torch.nn.Conv1d,torch.nn.Conv2d))]
def source_blocks(model,h,block=32):
 cs=convs(model.edge_convs[h['layer']])
 if not cs: return {'exact_source_status':'FAILED','exact_source_note':'no Conv1d/Conv2d found'}
 name,cv=cs[-1]; W=cv.weight.detach().float().cpu()
 if W.dim()<2 or W.shape[0]<h['end']: return {'exact_source_status':'FAILED','exact_source_note':f'last conv {name} shape {tuple(W.shape)} incompatible'}
 M=W[h['start']:h['end']].reshape(h['end']-h['start'],W.shape[1],-1).norm(dim=(0,2))
 items=[]
 for s in range(0,len(M),block): items.append((s,min(len(M),s+block),float(M[s:min(len(M),s+block)].norm())))
 items=sorted(items,key=lambda x:x[2],reverse=True)[:5]
 r={'exact_source_status':'OK_IMMEDIATE_CONV_INPUT','exact_source_note':f'immediate source blocks from last conv {name}; not full nonlinear previous-layer composition'}
 for i,(s,e,v) in enumerate(items,1): r[f'source_block_{i}']=f'{s}:{e}'; r[f'source_block_weight_{i}']=v
 return r
def islep(F,b,p): return F.shape[1]>=11 and bool((F[b,9,p]>0.5) or (F[b,10,p]>0.5))
def ishad(F,b,p): return F.shape[1]>=8 and bool((F[b,6,p]>0.5) or (F[b,7,p]>0.5))
def ispho(F,b,p): return F.shape[1]>=9 and bool(F[b,8,p]>0.5)
def pid(F,b,p):
 if F.shape[1]<11: return 'no_pid'
 vals={'charged_hadron':float(F[b,6,p]),'neutral_hadron':float(F[b,7,p]),'photon':float(F[b,8,p]),'electron':float(F[b,9,p]),'muon':float(F[b,10,p])}; return max(vals.items(),key=lambda kv:kv[1])[0]
def roles(F,PT,M,b):
 valid=[j for j in range(PT.shape[1]) if bool(M[b,j])]; leps=sorted([j for j in valid if islep(F,b,j)],key=lambda j:float(PT[b,j]),reverse=True); hads=sorted([j for j in valid if ishad(F,b,j)],key=lambda j:float(PT[b,j]),reverse=True)
 best=leps[0] if leps else None; second=leps[1] if len(leps)>1 else None; hardest=hads[0] if hads else None; hp=[float(PT[b,j]) for j in hads]; thr=hp[int(.7*(len(hp)-1))] if hp else 0
 out={}
 for j in valid:
  if j==0 and best==j: r='particle0_best_lepton'
  elif j==0: r='particle0'
  elif best==j: r='best_lepton'
  elif second==j: r='second_lepton'
  elif hardest==j: r='hardest_hadron'
  elif ishad(F,b,j) and float(PT[b,j])>=thr: r='hard_hadron'
  elif ishad(F,b,j): r='hadron_neighbor'
  elif ispho(F,b,j): r='photon_neighbor'
  elif islep(F,b,j): r='other_lepton'
  else: r='other'
  out[j]=r
 return out
def agg(rows,keys,val):
 d=defaultdict(list)
 for r in rows: d[tuple(r[k] for k in keys)].append(fnum(r[val]))
 return {k:sum(v)/len(v) for k,v in d.items()}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--phase1-events',default='reports/latest/tables/hqql_tbl_confusion_physics_events.csv'); ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt'); ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced')); ap.add_argument('--mode',default='kinpid'); ap.add_argument('--samples-per-file',type=int,default=4096); ap.add_argument('--max-files',type=int,default=1000); ap.add_argument('--max-tbl-correct',type=int,default=128); ap.add_argument('--isolation-threshold',type=float,default=.30); ap.add_argument('--head-step',type=int,default=32); ap.add_argument('--top-particles',type=int,default=3); ap.add_argument('--max-graphs',type=int,default=200); ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu'); ap.add_argument('--out-dir',default='reports/latest/particle_flow_graphs_v2'); ap.add_argument('--out-md',default='reports/latest/MATRIX_PROGRAM_FULL_TRACE_V2.md'); ap.add_argument('--out-db',default='reports/latest/tables/matrix_program_database_v2.csv'); ap.add_argument('--out-flow',default='reports/latest/tables/matrix_program_particle_role_flow_v2.csv'); ap.add_argument('--out-trig',default='reports/latest/tables/top_confusion_triggers_v2.csv'); ap.add_argument('--out-loss',default='reports/latest/tables/top_hqql_loss_paths_v2.csv'); ap.add_argument('--out-anom',default='reports/latest/tables/top_anomalous_paths_v2.csv'); ap.add_argument('--out-json',default='manifests/latest/matrix_program_full_trace_v2.json'); a=ap.parse_args()
 phase=readcsv(a.phase1_events); A,B=groups_from_phase(phase,a.isolation_threshold); model,res=make_model(a.checkpoint,a.mode,a.device); batch=load_balanced(a.data_dir,mode=a.mode,samples_per_file=a.samples_per_file,max_files=a.max_files,device=a.device); C=select_C(batch,forward_logits(model,batch),a.max_tbl_correct); ids=A+B+C; groups=['A']*len(A)+['B']*len(B)+['C']*len(C); sub=slice_batch(batch,ids); logits,caps=capture(model,sub,list(range(len(model.edge_convs)))); heads=heads_from_caps(caps,a.head_step); F=sub['features'].detach().cpu(); PT=pt_values(sub).detach().cpu(); M=real_mask(sub).detach().cpu().bool(); role=[roles(F,PT,M,i) for i in range(len(ids))]
 zero={h['head_id']:zero_logits(model,sub,h) for h in heads}; db=[]; flow=[]
 for h in heads:
  hid=h['head_id']; act=caps[h['layer']][:,h['start']:h['end'],:]; ev=((act*M.float().unsqueeze(1)).sum(2)/M.float().sum(1).clamp_min(1).unsqueeze(1)); sb=source_blocks(model,h,a.head_step)
  vals=[]
  for bi in range(len(ids)):
   base=logits[bi]; z=zero[hid][bi]; sc=float(base[SRC_ID]-z[SRC_ID]); tc=float(base[TGT_ID]-z[TGT_ID]); vals.append((groups[bi],float(ev[bi].norm()),sc,tc))
   pn=act[bi].transpose(0,1).norm(dim=1); valid=torch.where(M[bi])[0]; top=torch.topk(pn[valid],min(a.top_particles,len(valid))).indices.tolist() if len(valid) else []
   for rel in top:
    pi=int(valid[rel]); rr=role[bi].get(pi,'other'); pnorm=float(pn[pi])
    for cls,w in [(SRC,sc),(TGT,tc)]: flow.append({'event_idx':ids[bi],'group':groups[bi],'particle_role':rr,'pid':pid(F,bi,pi),'particle_idx':pi,'head_id':hid,'class_label':cls,'particle_to_head_weight':pnorm,'head_to_class_weight':w,'flow_weight':pnorm*w})
  row={'head_id':hid,'layer':h['layer'],'channels':f"{h['start']}:{h['end']}",**sb}
  for g in 'ABC':
   xs=[x for x in vals if x[0]==g]; row[g+'_act_norm']=sum(x[1] for x in xs)/max(1,len(xs)); row[g+'_src_contrib']=sum(x[2] for x in xs)/max(1,len(xs)); row[g+'_tgt_contrib']=sum(x[3] for x in xs)/max(1,len(xs))
  row['B_minus_A_src']=row['B_src_contrib']-row['A_src_contrib']; row['B_minus_A_tgt']=row['B_tgt_contrib']-row['A_tgt_contrib']; db.append(row)
 vals=agg(flow,['particle_role','head_id','class_label','group'],'flow_weight'); paths=[]; keyset=set(k[:3] for k in vals)
 for role0,hid,cls in keyset:
  A0=vals.get((role0,hid,cls,'A'),0); B0=vals.get((role0,hid,cls,'B'),0); C0=vals.get((role0,hid,cls,'C'),0); row={'particle_role':role0,'head_id':hid,'class_label':cls,'A_flow':A0,'B_flow':B0,'C_flow':C0,'B_minus_A':B0-A0,'B_minus_C':B0-C0}
  row['trigger_score']=abs(B0-A0)/(1+abs(B0-C0)) if cls==TGT else 0; row['loss_score']=max(0,A0-B0) if cls==SRC else 0; row['anomaly_score']=abs(B0-A0)*abs(B0-C0); paths.append(row)
 trig=sorted([p for p in paths if p['class_label']==TGT],key=lambda r:r['trigger_score'],reverse=True); loss=sorted([p for p in paths if p['class_label']==SRC],key=lambda r:r['loss_score'],reverse=True); anom=sorted(paths,key=lambda r:r['anomaly_score'],reverse=True)
 for arr,d in [(trig,'trigger'),(loss,'loss'),(anom,'anomaly')]:
  for r in arr: r['auto_formulation']=f"PATH: {r['particle_role']} -> {r['head_id']} -> {r['class_label']}; DIAGNOSIS: {d}; B-A={fmt(r['B_minus_A'])}; B-C={fmt(r['B_minus_C'])}; NEXT_PROBE: inspect particle geometry/source blocks."
 gdir=Path(a.out_dir); gdir.mkdir(parents=True,exist_ok=True)
 byev=defaultdict(list)
 for r in flow: byev[r['event_idx']].append(r)
 for i,(ei,rs) in enumerate(byev.items()):
  if i>=a.max_graphs: break
  nodes={}; edges=[]; grp=next((r['group'] for r in rs),'')
  for r in sorted(rs,key=lambda x:abs(fnum(x['flow_weight'])),reverse=True)[:80]:
   pn=f"particle:{r['particle_idx']}:{r['particle_role']}"; hn=f"head:{r['head_id']}"; cn=f"class:{r['class_label']}"; nodes[pn]={'type':'particle','role':r['particle_role'],'pid':r['pid']}; nodes[hn]={'type':'head'}; nodes[cn]={'type':'class'}; edges += [{'source':pn,'target':hn,'weight':r['particle_to_head_weight']},{'source':hn,'target':cn,'weight':r['head_to_class_weight'],'flow_weight':r['flow_weight']}]
  wjson(gdir/f'particle_flow_graph_event_{ei}_group_{grp}.json',{'event_idx':ei,'group':grp,'nodes':nodes,'edges':edges})
 wcsv(a.out_db,db); wcsv(a.out_flow,flow); wcsv(a.out_trig,trig); wcsv(a.out_loss,loss); wcsv(a.out_anom,anom); wjson(a.out_json,{'ok':True,'A':len(A),'B':len(B),'C':len(C),'heads':len(heads),'graphs':min(len(byev),a.max_graphs),'source_exact_note':'exact immediate Conv input blocks only; full nonlinear composition impossible without symbolic EdgeConv decomposition','missing':list(res.missing_keys),'unexpected':list(res.unexpected_keys)})
 md=['# MATRIX_PROGRAM_FULL_TRACE_V2\n\n',f'- A={len(A)} B={len(B)} C={len(C)} heads={len(heads)} graphs={min(len(byev),a.max_graphs)}\n\n','## Top confusion triggers\n',mdtab(['role','head','class','A','B','C','score','formulation'],[[r['particle_role'],r['head_id'],r['class_label'],fmt(r['A_flow']),fmt(r['B_flow']),fmt(r['C_flow']),fmt(r['trigger_score']),r['auto_formulation']] for r in trig[:20]]),'\n## Top Hqql loss paths\n',mdtab(['role','head','class','A','B','C','score','formulation'],[[r['particle_role'],r['head_id'],r['class_label'],fmt(r['A_flow']),fmt(r['B_flow']),fmt(r['C_flow']),fmt(r['loss_score']),r['auto_formulation']] for r in loss[:20]]),'\n## Top anomalous paths\n',mdtab(['role','head','class','A','B','C','score','formulation'],[[r['particle_role'],r['head_id'],r['class_label'],fmt(r['A_flow']),fmt(r['B_flow']),fmt(r['C_flow']),fmt(r['anomaly_score']),r['auto_formulation']] for r in anom[:20]]),'\n## Source exactness\n\n`exact_source_status=OK_IMMEDIATE_CONV_INPUT` means exact immediate Conv input blocks inside EdgeConv. It is not a full nonlinear previous-layer symbolic decomposition.\n']
 Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8'); print(json.dumps({'ok':True,'heads':len(heads),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
