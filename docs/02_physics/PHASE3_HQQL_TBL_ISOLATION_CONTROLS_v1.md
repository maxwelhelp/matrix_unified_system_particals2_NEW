# Phase 3 Hqql/Tbl Isolation Controls v1

Phase 2 showed the right direction but not a clean causal proof:

```text
2A hadronic injection > random_same_count, but the gap is modest.
```

Therefore Phase 3 focuses on isolating the physical variable.

## 3C — Isolation as continuous predictor

Use Phase 1 event table only. No patching.

For all true Hqql events:

```text
Hqql_correct + Hqql_to_Tbl
```

Bin by particle0 isolation proxy:

```text
0.00-0.10
0.10-0.15
0.15-0.20
0.20-0.30
0.30+
```

Measure:

```text
confusion_rate = Hqql_to_Tbl / all_Hqql_in_bin
```

If confusion rate rises with isolation, the physical observable is meaningful:

```text
isolated lepton/core route makes Hqql look Tbl-like.
```

## 3A — Matched PID / QCD control

For Hqql_to_Tbl events:

```text
3A_real_hqql_hadron:
  inject hadronic neighbors from matched Hqql_correct events

3A_control_qcd_hadron:
  inject hadronic neighbors from matched QCD events
```

If real Hqql hadronic context beats QCD matched hadrons, the effect is not just perturbation size.

## 3B — Hadron fraction sweep

For Hqql_to_Tbl events:

```text
fraction = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
```

Replace that fraction of KNN neighbors with Hqql_correct hadronic neighbors.

If success_to_Hqql rises monotonically with fraction, then hadronic density/context is the mechanism.

## Outputs

```text
reports/latest/PHASE3_HQQL_TBL_ISOLATION_CONTROLS_V1.md
reports/latest/tables/phase3_hqql_tbl_isolation_bins.csv
reports/latest/tables/phase3_hqql_tbl_matched_controls.csv
reports/latest/tables/phase3_hqql_tbl_sweep.csv
manifests/latest/phase3_hqql_tbl_isolation_controls_v1.json
```
