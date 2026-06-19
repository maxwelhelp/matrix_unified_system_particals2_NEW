#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_head_projection_composer_v2.py \
  --out-dir runs/particlenet_head_projection_composer_v2 \
  2>&1 | tee runs/particlenet_head_projection_composer_v2.log
cp -f runs/particlenet_head_projection_composer_v2/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md reports/latest/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md
cp -f runs/particlenet_head_projection_composer_v2/particlenet_head_projection_composer_v2_summary.json manifests/latest/particlenet_head_projection_composer_v2_summary.json
cp -f runs/particlenet_head_projection_composer_v2/tables/head_projection_question_map.csv reports/latest/tables/head_projection_question_map.csv
git add docs/WEIGHT_PROJECTION_HEAD_ANALYSIS_NOTES_v1.md tools/particlenet_head_projection_composer_v2.py scripts/RUN_PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.sh reports/latest manifests/latest
git commit -m "Update ParticleNet head projection composer" || true
git push

echo "DONE head projection composer. Report: reports/latest/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md"
