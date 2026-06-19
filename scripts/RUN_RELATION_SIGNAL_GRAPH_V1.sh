#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_relation_signal_graph_v1.py \
  --stream-index manifests/latest/research_stream_index_v1.json \
  --watcher manifests/latest/stream_task_watcher_v1.json \
  --events reports/latest/tables/research_stream_events.jsonl \
  --out-json manifests/latest/relation_signal_graph_v1.json \
  --out-md reports/latest/RELATION_SIGNAL_GRAPH_V1.md \
  --out-nodes reports/latest/tables/relation_signal_nodes.csv \
  --out-edges reports/latest/tables/relation_signal_edges.csv \
  --out-alerts reports/latest/tables/relation_signal_alerts.csv \
  2>&1 | tee runs/relation_signal_graph_v1.log

git add docs/RELATION_SIGNAL_GRAPH_v1.md \
  tools/build_relation_signal_graph_v1.py \
  tools/query_relation_signal_graph_v1.py \
  scripts/RUN_RELATION_SIGNAL_GRAPH_V1.sh \
  reports/latest/RELATION_SIGNAL_GRAPH_V1.md \
  reports/latest/tables/relation_signal_nodes.csv \
  reports/latest/tables/relation_signal_edges.csv \
  reports/latest/tables/relation_signal_alerts.csv \
  manifests/latest/relation_signal_graph_v1.json

git commit -m "Update relation signal graph" || true
git push

echo "DONE relation signal graph. Main report: reports/latest/RELATION_SIGNAL_GRAPH_V1.md"
