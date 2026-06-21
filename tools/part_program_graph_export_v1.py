#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path
from collections import defaultdict, Counter


def f(x,d=0.0):
    try:
        if x is None or x=='': return d
        return float(x)
    except Exception: return d


def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'


def rcsv(p):
    p=Path(p)
    if not p.exists(): return []
    with p.open(newline='',encoding='utf-8') as h: return list(csv.DictReader(h))


def wcsv(p,rows):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    if not rows: p.write_text('',encoding='utf-8'); return
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with p.open('w',newline='',encoding='utf-8') as h:
        w=csv.DictWriter(h,fieldnames=keys); w.writeheader(); w.writerows(rows)


def wjson(p,obj):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')


def mdtab(headers,rows):
    if not rows: return '_No rows._\n'
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in r)+' |' for r in rows])+'\n'


def block_of_head(hid):
    if '.attn.h' in hid: return hid.split('.attn.h')[0]
    return ''


def node_id(kind,name):
    return kind+':'+str(name)


def add_node(nodes,kind,name,label=None,**attrs):
    nid=node_id(kind,name)
    if nid not in nodes:
        d={'id':nid,'kind':kind,'name':name,'label':label or name}; d.update(attrs); nodes[nid]=d
    else:
        nodes[nid].update({k:v for k,v in attrs.items() if v not in ('',None)})
    return nid


def add_edge(edges,src,dst,kind,weight=0.0,**attrs):
    e={'source':src,'target':dst,'kind':kind,'weight':weight}; e.update(attrs); edges.append(e)


def linear_weight(row):
    # New pair-atlas classifier decoder writes weight_tgt_minus_src.
    # Old Hqql/Tbl reports wrote weight_tbl_minus_hqql.
    if row.get('weight_tgt_minus_src','') not in ('', None):
        return f(row.get('weight_tgt_minus_src'))
    if row.get('weight_tbl_minus_hqql','') not in ('', None):
        return f(row.get('weight_tbl_minus_hqql'))
    if row.get('legacy_weight_tbl_minus_hqql','') not in ('', None):
        return f(row.get('legacy_weight_tbl_minus_hqql'))
    return 0.0


def linear_bias(row):
    if row.get('bias_tgt_minus_src','') not in ('', None): return row.get('bias_tgt_minus_src')
    if row.get('bias_tbl_minus_hqql','') not in ('', None): return row.get('bias_tbl_minus_hqql')
    if row.get('legacy_bias_tbl_minus_hqql','') not in ('', None): return row.get('legacy_bias_tbl_minus_hqql')
    return ''


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--validation',default='reports/latest/tables/part_candidate_pair_validation_balanced_v1_summary.csv')
    ap.add_argument('--discovery',default='reports/latest/tables/part_discovery_candidates_real_contract_v1.csv')
    ap.add_argument('--residual',default='reports/latest/tables/part_residual_path_trace_summary_v2.csv')
    ap.add_argument('--role-residual',default='reports/latest/tables/part_residual_path_trace_role_summary_v2.csv')
    ap.add_argument('--classifier',default='reports/latest/tables/part_classifier_logit_decoder_summary_v1.csv')
    ap.add_argument('--classifier-dims',default='reports/latest/tables/part_classifier_logit_decoder_dims_v1.csv')
    ap.add_argument('--linear',default='reports/latest/tables/part_classifier_logit_decoder_final_linear_v1.csv')
    ap.add_argument('--out-json',default='manifests/latest/part_program_graph_export_v1.json')
    ap.add_argument('--out-nodes',default='reports/latest/tables/part_program_graph_nodes_v1.csv')
    ap.add_argument('--out-edges',default='reports/latest/tables/part_program_graph_edges_v1.csv')
    ap.add_argument('--out-md',default='reports/latest/PART_PROGRAM_GRAPH_EXPORT_V1.md')
    a=ap.parse_args()

    val=rcsv(a.validation); disc=rcsv(a.discovery); res=rcsv(a.residual); role_res=rcsv(a.role_residual); clf=rcsv(a.classifier); dims=rcsv(a.classifier_dims); lin=rcsv(a.linear)
    nodes={}; edges=[]

    src_label = next((r.get('src_label') for r in lin if r.get('src_label')), 'label_Hqql')
    tgt_label = next((r.get('tgt_label') for r in lin if r.get('tgt_label')), 'label_Tbl')
    objective_name = f'{tgt_label}-{src_label}'

    # Core logit/objective node
    logit=add_node(nodes,'objective',objective_name,f'J={objective_name}')

    # classifier nodes and edges
    fc=add_node(nodes,'classifier','mod.fc','classifier head')
    add_edge(edges,fc,logit,'classifier_to_objective',1.0,formula='logits=fc(z)',src_label=src_label,tgt_label=tgt_label)
    for r in sorted(lin,key=lambda r:abs(linear_weight(r)),reverse=True)[:24]:
        dim='fc_dim_'+str(r.get('dim'))
        w=linear_weight(r)
        dn=add_node(nodes,'classifier_dim',dim,dim,W_tgt_minus_src=w,bias_tgt_minus_src=linear_bias(r),src_label=r.get('src_label',src_label),tgt_label=r.get('tgt_label',tgt_label))
        add_edge(edges,dn,fc,'linear_direction',w,dim=r.get('dim'),src_label=r.get('src_label',src_label),tgt_label=r.get('tgt_label',tgt_label))

    # residual nodes -> classifier
    for r in sorted(res,key=lambda r:abs(f(r.get('mean_score')))+0.25*f(r.get('mean_abs_score')),reverse=True)[:60]:
        name=r.get('module'); n=add_node(nodes,'residual_'+r.get('kind','block'),name,name,kind2=r.get('kind'),top_group=r.get('analysis_group'))
        add_edge(edges,n,fc,'residual_to_classifier',f(r.get('mean_score')),objective=r.get('objective'),group=r.get('analysis_group'),mean_abs=r.get('mean_abs_score'))

    # validated attention pair nodes -> residual block nodes
    valid=[]
    for r in val:
        ok=f(r.get('direction_ok_runs'))>0
        strength=abs(f(r.get('best_B_delta_margin')))+2*abs(f(r.get('best_B_delta_tbl_pred')))
        if ok and strength>0: valid.append(r)
    valid=sorted(valid,key=lambda r:f(r.get('score')),reverse=True)
    for r in valid[:80]:
        hid=r.get('head_id'); pair=r.get('pair_role'); b=block_of_head(hid)
        pn=add_node(nodes,'attention_pair',hid+'|'+pair,hid+' '+pair,diagnosis=r.get('diagnosis'),B_write=r.get('B_write'),B_AxGrad=r.get('B_AxGrad'))
        rn=add_node(nodes,'residual_block',b,b)
        add_edge(edges,pn,rn,'validated_pair_to_residual',f(r.get('best_B_delta_margin')),B_flip=r.get('best_B_delta_tbl_pred'),action=r.get('action'),rules=r.get('rules'),score=r.get('score'))

    # role residual nodes attach to residual blocks
    for r in sorted(role_res,key=lambda r:abs(f(r.get('mean_score')))+0.2*f(r.get('mean_abs_score')),reverse=True)[:80]:
        role_id=r.get('module')+'|'+r.get('role')+'|'+r.get('analysis_group')
        rn=add_node(nodes,'residual_role',role_id,r.get('module')+' '+r.get('role'),role=r.get('role'),group=r.get('analysis_group'))
        bn=add_node(nodes,'residual_block',r.get('module'),r.get('module'))
        add_edge(edges,rn,bn,'role_to_residual',f(r.get('mean_score')),objective=r.get('objective'),group=r.get('analysis_group'))

    # classifier dimensions that matter for B
    for r in sorted([x for x in dims if x.get('analysis_group')=='B_Hqql_to_Tbl'],key=lambda r:abs(f(r.get('mean_contrib')))+0.2*f(r.get('mean_abs_contrib')),reverse=True)[:40]:
        dn=add_node(nodes,'classifier_activation_dim','fc_input_dim_'+str(r.get('dim')),'fc input dim '+str(r.get('dim')),activation=r.get('mean_activation'),grad=r.get('mean_grad'))
        add_edge(edges,fc,dn,'classifier_dim_observed',f(r.get('mean_contrib')),group='B_Hqql_to_Tbl',tensor=r.get('tensor'))

    node_rows=list(nodes.values())
    wcsv(a.out_nodes,node_rows); wcsv(a.out_edges,edges)
    bykind=Counter(n['kind'] for n in node_rows); byedge=Counter(e['kind'] for e in edges)
    obj={'ok':True,'nodes':len(node_rows),'edges':len(edges),'src_label':src_label,'tgt_label':tgt_label,'node_kinds':dict(bykind),'edge_kinds':dict(byedge),'top_validated_pairs':valid[:20]}
    wjson(a.out_json,obj)
    lines=['# PART_PROGRAM_GRAPH_EXPORT_V1\n\nMachine-readable program graph skeleton assembled from validated pair mechanisms, residual path v2, and classifier-logit decoder. This does not rerun the model; it joins existing evidence into nodes and edges.\n\n',f'- nodes: **{len(node_rows)}**\n',f'- edges: **{len(edges)}**\n',f'- src_label: `{src_label}`\n',f'- tgt_label: `{tgt_label}`\n',f'- node_kinds: `{dict(bykind)}`\n',f'- edge_kinds: `{dict(byedge)}`\n\n','## Top validated pair → residual edges\n']
    pe=[e for e in edges if e['kind']=='validated_pair_to_residual'][:40]
    lines.append(mdtab(['rank','source','target','weight/B_delta','B_flip','action','rules','score'],[[i+1,e['source'],e['target'],fmt(e['weight']),fmt(e.get('B_flip')),e.get('action'),e.get('rules'),fmt(e.get('score'))] for i,e in enumerate(pe)]))
    lines.append('\n## Top residual → classifier edges\n')
    re=[e for e in sorted([x for x in edges if x['kind']=='residual_to_classifier'],key=lambda x:abs(f(x.get('weight'))),reverse=True)[:40]]
    lines.append(mdtab(['rank','source','target','weight','objective','group'],[[i+1,e['source'],e['target'],fmt(e['weight']),e.get('objective'),e.get('group')] for i,e in enumerate(re)]))
    lines.append('\n## Top classifier linear directions\n')
    le=sorted([e for e in edges if e['kind']=='linear_direction'],key=lambda x:abs(f(x.get('weight'))),reverse=True)[:24]
    lines.append(mdtab(['rank','source','target','W_tgt-src','dim','src','tgt'],[[i+1,e['source'],e['target'],fmt(e['weight']),e.get('dim'),e.get('src_label'),e.get('tgt_label')] for i,e in enumerate(le)]))
    lines.append('\n## Graph formula\n\n```text\nattention_pair(h, q<-k) --validated_pair_to_residual--> residual_block\nresidual_block --residual_to_classifier--> classifier(fc)\nclassifier_dim --linear_direction--> classifier --classifier_to_objective--> J=tgt-src\nedge weights are signed causal/gradient/path contributions.\n```\n')
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(lines),encoding='utf-8')
    print(json.dumps({'ok':True,'nodes':len(node_rows),'edges':len(edges),'src_label':src_label,'tgt_label':tgt_label,'out_md':a.out_md},indent=2))
if __name__=='__main__': main()
