# Tools and commands — current ParticleNet Hqql/Tbl task

## Phase 1 statistics

```bash
PHASE1_STAGE=medium \
MICRO_BATCH=64 \
KNN_MICRO_BATCH=128 \
CHECKPOINT="local_checkpoints/part/ParticleNet_kinpid.pt" \
MODE=kinpid \
JETCLASS_TINY="$HOME/Рабочий стол/jetclass_tiny_balanced" \
bash scripts/RUN_PHASE1_HQQL_TBL_FULL_STATISTICS_V1.sh
```

## Phase 2 physical swaps

```bash
PHASE2_STAGE=medium \
MICRO_BATCH=64 \
MAX_TARGETS=80 \
PATCH_K=8 \
CHECKPOINT="local_checkpoints/part/ParticleNet_kinpid.pt" \
MODE=kinpid \
JETCLASS_TINY="$HOME/Рабочий стол/jetclass_tiny_balanced" \
bash scripts/RUN_PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.sh
```

## Phase 3 isolation controls

Fast observable-only run:

```bash
PHASE3_MODE=only-3c \
bash scripts/RUN_PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.sh
```

Full controls:

```bash
PHASE3_MODE=all \
PHASE3_STAGE=medium \
MICRO_BATCH=64 \
KNN_MICRO_BATCH=128 \
MAX_TARGETS=100 \
PATCH_K=8 \
CHECKPOINT="local_checkpoints/part/ParticleNet_kinpid.pt" \
MODEL_MODE=kinpid \
JETCLASS_TINY="$HOME/Рабочий стол/jetclass_tiny_balanced" \
bash scripts/RUN_PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.sh
```

## Residual V2

```bash
bash scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2.sh
```

## Residual V2.1 behavior surrogate

```bash
bash scripts/RUN_KNOWN_OBSERVABLE_RESIDUAL_V2_1_BEHAVIOR.sh
```

## Main source tools

```text
tools/hqql_tbl_confusion_physics_regime_v1.py
tools/phase2_hqql_tbl_physical_swaps_v1.py
tools/phase3_hqql_tbl_isolation_controls_v1.py
tools/known_observable_residual_v2.py
tools/known_observable_residual_v2_1_behavior.py
```

## Current next command after this organization

Next scientific step is Residual V3:

```text
known_observable_residual_v3_pairwise_subjet_geometry
```

It should add pairwise/subjet/b-like geometry features.
