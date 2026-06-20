#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

mkdir -p reports/latest/auto_pipeline_logs reports/latest/tables manifests/latest

# One automatic Hqql/Tbl program-graph pipeline.
# Defaults are P40-safe short mode. Override env only when you intentionally want heavier validation.
DIRECT_SCAN_LIMIT="${DIRECT_SCAN_LIMIT:-20000}"
DIRECT_MAX_PER_GROUP="${DIRECT_MAX_PER_GROUP:-256}"
NAT_MANUAL_EVENTS_PER_GROUP="${NAT_MANUAL_EVENTS_PER_GROUP:-32}"
NAT_MANUAL_MICRO_BATCH="${NAT_MANUAL_MICRO_BATCH:-4}"
VALUE_WRITE_EVENTS_PER_GROUP="${VALUE_WRITE_EVENTS_PER_GROUP:-32}"
VALUE_WRITE_MICRO_BATCH="${VALUE_WRITE_MICRO_BATCH:-4}"
PAIR_VAL_EVENTS_PER_GROUP="${PAIR_VAL_EVENTS_PER_GROUP:-32}"
PAIR_VAL_MICRO_BATCH="${PAIR_VAL_MICRO_BATCH:-8}"
PAIR_VAL_BALANCED_PER_DIAG="${PAIR_VAL_BALANCED_PER_DIAG:-3}"
PAIR_VAL_BALANCED_TOTAL="${PAIR_VAL_BALANCED_TOTAL:-12}"
PAIR_VAL_STRENGTHS="${PAIR_VAL_STRENGTHS:-40}"
RESIDUAL_TRACE_EVENTS_PER_GROUP="${RESIDUAL_TRACE_EVENTS_PER_GROUP:-32}"
RESIDUAL_TRACE_MICRO_BATCH="${RESIDUAL_TRACE_MICRO_BATCH:-8}"
CLASSIFIER_DECODER_EVENTS_PER_GROUP="${CLASSIFIER_DECODER_EVENTS_PER_GROUP:-32}"
CLASSIFIER_DECODER_MICRO_BATCH="${CLASSIFIER_DECODER_MICRO_BATCH:-8}"

export DIRECT_SCAN_LIMIT DIRECT_MAX_PER_GROUP \
  NAT_MANUAL_EVENTS_PER_GROUP NAT_MANUAL_MICRO_BATCH \
  VALUE_WRITE_EVENTS_PER_GROUP VALUE_WRITE_MICRO_BATCH \
  PAIR_VAL_EVENTS_PER_GROUP PAIR_VAL_MICRO_BATCH PAIR_VAL_BALANCED_PER_DIAG PAIR_VAL_BALANCED_TOTAL PAIR_VAL_STRENGTHS \
  RESIDUAL_TRACE_EVENTS_PER_GROUP RESIDUAL_TRACE_MICRO_BATCH \
  CLASSIFIER_DECODER_EVENTS_PER_GROUP CLASSIFIER_DECODER_MICRO_BATCH

run_step() {
  local name="$1"; shift
  echo
  echo "===== AUTO STEP: ${name} ====="
  echo "command: $*"
  { time "$@"; } 2>&1 | tee "reports/latest/auto_pipeline_logs/${name}.log"
}

echo "# PART_AUTO_HQQL_TBL_PROGRAM_GRAPH"
echo "repo: $(pwd)"
echo "started_at: $(date -Is)"
echo "mode: P40-safe short/default"

# Build replay-consistent groups if absent. If present, keep them to avoid wasting time.
if [[ ! -s reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv ]]; then
  run_step 01_direct_replay_groups bash commands/part_11_build_direct_replay_groups.sh
else
  echo "===== AUTO STEP: 01_direct_replay_groups SKIP existing ====="
fi

run_step 02_natural_attention_manual_grad bash commands/part_19_natural_attention_manual_grad.sh
run_step 03_value_write_grad bash commands/part_20_value_write_grad.sh
run_step 04_discovery_candidates bash commands/part_21_discovery_candidates.sh
run_step 05_balanced_pair_validation bash commands/part_23_balanced_candidate_pair_validation.sh
run_step 06_final_mechanism_report bash commands/part_24_mechanism_discovery_final.sh
run_step 07_residual_path_v2 bash commands/part_26_residual_path_trace_v2.sh
run_step 08_classifier_logit_decoder bash commands/part_27_classifier_logit_decoder.sh
run_step 09_program_graph_export bash commands/part_28_program_graph_export.sh
run_step 10_auto_status python tools/part_auto_pipeline_status_v1.py

echo
echo "===== AUTO PIPELINE DONE ====="
sed -n '1,220p' reports/latest/PART_AUTO_PIPELINE_STATUS_V1.md
