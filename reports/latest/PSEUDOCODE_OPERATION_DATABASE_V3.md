# Pseudocode Operation Database v3

Route-aware pseudocode. This merges semantic pseudocode, code/output alignment, question rankings, and EdgeConv inner trace events.

## Top route-aware rows
| head | route_role | questions | top_labels | event_core | knn_core | residual |
| --- | --- | --- | --- | --- | --- | --- |
| L0_ch40:48 | context builder / relay away from direct core readout | Q1_core_readout, Q2_local_builders, Q4_trace_priority | label_Hgg:2, label_Hcc:1, label_QCD:1, label_Wqq:1 | 0.0000 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L0_ch0:8 | context builder / relay away from direct core readout | Q2_local_builders, Q3_residual_axis, Q4_trace_priority |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch48:56 | context builder / relay away from direct core readout | Q2_local_builders, Q3_residual_axis, Q4_trace_priority |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch16:24 | context builder / relay away from direct core readout | Q2_local_builders, Q3_residual_axis |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch24:32 | context builder / relay away from direct core readout | Q2_local_builders |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch8:16 | context builder / relay away from direct core readout | Q2_local_builders |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch56:64 | context builder / relay away from direct core readout |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L0_ch32:40 | context builder / relay away from direct core readout |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch16:32 | context builder / relay away from direct core readout | Q2_local_builders, Q4_trace_priority |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch32:48 | context builder / relay away from direct core readout | Q2_local_builders, Q3_residual_axis, Q4_trace_priority |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch112:128 | context builder / relay away from direct core readout | Q1_core_readout, Q2_local_builders, Q3_residual_axis, Q4_trace_priority | label_Hcc:2, label_Tbl:2, label_Wqq:1, label_Hgg:1 | 0.2500 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L1_ch0:16 | context builder / relay away from direct core readout | Q1_core_readout | label_Tbl:4, label_QCD:2, label_Hcc:1, label_Tbqq:1 | 0.1250 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L1_ch96:112 | context builder / relay away from direct core readout |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch64:80 | context builder / relay away from direct core readout | Q2_local_builders |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch80:96 | context builder / relay away from direct core readout |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L1_ch48:64 | context builder / relay away from direct core readout |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |
| L2_ch128:160 | route-aware late core readout | Q1_core_readout, Q3_residual_axis, Q4_trace_priority | label_Tbl:8 | 1.0000 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch224:256 | route-aware late core readout | Q1_core_readout, Q3_residual_axis, Q4_trace_priority | label_Tbl:7, label_Hqql:1 | 1.0000 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch0:32 | late readout moderately core-aligned | Q1_core_readout, Q3_residual_axis, Q4_trace_priority | label_Tbl:6, label_Tbqq:2 | 0.7500 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch64:96 | route-aware late core readout | Q1_core_readout, Q3_residual_axis, Q4_trace_priority | label_Tbl:6, label_Hqql:2 | 1.0000 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch160:192 | route-aware late core readout | Q1_core_readout, Q3_residual_axis | label_Tbl:7, label_Tbqq:1 | 0.8750 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch32:64 | route-aware late core readout | Q1_core_readout | label_Tbl:7, label_Tbqq:1 | 0.8750 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch192:224 | late readout moderately core-aligned | Q1_core_readout | label_Tbqq:5, label_Tbl:3 | 0.3750 | 0.0000 | RESIDUAL_SIGNAL_REMAINS |
| L2_ch96:128 | late readout with distributed/non-core particle evidence |  |  | n/a | n/a | RESIDUAL_SIGNAL_REMAINS |

## Full route-aware pseudocode

### L0_ch40:48 — context builder / relay away from direct core readout

Questions: Q1_core_readout, Q2_local_builders, Q4_trace_priority

Code: edge_convs.0 / output[:, 40:48, :]

Inner trace: top_event_particle0=0.0000, top_event_leading=0.0000, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Hgg:2, label_Hcc:1, label_QCD:1, label_Wqq:1

```python
# L0_ch40:48: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: label_Hgg:2, label_Hcc:1, label_QCD:1, label_Wqq:1
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch0:8 — context builder / relay away from direct core readout

Questions: Q2_local_builders, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.0 / output[:, 0:8, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch0:8: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch48:56 — context builder / relay away from direct core readout

Questions: Q2_local_builders, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.0 / output[:, 48:56, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch48:56: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch16:24 — context builder / relay away from direct core readout

Questions: Q2_local_builders, Q3_residual_axis

Code: edge_convs.0 / output[:, 16:24, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch16:24: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch24:32 — context builder / relay away from direct core readout

Questions: Q2_local_builders

Code: edge_convs.0 / output[:, 24:32, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch24:32: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch8:16 — context builder / relay away from direct core readout

Questions: Q2_local_builders

Code: edge_convs.0 / output[:, 8:16, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch8:16: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch56:64 — context builder / relay away from direct core readout

Questions: 

Code: edge_convs.0 / output[:, 56:64, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch56:64: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch32:40 — context builder / relay away from direct core readout

Questions: 

Code: edge_convs.0 / output[:, 32:40, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L0_ch32:40: route-aware L0 local builder
for particle i:
    neighbors = knn(i, k=16)
    edge = compare_raw_particle_features(i, neighbors)
    local_pattern = detect_local_pid_pt_radial_edge(edge)
    write_L0_local_pattern(local_pattern)
    # role: context builder / relay away from direct core readout; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch16:32 — context builder / relay away from direct core readout

Questions: Q2_local_builders, Q4_trace_priority

Code: edge_convs.1 / output[:, 16:32, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch16:32: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch32:48 — context builder / relay away from direct core readout

Questions: Q2_local_builders, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.1 / output[:, 32:48, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch32:48: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch112:128 — context builder / relay away from direct core readout

Questions: Q1_core_readout, Q2_local_builders, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.1 / output[:, 112:128, :]

Inner trace: top_event_particle0=0.2500, top_event_leading=0.2500, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Hcc:2, label_Tbl:2, label_Wqq:1, label_Hgg:1

```python
# L1_ch112:128: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=0.2500
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch0:16 — context builder / relay away from direct core readout

Questions: Q1_core_readout

Code: edge_convs.1 / output[:, 0:16, :]

Inner trace: top_event_particle0=0.1250, top_event_leading=0.1250, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:4, label_QCD:2, label_Hcc:1, label_Tbqq:1

```python
# L1_ch0:16: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=0.1250
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch96:112 — context builder / relay away from direct core readout

Questions: 

Code: edge_convs.1 / output[:, 96:112, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch96:112: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch64:80 — context builder / relay away from direct core readout

Questions: Q2_local_builders

Code: edge_convs.1 / output[:, 64:80, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch64:80: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch80:96 — context builder / relay away from direct core readout

Questions: 

Code: edge_convs.1 / output[:, 80:96, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch80:96: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch48:64 — context builder / relay away from direct core readout

Questions: 

Code: edge_convs.1 / output[:, 48:64, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L1_ch48:64: route-aware L1 context relay
for particle i:
    neighbors = knn(i, k=16)
    l0_context = read_L0_edge_features(i, neighbors)
    route_context = mix_core_and_secondary(l0_context)
    write_L1_context(route_context)
    # role: context builder / relay away from direct core readout; top_event_particles_core_rate=n/a
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch128:160 — route-aware late core readout

Questions: Q1_core_readout, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.2 / output[:, 128:160, :]

Inner trace: top_event_particle0=1.0000, top_event_leading=1.0000, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:8

```python
# L2_ch128:160: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=1.0000, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: route-aware late core readout; classes: label_Tbl:8
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch224:256 — route-aware late core readout

Questions: Q1_core_readout, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.2 / output[:, 224:256, :]

Inner trace: top_event_particle0=1.0000, top_event_leading=1.0000, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:7, label_Hqql:1

```python
# L2_ch224:256: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=1.0000, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: route-aware late core readout; classes: label_Tbl:7, label_Hqql:1
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch0:32 — late readout moderately core-aligned

Questions: Q1_core_readout, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.2 / output[:, 0:32, :]

Inner trace: top_event_particle0=0.7500, top_event_leading=0.7500, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:6, label_Tbqq:2

```python
# L2_ch0:32: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=0.7500, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: late readout moderately core-aligned; classes: label_Tbl:6, label_Tbqq:2
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch64:96 — route-aware late core readout

Questions: Q1_core_readout, Q3_residual_axis, Q4_trace_priority

Code: edge_convs.2 / output[:, 64:96, :]

Inner trace: top_event_particle0=1.0000, top_event_leading=1.0000, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:6, label_Hqql:2

```python
# L2_ch64:96: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=1.0000, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: route-aware late core readout; classes: label_Tbl:6, label_Hqql:2
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch160:192 — route-aware late core readout

Questions: Q1_core_readout, Q3_residual_axis

Code: edge_convs.2 / output[:, 160:192, :]

Inner trace: top_event_particle0=0.8750, top_event_leading=0.8750, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:7, label_Tbqq:1

```python
# L2_ch160:192: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=0.8750, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: route-aware late core readout; classes: label_Tbl:7, label_Tbqq:1
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch32:64 — route-aware late core readout

Questions: Q1_core_readout

Code: edge_convs.2 / output[:, 32:64, :]

Inner trace: top_event_particle0=0.8750, top_event_leading=0.8750, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbl:7, label_Tbqq:1

```python
# L2_ch32:64: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=0.8750, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: route-aware late core readout; classes: label_Tbl:7, label_Tbqq:1
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch192:224 — late readout moderately core-aligned

Questions: Q1_core_readout

Code: edge_convs.2 / output[:, 192:224, :]

Inner trace: top_event_particle0=0.3750, top_event_leading=0.3750, knn_has_particle0=0.0000, knn_has_leading=0.0000

Top event labels: label_Tbqq:5, label_Tbl:3

```python
# L2_ch192:224: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=0.3750, knn_has_core=0.0000):
        logits += project_class_evidence(evidence)
    # role: late readout moderately core-aligned; classes: label_Tbqq:5, label_Tbl:3
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch96:128 — late readout with distributed/non-core particle evidence

Questions: 

Code: edge_convs.2 / output[:, 96:128, :]

Inner trace: top_event_particle0=n/a, top_event_leading=n/a, knn_has_particle0=n/a, knn_has_leading=n/a

Top event labels: 

```python
# L2_ch96:128: route-aware L2 readout
for event:
    top_particle = select_particle_by_head_output()
    neighbors = knn(top_particle, k=16)
    context = read_L1_context(top_particle, neighbors)
    evidence = aggregate_context(context)
    if route_matches_core(top_particle_rate=n/a, knn_has_core=n/a):
        logits += project_class_evidence(evidence)
    # role: late readout with distributed/non-core particle evidence; classes: 
```

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2
