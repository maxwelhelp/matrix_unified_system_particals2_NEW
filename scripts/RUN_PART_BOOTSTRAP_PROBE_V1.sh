#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest manifests/latest runs

PYTHONUNBUFFERED=1 python tools/part_bootstrap_probe_v1.py \
  --repo-dir "${PART_REPO_DIR:-external/particle_transformer}" \
  --out-md reports/latest/PART_BOOTSTRAP_PROBE_V1.md \
  --out-json manifests/latest/part_bootstrap_probe_v1.json \
  2>&1 | tee runs/part_bootstrap_probe_v1.log

git add docs/что_считает_нейронка/03_next_architecture_part/PART_MIGRATION_PLAN_V1.md \
  scripts/SETUP_PARTICLE_TRANSFORMER_V1.sh tools/part_bootstrap_probe_v1.py scripts/RUN_PART_BOOTSTRAP_PROBE_V1.sh \
  reports/latest/PART_BOOTSTRAP_PROBE_V1.md manifests/latest/part_bootstrap_probe_v1.json || true

git commit -m "Add Particle Transformer bootstrap probe" || true
git push

echo "DONE Part bootstrap probe. Main report: reports/latest/PART_BOOTSTRAP_PROBE_V1.md"
