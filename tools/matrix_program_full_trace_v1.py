#!/usr/bin/env python3
import argparse,csv,json,math
from pathlib import Path
from collections import defaultdict

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows: wr.writerow({k:r.get(k,'') for k in keys})
def wjson(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def fnum(x,d=0.0):
    try:
        v=float(x); return v if math.isfinite(v) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def mdtab(h,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']
    out += ['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rows]
    return '\n'.join(out)+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--events',default='reports/latest/tables/internal_activation_contrast_v2_events.csv')
    ap.add_argument('--particles',default='reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv')
    ap.add_argument('--head-summary',default='reports/latest/tables/internal_activation_contrast_v2_head_summary.csv')
    ap.add_argument('--source-class',default='label_Hqql')
    ap.add_argument('--target-class',default='label_Tbl')
    ap.add_argument('--out-md',default='reports/latest/MATRIX_PROGRAM_FULL_TRACE_V1.md')
    ap.add_argument('--out-db',default='reports/latest/tables/matrix_program_database_v1.csv')
    ap.add_argument('--out-flow',default='reports/latest/tables/matrix_program_particle_role_flow_v1.csv')
    ap.add_argument('--out-paths',default='reports/latest/tables/matrix_program_paths_v1.csv')
    ap.add_argument('--out-json',default='manifests/latest/matrix_program_full_trace_v1.json')
    a=ap.parse_args()
    ev=readcsv(a.events); pr=readcsv(a.particles); hs=readcsv(a.head_summary)
    if not ev or not pr: raise RuntimeError('Need V2 events and V2.1 annotated particles first')
    ekey={(r['event_idx'],r['group'],r['head_id']):r for r in ev}
    flow=[]
    for r in pr:
        k=(r['event_idx'],r['group'],r['head_id']); e=ekey.get(k)
        if not e: continue
        p2h=fnum(r.get('particle_activation_norm'))
        for cls,col in [(a.source_class,'contrib_hqql_logit_drop_when_zeroed'),(a.target_class,'contrib_tbl_logit_drop_when_zeroed')]:
            h2c=fnum(e.get(col))
            flow.append({'event_idx':r['event_idx'],'group':r['group'],'particle_role':r.get('particle_role',''),
                         'pid':r.get('pid',''),'particle_idx':r.get('particle_idx',''),'head_id':r['head_id'],
                         'layer':r['head_id'].split('_')[0],'class_label':cls,
                         'particle_to_head_weight':p2h,'head_to_class_weight':h2c,'flow_weight':p2h*h2c})
    by=defaultdict(list)
    for r in flow: by[(r['particle_role'],r['head_id'],r['class_label'],r['group'])].append(r)
    paths=[]; keys=set((role,hid,cls) for role,hid,cls,g in by)
    for role,hid,cls in keys:
        row={'particle_role':role,'head_id':hid,'class_label':cls}
        for p,g in [('A','A_protected_highiso'),('B','B_confused_highiso'),('C','C_Tbl_correct')]:
            xs=by.get((role,hid,cls,g),[]); row[p+'_n']=len(xs); row[p+'_flow']=sum(fnum(x['flow_weight']) for x in xs)/max(1,len(xs))
        row['B_minus_A']=row['B_flow']-row['A_flow']; row['B_minus_C']=row['B_flow']-row['C_flow']
        row['trigger_score']=abs(row['B_minus_A'])/(1.0+abs(row['B_minus_C'])) if cls==a.target_class else 0.0
        row['loss_score']=max(0.0,row['A_flow']-row['B_flow']) if cls==a.source_class else 0.0
        row['anomaly_score']=abs(row['B_minus_A'])*abs(row['B_minus_C'])
        if row['trigger_score']>0.1 and abs(row['B_minus_C'])<abs(row['B_minus_A']): d='target_like_trigger_candidate'
        elif row['loss_score']>0.1: d='source_evidence_loss_candidate'
        elif row['anomaly_score']>0.1: d='anomalous_third_topology_candidate'
        else: d='weak_or_unclear'
        row['diagnosis']=d; paths.append(row)
    paths=sorted(paths,key=lambda r:max(r['trigger_score'],r['loss_score'],r['anomaly_score']),reverse=True)
    # Head database = V2 summary plus most common particle roles.
    role_by_head=defaultdict(lambda:defaultdict(int))
    for r in pr: role_by_head[r['head_id']][r.get('particle_role','')]+=1
    db=[]
    for r in hs:
        roles=sorted(role_by_head[r['head_id']].items(),key=lambda kv:kv[1],reverse=True)[:5]
        rr=dict(r); rr['matrix_program_role']='auto_from_V2_activation_and_ablation'; rr['top_particle_roles']=';'.join(f'{k}:{v}' for k,v in roles)
        db.append(rr)
    wcsv(a.out_flow,flow); wcsv(a.out_paths,paths); wcsv(a.out_db,db)
    wjson(a.out_json,{'ok':True,'events_rows':len(ev),'particle_rows':len(pr),'paths':len(paths),'note':'V1 postprocesses V2/V2.1 outputs. Run V2 with HEADS=all for all pseudo-heads.'})
    md=['# MATRIX_PROGRAM_FULL_TRACE_V1\n\n','Postprocessor over INTERNAL_ACTIVATION_CONTRAST_V2/V2_1. It builds particle_role -> head -> class paths from top-particle activation and zero-slice class contribution.\n\n','## Top path mechanisms\n',mdtab(['diag','role','head','class','A','B','C','B-A','B-C','trigger','loss','anomaly'],[[r['diagnosis'],r['particle_role'],r['head_id'],r['class_label'],fmt(r['A_flow']),fmt(r['B_flow']),fmt(r['C_flow']),fmt(r['B_minus_A']),fmt(r['B_minus_C']),fmt(r['trigger_score']),fmt(r['loss_score']),fmt(r['anomaly_score'])] for r in paths[:50]]),'\n## Top head programs\n',mdtab(['head','diag','B_close_C','B-A source','B-A target','roles'],[[r.get('head_id',''),r.get('diagnosis',''),fmt(r.get('B_closer_to_C_score','')),fmt(r.get('B_minus_A_hqql_contrib_drop','')),fmt(r.get('B_minus_A_tbl_contrib_drop','')),r.get('top_particle_roles','')] for r in db[:40]]),'\n## Note\n\nThis V1 uses existing V2/V2.1 tables. To make it truly all-head, run V2 with a full HEADS list, then rerun this postprocessor. Exact EdgeConv source-block weight decomposition is reserved for V2 after module parsing is validated.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'paths':len(paths),'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
