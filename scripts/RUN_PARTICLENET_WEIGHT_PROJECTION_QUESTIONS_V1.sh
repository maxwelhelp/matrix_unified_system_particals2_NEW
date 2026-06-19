#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_weight_projection_question_lenses_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --mode "${MODE:-kinpid}" \
  --device "${DEVICE:-cpu}" \
  --topk "${TOPK:-250}" \
  --out-dir runs/particlenet_weight_projection_questions_v1 \
  2>&1 | tee runs/particlenet_weight_projection_questions_v1.log
cp -f runs/particlenet_weight_projection_questions_v1/PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md reports/latest/PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md
cp -f runs/particlenet_weight_projection_questions_v1/particlenet_weight_projection_questions_v1_summary.json manifests/latest/particlenet_weight_projection_questions_v1_summary.json
cp -f runs/particlenet_weight_projection_questions_v1/tables/weight_projection_questions.csv reports/latest/tables/weight_projection_questions.csv
git add docs/WEIGHT_PROJECTION_QUESTION_LENSES_v1.md tools/particlenet_weight_projection_question_lenses_v1.py scripts/RUN_PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.sh reports/latest manifests/latest
git commit -m "Update ParticleNet weight projection questions" || true
git push

echo "DONE weight projection questions. Report: reports/latest/PARTICLENET_WEIGHT_PROJECTION_QUESTIONS_V1.md"
