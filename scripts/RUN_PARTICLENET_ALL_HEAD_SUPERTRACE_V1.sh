#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_all_head_supertrace_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --head-groups "${HEAD_GROUPS:-8}" \
  --micro-batch "${MICRO_BATCH:-64}" \
  --top-events "${TOP_EVENTS:-30}" \
  --top-particles "${TOP_PARTICLES:-10}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_all_head_supertrace_v1 \
  2>&1 | tee runs/particlenet_all_head_supertrace_v1.log
cp -f runs/particlenet_all_head_supertrace_v1/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md reports/latest/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md
cp -f runs/particlenet_all_head_supertrace_v1/all_head_supertrace_summary.json manifests/latest/all_head_supertrace_summary.json
cp -f runs/particlenet_all_head_supertrace_v1/tables/all_head_gate_gradients.csv reports/latest/tables/all_head_gate_gradients.csv
cp -f runs/particlenet_all_head_supertrace_v1/tables/all_head_supertrace_events.csv reports/latest/tables/all_head_supertrace_events.csv
cp -f runs/particlenet_all_head_supertrace_v1/tables/all_head_supertrace_particles.csv reports/latest/tables/all_head_supertrace_particles.csv
cp -f runs/particlenet_all_head_supertrace_v1/tables/all_head_supertrace_class_summary.csv reports/latest/tables/all_head_supertrace_class_summary.csv
git add docs/DIFFERENTIABLE_ALL_HEAD_SUPERTRACE_PLAN_v1.md tools/particlenet_all_head_supertrace_v1.py scripts/RUN_PARTICLENET_ALL_HEAD_SUPERTRACE_V1.sh reports/latest/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md reports/latest/tables/all_head_gate_gradients.csv reports/latest/tables/all_head_supertrace_events.csv reports/latest/tables/all_head_supertrace_particles.csv reports/latest/tables/all_head_supertrace_class_summary.csv manifests/latest/all_head_supertrace_summary.json
git commit -m "Update ParticleNet all-head differentiable supertrace" || true
git push

echo "DONE all-head supertrace. Report: reports/latest/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md"
