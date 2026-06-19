#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_real_patch_controls_v3_official.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParT_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_real_patch_controls_v3_official \
  2>&1 | tee runs/particle_real_patch_controls_v3_official.log
cp -f runs/particle_real_patch_controls_v3_official/REAL_PARTICLE_PATCH_V3_OFFICIAL_REPORT.md reports/latest/REAL_PARTICLE_PATCH_V3_OFFICIAL_REPORT.md
cp -f runs/particle_real_patch_controls_v3_official/real_particle_patch_v3_official_summary.json manifests/latest/real_particle_patch_v3_official_summary.json
cp -f runs/particle_real_patch_controls_v3_official/tables/real_particle_patch_controls_v3_official.csv reports/latest/tables/real_particle_patch_controls_v3_official.csv
git add data/jetclass_tiny_loader_v3_official.py tools/particle_real_patch_controls_v3_official.py scripts/RUN_PARTICLE_REAL_PATCH_V3_OFFICIAL_PREPROCESS.sh reports/latest manifests/latest
git commit -m "Update official-preprocess real particle patch controls" || true
git push
