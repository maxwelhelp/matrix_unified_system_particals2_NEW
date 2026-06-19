# INTERNAL_DATA_INVENTORY_FOR_CONTRAST

The local search confirmed that internal trace data already exists.

## Existing files

```text
reports/latest/PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md
reports/latest/HEAD_OUTPUT_TRACE_V1.md
reports/latest/CLASS_SPECIFIC_ALL_HEAD_GRADIENTS_V1.md
reports/latest/FULL_HEAD_QUESTION_CATALOG.md
reports/latest/PARTICLENET_HEAD_PROJECTION_COMPOSER_V2.md
```

Important tables:

```text
reports/latest/tables/all_head_supertrace_events.csv
reports/latest/tables/all_head_supertrace_particles.csv
reports/latest/tables/all_head_gate_gradients.csv
reports/latest/tables/head_output_trace.csv
reports/latest/tables/class_specific_head_gradients.csv
reports/latest/tables/class_specific_head_gradient_summary.csv
reports/latest/tables/full_head_question_catalog.csv
reports/latest/tables/head_projection_question_map.csv
```

## What these files already contain

### all_head_supertrace_events.csv

Event-level trace summary:

```text
event_idx,true_label,pred_label,conf,pred_logit,super_max_particle_score,top_particle_indices
```

### all_head_supertrace_particles.csv

Particle-level trace summary:

```text
event_idx,particle_idx,super_score,pid/pT/charge/geometry features
```

### all_head_gate_gradients.csv

Global head/group gradient importance:

```text
layer,group_id,channels,grad,abs_grad,head_id
```

Important heads already visible:

```text
L2_ch224:256
L2_ch128:160
L2_ch160:192
```

### class_specific_head_gradients.csv

Class-specific head importance.

For Hqql, top heads include:

```text
L2_ch128:160
L2_ch0:32
L2_ch160:192
L2_ch64:96
```

For Tbl, top summary also points to:

```text
L2_ch128:160
```

## Important limitation

These files are enough to rank/prioritize heads and particles, but they do not appear to contain full per-event × per-head activation means for A/B/C contrast.

Therefore:

```text
V0 = reader/aggregator from existing tables
V1 = lightweight extractor for A/B/C internal activations
```

## Next implementation

Build:

```text
tools/internal_activation_contrast_v1.py
```

It should first try to read existing tables. If full activation table is missing, it should report that and recommend running a small extractor only for A/B/C events.
