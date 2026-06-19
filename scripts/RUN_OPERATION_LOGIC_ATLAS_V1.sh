#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_operation_logic_atlas_v1.py \
  --head-vectors reports/latest/tables/evidence_head_vectors.csv \
  --class-grads reports/latest/tables/class_specific_head_gradients.csv \
  --class-summary reports/latest/tables/class_specific_head_gradient_summary.csv \
  --relations reports/latest/tables/relation_signal_edges.csv \
  --stream-events reports/latest/tables/research_stream_events.jsonl \
  --control-summary reports/latest/tables/particle0_topk_control_summary_v2.csv \
  --confusion reports/latest/tables/control_confusion_summary.csv \
  --residual manifests/latest/known_observable_residual_v1.json \
  --out-json manifests/latest/operation_logic_atlas_v1.json \
  --out-csv reports/latest/tables/operation_logic_atlas.csv \
  --out-md reports/latest/OPERATION_LOGIC_ATLAS_V1.md \
  2>&1 | tee runs/operation_logic_atlas_v1.log

git add docs/01_method/OPERATION_LOGIC_ATLAS_PLAN_v1.md \
  tools/build_operation_logic_atlas_v1.py \
  scripts/RUN_OPERATION_LOGIC_ATLAS_V1.sh \
  reports/latest/OPERATION_LOGIC_ATLAS_V1.md \
  reports/latest/tables/operation_logic_atlas.csv \
  manifests/latest/operation_logic_atlas_v1.json

git commit -m "Update operation logic atlas" || true
git push

echo "DONE operation logic atlas. Main report: reports/latest/OPERATION_LOGIC_ATLAS_V1.md"
