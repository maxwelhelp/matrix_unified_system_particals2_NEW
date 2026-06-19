#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/particle_part_dummy_probe_v1.py \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particle_part_dummy_probe_v1 \
  2>&1 | tee runs/particle_part_dummy_probe_v1.log
cp -f runs/particle_part_dummy_probe_v1/DUMMY_PARTICLE_PROBE_REPORT.md reports/latest/DUMMY_PARTICLE_PROBE_REPORT.md
cp -f runs/particle_part_dummy_probe_v1/dummy_probe.json manifests/latest/dummy_particle_probe.json
git add adapters tools/particle_part_dummy_probe_v1.py scripts/RUN_PARTICLE_DUMMY_PROBE_V1.sh reports/latest manifests/latest docs README.md requirements*.txt .gitignore 2>/dev/null || true
git commit -m "Update particle dummy probe summaries" || true
git push
