#!/usr/bin/env python3
import argparse, csv, json, math, re
from pathlib import Path
from datetime import datetime, timezone

LABELS=['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
EVENT_TYPES=['RUN_SUMMARY','HEAD_GATE','HEAD_QUESTION','MODEL_EVENT','PARTICLE_TOP','HYPOTHESIS_UPDATE']
REL_TYPES=['run_has_head_signal','head_supports_hypothesis','particle_pattern_associated_with_class','pattern_supports_hypothesis','task_monitors_hypothesis']
CONF={'LOW':0.25,'MEDIUM':0.5,'HIGH':1.0,'NONE':0.0}
PRIO={'P0':1.0,'P1':0.6,'P2':0.3}


def fnum(x, default=0.0):
    try:
        if x is None or x=='': return default
        return float(x)
    except Exception:
        return default

def load_jsonl(path):
    p=Path(path)
    if not p.exists(): return []
    rows=[]
    with p.open('r',encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if not line: continue
            try: rows.append(json.loads(line))
            except Exception: pass
    return rows

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

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

def wjsonl(path,rows):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r,ensure_ascii=False)+'\n')

def norm_log(x, scale=10.0):
    x=max(0.0,fnum(x))
    return min(1.0, math.log1p(x)/math.log1p(scale))

def norm_abs(x, scale=10.0):
    return max(-1.0,min(1.0,fnum(x)/scale))

def has_text(row, s):
    blob=json.dumps(row,ensure_ascii=False).lower()
    return 1.0 if s.lower() in blob else 0.0

def first_label_from_text(row):
    blob=json.dumps(row,ensure_ascii=False)
    for lab in LABELS:
        if lab in blob: return lab
    return ''

def parse_head_id(text):
    m=re.search(r'L(\d+)_ch(\d+):(\d+)', text or '')
    if not m: return None
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def vector_json(row, keys):
    return json.dumps([fnum(row.get(k)) for k in keys], separators=(',',':'))

def event_embedding(ev):
    p=ev.get('payload') or {}
    tags=[str(t) for t in ev.get('tags',[])]
    blob=json.dumps(ev,ensure_ascii=False)
    head=parse_head_id(blob)
    label=first_label_from_text(ev)
    out={
        'source':'stream_event',
        'id':f"event:{ev.get('run_index')}:{ev.get('event_type')}:{abs(hash(ev.get('title',''))) % 100000000}",
        'event_type':ev.get('event_type',''),
        'run_index':ev.get('run_index'),
        'score_raw':fnum(ev.get('score')),
        'score_norm':norm_log(ev.get('score'),5),
        'is_head':1.0 if ev.get('event_type') in ('HEAD_GATE','HEAD_QUESTION') else 0.0,
        'is_particle':1.0 if ev.get('event_type')=='PARTICLE_TOP' else 0.0,
        'is_relation_or_hypothesis':1.0 if ev.get('event_type')=='HYPOTHESIS_UPDATE' else 0.0,
        'is_particle0':1.0 if 'particle0' in tags else 0.0,
        'is_core_high_pt':1.0 if 'core_high_pt' in tags else 0.0,
        'is_wide':1.0 if 'wide' in tags else 0.0,
        'is_charged':1.0 if 'charged' in tags else 0.0,
        'is_negative_gate':1.0 if 'negative_gate' in tags else 0.0,
        'pt_norm':norm_log(p.get('pt'),500),
        'energy_norm':norm_log(p.get('energy'),1000),
        'deltaR_norm':min(1.0,max(0.0,fnum(p.get('deltaR_from_axis')))),
        'charge_abs':min(1.0,abs(fnum(p.get('charge')))),
        'gate_abs_norm':norm_log(p.get('gate_abs_grad'),2),
        'gate_sign':1.0 if fnum(p.get('gate_grad'))>0 else -1.0 if fnum(p.get('gate_grad'))<0 else 0.0,
        'patch_drop_norm':norm_abs(p.get('patch_acc_drop'),1),
        'head_layer_norm':(head[0]/3.0 if head else 0.0),
        'head_ch_start_norm':(head[1]/256.0 if head else 0.0),
        'head_ch_width_norm':((head[2]-head[1])/256.0 if head else 0.0),
    }
    for et in EVENT_TYPES:
        out['etype_'+et]=1.0 if ev.get('event_type')==et else 0.0
    for lab in LABELS:
        out['class_'+lab]=1.0 if label==lab else 0.0
    vec_keys=['score_norm','is_head','is_particle','is_relation_or_hypothesis','is_particle0','is_core_high_pt','is_wide','is_charged','is_negative_gate','pt_norm','energy_norm','deltaR_norm','charge_abs','gate_abs_norm','gate_sign','patch_drop_norm','head_layer_norm','head_ch_start_norm','head_ch_width_norm'] + ['class_'+lab for lab in LABELS]
    out['embedding_json']=vector_json(out,vec_keys)
    out['embedding_dim']=len(vec_keys)
    return out

def relation_embedding(r):
    src=r.get('src',''); dst=r.get('dst',''); rel=r.get('relation_type','')
    out={
        'source':'relation_edge',
        'id':f"rel:{abs(hash(src+'|'+rel+'|'+dst)) % 100000000}",
        'src':src,'dst':dst,'relation_type':rel,
        'relation_signal':fnum(r.get('relation_signal')),
        'support_norm':norm_log(r.get('support'),200),
        'mean_strength_norm':norm_log(r.get('mean_strength'),5),
        'max_strength_norm':norm_log(r.get('max_strength'),5),
        'lift_norm':min(1.0,fnum(r.get('lift_like'))/3.0),
        'confidence_code':CONF.get(str(r.get('confidence','')).upper(),0.0),
        'has_missing_control':1.0 if r.get('next_control') else 0.0,
        'is_particle0_relation':1.0 if 'particle0' in (src+dst) else 0.0,
        'is_core_relation':1.0 if 'core_high_pt' in (src+dst) else 0.0,
        'is_wide_relation':1.0 if 'wide' in (src+dst) else 0.0,
        'is_head_relation':1.0 if 'head:' in (src+dst) else 0.0,
        'is_class_relation':1.0 if 'class:' in (src+dst) else 0.0,
        'is_hypothesis_relation':1.0 if 'hypothesis:' in (src+dst) else 0.0,
    }
    for rt in REL_TYPES:
        out['rtype_'+rt]=1.0 if rel==rt else 0.0
    for lab in LABELS:
        out['class_'+lab]=1.0 if lab in (src+dst+r.get('evidence','')) else 0.0
    vec_keys=['relation_signal','support_norm','mean_strength_norm','max_strength_norm','lift_norm','confidence_code','has_missing_control','is_particle0_relation','is_core_relation','is_wide_relation','is_head_relation','is_class_relation','is_hypothesis_relation'] + ['class_'+lab for lab in LABELS]
    out['embedding_json']=vector_json(out,vec_keys)
    out['embedding_dim']=len(vec_keys)
    return out

def control_embedding(r):
    name=r.get('control','')
    k=0
    m=re.search(r'(?:top|remove)(\d+)',name)
    if m: k=int(m.group(1))
    out={
        'source':'control_row',
        'id':'control:'+name,
        'control':name,
        'k_norm':min(1.0,k/16.0),
        'acc':fnum(r.get('acc')),
        'acc_drop':fnum(r.get('acc_drop_from_baseline')),
        'flip_rate':fnum(r.get('pred_flip_rate')),
        'delta_logit_norm':norm_abs(r.get('delta_base_pred_logit_mean'),30),
        'valid_particles_norm':norm_log(r.get('valid_particles_mean_after'),128),
        'is_remove':1.0 if name.startswith('remove') else 0.0,
        'is_keep':1.0 if name.startswith('keep') else 0.0,
        'is_random':1.0 if name.startswith('random') else 0.0,
        'is_particle0':1.0 if 'particle0' in name else 0.0,
        'is_topk':1.0 if 'top' in name else 0.0,
    }
    vec_keys=['k_norm','acc','acc_drop','flip_rate','delta_logit_norm','valid_particles_norm','is_remove','is_keep','is_random','is_particle0','is_topk']
    out['embedding_json']=vector_json(out,vec_keys)
    out['embedding_dim']=len(vec_keys)
    return out

def comparison_embedding(r):
    status=str(r.get('status',''))
    out={
        'source':'comparison_row',
        'id':'cmp:'+r.get('comparison_id',''),
        'comparison_id':r.get('comparison_id',''),
        'priority_code':PRIO.get(str(r.get('priority','')),0.0),
        'has_missing_control':1.0 if r.get('missing_control') else 0.0,
        'has_particle0':has_text(r,'particle0'),
        'has_order':has_text(r,'order'),
        'has_residual':has_text(r,'residual'),
        'has_heldout':has_text(r,'heldout'),
        'has_class_specific':has_text(r,'class-specific'),
        'status_needs':1.0 if status.startswith('NEEDS') or status.startswith('MISSING') else 0.0,
        'status_supported':1.0 if 'SUPPORTED' in status else 0.0,
        'status_ready':1.0 if 'READY' in status else 0.0,
    }
    vec_keys=['priority_code','has_missing_control','has_particle0','has_order','has_residual','has_heldout','has_class_specific','status_needs','status_supported','status_ready']
    out['embedding_json']=vector_json(out,vec_keys)
    out['embedding_dim']=len(vec_keys)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--events',default='reports/latest/tables/research_stream_events.jsonl')
    ap.add_argument('--relations',default='reports/latest/tables/relation_signal_edges.csv')
    ap.add_argument('--controls',default='reports/latest/tables/particle0_topk_control_summary_v2.csv')
    ap.add_argument('--comparisons',default='reports/latest/tables/automatic_comparison_rows_v2.csv')
    ap.add_argument('--out-json',default='manifests/latest/stream_feature_embeddings_v1.json')
    ap.add_argument('--out-events',default='reports/latest/tables/stream_event_embeddings.csv')
    ap.add_argument('--out-relations',default='reports/latest/tables/relation_edge_embeddings.csv')
    ap.add_argument('--out-controls',default='reports/latest/tables/control_result_embeddings.csv')
    ap.add_argument('--out-comparisons',default='reports/latest/tables/comparison_row_embeddings.csv')
    ap.add_argument('--out-jsonl',default='reports/latest/tables/all_feature_embeddings.jsonl')
    ap.add_argument('--out-md',default='reports/latest/STREAM_FEATURE_EMBEDDINGS_V1.md')
    args=ap.parse_args()

    events=[event_embedding(e) for e in load_jsonl(args.events)]
    relations=[relation_embedding(r) for r in readcsv(args.relations)]
    controls=[control_embedding(r) for r in readcsv(args.controls)]
    comparisons=[comparison_embedding(r) for r in readcsv(args.comparisons)]
    all_rows=events+relations+controls+comparisons
    wcsv(args.out_events,events)
    wcsv(args.out_relations,relations)
    wcsv(args.out_controls,controls)
    wcsv(args.out_comparisons,comparisons)
    wjsonl(args.out_jsonl,all_rows)
    summary={
        'schema':'stream_feature_embeddings.v1',
        'generated_at_utc':datetime.now(timezone.utc).isoformat(),
        'counts':{'events':len(events),'relations':len(relations),'controls':len(controls),'comparisons':len(comparisons),'all':len(all_rows)},
        'files':{
            'events':args.out_events,'relations':args.out_relations,'controls':args.out_controls,'comparisons':args.out_comparisons,'all_jsonl':args.out_jsonl
        },
        'note':'Deterministic structured evidence embeddings, not LLM semantic embeddings.'
    }
    wjson(args.out_json,summary)
    md=['# Stream Feature Embeddings v1\n\n',
        'Deterministic structured numeric embeddings for stream events, relation edges, controls, and comparison rows.\n\n',
        f"- event embeddings: **{len(events)}**\n",
        f"- relation embeddings: **{len(relations)}**\n",
        f"- control embeddings: **{len(controls)}**\n",
        f"- comparison embeddings: **{len(comparisons)}**\n",
        f"- all rows: **{len(all_rows)}**\n\n",
        '## Use\n\n',
        'These rows can be used for clustering, MLP watcher training, attention-over-events, anomaly scoring, and fast dashboards.\n\n',
        '## Files\n\n',
        f'- `{args.out_events}`\n',f'- `{args.out_relations}`\n',f'- `{args.out_controls}`\n',f'- `{args.out_comparisons}`\n',f'- `{args.out_jsonl}`\n']
    Path(args.out_md).parent.mkdir(parents=True,exist_ok=True)
    Path(args.out_md).write_text(''.join(md),encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
