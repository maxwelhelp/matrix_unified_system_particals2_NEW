#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/hard_hadron_geometry_probe_v1.py \
  --annotated-top-particles reports/latest/tables/internal_activation_contrast_v2_1_top_particles_annotated.csv \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-4096}" \
  --max-files "${MAX_FILES:-1000}" \
  --focus-head "${FOCUS_HEAD:-L1_ch80:96}" \
  --l2-head "${L2_HEAD:-L2_ch128:160}" \
  --knn-k "${KNN_K:-16}" \
  --device "${DEVICE:-cpu}" \
  --out-md reports/latest/HARD_HADRON_GEOMETRY_PROBE_V1.md \
  --out-rows reports/latest/tables/hard_hadron_geometry_probe_v1_rows.csv \
  --out-summary reports/latest/tables/hard_hadron_geometry_probe_v1_summary.csv \
  --out-json manifests/latest/hard_hadron_geometry_probe_v1.json \
  2>&1 | tee runs/hard_hadron_geometry_probe_v1.log

git add docs/что_считает_нейронка/02_текущая_задача_particlenet_hqql_tbl/06_next_steps/HARD_HADRON_GEOMETRY_PROBE_V1.md \
  tools/hard_hadron_geometry_probe_v1.py scripts/RUN_HARD_HADRON_GEOMETRY_PROBE_V1.sh \
  reports/latest/HARD_HADRON_GEOMETRY_PROBE_V1.md \
  reports/latest/tables/hard_hadron_geometry_probe_v1_rows.csv \
  reports/latest/tables/hard_hadron_geometry_probe_v1_summary.csv \
  manifests/latest/hard_hadron_geometry_probe_v1.json

git commit -m "Update hard hadron geometry probe v1" || true
git push

echo "DONE hard hadron geometry probe v1. Main report: reports/latest/HARD_HADRON_GEOMETRY_PROBE_V1.md"
