#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/official_weaver_pred_probe_v6.py \
  --pred-dir "${PRED_DIR:-runs/official_weaver_predict_v5_kinpid}" \
  --out-dir runs/official_weaver_pred_probe_v6 \
  2>&1 | tee runs/official_weaver_pred_probe_v6.log
cp -f runs/official_weaver_pred_probe_v6/OFFICIAL_WEAVER_PRED_PROBE_V6.md reports/latest/OFFICIAL_WEAVER_PRED_PROBE_V6.md
cp -f runs/official_weaver_pred_probe_v6/official_weaver_pred_probe_v6.json manifests/latest/official_weaver_pred_probe_v6.json
git add tools/official_weaver_pred_probe_v6.py scripts/RUN_OFFICIAL_WEAVER_PRED_PROBE_V6.sh reports/latest/OFFICIAL_WEAVER_PRED_PROBE_V6.md manifests/latest/official_weaver_pred_probe_v6.json
git commit -m "Update official Weaver prediction probe v6" || true
git push
