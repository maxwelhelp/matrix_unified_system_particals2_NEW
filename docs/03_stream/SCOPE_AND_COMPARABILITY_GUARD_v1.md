# Scope and Comparability Guard v1

This document fixes an important methodology risk:

```text
Do not compare a local control-run delta as if it were a global stream/dynamics change.
```

## Why this matters

The project now has several evidence layers:

```text
stream history over many snapshots
latest stream snapshot
local particle0/top-k control run
relation graph
comparison rows
feature embeddings
```

These are not all directly comparable.

## Correct comparison scopes

### 1. Local control-run scope

Examples:

```text
remove_particle0 vs baseline
keep_only_particle0 vs baseline
remove_top-k vs random_remove-k
```

These are valid only inside the same control run:

```text
same model
same batch/files
same labels
same preprocessing
same baseline logits
```

Allowed claim:

```text
In this control-run batch, particle0 removal caused X drop compared with the same-run baseline/random control.
```

Not allowed:

```text
This delta is a global stream trend.
```

### 2. Stream-history scope

Examples:

```text
head rank over snapshots
particle0 dominance over snapshots
Hqql/Tbl concentration over snapshots
```

Allowed claim:

```text
Across stream snapshots, this signal is stable/unstable.
```

Not allowed:

```text
A control-run delta from one batch proves a stream-wide trend.
```

### 3. Latest-stream relation scope

Examples:

```text
pattern:particle0 -> class:Hqql
head:L1_ch112:128 -> AH4
```

These are relation/prioritization signals. They are not causal proof.

### 4. Cross-scope comparison

Allowed only when explicitly labelled:

```text
stream suggested particle0 dominance
local control confirmed particle0 causality on matched control batch
remaining question: heldout/order/residual
```

This is a comparison of evidence types, not a direct numeric delta across all data.

## Embedding rule

Every embedding row must be treated as one of:

```text
history_stream
latest_stream
control_run_local
comparison_meta
relation_meta
```

A model/agent should not mix scopes unless the feature says it is allowed.

## Guard output

The guard produces:

```text
manifests/latest/scope_comparability_guard_v1.json
reports/latest/SCOPE_COMPARABILITY_GUARD_V1.md
reports/latest/tables/scope_comparability_checks.csv
reports/latest/tables/scoped_feature_manifest.csv
```

## Decision rule

A strong claim needs:

```text
stream signal
+ local causal control
+ heldout/per-file stability
+ order/shuffle control
+ known-observable residual
```

Without all of these, the claim remains a mechanism candidate, not a discovery claim.
