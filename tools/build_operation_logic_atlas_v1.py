#!/usr/bin/env python3
import argparse, csv, json, re
from pathlib import Path
from datetime import datetime, timezone


def fnum(x, default=0.0):
    try:
        if x is None or x=='': return default
        return float(x)
    except Exception:
        return default

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def loadjson(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

def load_jsonl(path, limit=None):
    p=Path(path)
    if not p.exists(): return []
    rows=[]
    with p.open('r',encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if not line: continue
            try: rows.append(json.loads(line))
            except Exception: pass
            if limit and len(rows)>=limit: break
    return rows

def wcsv(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k:r.get(k,'') for k in keys})

def wjson(path,obj):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')

def md_table(headers,rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def parse_head(h):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)', h or '')
    if not m: return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def stage_role(layer):
    if layer==0: return 'early local edge/particle feature reader'
    if layer==1: return 'middle neighborhood/context relay'
    if layer==2: return 'late class-evidence aggregation/readout'
    return 'unknown stage'

def default_input_state(layer):
    if layer==0:
        return 'raw particle kinematics/PID + KNN edge coordinates'
    if layer==1:
        return 'L0 local edge features already mixed into particle-neighborhood embeddings'
    if layer==2:
        return 'L1 contextual neighborhood features, class-route evidence, core/top-k summaries'
    return 'unknown transformed state'

def head_hint(head_id, layer, class_hits, relation_hits, stream_hits, residual):
    txt=' '.join([json.dumps(x,ensure_ascii=False) for x in (class_hits[:3]+relation_hits[:3]+stream_hits[:3])])
    if 'Hqql' in txt and 'Tbl' in txt:
        cls='Hqql/Tbl core-confusion axis'
    elif 'Hqql' in txt:
        cls='Hqql core/top-k separation'
    elif 'Tbl' in txt:
        cls='Tbl leading-core signature'
    elif 'H4q' in txt:
        cls='H4q/multi-prong attractor separation'
    elif 'Wqq' in txt or 'Zqq' in txt:
        cls='W/Z two-prong-like separation'
    else:
        cls='shared class evidence'
    if layer==0:
        op='read local particle-edge geometry, PID/charge, pt/radial summaries'
    elif layer==1:
        op='compose core particle with KNN/secondary context and route class evidence'
    elif layer==2:
        op='aggregate class evidence before classifier and suppress/boost alternatives'
    else:
        op='unknown operation'
    if residual.get('status')=='RESIDUAL_SIGNAL_REMAINS':
        op += '; residual not fully explained by simple known observables'
    return cls, op

def pseudocode(head_id, layer, cls, op):
    indent='    '
    if layer==0:
        lines=[f'# {head_id}: early reader', 'for particle i:', indent+'edge = knn_edges(i)', indent+'local = read(pt, deltaR, PID, charge, neighbor_features)', indent+f'write_local_features(local)  # supports {cls}']
    elif layer==1:
        lines=[f'# {head_id}: middle relay', 'for particle/neighborhood i:', indent+'core = read_topk_core_and_neighbors(i)', indent+'context = mix(core, radial_shape, secondary_particles)', indent+f'route_evidence(context)  # likely {cls}']
    else:
        lines=[f'# {head_id}: late readout', 'for event:', indent+'evidence = aggregate(core_context_heads)', indent+f'class_score += project(evidence)  # {cls}', indent+'suppress_or_compete_with_nearby_classes()']
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--head-vectors',default='reports/latest/tables/evidence_head_vectors.csv')
    ap.add_argument('--class-grads',default='reports/latest/tables/class_specific_head_gradients.csv')
    ap.add_argument('--class-summary',default='reports/latest/tables/class_specific_head_gradient_summary.csv')
    ap.add_argument('--relations',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--stream-events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--control-summary',default='reports/latest/tables/particle0_topk_control_summary_v2.csv')
    ap.add_argument('--confusion',default='reports/latest/tables/control_confusion_summary.csv')
    ap.add_argument('--residual',default='manifests/latest/known_observable_residual_v1.json')
    ap.add_argument('--out-json',default='manifests/latest/operation_logic_atlas_v1.json')
    ap.add_argument('--out-csv',default='reports/latest/tables/operation_logic_atlas.csv')
    ap.add_argument('--out-md',default='reports/latest/OPERATION_LOGIC_ATLAS_V1.md')
    args=ap.parse_args()
    heads=readcsv(args.head_vectors)
    class_grads=readcsv(args.class_grads)
    relations=readcsv(args.relations)
    events=load_jsonl(args.stream_events)
    residual=loadjson(args.residual)
    # Candidate heads: prefer class grads if available, else evidence head vectors.
    candidate_ids=[]
    for r in class_grads:
        h=r.get('head_id','')
        if h and h not in candidate_ids: candidate_ids.append(h)
    for r in heads:
        h=r.get('head_id','')
        if h and h not in candidate_ids: candidate_ids.append(h)
    rows=[]
    for h in candidate_ids:
        ph=parse_head(h)
        if not ph: continue
        layer,ch0,ch1=ph
        chits=sorted([r for r in class_grads if r.get('head_id')==h], key=lambda r:fnum(r.get('abs_grad')), reverse=True)
        rhits=[r for r in relations if h in json.dumps(r,ensure_ascii=False)]
        shits=[e for e in events if h in json.dumps(e,ensure_ascii=False)]
        hv=next((r for r in heads if r.get('head_id')==h),{})
        cls,op=head_hint(h,layer,chits,rhits,shits,residual)
        support=[]
        if chits:
            support.append('class_grad:'+', '.join(f"{r.get('class_label')}={fmt(r.get('abs_grad'))}" for r in chits[:3]))
        if hv:
            support.append('global_gate_abs='+fmt(hv.get('gate_abs_grad')))
        if rhits:
            support.append('relation_hits='+str(len(rhits)))
        if shits:
            support.append('stream_hits='+str(len(shits)))
        risk=[]
        if residual.get('status')=='RESIDUAL_SIGNAL_REMAINS': risk.append('simple known-observable surrogate incomplete')
        risk.append('semantic pseudocode, not literal model source')
        if not chits: risk.append('class-specific gradients missing or not run')
        rows.append({
            'head_id':h,'layer':layer,'channels':f'{ch0}:{ch1}','stage_role':stage_role(layer),'input_state':default_input_state(layer),'likely_operation':op,'particle_question':'Which core/top-k/neighbor particles does this group read or route?','class_question':cls,'evidence_sources':' | '.join(support),'pseudocode':pseudocode(h,layer,cls,op),'physics_meaning':f'candidate mechanism for {cls} after prior layer transformations','risks':'; '.join(risk),'next_test':'class-specific gradients + route-neighbor trace + heldout/per-file stability' if not chits else 'route-neighbor trace + heldout/per-file stability'
        })
    rows=sorted(rows,key=lambda r:(int(r['layer']), r['head_id']))
    wcsv(args.out_csv,rows)
    wjson(args.out_json,{'schema':'operation_logic_atlas.v1','generated_at_utc':datetime.now(timezone.utc).isoformat(),'n_heads':len(rows),'residual_status':residual.get('status'),'rows':rows})
    md=['# Operation Logic Atlas v1\n\n','Evidence-grounded semantic pseudocode for ParticleNet pseudo-head channel groups. This is not literal source code; it is a compact explanation of likely operations after previous layer transformations.\n\n','## Summary table\n',md_table(['head','stage','class question','operation','evidence'],[[r['head_id'],r['stage_role'],r['class_question'],r['likely_operation'],r['evidence_sources']] for r in rows[:40]]),'\n## Pseudocode by head\n']
    for r in rows[:60]:
        md += [f"\n### {r['head_id']} — {r['stage_role']}\n\n",f"**Input state:** {r['input_state']}\n\n",f"**Meaning:** {r['physics_meaning']}\n\n",'```python\n'+r['pseudocode']+'\n```\n\n',f"**Evidence:** {r['evidence_sources']}\n\n",f"**Risks:** {r['risks']}\n\n",f"**Next test:** {r['next_test']}\n"]
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps({'ok':True,'heads':len(rows),'out_md':args.out_md},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
