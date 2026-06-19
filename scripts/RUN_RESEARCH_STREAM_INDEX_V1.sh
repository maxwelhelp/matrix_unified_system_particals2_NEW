#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_research_stream_index_v1.py \
  --history-glob 'manifests/history/research_evidence_graph_*.json' \
  --latest manifests/latest/research_evidence_graph_v1.json \
  --out-json manifests/latest/research_stream_index_v1.json \
  --out-md reports/latest/RESEARCH_STREAM_INDEX_V1.md \
  --out-events reports/latest/tables/research_stream_events.jsonl \
  --out-cards reports/latest/tables/research_stream_cards.csv \
  --out-alerts reports/latest/tables/research_stream_alerts.csv \
  2>&1 | tee runs/research_stream_index_v1.log

git add docs/STREAMING_EVIDENCE_PIPELINE_v1.md \
  tools/build_research_stream_index_v1.py \
  tools/query_research_stream_v1.py \
  scripts/RUN_RESEARCH_STREAM_INDEX_V1.sh \
  reports/latest/RESEARCH_STREAM_INDEX_V1.md \
  reports/latest/tables/research_stream_events.jsonl \
  reports/latest/tables/research_stream_cards.csv \
  reports/latest/tables/research_stream_alerts.csv \
  manifests/latest/research_stream_index_v1.json

git commit -m "Update research stream index" || true
git push

echo "DONE stream index. Main file: reports/latest/RESEARCH_STREAM_INDEX_V1.md"
