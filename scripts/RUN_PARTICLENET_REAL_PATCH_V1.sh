#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_real_patch_controls_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_real_patch_controls_v1 \
  2>&1 | tee runs/particlenet_real_patch_controls_v1.log
cp -f runs/particlenet_real_patch_controls_v1/PARTICLENET_REAL_PATCH_REPORT.md reports/latest/PARTICLENET_REAL_PATCH_REPORT.md
cp -f runs/particlenet_real_patch_controls_v1/particlenet_patch_summary.json manifests/latest/particlenet_patch_summary.json
cp -f runs/particlenet_real_patch_controls_v1/tables/particlenet_patch_controls.csv reports/latest/tables/particlenet_patch_controls.csv
git add adapters/particlenet_adapter.py tools/particlenet_real_patch_controls_v1.py scripts/RUN_PARTICLENET_REAL_PATCH_V1.sh reports/latest manifests/latest
git commit -m "Update ParticleNet real patch controls" || true
git push

echo "DONE ParticleNet patch. Report: reports/latest/PARTICLENET_REAL_PATCH_REPORT.md"
