#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_pseudocode_operation_database_v1.py \
  --atlas reports/latest/tables/operation_logic_atlas.csv \
  --class-grads reports/latest/tables/class_specific_head_gradients.csv \
  --head-vectors reports/latest/tables/evidence_head_vectors.csv \
  --residual manifests/latest/known_observable_residual_v1.json \
  --out-csv reports/latest/tables/pseudocode_operation_database.csv \
  --out-jsonl reports/latest/tables/pseudocode_operation_database.jsonl \
  --out-json manifests/latest/pseudocode_operation_database_v1.json \
  --out-md reports/latest/PSEUDOCODE_OPERATION_DATABASE_V1.md \
  2>&1 | tee runs/pseudocode_operation_database_v1.log

git add docs/01_method/PSEUDOCODE_INTERPRETATION_LAYER_v1.md \
  tools/build_pseudocode_operation_database_v1.py \
  scripts/RUN_PSEUDOCODE_OPERATION_DATABASE_V1.sh \
  reports/latest/PSEUDOCODE_OPERATION_DATABASE_V1.md \
  reports/latest/tables/pseudocode_operation_database.csv \
  reports/latest/tables/pseudocode_operation_database.jsonl \
  manifests/latest/pseudocode_operation_database_v1.json

git commit -m "Update pseudocode operation database" || true
git push

echo "DONE pseudocode operation database. Main report: reports/latest/PSEUDOCODE_OPERATION_DATABASE_V1.md"
