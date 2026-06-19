#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_single_head_particle_trace_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --layer "${LAYER:-1}" \
  --group "${GROUP:-ch16:32}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --top-events "${TOP_EVENTS:-20}" \
  --top-particles "${TOP_PARTICLES:-8}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_single_head_particle_trace_v1 \
  2>&1 | tee runs/particlenet_single_head_particle_trace_v1.log
cp -f runs/particlenet_single_head_particle_trace_v1/PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.md reports/latest/PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.md
cp -f runs/particlenet_single_head_particle_trace_v1/single_head_particle_trace_summary.json manifests/latest/single_head_particle_trace_summary.json
cp -f runs/particlenet_single_head_particle_trace_v1/tables/single_head_event_trace.csv reports/latest/tables/single_head_event_trace.csv
cp -f runs/particlenet_single_head_particle_trace_v1/tables/single_head_particle_trace.csv reports/latest/tables/single_head_particle_trace.csv
cp -f runs/particlenet_single_head_particle_trace_v1/tables/single_head_class_summary.csv reports/latest/tables/single_head_class_summary.csv
git add docs/TOKEN_VS_PARTICLE_ANALYSIS_PLAN_v1.md tools/particlenet_single_head_particle_trace_v1.py scripts/RUN_PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.sh reports/latest/PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.md reports/latest/tables/single_head_event_trace.csv reports/latest/tables/single_head_particle_trace.csv reports/latest/tables/single_head_class_summary.csv manifests/latest/single_head_particle_trace_summary.json
git commit -m "Update ParticleNet single-head particle trace" || true
git push

echo "DONE single-head particle trace. Report: reports/latest/PARTICLENET_SINGLE_HEAD_PARTICLE_TRACE_V1.md"
