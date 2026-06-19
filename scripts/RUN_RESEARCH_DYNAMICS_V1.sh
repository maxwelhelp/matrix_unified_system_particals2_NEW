#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_research_dynamics_v1.py \
  --history-glob 'manifests/history/research_evidence_graph_*.json' \
  --latest manifests/latest/research_evidence_graph_v1.json \
  --out-json manifests/latest/research_dynamics_v1.json \
  --out-md reports/latest/RESEARCH_DYNAMICS_V1.md \
  --out-heads reports/latest/tables/dynamics_head_ranks.csv \
  --out-particles reports/latest/tables/dynamics_particle_patterns.csv \
  --out-hypotheses reports/latest/tables/dynamics_hypotheses.csv \
  2>&1 | tee runs/research_dynamics_v1.log

git add docs/DYNAMIC_EVIDENCE_ANALYTICS_v1.md \
  tools/build_research_dynamics_v1.py \
  scripts/RUN_RESEARCH_DYNAMICS_V1.sh \
  reports/latest/RESEARCH_DYNAMICS_V1.md \
  reports/latest/tables/dynamics_head_ranks.csv \
  reports/latest/tables/dynamics_particle_patterns.csv \
  reports/latest/tables/dynamics_hypotheses.csv \
  manifests/latest/research_dynamics_v1.json

git commit -m "Update research dynamics" || true
git push

echo "DONE dynamics. Main report: reports/latest/RESEARCH_DYNAMICS_V1.md"
