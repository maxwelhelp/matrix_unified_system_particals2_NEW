#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest

TOPK="${PAIR_ATLAS_TOPK:-3}"
START="${PAIR_ATLAS_START:-1}"
END=$((START + TOPK - 1))

echo "===== AUTO PAIR ATLAS TOPK ====="
echo "start=$START topk=$TOPK end=$END"

for R in $(seq "$START" "$END"); do
  echo
  echo "===== PAIR ATLAS RANK $R: build groups ====="
  PAIR_ATLAS_RANK="$R" \
  PAIR_DIRECT_SCAN_LIMIT="${PAIR_DIRECT_SCAN_LIMIT:-20000}" \
  PAIR_DIRECT_BATCH_SIZE="${PAIR_DIRECT_BATCH_SIZE:-64}" \
  PAIR_DIRECT_MAX_PER_GROUP="${PAIR_DIRECT_MAX_PER_GROUP:-256}" \
  bash commands/part_31_build_pair_direct_replay_groups.sh

  echo
  echo "===== PAIR ATLAS RANK $R: program graph ====="
  PAIR_ATLAS_RANK="$R" \
  PAIR_PIPE_EVENTS_PER_GROUP="${PAIR_PIPE_EVENTS_PER_GROUP:-16}" \
  PAIR_PIPE_MICRO_BATCH="${PAIR_PIPE_MICRO_BATCH:-4}" \
  PAIR_PIPE_VALUE_MICRO_BATCH="${PAIR_PIPE_VALUE_MICRO_BATCH:-4}" \
  PAIR_PIPE_VAL_EVENTS_PER_GROUP="${PAIR_PIPE_VAL_EVENTS_PER_GROUP:-16}" \
  PAIR_PIPE_VAL_MICRO_BATCH="${PAIR_PIPE_VAL_MICRO_BATCH:-8}" \
  PAIR_PIPE_MAX_CANDIDATES="${PAIR_PIPE_MAX_CANDIDATES:-8}" \
  PAIR_PIPE_STRENGTHS="${PAIR_PIPE_STRENGTHS:-40}" \
  bash commands/part_32_run_pair_rank_program_graph_adapter.sh

done

python - <<'PY'
import csv, json, re
from pathlib import Path

def safe_float(x):
    try: return float(x)
    except Exception: return 0.0

def tag_to_pair(tag):
    m=re.match(r'rank(\d+)_([^_]+)_to_(.+)', tag)
    if not m: return ('', '', '')
    return (int(m.group(1)), 'label_'+m.group(2), 'label_'+m.group(3))

def load_json(path):
    p=Path(path)
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding='utf-8'))
    except Exception: return {}

rows=[]
for p in sorted(Path('manifests/latest').glob('part_pair_program_graph_rank*_v1.json')):
    tag=p.name.replace('part_pair_program_graph_','').replace('_v1.json','')
    rank,src,tgt=tag_to_pair(tag)
    pg=load_json(p)
    val=load_json(f'manifests/latest/part_pair_validation_{tag}_v1.json')
    disc=load_json(f'manifests/latest/part_pair_discovery_{tag}_v1.json')
    best=(val.get('top') or [{}])[0]
    rows.append({
        'rank':rank,'tag':tag,'src_label':src,'tgt_label':tgt,
        'nodes':pg.get('nodes',''),'edges':pg.get('edges',''),
        'discovery_candidates':disc.get('candidates',''),
        'validation_rows':val.get('summary_rows',''),
        'best_head':best.get('head_id',''),
        'best_pair':best.get('pair_role',''),
        'best_diag':best.get('diagnosis',''),
        'best_B_delta':best.get('best_B_delta_margin',''),
        'best_B_flip':best.get('best_B_delta_tbl_pred',''),
        'best_score':best.get('score',''),
    })
rows.sort(key=lambda r: int(r['rank'] or 9999))
Path('reports/latest/tables').mkdir(parents=True,exist_ok=True)
with open('reports/latest/tables/part_pair_atlas_summary_v1.csv','w',newline='',encoding='utf-8') as f:
    fields=list(rows[0].keys()) if rows else ['rank']
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
Path('manifests/latest/part_pair_atlas_summary_v1.json').write_text(json.dumps({'ok':True,'pairs':len(rows),'rows':rows},indent=2,ensure_ascii=False),encoding='utf-8')
lines=['# PART_PAIR_ATLAS_SUMMARY_V1\n\nAll-class pair atlas summary over generated pair program graphs.\n\n',f'- pairs: **{len(rows)}**\n\n','| rank | src | tgt | nodes | edges | discovery | validation | best_head | best_pair | B_delta | B_flip | score |\n','| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: |\n']
for r in rows:
    lines.append(f"| {r['rank']} | {r['src_label']} | {r['tgt_label']} | {r['nodes']} | {r['edges']} | {r['discovery_candidates']} | {r['validation_rows']} | `{r['best_head']}` | `{r['best_pair']}` | {r['best_B_delta']} | {r['best_B_flip']} | {r['best_score']} |\n")
lines.append('\n## Decision\n\n')
lines.append('`PAIR_ATLAS_SUMMARY_OK`: all generated pair graphs were summarized.\n' if rows else '`PAIR_ATLAS_EMPTY`: no pair graphs found.\n')
Path('reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md').write_text(''.join(lines),encoding='utf-8')
print(json.dumps({'ok':True,'pairs':len(rows),'out_md':'reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md'},indent=2))
PY

echo
sed -n '1,260p' reports/latest/PART_PAIR_ATLAS_SUMMARY_V1.md
