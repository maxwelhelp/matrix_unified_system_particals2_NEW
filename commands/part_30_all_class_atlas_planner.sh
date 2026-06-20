#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python tools/part_all_class_atlas_planner_v1.py \
  --pred-glob "${ATLAS_PRED_GLOB:-reports/latest/part_weaver_predict_smoke_v3_*.root}" \
  --manifest "${ATLAS_MANIFEST:-manifests/latest/part_weaver_predict_smoke_v3_args.txt}" \
  --top-pairs "${ATLAS_TOP_PAIRS:-30}" \
  --min-error "${ATLAS_MIN_ERROR:-4}"

sed -n '1,260p' reports/latest/PART_ALL_CLASS_ATLAS_PLANNER_V1.md
