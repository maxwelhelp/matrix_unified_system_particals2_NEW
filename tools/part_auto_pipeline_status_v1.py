#!/usr/bin/env python3
import json, csv, os
from pathlib import Path

REQ = [
    ('direct_groups', 'reports/latest/PART_DIRECT_REPLAY_GROUP_BUILDER_V1.md'),
    ('natural_attention', 'reports/latest/PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1.md'),
    ('value_write', 'reports/latest/PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1.md'),
    ('discovery', 'reports/latest/PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1.md'),
    ('pair_validation', 'reports/latest/PART_CANDIDATE_PAIR_VALIDATION_BALANCED_V1.md'),
    ('final_mechanisms', 'reports/latest/PART_MECHANISM_DISCOVERY_FINAL_V1.md'),
    ('residual_v2', 'reports/latest/PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2.md'),
    ('classifier', 'reports/latest/PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1.md'),
    ('program_graph', 'reports/latest/PART_PROGRAM_GRAPH_EXPORT_V1.md'),
]
JSONS = [
    ('natural_attention', 'manifests/latest/part_natural_attention_manual_grad_real_contract_v1.json'),
    ('value_write', 'manifests/latest/part_value_write_grad_real_contract_v1.json'),
    ('discovery', 'manifests/latest/part_discovery_candidates_real_contract_v1.json'),
    ('pair_validation', 'manifests/latest/part_candidate_pair_validation_balanced_v1.json'),
    ('residual_v2', 'manifests/latest/part_residual_path_trace_real_contract_v2.json'),
    ('classifier', 'manifests/latest/part_classifier_logit_decoder_real_contract_v1.json'),
    ('program_graph', 'manifests/latest/part_program_graph_export_v1.json'),
]

def load_json(p):
    try:
        return json.loads(Path(p).read_text(encoding='utf-8'))
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def count_csv(path):
    p=Path(path)
    if not p.exists(): return 0
    try:
        with p.open(newline='', encoding='utf-8') as f:
            return max(0, sum(1 for _ in csv.DictReader(f)))
    except Exception:
        return 0

def main():
    Path('reports/latest').mkdir(parents=True, exist_ok=True)
    rows=[]; ok=True
    for name,path in REQ:
        exists=Path(path).exists(); size=Path(path).stat().st_size if exists else 0
        if not exists or size == 0: ok=False
        rows.append({'stage':name,'path':path,'exists':exists,'size':size})
    metrics=[]
    for name,path in JSONS:
        obj=load_json(path)
        metrics.append({'stage':name,'path':path,'ok':obj.get('ok'), 'events':obj.get('events',''), 'rows':obj.get('rows',''), 'summary_rows':obj.get('summary_rows',''), 'nodes':obj.get('nodes',''), 'edges':obj.get('edges',''), 'candidates':obj.get('candidates',''), 'validated_strong_rows':obj.get('validated_strong_rows','')})
    csv_counts = {
        'program_graph_nodes': count_csv('reports/latest/tables/part_program_graph_nodes_v1.csv'),
        'program_graph_edges': count_csv('reports/latest/tables/part_program_graph_edges_v1.csv'),
        'pair_validation_summary': count_csv('reports/latest/tables/part_candidate_pair_validation_balanced_v1_summary.csv'),
        'discovery_candidates': count_csv('reports/latest/tables/part_discovery_candidates_real_contract_v1.csv'),
    }
    # hard checks for current Hqql/Tbl graph
    pg = load_json('manifests/latest/part_program_graph_export_v1.json')
    if int(pg.get('nodes') or 0) <= 0 or int(pg.get('edges') or 0) <= 0:
        ok = False
    val = load_json('manifests/latest/part_candidate_pair_validation_balanced_v1.json')
    if int(val.get('summary_rows') or 0) <= 0:
        ok = False
    lines=[]
    lines.append('# PART_AUTO_PIPELINE_STATUS_V1\n')
    lines.append('Automated Hqql/Tbl program-graph pipeline status.\n')
    lines.append(f'\n- status: **{"OK" if ok else "FAIL"}**\n')
    lines.append(f'- program_graph_nodes: **{pg.get("nodes", "n/a")}**\n')
    lines.append(f'- program_graph_edges: **{pg.get("edges", "n/a")}**\n')
    lines.append(f'- pair_validation_summary_rows: **{val.get("summary_rows", "n/a")}**\n')
    lines.append('\n## Required artifacts\n')
    lines.append('| stage | exists | size | path |\n| --- | ---: | ---: | --- |\n')
    for r in rows:
        lines.append(f"| {r['stage']} | {r['exists']} | {r['size']} | `{r['path']}` |\n")
    lines.append('\n## JSON metrics\n')
    lines.append('| stage | ok | events | rows | summary_rows | nodes | edges | candidates | validated |\n| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |\n')
    for m in metrics:
        lines.append(f"| {m['stage']} | {m['ok']} | {m['events']} | {m['rows']} | {m['summary_rows']} | {m['nodes']} | {m['edges']} | {m['candidates']} | {m['validated_strong_rows']} |\n")
    lines.append('\n## CSV counts\n')
    lines.append('| name | rows |\n| --- | ---: |\n')
    for k,v in csv_counts.items():
        lines.append(f'| {k} | {v} |\n')
    Path('reports/latest/PART_AUTO_PIPELINE_STATUS_V1.md').write_text(''.join(lines), encoding='utf-8')
    Path('manifests/latest').mkdir(parents=True, exist_ok=True)
    Path('manifests/latest/part_auto_pipeline_status_v1.json').write_text(json.dumps({'ok':ok,'required':rows,'metrics':metrics,'csv_counts':csv_counts}, indent=2), encoding='utf-8')
    print(json.dumps({'ok':ok,'out_md':'reports/latest/PART_AUTO_PIPELINE_STATUS_V1.md','nodes':pg.get('nodes'),'edges':pg.get('edges')}, indent=2))
    if not ok:
        raise SystemExit(2)
if __name__ == '__main__':
    main()
