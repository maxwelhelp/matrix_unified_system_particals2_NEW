#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path
from collections import Counter,defaultdict

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
def route_stats(events):
    if not events: return {}
    n=len(events); top0=sum(int(fnum(e.get('top_is_particle0'))) for e in events); toplead=sum(int(fnum(e.get('top_is_leading_pt'))) for e in events)
    labels=Counter(e.get('true_label','') for e in events); preds=Counter(e.get('pred_label','') for e in events)
    knn_has0=0; knn_haslead=0; neigh_first=[]
    for e in events:
        try: nb=json.loads(e.get('knn_neighbors_of_top_particle','[]'))
        except Exception: nb=[]
        if 0 in nb: knn_has0 += 1
        lead=int(fnum(e.get('leading_pt_particle'),-999))
        if lead in nb: knn_haslead += 1
        if nb: neigh_first.append(str(nb[0]))
    return {'top_events':n,'top_particle0_event_rate':top0/n,'top_leading_event_rate':toplead/n,'knn_contains_particle0_rate':knn_has0/n,'knn_contains_leading_rate':knn_haslead/n,'top_true_labels':', '.join(f'{k}:{v}' for k,v in labels.most_common(4)),'top_pred_labels':', '.join(f'{k}:{v}' for k,v in preds.most_common(4)),'first_neighbor_modes':', '.join(f'{k}:{v}' for k,v in Counter(neigh_first).most_common(5))}
def role(row,rs):
    layer=int(fnum(row.get('layer'))); lead=fnum(row.get('output_leading_pt_match_rate')); evlead=fnum(rs.get('top_leading_event_rate')); knnlead=fnum(rs.get('knn_contains_leading_rate'))
    if layer==2 and (lead>0.45 or evlead>0.75): return 'route-aware late core readout'
    if layer==2 and knnlead>0.4: return 'late readout with core-neighbor route'
    if layer<=1 and evlead<0.4: return 'context builder / relay away from direct core readout'
    return row.get('output_role','mixed route')
def route_code(head,row,rs):
    layer=int(fnum(row.get('layer'))); rr=role(row,rs)
    if layer==2:
        return f"# {head}: route-aware L2 readout\nfor event:\n    top_particle = select_particle_by_head_output()\n    neighbors = knn(top_particle, k=16)\n    context = read_L1_context(top_particle, neighbors)\n    evidence = aggregate_context(context)\n    if route_matches_core(top_particle_rate={fmt(rs.get('top_particle0_event_rate'))}, knn_has_core={fmt(rs.get('knn_contains_particle0_rate'))}):\n        logits += project_class_evidence(evidence)\n    # role: {rr}; classes: {rs.get('top_true_labels','')}"
    if layer==1:
        return f"# {head}: route-aware L1 context relay\nfor particle i:\n    neighbors = knn(i, k=16)\n    l0_context = read_L0_edge_features(i, neighbors)\n    route_context = mix_core_and_secondary(l0_context)\n    write_L1_context(route_context)\n    # role: {rr}; top_event_particles_core_rate={fmt(rs.get('top_particle0_event_rate'))}"
    return f"# {head}: route-aware L0 local builder\nfor particle i:\n    neighbors = knn(i, k=16)\n    edge = compare_raw_particle_features(i, neighbors)\n    local_pattern = detect_local_pid_pt_radial_edge(edge)\n    write_L0_local_pattern(local_pattern)\n    # role: {rr}; classes: {rs.get('top_true_labels','')}"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pseudo-v2',default='reports/latest/tables/pseudocode_operation_database_v2.csv')
    ap.add_argument('--inner-heads',default='reports/latest/tables/edgeconv_inner_trace_heads.csv')
    ap.add_argument('--inner-events',default='reports/latest/tables/edgeconv_inner_trace_events.csv')
    ap.add_argument('--rankings',default='reports/latest/tables/question_driven_head_rankings.csv')
    ap.add_argument('--residual',default='manifests/latest/known_observable_residual_v1.json')
    ap.add_argument('--out-csv',default='reports/latest/tables/pseudocode_operation_database_v3.csv')
    ap.add_argument('--out-jsonl',default='reports/latest/tables/pseudocode_operation_database_v3.jsonl')
    ap.add_argument('--out-json',default='manifests/latest/pseudocode_operation_database_v3.json')
    ap.add_argument('--out-md',default='reports/latest/PSEUDOCODE_OPERATION_DATABASE_V3.md')
    a=ap.parse_args(); pseudo=readcsv(a.pseudo_v2); heads={r.get('head_id'):r for r in readcsv(a.inner_heads)}; ev_by=defaultdict(list)
    for e in readcsv(a.inner_events): ev_by[e.get('head_id')].append(e)
    rank_by=defaultdict(list)
    for r in readcsv(a.rankings): rank_by[r.get('head_id')].append(r.get('question_id'))
    residual=loadjson(a.residual); rows=[]
    for r in pseudo:
        h=r.get('head_id',''); rs=route_stats(ev_by.get(h,[])); ih=heads.get(h,{})
        rr=dict(r); rr.update({
            'route_role':role(r,rs),'inner_trace_activation_mean_abs':ih.get('activation_mean_abs',''),'inner_trace_activation_max_abs':ih.get('activation_max_abs',''),
            'inner_trace_particle0_top_rate':ih.get('particle0_top_rate',''),'inner_trace_leading_pt_match_rate':ih.get('leading_pt_match_rate',''),
            'inner_conv_shapes':ih.get('inner_conv_shapes',''),'top_event_true_labels':rs.get('top_true_labels',''),'top_event_pred_labels':rs.get('top_pred_labels',''),
            'top_event_particle0_rate':rs.get('top_particle0_event_rate',''),'top_event_leading_rate':rs.get('top_leading_event_rate',''),
            'knn_contains_particle0_rate':rs.get('knn_contains_particle0_rate',''),'knn_contains_leading_rate':rs.get('knn_contains_leading_rate',''),
            'knn_first_neighbor_modes':rs.get('first_neighbor_modes',''),'question_tags':', '.join(sorted(set(rank_by.get(h,[])))),
            'route_aware_pseudocode':route_code(h,r,rs),'route_validation_status':'NEEDS_EDGE_CONV_INNER_TRACE_V2' if not rs else 'ROUTE_TRACE_V1_AVAILABLE',
            'residual_context':residual.get('status','')})
        rows.append(rr)
    rows=sorted(rows,key=lambda x:(int(fnum(x.get('layer'))),-fnum(x.get('inner_trace_leading_pt_match_rate')),-fnum(x.get('top_class_abs_grad'))))
    wcsv(a.out_csv,rows); wjsonl(a.out_jsonl,rows); wjson(a.out_json,{'ok':True,'rows':len(rows),'residual_status':residual.get('status'),'note':'route-aware pseudocode v3 merges pseudocode v2 + EdgeConv inner trace v1'})
    md=['# Pseudocode Operation Database v3\n\nRoute-aware pseudocode. This merges semantic pseudocode, code/output alignment, question rankings, and EdgeConv inner trace events.\n\n','## Top route-aware rows\n',mdtab(['head','route_role','questions','top_labels','event_core','knn_core','residual'],[[r['head_id'],r.get('route_role',''),r.get('question_tags',''),r.get('top_event_true_labels',''),fmt(r.get('top_event_particle0_rate')),fmt(r.get('knn_contains_particle0_rate')),r.get('residual_context','')] for r in rows[:40]]),'\n## Full route-aware pseudocode\n']
    for r in rows:
        md += [f"\n### {r['head_id']} — {r.get('route_role','')}\n\n",f"Questions: {r.get('question_tags','')}\n\n",f"Code: {r.get('code_module','')} / {r.get('code_slice','')}\n\n",f"Inner trace: top_event_particle0={fmt(r.get('top_event_particle0_rate'))}, top_event_leading={fmt(r.get('top_event_leading_rate'))}, knn_has_particle0={fmt(r.get('knn_contains_particle0_rate'))}, knn_has_leading={fmt(r.get('knn_contains_leading_rate'))}\n\n",f"Top event labels: {r.get('top_event_true_labels','')}\n\n",'```python\n'+r.get('route_aware_pseudocode','')+'\n```\n\n',f"Risks: {r.get('remaining_risks','')}\n\nNext: {r.get('next_tests','')}\n"]
    Path(a.out_md).parent.mkdir(parents=True,exist_ok=True); Path(a.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'rows':len(rows),'out_md':a.out_md},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
