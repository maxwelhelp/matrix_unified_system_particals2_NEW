#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"
mkdir -p reports/latest/tables manifests/latest

GLOB_PATTERN="${PART_ROOT_GLOB:-reports/latest/part_weaver_predict_smoke_v3_*.root}"
OUT_MD="${PART_ANALYZER_MD:-reports/latest/PART_WEAVER_OUTPUT_ANALYZER_V1.md}"
OUT_SUMMARY="${PART_ANALYZER_SUMMARY:-reports/latest/tables/part_weaver_output_analyzer_v1_summary.csv}"
OUT_PAIRS="${PART_ANALYZER_PAIRS:-reports/latest/tables/part_weaver_output_analyzer_v1_pairs.csv}"
OUT_COUNTS="${PART_ANALYZER_COUNTS:-reports/latest/tables/part_weaver_output_analyzer_v1_counts.csv}"
OUT_JSON="${PART_ANALYZER_JSON:-manifests/latest/part_weaver_output_analyzer_v1.json}"

echo "=== analyze Weaver ROOT outputs ==="
echo "glob: $GLOB_PATTERN"

shopt -s nullglob
files=( $GLOB_PATTERN )
shopt -u nullglob

if [ "${#files[@]}" -eq 0 ]; then
  cat > "$OUT_MD" <<EOF
# PART_WEAVER_OUTPUT_ANALYZER_V1

No ROOT files found for glob:

\`\`\`text
$GLOB_PATTERN
\`\`\`

This is not an error if you have not run prediction yet.
EOF
  cat > "$OUT_JSON" <<EOF
{"ok": false, "reason": "no_root_files", "glob": "$GLOB_PATTERN"}
EOF
  cat "$OUT_MD"
  exit 0
fi

python tools/part_weaver_output_analyzer_v1.py \
  --glob "$GLOB_PATTERN" \
  --out-md "$OUT_MD" \
  --out-summary "$OUT_SUMMARY" \
  --out-pairs "$OUT_PAIRS" \
  --out-counts "$OUT_COUNTS" \
  --out-json "$OUT_JSON"

echo "=== analyzer report ==="
sed -n '1,140p' "$OUT_MD"
