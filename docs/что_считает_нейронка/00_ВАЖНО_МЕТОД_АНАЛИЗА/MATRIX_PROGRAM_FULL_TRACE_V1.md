# MATRIX_PROGRAM_FULL_TRACE_V1

## Goal

Build an automatic full matrix-program trace for all pseudo-heads, not one head at a time.

The goal is to see the whole path:

```text
particle role -> L0/L1/L2 pseudo-head -> class direction / logit contribution
```

and compare the path across groups:

```text
A = protected/correct source class
B = confused source -> target
C = correct target class
```

For Hqql/Tbl:

```text
A = Hqql_correct_highiso
B = Hqql_to_Tbl_highiso
C = Tbl_correct
```

## Why this matters

Previous direct probes found a split mechanism:

```text
L1_ch80:96:
  anomalous hard/hadron route in B

L2_ch128:160:
  loss of Hqql evidence in B
```

But this was still head-by-head.

Full trace should automatically identify all paths:

```text
confusion_triggers
hqql_loss_paths
anomalous_paths
```

## What V1 computes

For each pseudo-head/channel slice in L0/L1/L2:

```text
head_id
layer
channels
activation by group A/B/C
class contribution by zero-slice ablation
approx class projection when available
top particle roles by group
```

For each event it writes a graph:

```text
particle_role -> head -> class
```

where edge weights are based on:

```text
particle->head edge = particle activation norm in that head
head->class edge = logit drop when that head is zeroed
```

For all groups it aggregates mean flow:

```text
mean_flow_A[particle_role, head, class]
mean_flow_B[particle_role, head, class]
mean_flow_C[particle_role, head, class]
```

## Path ranking

V1 ranks paths by:

```text
trigger_score:
  |flow_B - flow_A| and B similar to C

loss_score:
  flow_A - flow_B for source-class direction

anomaly_score:
  |flow_B - flow_A| * |flow_B - flow_C|
```

For Hqql/Tbl, an anomalous path is very important because current evidence suggests:

```text
B is not normal Tbl.
B is a third topology / imitation-confound.
```

## Output

```text
reports/latest/MATRIX_PROGRAM_FULL_TRACE_V1.md
reports/latest/tables/matrix_program_database_v1.csv
reports/latest/tables/matrix_program_paths_v1.csv
reports/latest/tables/matrix_program_particle_role_flow_v1.csv
reports/latest/tables/matrix_program_head_summary_v1.csv
reports/latest/particle_flow_graphs_v1/*.json
manifests/latest/matrix_program_full_trace_v1.json
```

## Important limitation

V1 is a robust first automatic trace, not the final exact mathematical decompiler.

It uses:

```text
activation hooks
particle activation norms
zero-slice ablation for class contribution
approx source/flow from activations
```

Exact source-block decomposition from EdgeConv internal weights should be added in V2 after confirming module internals for every model variant.

## Required interpretation

Do not read any path alone.

Always compare:

```text
B vs A
B vs C
```

Diagnoses:

```text
B != A and B ~= C:
  target-like trigger

B << A on source class:
  source evidence loss

B != A and B != C:
  anomalous third-topology mechanism
```
