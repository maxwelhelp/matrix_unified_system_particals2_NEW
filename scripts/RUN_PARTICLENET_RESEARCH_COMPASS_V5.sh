#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_research_compass_v5.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --edge-head-groups "${EDGE_HEAD_GROUPS:-8}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_research_compass_v5 \
  2>&1 | tee runs/particlenet_research_compass_v5.log
cp -f runs/particlenet_research_compass_v5/PARTICLENET_RESEARCH_COMPASS_V5.md reports/latest/PARTICLENET_RESEARCH_COMPASS_V5.md
cp -f runs/particlenet_research_compass_v5/particlenet_research_compass_v5_summary.json manifests/latest/particlenet_research_compass_v5_summary.json
cp -f runs/particlenet_research_compass_v5/tables/research_edge_channel_heads.csv reports/latest/tables/research_edge_channel_heads.csv
cp -f runs/particlenet_research_compass_v5/tables/research_edge_channel_heads_per_class.csv reports/latest/tables/research_edge_channel_heads_per_class.csv
cp -f runs/particlenet_research_compass_v5/tables/research_feature_channels_per_class.csv reports/latest/tables/research_feature_channels_per_class.csv
cp -f runs/particlenet_research_compass_v5/tables/research_known_observables_by_class.csv reports/latest/tables/research_known_observables_by_class.csv
cp -f runs/particlenet_research_compass_v5/tables/research_class_contrasts.csv reports/latest/tables/research_class_contrasts.csv
git add docs/PARTICLE_RESEARCH_NOTEBOOK_v1.md tools/particlenet_research_compass_v5.py scripts/RUN_PARTICLENET_RESEARCH_COMPASS_V5.sh reports/latest manifests/latest
git commit -m "Update ParticleNet research compass v5" || true
git push

echo "DONE research compass. Report: reports/latest/PARTICLENET_RESEARCH_COMPASS_V5.md"
