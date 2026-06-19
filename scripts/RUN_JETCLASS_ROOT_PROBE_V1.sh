#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/jetclass_root_probe_v1.py \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny}" \
  --max-files "${MAX_FILES:-5}" \
  --out-dir runs/jetclass_root_probe_v1 \
  2>&1 | tee runs/jetclass_root_probe_v1.log
cp -f runs/jetclass_root_probe_v1/JETCLASS_ROOT_PROBE_REPORT.md reports/latest/JETCLASS_ROOT_PROBE_REPORT.md
cp -f runs/jetclass_root_probe_v1/jetclass_root_probe.json manifests/latest/jetclass_root_probe.json
git add tools/jetclass_root_probe_v1.py scripts/RUN_JETCLASS_ROOT_PROBE_V1.sh reports/latest manifests/latest
git commit -m "Update JetClass ROOT probe report" || true
git push
