# Phase experiments map

## Phase 1 — Confusion regime statistics

Goal:

```text
Get enough Hqql_to_Tbl and Tbl_to_Hqql events.
```

Key outputs:

```text
reports/latest/HQQL_TBL_CONFUSION_PHYSICS_REGIME_V1.md
reports/latest/PHASE1_HQQL_TBL_STATS_GATE_V1.md
reports/latest/tables/hqql_tbl_confusion_physics_events.csv
reports/latest/tables/hqql_tbl_confusion_physics_summary.csv
```

Result:

```text
Hqql_to_Tbl = 154
Tbl_to_Hqql = 145
PASS
```

## Phase 2 — Physical swaps / route causality

Goal:

```text
Test lepton/core swap, neighbor swap, hadronic injection.
```

Key outputs:

```text
reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md
reports/latest/tables/phase2_hqql_tbl_physical_swaps.csv
reports/latest/tables/phase2_hqql_tbl_physical_swaps_summary.csv
```

Result:

```text
2A hadronic injection: success_to_Hqql = 0.6200
random_same_count: success_to_Hqql = 0.5333
2C neighbor swap: weaker than random
```

Interpretation:

```text
Patch direction is suggestive, but random perturbation is too strong.
Need stricter controls.
```

## Phase 3 — Isolation controls

Goal:

```text
Test whether isolation itself predicts Hqql->Tbl behavior.
```

Key outputs:

```text
reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md
reports/latest/tables/phase3_hqql_tbl_isolation_bins.csv
reports/latest/tables/phase3_hqql_tbl_matched_controls_summary.csv
reports/latest/tables/phase3_hqql_tbl_sweep_summary.csv
```

Result:

```text
confusion rate rises from 0.0264 to 0.2558 across isolation bins.
```

Interpretation:

```text
This is the cleanest observable signal so far.
```
