#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_real_patch_controls_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParT_full.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --limit "${LIMIT:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_real_patch_controls_v1 \
  2>&1 | tee runs/particle_real_patch_controls_v1.log
cp -f runs/particle_real_patch_controls_v1/REAL_PARTICLE_PATCH_REPORT.md reports/latest/REAL_PARTICLE_PATCH_REPORT.md
cp -f runs/particle_real_patch_controls_v1/real_particle_patch_summary.json manifests/latest/real_particle_patch_summary.json
cp -f runs/particle_real_patch_controls_v1/tables/real_particle_patch_controls.csv reports/latest/tables/real_particle_patch_controls.csv
git add data/jetclass_tiny_loader.py tools/particle_real_patch_controls_v1.py scripts/RUN_PARTICLE_REAL_PATCH_V1.sh reports/latest manifests/latest
git commit -m "Update real particle patch controls" || true
git push
