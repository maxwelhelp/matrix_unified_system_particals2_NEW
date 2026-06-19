#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest manifests/history runs
PYTHONUNBUFFERED=1 python tools/build_research_evidence_graph_v1.py \
  --out-json manifests/latest/research_evidence_graph_v1.json \
  --out-heads reports/latest/tables/evidence_head_vectors.csv \
  --out-particles reports/latest/tables/evidence_particle_vectors.csv \
  --out-edges reports/latest/tables/evidence_edges.csv \
  --out-md reports/latest/RESEARCH_EVIDENCE_GRAPH_V1.md \
  ${HISTORY_COPY:+--history-copy} \
  2>&1 | tee runs/research_evidence_graph_v1.log

git add docs/UPDATED_RESEARCH_STATE_AFTER_ALL_HEAD_SUPERTRACE_v1.md \
  docs/EVIDENCE_GRAPH_AND_DYNAMIC_TRACE_DATASET_v1.md \
  tools/build_research_evidence_graph_v1.py \
  scripts/RUN_RESEARCH_EVIDENCE_GRAPH_V1.sh \
  reports/latest/RESEARCH_EVIDENCE_GRAPH_V1.md \
  reports/latest/tables/evidence_head_vectors.csv \
  reports/latest/tables/evidence_particle_vectors.csv \
  reports/latest/tables/evidence_edges.csv \
  manifests/latest/research_evidence_graph_v1.json \
  manifests/history || true

git commit -m "Update research evidence graph" || true
git push

echo "DONE evidence graph. Main JSON: manifests/latest/research_evidence_graph_v1.json"
