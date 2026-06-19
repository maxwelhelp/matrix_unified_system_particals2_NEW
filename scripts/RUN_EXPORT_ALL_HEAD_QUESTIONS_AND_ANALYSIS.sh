#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest manifests/latest runs
PYTHONUNBUFFERED=1 python tools/export_all_head_questions_and_analysis_v1.py \
  --input reports/latest/tables/head_projection_question_map.csv \
  --out-md reports/latest/ALL_HEAD_QUESTIONS_AND_ANALYSIS.md \
  --out-json manifests/latest/all_head_questions_and_analysis.json \
  2>&1 | tee runs/export_all_head_questions_and_analysis.log
git add tools/export_all_head_questions_and_analysis_v1.py scripts/RUN_EXPORT_ALL_HEAD_QUESTIONS_AND_ANALYSIS.sh reports/latest/ALL_HEAD_QUESTIONS_AND_ANALYSIS.md manifests/latest/all_head_questions_and_analysis.json
git commit -m "Update all head questions and analysis export" || true
git push

echo "DONE all-head export. Main file: reports/latest/ALL_HEAD_QUESTIONS_AND_ANALYSIS.md"
