#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/question_driven_stage_analyzer_v1.py \
  --pseudo-v2 reports/latest/tables/pseudocode_operation_database_v2.csv \
  --comparison manifests/latest/automatic_comparison_engine_v2.json \
  --residual manifests/latest/known_observable_residual_v1.json \
  --scope manifests/latest/scope_comparability_guard_v1.json \
  --out-md reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md \
  --out-answers reports/latest/tables/question_driven_stage_answers.csv \
  --out-heads reports/latest/tables/question_driven_head_rankings.csv \
  --out-json manifests/latest/question_driven_stage_analyzer_v1.json \
  2>&1 | tee runs/question_driven_stage_analyzer_v1.log

git add docs/01_method/QUESTION_DRIVEN_STAGE_ANALYZER_v1.md \
  tools/question_driven_stage_analyzer_v1.py scripts/RUN_QUESTION_DRIVEN_STAGE_ANALYZER_V1.sh \
  reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md reports/latest/tables/question_driven_stage_answers.csv reports/latest/tables/question_driven_head_rankings.csv manifests/latest/question_driven_stage_analyzer_v1.json

git commit -m "Update question-driven stage analyzer" || true
git push

echo "DONE question-driven stage analyzer. Main report: reports/latest/QUESTION_DRIVEN_STAGE_ANALYZER_V1.md"
