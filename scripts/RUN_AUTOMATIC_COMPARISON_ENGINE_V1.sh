#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_automatic_comparison_engine_v1.py \
  --relation-edges reports/latest/tables/relation_signal_edges.csv \
  --watcher manifests/latest/stream_task_watcher_v1.json \
  --dynamics-heads reports/latest/tables/dynamics_head_ranks.csv \
  --head-vectors reports/latest/tables/evidence_head_vectors.csv \
  --out-json manifests/latest/automatic_comparison_engine_v1.json \
  --out-md reports/latest/AUTOMATIC_COMPARISON_ENGINE_V1.md \
  --out-csv reports/latest/tables/automatic_comparison_rows.csv \
  --out-dataset reports/latest/tables/automatic_comparison_training_dataset.jsonl \
  2>&1 | tee runs/automatic_comparison_engine_v1.log

git add docs/AUTOMATIC_COMPARISON_ENGINE_v1.md \
  tools/build_automatic_comparison_engine_v1.py \
  scripts/RUN_AUTOMATIC_COMPARISON_ENGINE_V1.sh \
  reports/latest/AUTOMATIC_COMPARISON_ENGINE_V1.md \
  reports/latest/tables/automatic_comparison_rows.csv \
  reports/latest/tables/automatic_comparison_training_dataset.jsonl \
  manifests/latest/automatic_comparison_engine_v1.json

git commit -m "Update automatic comparison engine" || true
git push

echo "DONE automatic comparison engine. Main report: reports/latest/AUTOMATIC_COMPARISON_ENGINE_V1.md"
