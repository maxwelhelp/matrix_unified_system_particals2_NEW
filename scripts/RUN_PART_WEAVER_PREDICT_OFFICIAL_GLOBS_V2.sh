#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p reports/latest manifests/latest runs

PART_REPO_DIR="${PART_REPO_DIR:-external/particle_transformer}"
JETCLASS_OFFICIAL="${JETCLASS_OFFICIAL:-$HOME/Рабочий стол/JetClassOfficial}"
SPLIT_DIR="${SPLIT_DIR:-val_5M}"
DATADIR="$JETCLASS_OFFICIAL/$SPLIT_DIR"
MODE="${MODE:-kinpid}"
PART_CHECKPOINT="${PART_CHECKPOINT:-$PART_REPO_DIR/models/ParT_${MODE}.pt}"
BATCH_SIZE="${BATCH_SIZE:-64}"
NUM_WORKERS="${NUM_WORKERS:-1}"
GPUS="${GPUS:-0}"

if [ ! -d "$DATADIR" ]; then
  echo "ERROR: split dir not found: $DATADIR"
  exit 1
fi
if [ ! -f "$PART_CHECKPOINT" ]; then
  echo "ERROR: checkpoint not found: $PART_CHECKPOINT"
  exit 1
fi

# Official-style group:glob syntax. Important: TTBar uses TTBar_[0-9]*.root, not TTBar*.root,
# because TTBar*.root also matches TTBarLep_*.root.
DATA_ARGS=(
  "HToBB:${DATADIR}/HToBB_*.root"
  "HToCC:${DATADIR}/HToCC_*.root"
  "HToGG:${DATADIR}/HToGG_*.root"
  "HToWW2Q1L:${DATADIR}/HToWW2Q1L_*.root"
  "HToWW4Q:${DATADIR}/HToWW4Q_*.root"
  "TTBar:${DATADIR}/TTBar_[0-9]*.root"
  "TTBarLep:${DATADIR}/TTBarLep_*.root"
  "WToQQ:${DATADIR}/WToQQ_*.root"
  "ZToQQ:${DATADIR}/ZToQQ_*.root"
  "ZJetsToNuNu:${DATADIR}/ZJetsToNuNu_*.root"
)

printf '%s\n' "${DATA_ARGS[@]}" > manifests/latest/part_weaver_predict_official_globs_v2_args.txt

echo "Data dir: $DATADIR"
echo "Checkpoint: $PART_CHECKPOINT"
echo "Args:"
printf '  %s\n' "${DATA_ARGS[@]}"

weaver \
  --predict \
  --run-mode test \
  --data-test "${DATA_ARGS[@]}" \
  --data-config "$PART_REPO_DIR/data/JetClass/JetClass_${MODE}.yaml" \
  --network-config "$PART_REPO_DIR/networks/example_ParticleTransformer.py" \
  --model-prefix "$PART_CHECKPOINT" \
  --predict-output reports/latest/part_weaver_predict_official_globs_v2.root \
  --batch-size "$BATCH_SIZE" \
  --batch-size-test "$BATCH_SIZE" \
  --num-workers "$NUM_WORKERS" \
  --fetch-step 1 \
  --gpus "$GPUS" \
  --log runs/part_weaver_predict_official_globs_v2.log

cat > reports/latest/PART_WEAVER_PREDICT_OFFICIAL_GLOBS_V2.md <<EOF
# PART_WEAVER_PREDICT_OFFICIAL_GLOBS_V2

Official-style ParT/Weaver predict with group:glob syntax.

- data_dir: ${DATADIR}
- mode: ${MODE}
- checkpoint: ${PART_CHECKPOINT}
- output prefix: reports/latest/part_weaver_predict_official_globs_v2.root
- log: runs/part_weaver_predict_official_globs_v2.log

Fix vs V1: TTBar uses TTBar_[0-9]*.root to avoid accidentally including TTBarLep files.
EOF

git add scripts/RUN_PART_WEAVER_PREDICT_OFFICIAL_GLOBS_V2.sh reports/latest/PART_WEAVER_PREDICT_OFFICIAL_GLOBS_V2.md manifests/latest/part_weaver_predict_official_globs_v2_args.txt reports/latest/part_weaver_predict_official_globs_v2*.root runs/part_weaver_predict_official_globs_v2.log || true
git commit -m "Add official ParT Weaver glob predict v2" || true
git push || true

echo "DONE official glob ParT predict. Report: reports/latest/PART_WEAVER_PREDICT_OFFICIAL_GLOBS_V2.md"
