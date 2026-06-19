#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs
PYTHONUNBUFFERED=1 python tools/event_forecast_explainer_v1.py \
  --checkpoint "${CHECKPOINT:-local_checkpoints/part/ParticleNet_kinpid.pt}" \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --mode "${MODE:-kinpid}" \
  --samples-per-file "${SAMPLES_PER_FILE:-64}" \
  --max-files "${MAX_FILES:-20}" \
  --top-events "${TOP_EVENTS:-20}" \
  --top-heads "${TOP_HEADS:-10}" \
  --event-indices "${EVENT_INDICES:-}" \
  --rankings reports/latest/tables/question_driven_head_rankings.csv \
  --pseudo-v3 reports/latest/tables/pseudocode_operation_database_v3.csv \
  --inner-events reports/latest/tables/edgeconv_inner_trace_v2_events.csv \
  --residual-events reports/latest/tables/known_observable_residual_top_events.csv \
  --residual-json manifests/latest/known_observable_residual_v1.json \
  --out-events reports/latest/tables/event_forecast_explanations.csv \
  --out-routes reports/latest/tables/event_forecast_active_routes.csv \
  --out-json manifests/latest/event_forecast_explainer_v1.json \
  --out-md reports/latest/EVENT_FORECAST_EXPLAINER_V1.md \
  2>&1 | tee runs/event_forecast_explainer_v1.log

git add docs/02_physics/EVENT_FORECAST_EXPLAINER_v1.md tools/event_forecast_explainer_v1.py scripts/RUN_EVENT_FORECAST_EXPLAINER_V1.sh \
  reports/latest/EVENT_FORECAST_EXPLAINER_V1.md reports/latest/tables/event_forecast_explanations.csv reports/latest/tables/event_forecast_active_routes.csv manifests/latest/event_forecast_explainer_v1.json

git commit -m "Update event forecast explainer" || true
git push

echo "DONE event forecast explainer. Main report: reports/latest/EVENT_FORECAST_EXPLAINER_V1.md"
