# Order + Confusion Summary v1

## Current result

The order control and confusion atlas were completed after the particle0/top-k controls.

## Order control

Run state:

```text
n_events = 2560
baseline_acc = 0.7574
verdict = ORDER_INVARIANT_OR_NEAR_INVARIANT
```

Important checks:

```text
reverse:              acc 0.7574, flip 0.0000
particle0_to_end:     acc 0.7574, flip 0.0000
particle0_to_middle:  acc 0.7574, flip 0.0000
sort_pt_desc:         acc 0.7574, flip 0.0000
sort_pt_asc:          acc 0.7574, flip 0.0000
random_shuffle:       acc 0.7574, flip 0.0000
```

Interpretation:

```text
The particle0/top-k effect is not explained by literal array position.
ParticleNet is effectively permutation invariant in this control.
The remaining risk is not index order; it is known-observable proxy or class-specific shortcut.
```

## Confusion atlas

Global control summary:

```text
remove_particle0:    acc 0.5633, flip 0.3160
keep_only_particle0: acc 0.2027, flip 0.7941
remove_top4:         acc 0.3492, flip 0.5922
keep_top4:           acc 0.2922, flip 0.7004
remove_top16:        acc 0.1980, flip 0.7871
keep_top16:          acc 0.5391, flip 0.4051
```

Main class transitions after remove_particle0:

```text
Hqql -> H4q
Tbl  -> QCD / Hbb / Tbqq
Zqq  -> H4q / Wqq
Wqq  -> Zqq / H4q
```

Main class transitions after keep_only_particle0:

```text
Hqql -> Tbl
many classes -> Wqq/QCD-like alternatives
```

Main transitions after remove_top16:

```text
Tbl, Hqql, Wqq, Zqq, Hcc -> QCD
```

## Updated interpretation

Current best model:

```text
leading/core top-k content is causally important;
it is not a simple array-index artifact;
it is not sufficient alone globally;
class-specific context is needed for Hqql/Tbl and nearby class separation.
```

## Updated statuses

```text
AH1 core-anchor + context:
  SUPPORTED_BY_TARGETED_CONTROL_AND_ORDER_CONTROL

AH2 Hqql/Tbl signature:
  SUPPORTED_BY_CONTROL_AND_CONFUSION_ATLAS

Global particle0-only shortcut:
  REJECTED_AS_GLOBAL_EXPLANATION

Class-local proxy risk:
  STILL_ACTIVE_FOR_TBL/HQQL
```

## Remaining P0

```text
known-observable residual
class-specific all-head gradients
per-file/heldout stability
class-distribution check
```

## Next coding priorities

```text
1. KNOWN_OBSERVABLE_RESIDUAL_V1
2. CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1
3. PER_FILE_HELDOUT_STABILITY_V1
4. CROSS_MODEL_AGREEMENT_V1
```
