# Phase 2 Hqql/Tbl Physical Swaps v1

Phase 1 passed: enough Hqql<->Tbl confused events exist to study physical regimes.

Main Phase 1 signal:

```text
Hqql_to_Tbl has higher particle0 isolation than Hqql_correct.
```

Working hypothesis:

```text
When the leptonic/core particle in Hqql is too isolated from hadronic/KNN context, ParticleNet reads it as Tbl-like and loses Hqql evidence.
```

## Phase 2 tests

### 2A — Isolation / hadronic-neighbor patch

Target:

```text
true Hqql, pred Tbl
```

Patch:

```text
keep particle0/lepton fixed
replace KNN neighbors around particle0 with hadronic neighbors from matched Hqql_correct event
```

Question:

```text
Does adding Hqql-like hadronic context around the same lepton/core restore Hqql prediction?
```

### 2B — Lepton/core swap

Target:

```text
true Tbl, pred Tbl
```

Patch:

```text
replace particle0/lepton with particle0/lepton from matched Hqql_correct event
keep Tbl neighbors/context unchanged
```

Question:

```text
Does the lepton itself distinguish Hqql vs Tbl?
```

### 2C — Neighbor swap

Target:

```text
true Hqql, pred Tbl
```

Patch:

```text
keep target particle0/lepton unchanged
replace only KNN neighbors with matched Hqql_correct KNN neighbors
```

Question:

```text
Does secondary KNN context causally restore Hqql?
```

## Metrics

Primary:

```text
flip_rate: targeted prediction changes toward Hqql/Tbl as expected
```

Secondary:

```text
delta_margin = (Hqql_logit - Tbl_logit)_patched - (Hqql_logit - Tbl_logit)_baseline
```

Control:

```text
random_same_count patch
```

Strong support:

```text
targeted_flip_rate / random_flip_rate > 3x
and targeted_delta_margin > random_delta_margin
```

## Outputs

```text
reports/latest/PHASE2_HQQL_TBL_PHYSICAL_SWAPS_V1.md
reports/latest/tables/phase2_hqql_tbl_physical_swaps.csv
reports/latest/tables/phase2_hqql_tbl_physical_swaps_summary.csv
manifests/latest/phase2_hqql_tbl_physical_swaps_v1.json
```
