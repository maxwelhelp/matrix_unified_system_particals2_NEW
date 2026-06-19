#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/route_specific_patch_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --events-csv reports/latest/tables/event_forecast_explanations.csv \
  --event-indices "${EVENT_INDICES:-}" \
  --max-events "${MAX_EVENTS:-12}" \
  --heads "${HEADS:-L2_ch224:256,L2_ch128:160,L2_ch32:64,L2_ch0:32}" \
  --random-seed "${SEED:-123}" \
  --device "${DEVICE:-cuda}" \
  --out-csv reports/latest/tables/route_specific_patch_results.csv \
  --out-json manifests/latest/route_specific_patch_v1.json \
  --out-md reports/latest/ROUTE_SPECIFIC_PATCH_V1.md \
  2>&1 | tee runs/route_specific_patch_v1.log

git add docs/02_physics/ROUTE_SPECIFIC_PATCH_v1.md tools/route_specific_patch_v1.py scripts/RUN_ROUTE_SPECIFIC_PATCH_V1.sh \
  reports/latest/ROUTE_SPECIFIC_PATCH_V1.md reports/latest/tables/route_specific_patch_results.csv manifests/latest/route_specific_patch_v1.json

git commit -m "Update route specific patch" || true
git push

echo "DONE route specific patch. Main report: reports/latest/ROUTE_SPECIFIC_PATCH_V1.md"
