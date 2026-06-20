#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest

RANK="${PAIR_ATLAS_RANK:-1}"
TAG=$(python - <<'PY'
import csv, os, re
rank=int(os.environ.get('PAIR_ATLAS_RANK','1'))
rows=list(csv.DictReader(open('reports/latest/tables/part_all_class_atlas_pairs_v1.csv', newline='', encoding='utf-8')))
r=rows[rank-1]
def safe(x): return re.sub(r'[^A-Za-z0-9]+','_',x.replace('label_','')).strip('_')
print(f"rank{rank:03d}_{safe(r['src_label'])}_to_{safe(r['tgt_label'])}")
PY
)
SRC=$(python - <<'PY'
import csv, os
rank=int(os.environ.get('PAIR_ATLAS_RANK','1'))
rows=list(csv.DictReader(open('reports/latest/tables/part_all_class_atlas_pairs_v1.csv', newline='', encoding='utf-8')))
print(rows[rank-1]['src_label'])
PY
)
TGT=$(python - <<'PY'
import csv, os
rank=int(os.environ.get('PAIR_ATLAS_RANK','1'))
rows=list(csv.DictReader(open('reports/latest/tables/part_all_class_atlas_pairs_v1.csv', newline='', encoding='utf-8')))
print(rows[rank-1]['tgt_label'])
PY
)
export PART_PAIR_SRC_LABEL="$SRC"
export PART_PAIR_TGT_LABEL="$TGT"
NET="external/particle_transformer/networks/example_ParticleTransformer_pair_adapter.py"
PAIR_GROUPS="reports/latest/tables/part_pair_groups_${TAG}_v1.csv"
ADAPT_GROUPS="reports/latest/tables/part_pair_as_hqql_tbl_${TAG}_v1.csv"

echo "===== PAIR PROGRAM GRAPH ADAPTER ====="
echo "rank=$RANK tag=$TAG src=$SRC tgt=$TGT"

if [[ ! -s "$PAIR_GROUPS" ]]; then
  echo "ERROR: missing $PAIR_GROUPS"
  echo "Run: PAIR_ATLAS_RANK=$RANK bash commands/part_31_build_pair_direct_replay_groups.sh"
  exit 2
fi

python tools/part_pair_to_hqql_tbl_adapter_v1.py \
  --pair-groups "$PAIR_GROUPS" \
  --out-csv "$ADAPT_GROUPS" \
  --out-json "manifests/latest/part_pair_as_hqql_tbl_${TAG}_v1.json" \
  --out-md "reports/latest/PART_PAIR_AS_HQQL_TBL_${TAG}_V1.md"

python tools/part_natural_attention_manual_grad_real_contract_v1.py \
  --groups-csv "$ADAPT_GROUPS" \
  --network-file "$NET" \
  --events-per-group "${PAIR_PIPE_EVENTS_PER_GROUP:-24}" \
  --micro-batch "${PAIR_PIPE_MICRO_BATCH:-4}" \
  --out-md "reports/latest/PART_PAIR_NATURAL_ATTENTION_${TAG}_V1.md" \
  --out-rows "reports/latest/tables/part_pair_natural_attention_${TAG}_rows_v1.csv" \
  --out-summary "reports/latest/tables/part_pair_natural_attention_${TAG}_summary_v1.csv" \
  --out-json "manifests/latest/part_pair_natural_attention_${TAG}_v1.json"

python tools/part_value_write_grad_real_contract_v1.py \
  --groups-csv "$ADAPT_GROUPS" \
  --network-file "$NET" \
  --events-per-group "${PAIR_PIPE_EVENTS_PER_GROUP:-24}" \
  --micro-batch "${PAIR_PIPE_VALUE_MICRO_BATCH:-4}" \
  --out-md "reports/latest/PART_PAIR_VALUE_WRITE_${TAG}_V1.md" \
  --out-rows "reports/latest/tables/part_pair_value_write_${TAG}_rows_v1.csv" \
  --out-summary "reports/latest/tables/part_pair_value_write_${TAG}_summary_v1.csv" \
  --out-json "manifests/latest/part_pair_value_write_${TAG}_v1.json"

python tools/part_discovery_candidates_real_contract_v1.py \
  --nat-summary "reports/latest/tables/part_pair_natural_attention_${TAG}_summary_v1.csv" \
  --write-summary "reports/latest/tables/part_pair_value_write_${TAG}_summary_v1.csv" \
  --head-grad "reports/latest/tables/__missing_pair_head_grad.csv" \
  --rules-csv "reports/latest/tables/__missing_pair_rules.csv" \
  --bundle-csv "reports/latest/tables/__missing_pair_bundle.csv" \
  --bundle-sweep-csv "reports/latest/tables/__missing_pair_bundle_sweep.csv" \
  --out-md "reports/latest/PART_PAIR_DISCOVERY_${TAG}_V1.md" \
  --out-csv "reports/latest/tables/part_pair_discovery_${TAG}_v1.csv" \
  --out-json "manifests/latest/part_pair_discovery_${TAG}_v1.json"

python tools/part_candidate_pair_validation_v1.py \
  --groups-csv "$ADAPT_GROUPS" \
  --candidates-csv "reports/latest/tables/part_pair_discovery_${TAG}_v1.csv" \
  --network-file "$NET" \
  --events-per-group "${PAIR_PIPE_VAL_EVENTS_PER_GROUP:-24}" \
  --micro-batch "${PAIR_PIPE_VAL_MICRO_BATCH:-8}" \
  --max-candidates "${PAIR_PIPE_MAX_CANDIDATES:-8}" \
  --strengths "${PAIR_PIPE_STRENGTHS:-40}" \
  --out-md "reports/latest/PART_PAIR_VALIDATION_${TAG}_V1.md" \
  --out-rows "reports/latest/tables/part_pair_validation_${TAG}_rows_v1.csv" \
  --out-summary "reports/latest/tables/part_pair_validation_${TAG}_summary_v1.csv" \
  --out-json "manifests/latest/part_pair_validation_${TAG}_v1.json"

python tools/part_residual_path_trace_real_contract_v2.py \
  --groups-csv "$ADAPT_GROUPS" \
  --network-file "$NET" \
  --events-per-group "${PAIR_PIPE_EVENTS_PER_GROUP:-24}" \
  --micro-batch "${PAIR_PIPE_MICRO_BATCH:-8}" \
  --out-md "reports/latest/PART_PAIR_RESIDUAL_PATH_${TAG}_V1.md" \
  --out-summary "reports/latest/tables/part_pair_residual_path_${TAG}_summary_v1.csv" \
  --out-role "reports/latest/tables/part_pair_residual_path_${TAG}_role_summary_v1.csv" \
  --out-json "manifests/latest/part_pair_residual_path_${TAG}_v1.json"

python tools/part_classifier_logit_decoder_real_contract_v1.py \
  --groups-csv "$ADAPT_GROUPS" \
  --network-file "$NET" \
  --events-per-group "${PAIR_PIPE_EVENTS_PER_GROUP:-24}" \
  --micro-batch "${PAIR_PIPE_MICRO_BATCH:-8}" \
  --out-md "reports/latest/PART_PAIR_CLASSIFIER_${TAG}_V1.md" \
  --out-summary "reports/latest/tables/part_pair_classifier_${TAG}_summary_v1.csv" \
  --out-dims "reports/latest/tables/part_pair_classifier_${TAG}_dims_v1.csv" \
  --out-linear "reports/latest/tables/part_pair_classifier_${TAG}_linear_v1.csv" \
  --out-json "manifests/latest/part_pair_classifier_${TAG}_v1.json"

python tools/part_program_graph_export_v1.py \
  --validation "reports/latest/tables/part_pair_validation_${TAG}_summary_v1.csv" \
  --discovery "reports/latest/tables/part_pair_discovery_${TAG}_v1.csv" \
  --residual "reports/latest/tables/part_pair_residual_path_${TAG}_summary_v1.csv" \
  --role-residual "reports/latest/tables/part_pair_residual_path_${TAG}_role_summary_v1.csv" \
  --classifier "reports/latest/tables/part_pair_classifier_${TAG}_summary_v1.csv" \
  --classifier-dims "reports/latest/tables/part_pair_classifier_${TAG}_dims_v1.csv" \
  --linear "reports/latest/tables/part_pair_classifier_${TAG}_linear_v1.csv" \
  --out-json "manifests/latest/part_pair_program_graph_${TAG}_v1.json" \
  --out-nodes "reports/latest/tables/part_pair_program_graph_${TAG}_nodes_v1.csv" \
  --out-edges "reports/latest/tables/part_pair_program_graph_${TAG}_edges_v1.csv" \
  --out-md "reports/latest/PART_PAIR_PROGRAM_GRAPH_${TAG}_V1.md"

echo "===== PAIR PROGRAM GRAPH DONE ====="
sed -n '1,220p' "reports/latest/PART_PAIR_PROGRAM_GRAPH_${TAG}_V1.md"
