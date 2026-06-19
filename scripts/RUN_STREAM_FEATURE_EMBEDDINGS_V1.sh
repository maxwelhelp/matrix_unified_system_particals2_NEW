#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_stream_feature_embeddings_v1.py \
  --events reports/latest/tables/research_stream_events.jsonl \
  --relations reports/latest/tables/relation_signal_edges.csv \
  --controls reports/latest/tables/particle0_topk_control_summary_v2.csv \
  --comparisons reports/latest/tables/automatic_comparison_rows_v2.csv \
  --out-json manifests/latest/stream_feature_embeddings_v1.json \
  --out-events reports/latest/tables/stream_event_embeddings.csv \
  --out-relations reports/latest/tables/relation_edge_embeddings.csv \
  --out-controls reports/latest/tables/control_result_embeddings.csv \
  --out-comparisons reports/latest/tables/comparison_row_embeddings.csv \
  --out-jsonl reports/latest/tables/all_feature_embeddings.jsonl \
  --out-md reports/latest/STREAM_FEATURE_EMBEDDINGS_V1.md \
  2>&1 | tee runs/stream_feature_embeddings_v1.log

git add docs/03_stream/STREAM_FEATURE_EMBEDDINGS_v1.md \
  tools/build_stream_feature_embeddings_v1.py \
  scripts/RUN_STREAM_FEATURE_EMBEDDINGS_V1.sh \
  reports/latest/STREAM_FEATURE_EMBEDDINGS_V1.md \
  reports/latest/tables/stream_event_embeddings.csv \
  reports/latest/tables/relation_edge_embeddings.csv \
  reports/latest/tables/control_result_embeddings.csv \
  reports/latest/tables/comparison_row_embeddings.csv \
  reports/latest/tables/all_feature_embeddings.jsonl \
  manifests/latest/stream_feature_embeddings_v1.json

git commit -m "Update stream feature embeddings" || true
git push

echo "DONE stream feature embeddings. Main report: reports/latest/STREAM_FEATURE_EMBEDDINGS_V1.md"
