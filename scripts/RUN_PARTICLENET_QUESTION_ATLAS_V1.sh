#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_question_atlas_v1.py \
  --out-dir runs/particlenet_question_atlas_v1 \
  2>&1 | tee runs/particlenet_question_atlas_v1.log
cp -f runs/particlenet_question_atlas_v1/PARTICLENET_QUESTION_ATLAS_V1.md reports/latest/PARTICLENET_QUESTION_ATLAS_V1.md
cp -f runs/particlenet_question_atlas_v1/particlenet_question_atlas_v1_summary.json manifests/latest/particlenet_question_atlas_v1_summary.json
cp -f runs/particlenet_question_atlas_v1/tables/network_question_map.csv reports/latest/tables/network_question_map.csv
git add docs/NETWORK_QUESTION_ATLAS_v1.md docs/LENS_REGISTRY_v1.md tools/particlenet_question_atlas_v1.py scripts/RUN_PARTICLENET_QUESTION_ATLAS_V1.sh reports/latest manifests/latest
git commit -m "Update ParticleNet question atlas v1" || true
git push

echo "DONE question atlas. Report: reports/latest/PARTICLENET_QUESTION_ATLAS_V1.md"
