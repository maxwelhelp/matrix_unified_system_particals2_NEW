#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_accuracy_diagnostic_v4.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParT_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --samples-per-file "${SAMPLES_PER_FILE:-256}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_accuracy_diagnostic_v4 \
  2>&1 | tee runs/particle_accuracy_diagnostic_v4.log
cp -f runs/particle_accuracy_diagnostic_v4/PARTICLE_ACCURACY_DIAGNOSTIC_V4.md reports/latest/PARTICLE_ACCURACY_DIAGNOSTIC_V4.md
cp -f runs/particle_accuracy_diagnostic_v4/particle_accuracy_diagnostic_v4.json manifests/latest/particle_accuracy_diagnostic_v4.json
git add tools/particle_accuracy_diagnostic_v4.py scripts/RUN_PARTICLE_ACCURACY_DIAGNOSTIC_V4.sh reports/latest manifests/latest
git commit -m "Update particle accuracy diagnostic v4" || true
git push
