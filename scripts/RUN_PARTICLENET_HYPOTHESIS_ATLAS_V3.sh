#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_hypothesis_atlas_v3.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --examples-per-class "${EXAMPLES_PER_CLASS:-2}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_hypothesis_atlas_v3 \
  2>&1 | tee runs/particlenet_hypothesis_atlas_v3.log
cp -f runs/particlenet_hypothesis_atlas_v3/PARTICLENET_HYPOTHESIS_ATLAS_V3.md reports/latest/PARTICLENET_HYPOTHESIS_ATLAS_V3.md
cp -f runs/particlenet_hypothesis_atlas_v3/particlenet_hypothesis_atlas_summary.json manifests/latest/particlenet_hypothesis_atlas_summary.json
cp -f runs/particlenet_hypothesis_atlas_v3/tables/hypothesis_global_patches.csv reports/latest/tables/hypothesis_global_patches.csv
cp -f runs/particlenet_hypothesis_atlas_v3/tables/hypothesis_per_class.csv reports/latest/tables/hypothesis_per_class.csv
cp -f runs/particlenet_hypothesis_atlas_v3/tables/hypothesis_examples.csv reports/latest/tables/hypothesis_examples.csv
git add docs/HYPOTHESIS_DISCOVERY_ROADMAP_v1.md tools/particlenet_hypothesis_atlas_v3.py scripts/RUN_PARTICLENET_HYPOTHESIS_ATLAS_V3.sh reports/latest manifests/latest
git commit -m "Update ParticleNet hypothesis atlas v3" || true
git push

echo "DONE hypothesis atlas. Report: reports/latest/PARTICLENET_HYPOTHESIS_ATLAS_V3.md"
