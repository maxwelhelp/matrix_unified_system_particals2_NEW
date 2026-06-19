#!/usr/bin/env python3
import argparse, csv, json
from pathlib import Path

QUESTION_TEMPLATES = [
    {
        'question_id':'CORE_CURRENT_QUESTION',
        'status':'ANSWERED_PARTIAL',
        'priority':'P0',
        'question':'What is the current best natural-language question this pseudo-head appears to ask?',
        'what_it_means_if_true':'This gives the current semantic label for the head, based on causal patch + weight projection + class effects.',
        'what_to_compute_next':'Refine the label with activation clustering and more specific projection lenses.',
        'next_script_or_lens':'head_projection_composer_v2 + activation-cluster pseudo-head lens',
        'risk':'Current semantic hint is weak and can be too generic.',
    },
    {
        'question_id':'WEIGHT_SOURCE_TO_HEAD',
        'status':'ANSWERED_PARTIAL',
        'priority':'P0',
        'question':'Which weight/source blocks feed this pseudo-head output group?',
        'what_it_means_if_true':'The head may be reading a specific hidden/source subspace rather than all previous features equally.',
        'what_to_compute_next':'Map strongest source blocks to activation clusters and physical/route evidence.',
        'next_script_or_lens':'weight projection WL4 block interaction + activation source clustering',
        'risk':'Flat source slices in deeper layers may not map to clear semantics.',
    },
    {
        'question_id':'PHYSICAL_FEATURE_TO_HEAD',
        'status':'ANSWERED_PARTIAL' ,
        'priority':'P0',
        'question':'Does this head read physical feature evidence such as kinematics, PID/charge, or geometry?',
        'what_it_means_if_true':'The head may be grounded in explicit physics-like input channels.',
        'what_to_compute_next':'Use feature-channel patch/noise/permutation controls and check per-class effects.',
        'next_script_or_lens':'feature-channel lens + permutation/noise controls',
        'risk':'Physical feature projections are reliable mainly in early layers; deeper layers are mixed.',
    },
    {
        'question_id':'ROUTE_WIDTH_TO_HEAD',
        'status':'TODO_P0',
        'priority':'P0',
        'question':'Does this head encode compact-vs-wide learned particle-neighbor routing?',
        'what_it_means_if_true':'The head may transform KNN route width into class evidence, e.g. compact W-like vs wide top-like routes.',
        'what_to_compute_next':'Patch compact/wide route groups and measure this head activation/logit drop.',
        'next_script_or_lens':'compact/wide route causal lens',
        'risk':'Route width can be a proxy for jet mass or multiplicity.',
    },
    {
        'question_id':'LEADING_PARTICLE_TO_HEAD',
        'status':'TODO_P0',
        'priority':'P0',
        'question':'Does this head depend on leading top-pT/top-energy particles?',
        'what_it_means_if_true':'The head may compute a leading-particle core / energy-flow signal.',
        'what_to_compute_next':'Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16.',
        'next_script_or_lens':'leading-particle top-k sweep lens',
        'risk':'Top-pT and top-energy sets overlap; need random and same-count controls.',
    },
    {
        'question_id':'HEAD_TO_CLASS_EFFECT',
        'status':'ANSWERED_PARTIAL',
        'priority':'P0',
        'question':'Which classes lose logit/accuracy when this head is patched?',
        'what_it_means_if_true':'The head supports particular class decisions rather than generic accuracy only.',
        'what_to_compute_next':'Make per-class and per-example signed logit attribution for this head.',
        'next_script_or_lens':'per-class head patch + signed logit attribution',
        'risk':'A class drop can be indirect through distribution shift after patching.',
    },
    {
        'question_id':'HEAD_TO_CLASS_CONTRAST',
        'status':'TODO_P0',
        'priority':'P0',
        'question':'Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc?',
        'what_it_means_if_true':'The head can be interpreted as a contrast-specific answer, not just a class-support feature.',
        'what_to_compute_next':'Project head activations into classifier contrast directions and patch the head.',
        'next_script_or_lens':'class contrast projection lens WL6 + component activation projection',
        'risk':'Classifier contrast weights alone do not prove head-specific responsibility.',
    },
    {
        'question_id':'ACTIVATION_CLUSTER_HEAD',
        'status':'TODO_P0',
        'priority':'P0',
        'question':'Is this equal channel-slice actually a learned activation cluster, or should it be split/merged?',
        'what_it_means_if_true':'The real functional head may be an activation cluster, not the current fixed slice.',
        'what_to_compute_next':'Cluster EdgeConv activations by covariance/class response; patch learned clusters.',
        'next_script_or_lens':'activation-cluster pseudo-head lens',
        'risk':'Current channel slices are arbitrary.',
    },
    {
        'question_id':'RANDOM_CHANNEL_CONTROL',
        'status':'TODO_P0',
        'priority':'P0',
        'question':'Is this head stronger than random channel groups of the same size?',
        'what_it_means_if_true':'The head is not an artifact of patching any random channels.',
        'what_to_compute_next':'Patch random channel groups with same size and compare effect distribution.',
        'next_script_or_lens':'random channel-group control',
        'risk':'Without random controls, head importance can be overestimated.',
    },
    {
        'question_id':'WEIGHT_PATCH_CONSISTENCY',
        'status':'TODO_P1',
        'priority':'P1',
        'question':'Do weight-projection questions agree with causal patch evidence for this head?',
        'what_it_means_if_true':'The interpretation is triangulated: written in weights and causally used in behavior.',
        'what_to_compute_next':'Compare projection score, activation strength, patch effect, and class drops for the same head.',
        'next_script_or_lens':'weight-vs-activation-vs-patch consistency lens',
        'risk':'Weight-only and patch-only evidence can disagree.',
    },
    {
        'question_id':'HELDOUT_STABILITY',
        'status':'TODO_P1',
        'priority':'P1',
        'question':'Does this head ask the same question on more files / heldout samples?',
        'what_it_means_if_true':'The head interpretation is stable and less likely to be a tiny-subset artifact.',
        'what_to_compute_next':'Run the same head map on more ROOT files and compare effect sizes/ranks.',
        'next_script_or_lens':'heldout stability lens',
        'risk':'Current evidence may be subset-specific.',
    },
    {
        'question_id':'ERROR_ROUTE_HEAD',
        'status':'TODO_P2',
        'priority':'P2',
        'question':'When the model is wrong, does this head answer like the predicted class instead of the true class?',
        'what_it_means_if_true':'Misclassifications may be explained by head-level question/answer confusion.',
        'what_to_compute_next':'Build true->pred error atlas and compare head activation/question answers on errors.',
        'next_script_or_lens':'error-route lens',
        'risk':'Requires enough wrong examples per confusion pair.',
    },
    {
        'question_id':'KNN_NEIGHBOR_TO_HEAD',
        'status':'TODO_P1',
        'priority':'P1',
        'question':'Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors?',
        'what_it_means_if_true':'The head can be linked to a particle-interaction pattern, not only a channel group.',
        'what_to_compute_next':'Measure head activation under compact/wide/top-pT/random neighbor route interventions.',
        'next_script_or_lens':'KNN neighbor-to-head route lens',
        'risk':'Need actual route intervention, not only descriptive route stats.',
    },
    {
        'question_id':'MULTI_HEAD_COMBINATION',
        'status':'TODO_P1',
        'priority':'P1',
        'question':'Does this head work together with another head to answer a larger composite question?',
        'what_it_means_if_true':'The model may distribute a physical/logical question across several pseudo-heads.',
        'what_to_compute_next':'Patch head pairs/groups and compare to additive single-head effects.',
        'next_script_or_lens':'multi-head composition lens',
        'risk':'Pairwise patching grows combinatorially; start with top heads only.',
    },
]


def fnum(x, default=0.0):
    try:
        if x is None or x == '': return default
        return float(x)
    except Exception:
        return default

def readcsv(path):
    p=Path(path)
    if not p.exists(): return []
    with p.open('r',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def writecsv(path, rows):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    keys=[]; seen=set()
    for r in rows:
        for k in r:
            if k not in seen:
                keys.append(k); seen.add(k)
    with p.open('w', encoding='utf-8', newline='') as f:
        wr=csv.DictWriter(f, fieldnames=keys); wr.writeheader()
        for r in rows:
            wr.writerow({k:r.get(k,'') for k in keys})

def wjson(path, obj):
    p=Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')

def fmt(x):
    try: x=float(x)
    except Exception: return 'n/a'
    return f'{x:.3e}' if abs(x)>0 and (abs(x)<1e-3 or abs(x)>1e4) else f'{x:.4f}'

def md_table(headers, rows):
    if not rows: return '_No rows._\n'
    out=['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']
    for r in rows:
        out.append('| '+' | '.join(str(x).replace('\n',' ') for x in r)+' |')
    return '\n'.join(out)+'\n'

def enrich_answer(head, qid):
    if qid == 'CORE_CURRENT_QUESTION':
        return head.get('question','')
    if qid == 'WEIGHT_SOURCE_TO_HEAD':
        return head.get('top_weight_projection_evidence','') or 'Weight projection evidence not attached yet.'
    if qid == 'PHYSICAL_FEATURE_TO_HEAD':
        return head.get('semantic_hint','') or 'No physical feature hint yet.'
    if qid == 'HEAD_TO_CLASS_EFFECT':
        return head.get('top_class_effects','') or 'Per-class head effects not attached yet.'
    return 'Not computed yet for this specific head.'

def build_catalog(heads):
    rows=[]
    for h in heads:
        for t in QUESTION_TEMPLATES:
            row={
                'head_id':h.get('head_id'),
                'layer':h.get('layer'),
                'group':h.get('group'),
                'channels':h.get('channels'),
                'role':h.get('role'),
                'acc_drop':h.get('acc_drop'),
                'patch_acc':h.get('patch_acc'),
                'delta_pred_logit':h.get('delta_pred_logit'),
                'confidence':h.get('confidence'),
                'question_id':t['question_id'],
                'question':t['question'],
                'current_answer':enrich_answer(h,t['question_id']),
                'status':t['status'],
                'priority':t['priority'],
                'evidence_now':'head_projection_question_map.csv + weight_projection_questions.csv + causal patch tables',
                'what_it_means_if_true':t['what_it_means_if_true'],
                'what_to_compute_next':t['what_to_compute_next'],
                'next_script_or_lens':t['next_script_or_lens'],
                'risk':t['risk'],
                'composite_lens':h.get('composite_lens'),
                'semantic_hint':h.get('semantic_hint'),
            }
            rows.append(row)
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--heads', default='reports/latest/tables/head_projection_question_map.csv')
    ap.add_argument('--out-md', default='reports/latest/FULL_HEAD_QUESTION_CATALOG.md')
    ap.add_argument('--out-csv', default='reports/latest/tables/full_head_question_catalog.csv')
    ap.add_argument('--out-json', default='manifests/latest/full_head_question_catalog.json')
    args=ap.parse_args()
    heads=readcsv(args.heads)
    heads=sorted(heads, key=lambda r:fnum(r.get('acc_drop')), reverse=True)
    rows=build_catalog(heads)
    writecsv(args.out_csv, rows)
    by_head={}
    by_q={}
    by_status={}
    for r in rows:
        by_head.setdefault(r['head_id'], []).append(r)
        by_q[r['question_id']]=by_q.get(r['question_id'],0)+1
        by_status[r['status']]=by_status.get(r['status'],0)+1
    data={
        'schema':'full_head_question_catalog.v1',
        'n_heads':len(heads),
        'questions_per_head':len(QUESTION_TEMPLATES),
        'n_question_rows':len(rows),
        'question_ids':[t['question_id'] for t in QUESTION_TEMPLATES],
        'counts_by_status':by_status,
        'counts_by_question':by_q,
        'heads':heads,
        'catalog':rows,
    }
    wjson(args.out_json,data)
    md=['# FULL HEAD QUESTION CATALOG\n\n',
        'This is the huge explicit list the project needs: every current pseudo-head multiplied by every question/lens we should ask.\n\n',
        '## Counts\n\n',
        f'- Heads: **{len(heads)}**\n',
        f'- Questions per head: **{len(QUESTION_TEMPLATES)}**\n',
        f'- Total question rows: **{len(rows)}**\n',
        f'- Status counts: `{json.dumps(by_status, ensure_ascii=False)}`\n\n',
        '## Question types\n\n',
        md_table(['question_id','status','priority','question','next lens'],[[t['question_id'],t['status'],t['priority'],t['question'],t['next_script_or_lens']] for t in QUESTION_TEMPLATES]),
        '\n## Heads overview\n\n',
        md_table(['head','layer','group','acc_drop','role','current best question','semantic hint'],[[h.get('head_id'),h.get('layer'),h.get('group'),fmt(h.get('acc_drop')),h.get('role'),h.get('question'),h.get('semantic_hint')] for h in heads]),
    ]
    for h in heads:
        qs=by_head.get(h.get('head_id'),[])
        md += [f"\n## {h.get('head_id')} — {h.get('role')}\n\n",
               f"**Effect:** acc_drop `{fmt(h.get('acc_drop'))}`, patch_acc `{fmt(h.get('patch_acc'))}`, delta_logit `{fmt(h.get('delta_pred_logit'))}`.\n\n",
               f"**Current best question:** {h.get('question')}\n\n",
               f"**Semantic hint:** {h.get('semantic_hint')}\n\n",
               f"**Composite lens:** `{h.get('composite_lens')}`\n\n",
               md_table(['qid','status','priority','question','current answer','what to compute next'],[[q['question_id'],q['status'],q['priority'],q['question'],q['current_answer'],q['what_to_compute_next']] for q in qs])]
    md += ['\n## Files\n\n',
           f'- CSV: `{args.out_csv}`\n',
           f'- JSON: `{args.out_json}`\n']
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(''.join(md), encoding='utf-8')
    print(json.dumps({'ok':True,'heads':len(heads),'questions_per_head':len(QUESTION_TEMPLATES),'rows':len(rows),'out_md':args.out_md}, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
