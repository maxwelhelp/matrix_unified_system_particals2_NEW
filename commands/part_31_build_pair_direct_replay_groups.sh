#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_pair_direct_replay_group_builder_v1.py \
  --rank "${PAIR_ATLAS_RANK:-1}" \
  --scan-limit "${PAIR_DIRECT_SCAN_LIMIT:-20000}" \
  --batch-size "${PAIR_DIRECT_BATCH_SIZE:-64}" \
  --max-per-group "${PAIR_DIRECT_MAX_PER_GROUP:-256}"

TAG=$(python - <<'PY'
import csv, re, os
rank=int(os.environ.get('PAIR_ATLAS_RANK','1'))
rows=list(csv.DictReader(open('reports/latest/tables/part_all_class_atlas_pairs_v1.csv', newline='', encoding='utf-8')))
r=rows[rank-1]
def safe(x): return re.sub(r'[^A-Za-z0-9]+','_',x.replace('label_','')).strip('_')
print(f"rank{rank:03d}_{safe(r['src_label'])}_to_{safe(r['tgt_label'])}")
PY
)

sed -n '1,220p' "reports/latest/PART_PAIR_DIRECT_REPLAY_GROUPS_${TAG}_V1.md"
