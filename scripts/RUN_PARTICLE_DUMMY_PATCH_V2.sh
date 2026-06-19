#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

mkdir -p runs reports/latest/tables manifests/latest

PYTHONUNBUFFERED=1 python tools/particle_dummy_patch_controls_v2.py \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_dummy_patch_controls_v2 \
  2>&1 | tee runs/particle_dummy_patch_controls_v2.log

cp -f runs/particle_dummy_patch_controls_v2/DUMMY_PARTICLE_PATCH_REPORT.md \
  reports/latest/DUMMY_PARTICLE_PATCH_REPORT.md

cp -f runs/particle_dummy_patch_controls_v2/dummy_patch_controls_summary.json \
  manifests/latest/dummy_particle_patch_controls_summary.json

cp -f runs/particle_dummy_patch_controls_v2/tables/dummy_patch_controls.csv \
  reports/latest/tables/dummy_particle_patch_controls.csv

git add \
  tools/particle_dummy_patch_controls_v2.py \
  scripts/RUN_PARTICLE_DUMMY_PATCH_V2.sh \
  reports/latest \
  manifests/latest

git commit -m "Update dummy particle patch controls" || true

git push
