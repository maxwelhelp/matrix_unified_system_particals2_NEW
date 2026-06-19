#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p runs reports/latest manifests/latest
PYTHONUNBUFFERED=1 python tools/build_research_dashboard_latest.py \
  --out-dir runs/research_dashboard_latest \
  2>&1 | tee runs/research_dashboard_latest.log
cp -f runs/research_dashboard_latest/RESEARCH_DASHBOARD_LATEST.md reports/latest/RESEARCH_DASHBOARD_LATEST.md
cp -f runs/research_dashboard_latest/research_dashboard_latest.json manifests/latest/research_dashboard_latest.json
git add docs/RESEARCH_DASHBOARD_JSON_SPEC_v1.md tools/build_research_dashboard_latest.py scripts/RUN_RESEARCH_DASHBOARD_LATEST.sh reports/latest/RESEARCH_DASHBOARD_LATEST.md manifests/latest/research_dashboard_latest.json
git commit -m "Update latest research dashboard" || true
git push

echo "DONE dashboard. Main JSON: manifests/latest/research_dashboard_latest.json"
