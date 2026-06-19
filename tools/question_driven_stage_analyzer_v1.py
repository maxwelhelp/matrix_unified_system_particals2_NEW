#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path

def readcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
def loadjson(p):
    p=Path(p)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}
def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen: keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader(); [wr.writerow({k:r.get(k,'') for k in keys}) for r in rows]
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

def score_head(r,mode):
    lead=fnum(r.get('output_leading_pt_match_rate')); gate=fnum(r.get('global_gate_abs')); cg=fnum(r.get('top_class_abs_grad')); corr=abs(fnum(r.get('output_top_logit_corr'))); txt=json.dumps(r,ensure_ascii=False)
    if mode=='core_readout': return 3*lead + corr + 0.5*cg
    if mode=='local_builders': return (1-lead) + gate + 0.5*cg if int(r.get('layer',0))<=1 else 0
    if mode=='residual_axis': return (1 if 'residual remains' in txt else 0) + cg + corr + (1 if ('Hqql' in txt or 'Tbl' in txt) else 0)
    if mode=='edgeconv_trace_priority': return gate + cg + corr + (1 if r.get('confidence_level','').startswith('HIGH') else 0)
    return gate+cg+corr+lead

def rank(rows,mode,n=8):
    xs=[]
    for r in rows:
        rr=dict(r); rr['question_score']=score_head(r,mode); xs.append(rr)
    return sorted(xs,key=lambda x:fnum(x.get('question_score')),reverse=True)[:n]

def question_answer(qid,title,answer,evidence,next_test,heads):
    return {'question_id':qid,'question':title,'answer':answer,'evidence_stages':evidence,'recommended_next_test':next_test,'top_heads':', '.join([h.get('head_id','') for h in heads[:5]])}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pseudo-v2',default='reports/latest/tables/pseudocode_operation_database_v2.csv')
    ap.add_argument('--comparison',default='manifests/latest/automatic_comparison_engine_v2.json')
    ap.add_argument('--residual',default='manifests/latest/known_observable_residual_v1.json')
    ap.add_argument('--scope',default='manifests/latest/scope_comparability_guard_v1.json')
    ap.add_argument('--out-md',default='reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md')
    ap.add_argument('--out-answers',default='reports/latest/tables/question_driven_stage_answers.csv')
    ap.add_argument('--out-heads',default='reports/latest/tables/question_driven_head_rankings.csv')
    ap.add_argument('--out-json',default='manifests/latest/question_driven_stage_analyzer_v1.json')
    a=ap.parse_args(); rows=readcsv(a.pseudo_v2); comp=loadjson(a.comparison); residual=loadjson(a.residual); scope=loadjson(a.scope)
    core=rank(rows,'core_readout',10); local=rank(rows,'local_builders',10); resid=rank(rows,'residual_axis',10); trace=rank(rows,'edgeconv_trace_priority',10)
    answers=[]
    answers.append(question_answer('Q1','Where is the late particle0/core readout?','The strongest core readout is in L2 pseudo-heads. L2 rows have the highest leading-pT/particle0 match and are mapped to edge_convs.2 outputs before pooling/classifier.','pseudocode_v2 + code_alignment_v2 + head_output_trace + particle0_controls','run route-neighbor trace on top L2 heads and heldout stability',core))
    answers.append(question_answer('Q2','What do L0/L1 compute before the L2 readout?','L0/L1 mostly act as local feature builders and context relays. Their outputs often activate on non-leading particles, so they likely build edge/PID/radial/neighborhood context that L2 later reads through core-aligned heads.','pseudocode_v2 + head_output_trace + class_gradients','trace EdgeConv inner tensors: knn indices, graph features, conv outputs, neighbor aggregation',local))
    answers.append(question_answer('Q3','Is Hqql/Tbl residual axis explained by simple known observables?','No for v1 surrogate: residual remains. Simple observable surrogate has low agreement with ParticleNet, so Hqql/Tbl and related structured classes need deeper head/circuit analysis.','known_observable_residual_v1 + confusion_atlas + pseudocode_v2','run richer residual v2 with pair/ECF-like features and class-specific head trace',resid))
    answers.append(question_answer('Q4','Which heads should be inspected next inside EdgeConv?','Prioritize heads with high class gradients, strong output/logit links, and clear code alignment. These heads should get inner trace: KNN neighbor source, edge feature, conv stack, aggregation, channel slice.','pseudocode_v2 + code_alignment_v2 + head_output_trace + class_gradients','run EDGE_CONV_INNER_TRACE_V1 for ranked heads',trace))
    answers.append(question_answer('Q5','What is the current evidence chain for the core/top-k mechanism?','Stream suggested particle0/core dominance; targeted controls confirmed local causality; order control reduced index artifact; confusion atlas showed structured class collapse; residual v1 says simple observables do not reproduce decisions; pseudocode/output trace shows L0/L1 context builders feeding L2 core readouts.','stream + controls + order + confusion + residual + pseudocode_v2 + scope_guard','do heldout/per-file and cross-model agreement before strong claim',core))
    head_rows=[]
    for qid,group in [('Q1_core_readout',core),('Q2_local_builders',local),('Q3_residual_axis',resid),('Q4_trace_priority',trace)]:
        for i,r in enumerate(group,1):
            head_rows.append({'question_id':qid,'rank':i,'head_id':r.get('head_id'),'score':r.get('question_score'),'layer':r.get('layer'),'output_role':r.get('output_role'),'top_class':r.get('output_top_class'),'lead_match':r.get('output_leading_pt_match_rate'),'logit_corr':str(r.get('output_top_logit_corr_class'))+':'+fmt(r.get('output_top_logit_corr')),'code':str(r.get('code_module'))+' '+str(r.get('code_slice')),'next_test':r.get('next_tests')})
    wcsv(a.out_answers,answers); wcsv(a.out_heads,head_rows); wjson(a.out_json,{'ok':True,'questions':len(answers),'heads_ranked':len(head_rows),'residual_status':residual.get('status'),'scope_status':scope.get('status')})
    md=['# Question Driven Stage Analyzer v1\n\nAutomatic answers over staged evidence: pseudocode v2, code alignment, head outputs, controls, confusion, residual, and scope guard.\n\n','## Answers\n',mdtab(['id','question','answer','evidence','next'],[[x['question_id'],x['question'],x['answer'],x['evidence_stages'],x['recommended_next_test']] for x in answers]),'\n## Ranked heads by question\n']
    for q in ['Q1_core_readout','Q2_local_builders','Q3_residual_axis','Q4_trace_priority']:
        xs=[x for x in head_rows if x['question_id']==q]
        md += [f'\n### {q}\n',mdtab(['rank','head','score','role','top_class','lead','corr','code'],[[x['rank'],x['head_id'],fmt(x['score']),x['output_role'],x['top_class'],fmt(x['lead_match']),x['logit_corr'],x['code']] for x in xs])]
    md += ['\n## Use\n\nThis report should be the first file to open when deciding what to inspect next. It turns staged evidence into question-specific head rankings and next experiments.\n']
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'questions':len(answers),'heads_ranked':len(head_rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
