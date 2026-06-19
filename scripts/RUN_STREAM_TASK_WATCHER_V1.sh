#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/stream_task_watcher_v1.py \
  --stream-index manifests/latest/research_stream_index_v1.json \
  --events reports/latest/tables/research_stream_events.jsonl \
  --dynamics-heads reports/latest/tables/dynamics_head_ranks.csv \
  --out-json manifests/latest/stream_task_watcher_v1.json \
  --out-md reports/latest/STREAM_TASK_WATCHER_V1.md \
  --out-scores reports/latest/tables/stream_task_watcher_scores.csv \
  --out-dataset reports/latest/tables/stream_task_training_dataset.jsonl \
  2>&1 | tee runs/stream_task_watcher_v1.log

git add docs/STREAM_TASK_WATCHER_v1.md \
  tools/stream_task_watcher_v1.py \
  scripts/RUN_STREAM_TASK_WATCHER_V1.sh \
  reports/latest/STREAM_TASK_WATCHER_V1.md \
  reports/latest/tables/stream_task_watcher_scores.csv \
  reports/latest/tables/stream_task_training_dataset.jsonl \
  manifests/latest/stream_task_watcher_v1.json

git commit -m "Update stream task watcher" || true
git push

echo "DONE stream task watcher. Main report: reports/latest/STREAM_TASK_WATCHER_V1.md"
