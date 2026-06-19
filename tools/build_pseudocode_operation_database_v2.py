#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path

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
def wjsonl(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
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
def output_role(layer,p0,lead,corr,topcls):
    if layer==0:
        if lead>0.20: return 'early local reader with partial leading-core sensitivity'
        return 'early local/context feature builder over non-leading neighbor particles'
    if layer==1:
        if lead>0.20: return 'middle relay mixing context with some core alignment'
        return 'middle context relay mostly away from literal leading particle'
    if lead>0.50: return 'late readout strongly anchored on particle0/leading-pT core'
    if lead>0.25: return 'late readout moderately core-aligned'
    return 'late readout with distributed/non-core particle evidence'
def refined_code(r,o):
    h=r.get('head_id'); layer=int(r.get('layer',0)); role=o.get('output_role',''); top=o.get('top_activation_class','')
    p0=fnum(o.get('particle0_top_rate')); lead=fnum(o.get('top_activation_matches_leading_pt_rate'))
    if layer==0:
        return f"# {h}: L0 output-aware pseudocode\nfor particle i:\n    nb = knn(i)\n    local = read_raw_edge_features(i, nb)\n    score = detect_local_pattern(local)\n    write_L0_channels(score)  # output role: {role}; top_class={top}; lead_match={lead:.2f}"
    if layer==1:
        return f"# {h}: L1 output-aware pseudocode\nfor particle/neighborhood i:\n    l0 = read_L0_local_features(i)\n    ctx = mix_neighbors_core_and_secondary(l0)\n    write_L1_context(ctx)  # output role: {role}; particle0_top={p0:.2f}; top_class={top}"
    return f"# {h}: L2 output-aware pseudocode\nfor event:\n    ctx = collect_L1_context()\n    evidence = aggregate_class_evidence(ctx)\n    if top_particle_is_core_or_particle0(rate={lead:.2f}):\n        logits += project_core_readout(evidence)\n    # output role: {role}; top_class={top}; corr={o.get('top_logit_corr_class','')}:{fmt(o.get('top_logit_corr'))}"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pseudo',default='reports/latest/tables/pseudocode_operation_database.csv')
    ap.add_argument('--trace',default='reports/latest/tables/head_output_trace.csv')
    ap.add_argument('--align',default='reports/latest/tables/layer_code_alignment_v2.csv')
    ap.add_argument('--out-csv',default='reports/latest/tables/pseudocode_operation_database_v2.csv')
    ap.add_argument('--out-jsonl',default='reports/latest/tables/pseudocode_operation_database_v2.jsonl')
    ap.add_argument('--out-json',default='manifests/latest/pseudocode_operation_database_v2.json')
    ap.add_argument('--out-md',default='reports/latest/PSEUDOCODE_OPERATION_DATABASE_V2.md')
    a=ap.parse_args(); pseudo=readcsv(a.pseudo); trace={r.get('head_id'):r for r in readcsv(a.trace)}; align={r.get('head_id'):r for r in readcsv(a.align)}
    rows=[]
    for r in pseudo:
        h=r.get('head_id',''); tr=trace.get(h,{}); al=align.get(h,{})
        layer=int(r.get('layer',0)); p0=fnum(tr.get('particle0_top_rate')); lead=fnum(tr.get('top_activation_matches_leading_pt_rate')); corr=fnum(tr.get('top_logit_corr'))
        outrole=output_role(layer,p0,lead,corr,tr.get('top_activation_class',''))
        rr=dict(r); rr.update({'code_module':al.get('module_path',''),'code_slice':al.get('channel_slice',''),'code_output_shape':al.get('output_shape',''),'output_activation_mean_abs':tr.get('activation_mean_abs',''),'output_top_class':tr.get('top_activation_class',''),'output_class_contrast':tr.get('class_activation_contrast',''),'output_particle0_top_rate':p0,'output_leading_pt_match_rate':lead,'output_top_logit_corr_class':tr.get('top_logit_corr_class',''),'output_top_logit_corr':corr,'output_role':outrole,'output_interpretation':tr.get('output_interpretation',''),'refined_pseudocode':refined_code(r,dict(tr,output_role=outrole))})
        rows.append(rr)
    rows=sorted(rows,key=lambda x:(int(x.get('layer',0)),-fnum(x.get('output_leading_pt_match_rate')),-fnum(x.get('output_activation_mean_abs'))))
    wcsv(a.out_csv,rows); wjsonl(a.out_jsonl,rows); wjson(a.out_json,{'ok':True,'rows':len(rows),'note':'v2 merges semantic pseudocode + code alignment v2 + head output trace'})
    md=['# Pseudocode Operation Database v2\n\nThis version merges semantic pseudocode with corrected code alignment and actual pseudo-head output trace.\n\n','## Top output-aware rows\n',mdtab(['head','module','slice','output_role','top_class','lead_match','logit_corr'],[[r['head_id'],r.get('code_module',''),r.get('code_slice',''),r.get('output_role',''),r.get('output_top_class',''),fmt(r.get('output_leading_pt_match_rate')),str(r.get('output_top_logit_corr_class',''))+':'+fmt(r.get('output_top_logit_corr'))] for r in rows[:40]]),'\n## Full refined pseudocode\n']
    for r in rows:
        md += [f"\n### {r['head_id']} — {r.get('stage_role','')}\n\n",f"Code: `{r.get('code_module','')}` / `{r.get('code_slice','')}` / shape `{r.get('code_output_shape','')}`\n\n",f"Output role: **{r.get('output_role','')}**\n\n",f"Output: top_class={r.get('output_top_class','')}, particle0_top={fmt(r.get('output_particle0_top_rate'))}, lead_match={fmt(r.get('output_leading_pt_match_rate'))}, logit_corr={r.get('output_top_logit_corr_class','')}:{fmt(r.get('output_top_logit_corr'))}\n\n",'```python\n'+r.get('refined_pseudocode','')+'\n```\n\n',f"Evidence: {r.get('supporting_evidence','')}\n\nRisks: {r.get('remaining_risks','')}\n"]
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
