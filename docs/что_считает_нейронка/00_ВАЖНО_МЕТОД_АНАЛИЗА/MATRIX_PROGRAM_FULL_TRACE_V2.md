# MATRIX_PROGRAM_FULL_TRACE_V2

## Status

This is the strict version requested after V1.

V1 was useful but incomplete:

```text
V1 = postprocessor over V2/V2.1 outputs
V2 = direct model run + all heads + per-event graphs + exact/validated source-block attempt
```

## Required guarantees

V2 must not pretend approximation is exact.

For every pseudo-head it writes:

```text
exact_source_status = OK / FAILED
exact_source_note
```

If EdgeConv weight parsing fails, the report must say so and still complete all activation/ablation/graph outputs.

## Steps

### STEP 1 — All heads

Trace all pseudo-head slices in L0/L1/L2.

Default slices:

```text
L0: 0:32,32:64,64:96,96:128,128:160,160:192,192:224,224:256
L1: 0:32,32:64,64:96,96:128,128:160,160:192,192:224,224:256
L2: 0:32,32:64,64:96,96:128,128:160,160:192,192:224,224:256
```

Invalid slices that exceed actual activation channels are skipped with status.

### STEP 2 — Exact source-block decomposition

Try to parse EdgeConv internal Conv weights directly from `model.edge_convs[layer]`.

Output per head:

```text
source_block_1..source_block_5
source_block_weight_1..source_block_weight_5
exact_source_status
exact_source_note
```

### STEP 3 — Per-event particle flow graph

For each A/B/C event:

```text
particle_i -> head_j -> class
```

Save JSON per event.

### STEP 4 — Ranked paths

Output separate CSVs:

```text
top_confusion_triggers_v2.csv
top_hqql_loss_paths_v2.csv
top_anomalous_paths_v2.csv
```

### STEP 5 — Auto-formulation

For top paths, write a readable interpretation:

```text
PATH: particle_role -> head -> class
DIAGNOSIS: trigger/loss/anomaly
PHYSICAL MEANING: ...
NEXT PROBE: ...
```

## Output

```text
reports/latest/MATRIX_PROGRAM_FULL_TRACE_V2.md
reports/latest/tables/matrix_program_database_v2.csv
reports/latest/tables/matrix_program_particle_role_flow_v2.csv
reports/latest/tables/top_confusion_triggers_v2.csv
reports/latest/tables/top_hqql_loss_paths_v2.csv
reports/latest/tables/top_anomalous_paths_v2.csv
reports/latest/particle_flow_graphs_v2/*.json
manifests/latest/matrix_program_full_trace_v2.json
```

## Interpretation rule

A path is only strong if it is supported by:

```text
activation flow
zero-slice class contribution
A/B/C contrast
reasonable particle role
```

Do not rely only on a single scalar score.
