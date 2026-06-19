# MATRIX_PROGRAM_FULL_TRACE_V3 — all heads

## Purpose

Analyze all pseudo-head/channel slices, not only suspicious heads.

Default:

```text
layers = L0,L1,L2
slice_size = 32
heads = 24 total
```

Optional:

```text
slice_size = 16 -> 48 heads
slice_size = 8  -> 96 heads
```

## Groups

```text
A = protected_highiso Hqql->Hqql
B = confused_highiso Hqql->Tbl
C = Tbl_correct
```

## For every head

V3 computes:

```text
activation norms A/B/C
class-direction projection for all classes
Hqql/Tbl projection summary
zero-slice ablation contribution for all classes
Hqql/Tbl ablation summary
top particle role rates A/B/C
automatic diagnosis:
  active_tbl_trigger
  hqql_loss
  anomalous_third_topology
  neutral_or_weak
```

## Key idea

A head is interpreted as a matrix program:

```text
read source blocks / KNN context
project to channel slice
write route or class evidence
move class directions
activate on particle roles
```

The output should show the whole network map:

```text
which heads build wrong route
which heads lose Hqql evidence
which heads are anomalous third-topology heads
which heads are neutral
```

## Outputs

```text
reports/latest/MATRIX_PROGRAM_FULL_TRACE_V3_SUMMARY.md
reports/latest/tables/matrix_program_full_trace_v3_all_heads_database.csv
reports/latest/tables/matrix_program_full_trace_v3_all_heads_ranked.csv
reports/latest/tables/matrix_program_full_trace_v3_top_particle_roles.csv
reports/latest/tables/matrix_program_full_trace_v3_event_head_rows.csv
manifests/latest/matrix_program_full_trace_v3.json
```

## After run

Use this file as the all-head map for Hqql/Tbl. Then the same tool can be adapted to other class pairs from the stream monitor, such as Zqq/Wqq or Hbb/Hcc.
