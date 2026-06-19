#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/build_scope_comparability_guard_v1.py \
  --stream-index manifests/latest/research_stream_index_v1.json \
  --dynamics manifests/latest/research_dynamics_v1.json \
  --controls manifests/latest/particle0_topk_controls_v2.json \
  --embeddings manifests/latest/stream_feature_embeddings_v1.json \
  --comparison manifests/latest/automatic_comparison_engine_v2.json \
  --out-json manifests/latest/scope_comparability_guard_v1.json \
  --out-md reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md \
  --out-checks reports/latest/tables/scope_comparability_checks.csv \
  --out-manifest reports/latest/tables/scoped_feature_manifest.csv \
  2>&1 | tee runs/scope_comparability_guard_v1.log

git add docs/03_stream/SCOPE_AND_COMPARABILITY_GUARD_v1.md \
  tools/build_scope_comparability_guard_v1.py \
  scripts/RUN_SCOPE_COMPARABILITY_GUARD_V1.sh \
  reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md \
  reports/latest/tables/scope_comparability_checks.csv \
  reports/latest/tables/scoped_feature_manifest.csv \
  manifests/latest/scope_comparability_guard_v1.json

git commit -m "Update scope comparability guard" || true
git push

echo "DONE scope comparability guard. Main report: reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md"
