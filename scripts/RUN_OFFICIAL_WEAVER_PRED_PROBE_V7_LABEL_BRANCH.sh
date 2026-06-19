#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/official_weaver_pred_probe_v7_label_branch.py \
  --pred-dir "${PRED_DIR:-runs/official_weaver_predict_v5_kinpid}" \
  --out-dir runs/official_weaver_pred_probe_v7_label_branch \
  2>&1 | tee runs/official_weaver_pred_probe_v7_label_branch.log
cp -f runs/official_weaver_pred_probe_v7_label_branch/OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md reports/latest/OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md
cp -f runs/official_weaver_pred_probe_v7_label_branch/official_weaver_pred_probe_v7_label_branch.json manifests/latest/official_weaver_pred_probe_v7_label_branch.json
git add tools/official_weaver_pred_probe_v7_label_branch.py scripts/RUN_OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.sh reports/latest/OFFICIAL_WEAVER_PRED_PROBE_V7_LABEL_BRANCH.md manifests/latest/official_weaver_pred_probe_v7_label_branch.json
git commit -m "Update official Weaver label-branch prediction probe v7" || true
git push
