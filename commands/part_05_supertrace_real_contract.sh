#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

OLD="${OLD_REPO:-$HOME/Рабочий стол/matrix_unified_system_particals}"
MANIFEST="manifests/latest/part_weaver_predict_smoke_v3_args.txt"

mkdir -p reports/latest/tables manifests/latest

if [ ! -f "$MANIFEST" ] && [ -f "$OLD/$MANIFEST" ]; then
  cp -v "$OLD/$MANIFEST" "$MANIFEST"
fi

if [ ! -f "$MANIFEST" ]; then
  echo "ERROR: missing $MANIFEST"
  echo "Need group:source_root mapping so supertrace can read original particle branches, not prediction ROOT only."
  exit 2
fi

python tools/part_attention_supertrace_real_contract_v1.py \
  --data-config external/particle_transformer/data/JetClass/JetClass_kinpid.yaml \
  --checkpoint external/particle_transformer/models/ParT_kinpid.pt \
  --network-file external/particle_transformer/networks/example_ParticleTransformer_legacy.py \
  --root-glob 'reports/latest/part_weaver_predict_smoke_v3_*.root' \
  --manifest "$MANIFEST" \
  --batch-size "${SUPERTRACE_BATCH_SIZE:-8}" \
  --topk "${SUPERTRACE_TOPK:-4}" \
  --max-a "${SUPERTRACE_MAX_A:-256}" \
  --max-b "${SUPERTRACE_MAX_B:-256}" \
  --max-c "${SUPERTRACE_MAX_C:-256}" \
  --max-d "${SUPERTRACE_MAX_D:-256}"

echo "===== REAL CONTRACT SUPERTRACE REPORT ====="
sed -n '1,220p' reports/latest/PART_ATTENTION_SUPERTRACE_REAL_CONTRACT_V1.md
