#!/usr/bin/env python3
import argparse,csv,json,math,sys,datetime
from pathlib import Path
from collections import defaultdict
import torch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.particlenet_real_patch_controls_v1 import load_balanced
from tools.particle0_topk_controls_v2 import make_model
from data.jetclass_tiny_loader_v3_official import LABELS

def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def loadjson(p):
    p=Path(p)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}
def wjson(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def slice_batch(batch,s,e):
    return {k:(v[s:e] if torch.is_tensor(v) and v.shape[0]>=e else v) for k,v in batch.items()}
def forward_micro(model,batch,mb,device):
    B=int(batch['y'].shape[0]); outs=[]
    with torch.no_grad():
        for s in range(0,B,mb):
            e=min(B,s+mb); b=slice_batch(batch,s,e)
            outs.append(model(b['points'],b['features'],b['mask']).detach().cpu())
            if str(device).startswith('cuda'): torch.cuda.empty_cache()
    return torch.cat(outs,0)
def status_for(rate,delta,count,args):
    if count < args.min_pair_count: return 'OK'
    if rate >= args.alert_rate or delta >= args.alert_delta: return 'ALERT'
    if rate >= args.watch_rate or delta >= args.watch_delta: return 'WATCH'
    return 'OK'
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--checkpoint',default='local_checkpoints/part/ParticleNet_kinpid.pt')
    ap.add_argument('--data-dir',default=str(Path.home()/'Рабочий стол/jetclass_tiny_balanced'))
    ap.add_argument('--mode',default='kinpid')
    ap.add_argument('--samples-per-file',type=int,default=1024)
    ap.add_argument('--max-files',type=int,default=100)
    ap.add_argument('--micro-batch',type=int,default=64)
    ap.add_argument('--device',default='cuda' if torch.cuda.is_available() else 'cpu')
    ap.add_argument('--baseline-json',default='manifests/latest/confusion_monitor_v1_baseline.json')
    ap.add_argument('--update-baseline',action='store_true')
    ap.add_argument('--watch-rate',type=float,default=0.02)
    ap.add_argument('--alert-rate',type=float,default=0.05)
    ap.add_argument('--watch-delta',type=float,default=0.01)
    ap.add_argument('--alert-delta',type=float,default=0.03)
    ap.add_argument('--min-pair-count',type=int,default=10)
    ap.add_argument('--out-md',default='reports/latest/CONFUSION_MONITOR_V1.md')
    ap.add_argument('--out-json',default='manifests/latest/confusion_monitor_v1.json')
    ap.add_argument('--out-pairs',default='reports/latest/tables/confusion_monitor_v1_pairs.csv')
    ap.add_argument('--out-matrix',default='reports/latest/tables/confusion_monitor_v1_matrix.csv')
    ap.add_argument('--out-signal-board',default='reports/latest/tables/signal_board_v1.csv')
    args=ap.parse_args()
    model,res=make_model(args.checkpoint,args.mode,args.device)
    batch=load_balanced(args.data_dir,mode=args.mode,samples_per_file=args.samples_per_file,max_files=args.max_files,device=args.device)
    logits=forward_micro(model,batch,max(1,args.micro_batch),args.device)
    y=batch['y'].detach().cpu().long(); pred=logits.argmax(1).long(); probs=torch.softmax(logits.float(),1)
    n=len(LABELS); mat=torch.zeros(n,n,dtype=torch.long)
    conf_sum=torch.zeros(n,n,dtype=torch.float64)
    for i in range(len(y)):
        a=int(y[i]); b=int(pred[i]); mat[a,b]+=1; conf_sum[a,b]+=float(probs[i,b])
    totals=mat.sum(1).clamp_min(1)
    baseline=loadjson(args.baseline_json)
    base_rates=baseline.get('pair_rates',{}) if isinstance(baseline,dict) else {}
    matrix_rows=[]
    for i,la in enumerate(LABELS):
        row={'true_label':la,'total':int(totals[i])}
        for j,lb in enumerate(LABELS): row[lb]=int(mat[i,j])
        matrix_rows.append(row)
    pair_rows=[]; signal_rows=[]
    for i,la in enumerate(LABELS):
        for j,lb in enumerate(LABELS):
            if i==j: continue
            count=int(mat[i,j]); true_total=int(totals[i]); rate=count/max(1,true_total)
            key=f'{la}->{lb}'; base=float(base_rates.get(key,0.0)); delta=rate-base
            mean_conf=float(conf_sum[i,j]/count) if count else 0.0
            status=status_for(rate,delta,count,args)
            score=rate*math.log1p(count)+max(0.0,delta)*10.0
            row={'class_pair':key,'true_label':la,'pred_label':lb,'count':count,'true_total':true_total,'confusion_rate':rate,'baseline_rate':base,'delta_vs_baseline':delta,'mean_pred_confidence':mean_conf,'score':score,'status':status}
            pair_rows.append(row)
            if status in ('WATCH','ALERT'):
                signal_rows.append({'signal_id':f'confusion::{key}','source':'CONFUSION_MONITOR_V1','class_pair':key,'status':status,'score':score,'reason':f'confusion_rate={rate:.4f}, delta={delta:.4f}, count={count}','recommended_next_action':'run feature ranker for this class pair','claim_level':0})
    pair_rows=sorted(pair_rows,key=lambda r:(r['status']!='ALERT',r['status']!='WATCH',-r['score']))
    signal_rows=sorted(signal_rows,key=lambda r:(r['status']!='ALERT',-r['score']))
    accuracy=float((pred==y).float().mean())
    pair_rates={r['class_pair']:r['confusion_rate'] for r in pair_rows}
    manifest={'schema':'confusion_monitor.v1','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'n_events':int(len(y)),'accuracy':accuracy,'labels':LABELS,'pair_rates':pair_rates,'signals':signal_rows,'settings':{'samples_per_file':args.samples_per_file,'max_files':args.max_files,'watch_rate':args.watch_rate,'alert_rate':args.alert_rate,'watch_delta':args.watch_delta,'alert_delta':args.alert_delta,'min_pair_count':args.min_pair_count},'model_missing':list(res.missing_keys),'model_unexpected':list(res.unexpected_keys)}
    wcsv(args.out_pairs,pair_rows); wcsv(args.out_matrix,matrix_rows); wcsv(args.out_signal_board,signal_rows); wjson(args.out_json,manifest)
    if args.update_baseline:
        wjson(args.baseline_json,manifest)
    top=signal_rows[:20]
    md=['# Confusion Monitor v1\n\nAutomatic stream monitor for class-pair confusion shifts. No LLM is used.\n\n',f'- events: **{len(y)}**\n',f'- accuracy: **{accuracy:.4f}**\n',f'- signals: **{len(signal_rows)}**\n',f'- baseline: `{args.baseline_json}`\n',f'- update_baseline: `{args.update_baseline}`\n\n','## Signal board\n',mdtab(['status','class_pair','score','reason','next'],[[r['status'],r['class_pair'],fmt(r['score']),r['reason'],r['recommended_next_action']] for r in top]),'\n## Top confusion pairs\n',mdtab(['status','pair','count','rate','baseline','delta','conf','score'],[[r['status'],r['class_pair'],r['count'],fmt(r['confusion_rate']),fmt(r['baseline_rate']),fmt(r['delta_vs_baseline']),fmt(r['mean_pred_confidence']),fmt(r['score'])] for r in pair_rows[:30]]),'\n## Interpretation\n\nWATCH/ALERT rows should be passed to the Feature Ranker. Deep probes should run only after a feature candidate passes contrastive/monotonic filters.\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True); Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'events':len(y),'accuracy':accuracy,'signals':len(signal_rows),'out_md':args.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
