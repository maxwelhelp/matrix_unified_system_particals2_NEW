#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_discovery_atlas_v4.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_discovery_atlas_v4 \
  2>&1 | tee runs/particlenet_discovery_atlas_v4.log
cp -f runs/particlenet_discovery_atlas_v4/PARTICLENET_DISCOVERY_ATLAS_V4.md reports/latest/PARTICLENET_DISCOVERY_ATLAS_V4.md
cp -f runs/particlenet_discovery_atlas_v4/particlenet_discovery_atlas_v4_summary.json manifests/latest/particlenet_discovery_atlas_v4_summary.json
cp -f runs/particlenet_discovery_atlas_v4/tables/discovery_route_knn_stats.csv reports/latest/tables/discovery_route_knn_stats.csv
cp -f runs/particlenet_discovery_atlas_v4/tables/discovery_particle_controls.csv reports/latest/tables/discovery_particle_controls.csv
git add docs/PARTICLE_DISCOVERY_CLAIMS_POLICY_v1.md tools/particlenet_discovery_atlas_v4.py scripts/RUN_PARTICLENET_DISCOVERY_ATLAS_V4.sh reports/latest manifests/latest
git commit -m "Update ParticleNet discovery atlas v4" || true
git push

echo "DONE discovery atlas. Report: reports/latest/PARTICLENET_DISCOVERY_ATLAS_V4.md"
