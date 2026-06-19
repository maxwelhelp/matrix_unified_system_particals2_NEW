#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest/tables manifests/latest
PYTHONUNBUFFERED=1 python tools/particlenet_why_class_report_v2.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-128}" \
  --max-files "${MAX_FILES:-20}" \
  --examples-per-class "${EXAMPLES_PER_CLASS:-3}" \
  --device "${DEVICE:-cuda}" \
  --out-dir runs/particlenet_why_class_report_v2 \
  2>&1 | tee runs/particlenet_why_class_report_v2.log
cp -f runs/particlenet_why_class_report_v2/PARTICLENET_WHY_CLASS_REPORT.md reports/latest/PARTICLENET_WHY_CLASS_REPORT.md
cp -f runs/particlenet_why_class_report_v2/particlenet_why_class_summary.json manifests/latest/particlenet_why_class_summary.json
cp -f runs/particlenet_why_class_report_v2/tables/why_class_examples.csv reports/latest/tables/why_class_examples.csv
cp -f runs/particlenet_why_class_report_v2/tables/why_class_global_patches.csv reports/latest/tables/why_class_global_patches.csv
git add tools/particlenet_why_class_report_v2.py scripts/RUN_PARTICLENET_WHY_CLASS_V2.sh reports/latest manifests/latest
git commit -m "Update ParticleNet why-class report" || true
git push

echo "DONE ParticleNet why-class. Report: reports/latest/PARTICLENET_WHY_CLASS_REPORT.md"
