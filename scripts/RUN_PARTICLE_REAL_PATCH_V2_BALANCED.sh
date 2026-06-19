#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_real_patch_controls_v2_balanced.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParT_full.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --samples-per-file "${SAMPLES_PER_FILE:-32}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_real_patch_controls_v2_balanced \
  2>&1 | tee runs/particle_real_patch_controls_v2_balanced.log
cp -f runs/particle_real_patch_controls_v2_balanced/REAL_PARTICLE_PATCH_BALANCED_REPORT.md reports/latest/REAL_PARTICLE_PATCH_BALANCED_REPORT.md
cp -f runs/particle_real_patch_controls_v2_balanced/real_particle_patch_balanced_summary.json manifests/latest/real_particle_patch_balanced_summary.json
cp -f runs/particle_real_patch_controls_v2_balanced/tables/real_particle_patch_controls_balanced.csv reports/latest/tables/real_particle_patch_controls_balanced.csv
git add tools/particle_real_patch_controls_v2_balanced.py scripts/RUN_PARTICLE_REAL_PATCH_V2_BALANCED.sh reports/latest manifests/latest
git commit -m "Update balanced real particle patch controls" || true
git push
