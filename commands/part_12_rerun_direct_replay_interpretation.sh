#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

GROUPS="reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv"

if [ ! -f "$GROUPS" ]; then
  echo "ERROR: missing $GROUPS"
  echo "Run: DIRECT_SCAN_LIMIT=20000 DIRECT_MAX_PER_GROUP=256 bash commands/part_11_build_direct_replay_groups.sh"
  exit 2
fi

python tools/part_attention_supertrace_real_contract_v1.py \
  --groups-csv "$GROUPS" \
  --data-config external/particle_transformer/data/JetClass/JetClass_kinpid.yaml \
  --checkpoint external/particle_transformer/models/ParT_kinpid.pt \
  --network-file external/particle_transformer/networks/example_ParticleTransformer_legacy.py \
  --batch-size "${SUPERTRACE_BATCH_SIZE:-8}" \
  --topk "${SUPERTRACE_TOPK:-4}" \
  --max-a "${SUPERTRACE_MAX_A:-256}" \
  --max-b "${SUPERTRACE_MAX_B:-256}" \
  --max-c "${SUPERTRACE_MAX_C:-256}" \
  --max-d "${SUPERTRACE_MAX_D:-256}"

python tools/part_supertrace_physics_interpreter_v1.py
python tools/part_pad_control_v1.py
python tools/part_real_contract_pseudocode_compiler_v1.py

python tools/part_all_head_gate_trace_real_contract_v1.py \
  --groups-csv "$GROUPS" \
  --data-config external/particle_transformer/data/JetClass/JetClass_kinpid.yaml \
  --checkpoint external/particle_transformer/models/ParT_kinpid.pt \
  --network-file external/particle_transformer/networks/example_ParticleTransformer_legacy.py \
  --events-per-group "${GATE_EVENTS_PER_GROUP:-64}" \
  --micro-batch "${GATE_MICRO_BATCH:-8}"

python tools/part_exact_route_patch_real_contract_v1.py \
  --groups-csv "$GROUPS" \
  --data-config external/particle_transformer/data/JetClass/JetClass_kinpid.yaml \
  --checkpoint external/particle_transformer/models/ParT_kinpid.pt \
  --network-file external/particle_transformer/networks/example_ParticleTransformer_legacy.py \
  --events-per-group "${PATCH_EVENTS_PER_GROUP:-32}" \
  --micro-batch "${PATCH_MICRO_BATCH:-8}" \
  --top-rules "${PATCH_TOP_RULES:-8}" \
  --patch-strength "${PATCH_STRENGTH:-40}"

echo "===== DIRECT REPLAY INTERPRETATION SUMMARY ====="
echo
sed -n '1,80p' reports/latest/PART_DIRECT_REPLAY_GROUP_BUILDER_V1.md || true
echo
sed -n '1,140p' reports/latest/PART_ATTENTION_SUPERTRACE_REAL_CONTRACT_V1.md || true
echo
sed -n '1,120p' reports/latest/PART_REAL_CONTRACT_PSEUDOCODE_COMPILER_V1.md || true
echo
sed -n '1,160p' reports/latest/PART_ALL_HEAD_GATE_TRACE_REAL_CONTRACT_V1.md || true
echo
sed -n '1,220p' reports/latest/PART_EXACT_ROUTE_PATCH_REAL_CONTRACT_V1.md || true
