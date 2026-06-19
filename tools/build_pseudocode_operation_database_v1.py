#!/usr/bin/env python3
import argparse,csv,json,re
from pathlib import Path
from datetime import datetime,timezone

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def loadjson(p):
    p=Path(p)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}
def fnum(x,d=0.0):
    try: return float(x) if x not in ('',None) else d
    except Exception: return d
def fmt(x):
    try: return f'{float(x):.4f}'
    except Exception: return 'n/a'
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
def wjsonl(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
def wjson(p,o): p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,ensure_ascii=False),encoding='utf-8')
def mdtab(h,rs):
    if not rs: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |' for r in rs])+'\n'
def parse(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)',h or '')
    return tuple(map(int,m.groups())) if m else None

def stage(l): return {0:'L0 early local reader',1:'L1 middle context relay',2:'L2 late readout'}.get(l,'unknown')
def pre(l):
    return ['raw particles + KNN edge coordinates','L0 local edge features already mixed','L1 context and class-route evidence already mixed'][l] if l in (0,1,2) else 'unknown'
def axis(text):
    if 'Hqql' in text and 'Tbl' in text: return 'Hqql/Tbl core-confusion axis'
    if 'Wqq' in text or 'Zqq' in text: return 'W/Z structured-prong axis'
    if 'H4q' in text: return 'H4q multi-prong attractor axis'
    if 'Tbl' in text: return 'Tbl leading-core axis'
    if 'Hqql' in text: return 'Hqql compact-core axis'
    if 'QCD' in text: return 'QCD/background axis'
    return 'shared class-evidence axis'
def reads(l):
    return ['pt/energy, deltaR, PID/charge, neighbor edge differences','L0 local features, top-k core, neighbor context, wide particles','L1 context, class-evidence summaries, core/secondary competition'][l] if l in (0,1,2) else 'unknown'
def steps(l):
    return ['build KNN edge features -> detect local core/radial/PID pattern -> write local evidence','read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence','read L1 context -> aggregate class evidence -> write classifier support/competition'][l] if l in (0,1,2) else 'unknown'
def writes(l):
    return ['local particle-edge features for L1','core+context vectors for L2','class evidence and class-competition support'][l] if l in (0,1,2) else 'unknown'
def code(h,l,a):
    if l==0: return f"# {h}\nfor particle i:\n    nb = knn(i)\n    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))\n    write_local(local, axis='{a}')"
    if l==1: return f"# {h}\nfor neighborhood i:\n    local = read_L0(i)\n    context = mix(topk_core(i), neighbors(i), secondary_context(i))\n    write_context(context, axis='{a}')"
    return f"# {h}\nfor event:\n    context = collect_L1_context()\n    evidence = aggregate(context, axis='{a}')\n    write_class_evidence(evidence)"
def conf(g,c,e):
    s=(2 if g>=0.5 else 1 if g>=0.2 else 0)+(2 if c>=1 else 1 if c>=0.4 else 0)+(1 if e else 0)
    return 'HIGH_CANDIDATE' if s>=4 else 'MEDIUM_CANDIDATE' if s>=2 else 'LOW_NEEDS_MORE_EVIDENCE'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--atlas',default='reports/latest/tables/operation_logic_atlas.csv')
    ap.add_argument('--class-grads',default='reports/latest/tables/class_specific_head_gradients.csv')
    ap.add_argument('--head-vectors',default='reports/latest/tables/evidence_head_vectors.csv')
    ap.add_argument('--residual',default='manifests/latest/known_observable_residual_v1.json')
    ap.add_argument('--out-csv',default='reports/latest/tables/pseudocode_operation_database.csv')
    ap.add_argument('--out-jsonl',default='reports/latest/tables/pseudocode_operation_database.jsonl')
    ap.add_argument('--out-json',default='manifests/latest/pseudocode_operation_database_v1.json')
    ap.add_argument('--out-md',default='reports/latest/PSEUDOCODE_OPERATION_DATABASE_V1.md')
    a=ap.parse_args(); atlas=readcsv(a.atlas); grads=readcsv(a.class_grads); heads=readcsv(a.head_vectors); residual=loadjson(a.residual)
    rows=[]
    for r in atlas:
        h=r.get('head_id',''); p=parse(h)
        if not p: continue
        l,ch0,ch1=p; hg=sorted([x for x in grads if x.get('head_id')==h],key=lambda x:fnum(x.get('abs_grad')),reverse=True); hv=next((x for x in heads if x.get('head_id')==h),{})
        txt=json.dumps(r,ensure_ascii=False)+json.dumps(hg[:5],ensure_ascii=False); ax=axis(txt); g=fnum(hv.get('gate_abs_grad')); c=fnum(hg[0].get('abs_grad')) if hg else 0.0
        top=', '.join([x.get('class_label','')+':'+fmt(x.get('abs_grad')) for x in hg[:5]])
        rows.append({'head_id':h,'layer':l,'channels':f'{ch0}:{ch1}','stage_role':stage(l),'pre_layer_state':pre(l),'reads':reads(l),'core_operation_steps':steps(l),'writes':writes(l),'class_axis':ax,'particle_interpretation':'core/top-k content with KNN/secondary context; not literal order index','physics_interpretation':ax+'; residual remains' if residual.get('status')=='RESIDUAL_SIGNAL_REMAINS' else ax,'pseudocode':code(h,l,ax),'supporting_evidence':r.get('evidence_sources','')+' | class_grads='+top,'global_gate_abs':g,'top_class_abs_grad':c,'confidence_level':conf(g,c,top),'remaining_risks':'semantic pseudocode; needs route trace, residual v2, heldout/cross-model','next_tests':'route-neighbor trace; head-pair synergy; per-file heldout; residual v2'})
    rows=sorted(rows,key=lambda x:(x['layer'],-x['top_class_abs_grad'],x['head_id']))
    wcsv(a.out_csv,rows); wjsonl(a.out_jsonl,rows); wjson(a.out_json,{'schema':'pseudocode_operation_database.v1','generated_at_utc':datetime.now(timezone.utc).isoformat(),'rows':len(rows),'residual_status':residual.get('status')})
    md=['# Pseudocode Operation Database v1\n\nFull semantic pseudocode database: one row per pseudo-head/channel group.\n\n','## Top candidates\n',mdtab(['head','stage','axis','confidence','gate','class_grad'],[[r['head_id'],r['stage_role'],r['class_axis'],r['confidence_level'],fmt(r['global_gate_abs']),fmt(r['top_class_abs_grad'])] for r in rows[:30]]),'\n## Full pseudocode\n']
    for r in rows:
        md += [f"\n### {r['head_id']} — {r['stage_role']}\n\n",f"Pre-layer state: {r['pre_layer_state']}\n\nReads: {r['reads']}\n\nSteps: {r['core_operation_steps']}\n\nWrites: {r['writes']}\n\nAxis: {r['class_axis']}\n\n```python\n{r['pseudocode']}\n```\n\nEvidence: {r['supporting_evidence']}\n\nConfidence: {r['confidence_level']}\n\nRisks: {r['remaining_risks']}\n\nNext: {r['next_tests']}\n"]
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
