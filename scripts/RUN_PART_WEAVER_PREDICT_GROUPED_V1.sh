#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest manifests/latest runs

PART_REPO_DIR="${PART_REPO_DIR:-external/particle_transformer}"
DATADIR="${JETCLASS_TINY:-$HOME/Рабочий стол/jetclass_tiny_balanced}"
MODE="${MODE:-kinpid}"
PART_CHECKPOINT="${PART_CHECKPOINT:-$PART_REPO_DIR/models/ParT_${MODE}.pt}"
BATCH_SIZE="${BATCH_SIZE:-64}"
NUM_WORKERS="${NUM_WORKERS:-1}"
GPUS="${GPUS:-0}"
MAX_PER_CLASS="${MAX_PER_CLASS:-50}"

add_group_files() {
  local group="$1"; shift
  local pattern="$1"; shift
  local n=0
  while IFS= read -r -d '' f; do
    DATA_ARGS+=("${group}:${f}")
    echo "${group}:${f}" >> manifests/latest/part_weaver_predict_grouped_v1_files.txt
    n=$((n+1))
    [ "$n" -ge "$MAX_PER_CLASS" ] && break
  done < <(find "$DATADIR" -type f -name "$pattern" -print0 | sort -z)
  echo "$group $n files"
}

: > manifests/latest/part_weaver_predict_grouped_v1_files.txt
DATA_ARGS=()
add_group_files HToBB 'HToBB*.root'
add_group_files HToCC 'HToCC*.root'
add_group_files HToGG 'HToGG*.root'
add_group_files HToWW2Q1L 'HToWW2Q1L*.root'
add_group_files HToWW4Q 'HToWW4Q*.root'
add_group_files TTBarLep 'TTBarLep*.root'
add_group_files TTBar 'TTBar*.root'
add_group_files WToQQ 'WToQQ*.root'
add_group_files ZToQQ 'ZToQQ*.root'
add_group_files ZJetsToNuNu 'ZJetsToNuNu*.root'

if [ "${#DATA_ARGS[@]}" -eq 0 ]; then
  echo "ERROR: no grouped ROOT files found under $DATADIR"
  echo "Check names: find \"$DATADIR\" -type f -name '*.root' | head -50"
  exit 1
fi

echo "Total grouped args: ${#DATA_ARGS[@]}"

weaver \
  --predict \
  --run-mode test \
  --data-test "${DATA_ARGS[@]}" \
  --data-config "$PART_REPO_DIR/data/JetClass/JetClass_${MODE}.yaml" \
  --network-config "$PART_REPO_DIR/networks/example_ParticleTransformer.py" \
  --model-prefix "$PART_CHECKPOINT" \
  --predict-output reports/latest/part_weaver_predict_grouped_v1.root \
  --batch-size "$BATCH_SIZE" \
  --batch-size-test "$BATCH_SIZE" \
  --num-workers "$NUM_WORKERS" \
  --fetch-step 1 \
  --gpus "$GPUS" \
  --log runs/part_weaver_predict_grouped_v1.log

cat > reports/latest/PART_WEAVER_PREDICT_GROUPED_V1.md <<EOF
# PART_WEAVER_PREDICT_GROUPED_V1

Official-style grouped Weaver predict for ParT.

- data_dir: ${DATADIR}
- mode: ${MODE}
- grouped args: ${#DATA_ARGS[@]}
- checkpoint: ${PART_CHECKPOINT}
- output: reports/latest/part_weaver_predict_grouped_v1.root
- log: runs/part_weaver_predict_grouped_v1.log

This mirrors the official train_JetClass.sh class-group syntax instead of passing a flat ROOT list.
EOF

git add scripts/RUN_PART_WEAVER_PREDICT_GROUPED_V1.sh reports/latest/PART_WEAVER_PREDICT_GROUPED_V1.md manifests/latest/part_weaver_predict_grouped_v1_files.txt reports/latest/part_weaver_predict_grouped_v1.root runs/part_weaver_predict_grouped_v1.log || true
git commit -m "Update grouped ParT Weaver predict" || true
git push

echo "DONE grouped ParT Weaver predict. Report: reports/latest/PART_WEAVER_PREDICT_GROUPED_V1.md"
