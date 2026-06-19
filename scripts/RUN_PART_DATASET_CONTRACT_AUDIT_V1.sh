#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest/tables manifests/latest runs

PYTHONUNBUFFERED=1 python tools/part_dataset_contract_audit_v1.py \
  --data-dir "${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}" \
  --max-files "${MAX_FILES:-200}" \
  --entry-stop "${ENTRY_STOP:-2000}" \
  --out-md reports/latest/PART_DATASET_CONTRACT_AUDIT_V1.md \
  --out-csv reports/latest/tables/part_dataset_contract_audit_v1_files.csv \
  --out-json manifests/latest/part_dataset_contract_audit_v1.json \
  2>&1 | tee runs/part_dataset_contract_audit_v1.log

git add tools/part_dataset_contract_audit_v1.py scripts/RUN_PART_DATASET_CONTRACT_AUDIT_V1.sh \
  reports/latest/PART_DATASET_CONTRACT_AUDIT_V1.md \
  reports/latest/tables/part_dataset_contract_audit_v1_files.csv \
  manifests/latest/part_dataset_contract_audit_v1.json || true

git commit -m "Update ParT dataset contract audit" || true
git push

echo "DONE ParT dataset contract audit. Main report: reports/latest/PART_DATASET_CONTRACT_AUDIT_V1.md"
