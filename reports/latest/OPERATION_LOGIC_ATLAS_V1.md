# Operation Logic Atlas v1

Evidence-grounded semantic pseudocode for ParticleNet pseudo-head channel groups. This is not literal source code; it is a compact explanation of likely operations after previous layer transformations.

## Summary table
| head | stage | class question | operation | evidence |
| --- | --- | --- | --- | --- |
| L0_ch0:8 | early local edge/particle feature reader | Hqql/Tbl core-confusion axis | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_H4q=1.1571, label_Hqql=0.5866, label_QCD=0.5120 | global_gate_abs=0.2042 | relation_hits=3 | stream_hits=30 |
| L0_ch16:24 | early local edge/particle feature reader | Tbl leading-core signature | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_H4q=0.9509, label_Tbl=0.3513, label_Hcc=0.3307 | global_gate_abs=0.0896 | relation_hits=2 | stream_hits=30 |
| L0_ch24:32 | early local edge/particle feature reader | Hqql core/top-k separation | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_Wqq=0.7906, label_Hqql=0.3870, label_H4q=0.2608 | global_gate_abs=0.2271 | relation_hits=2 | stream_hits=30 |
| L0_ch32:40 | early local edge/particle feature reader | W/Z two-prong-like separation | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_QCD=0.2724, label_Hcc=0.2370, label_Zqq=0.1604 | global_gate_abs=0.1125 | relation_hits=2 | stream_hits=30 |
| L0_ch40:48 | early local edge/particle feature reader | Hqql core/top-k separation | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_Wqq=1.1670, label_Zqq=0.9496, label_Hcc=0.9443 | global_gate_abs=0.7156 | relation_hits=2 | stream_hits=30 |
| L0_ch48:56 | early local edge/particle feature reader | Tbl leading-core signature | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_H4q=0.9793, label_QCD=0.8989, label_Tbl=0.8825 | global_gate_abs=0.3769 | relation_hits=2 | stream_hits=30 |
| L0_ch56:64 | early local edge/particle feature reader | Hqql core/top-k separation | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_Hqql=0.4484, label_H4q=0.3784, label_Zqq=0.2666 | global_gate_abs=0.0186 | relation_hits=3 | stream_hits=30 |
| L0_ch8:16 | early local edge/particle feature reader | Tbl leading-core signature | read local particle-edge geometry, PID/charge, pt/radial summaries; residual not fully explained by simple known observables | class_grad:label_Tbl=0.7731, label_Hcc=0.7574, label_Zqq=0.6469 | global_gate_abs=0.3577 | relation_hits=2 | stream_hits=30 |
| L1_ch0:16 | middle neighborhood/context relay | Hqql core/top-k separation | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_H4q=0.5761, label_Zqq=0.2802, label_Hcc=0.2169 | global_gate_abs=0.0146 | relation_hits=3 | stream_hits=30 |
| L1_ch112:128 | middle neighborhood/context relay | H4q/multi-prong attractor separation | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_Hcc=1.2414, label_H4q=0.9725, label_Wqq=0.9042 | global_gate_abs=0.8689 | relation_hits=2 | stream_hits=30 |
| L1_ch16:32 | middle neighborhood/context relay | H4q/multi-prong attractor separation | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_Wqq=1.6597, label_Zqq=1.0984, label_H4q=0.9520 | global_gate_abs=0.7480 | relation_hits=2 | stream_hits=30 |
| L1_ch32:48 | middle neighborhood/context relay | Hqql/Tbl core-confusion axis | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_Tbl=1.3994, label_QCD=0.5415, label_Hqql=0.5251 | global_gate_abs=0.2108 | relation_hits=2 | stream_hits=30 |
| L1_ch48:64 | middle neighborhood/context relay | Tbl leading-core signature | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_Hcc=0.1854, label_Tbl=0.1819, label_QCD=0.0978 | global_gate_abs=0.1366 | relation_hits=2 | stream_hits=30 |
| L1_ch64:80 | middle neighborhood/context relay | H4q/multi-prong attractor separation | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_QCD=0.5339, label_Wqq=0.4825, label_Zqq=0.3464 | global_gate_abs=0.1835 | relation_hits=3 | stream_hits=30 |
| L1_ch80:96 | middle neighborhood/context relay | Hqql/Tbl core-confusion axis | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_H4q=0.4375, label_Hqql=0.2887, label_Zqq=0.2790 | global_gate_abs=0.1692 | relation_hits=3 | stream_hits=30 |
| L1_ch96:112 | middle neighborhood/context relay | Hqql core/top-k separation | compose core particle with KNN/secondary context and route class evidence; residual not fully explained by simple known observables | class_grad:label_QCD=0.5720, label_Hcc=0.4957, label_Hqql=0.4296 | global_gate_abs=0.0286 | relation_hits=2 | stream_hits=30 |
| L2_ch0:32 | late class-evidence aggregation/readout | Hqql/Tbl core-confusion axis | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_H4q=1.0545, label_Tbl=1.0411, label_Hqql=0.6474 | global_gate_abs=0.2611 | relation_hits=2 | stream_hits=30 |
| L2_ch128:160 | late class-evidence aggregation/readout | Hqql/Tbl core-confusion axis | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Hqql=1.8701, label_Tbl=1.5447, label_Wqq=0.1695 | global_gate_abs=0.3421 | relation_hits=2 | stream_hits=30 |
| L2_ch160:192 | late class-evidence aggregation/readout | Hqql/Tbl core-confusion axis | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Hqql=0.4768, label_QCD=0.2924, label_H4q=0.2516 | global_gate_abs=0.0423 | relation_hits=3 | stream_hits=30 |
| L2_ch192:224 | late class-evidence aggregation/readout | Tbl leading-core signature | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Wqq=0.3293, label_Tbl=0.2347, label_Hcc=0.1566 | global_gate_abs=0.0369 | relation_hits=2 | stream_hits=30 |
| L2_ch224:256 | late class-evidence aggregation/readout | W/Z two-prong-like separation | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Wqq=1.1221, label_Zqq=1.0057, label_Hcc=0.7717 | global_gate_abs=0.7083 | relation_hits=2 | stream_hits=30 |
| L2_ch32:64 | late class-evidence aggregation/readout | Tbl leading-core signature | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Tbl=0.4565, label_Hcc=0.3231, label_QCD=0.1790 | global_gate_abs=0.1306 | relation_hits=3 | stream_hits=30 |
| L2_ch64:96 | late class-evidence aggregation/readout | Hqql/Tbl core-confusion axis | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_QCD=0.9095, label_Hqql=0.4053, label_Tbl=0.4048 | global_gate_abs=0.3056 | relation_hits=2 | stream_hits=30 |
| L2_ch96:128 | late class-evidence aggregation/readout | Tbl leading-core signature | aggregate class evidence before classifier and suppress/boost alternatives; residual not fully explained by simple known observables | class_grad:label_Tbl=0.2700, label_Hcc=0.1736, label_QCD=0.1453 | global_gate_abs=0.0666 | relation_hits=3 | stream_hits=30 |

## Pseudocode by head

### L0_ch0:8 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L0_ch0:8: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Hqql/Tbl core-confusion axis
```

**Evidence:** class_grad:label_H4q=1.1571, label_Hqql=0.5866, label_QCD=0.5120 | global_gate_abs=0.2042 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch16:24 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L0_ch16:24: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Tbl leading-core signature
```

**Evidence:** class_grad:label_H4q=0.9509, label_Tbl=0.3513, label_Hcc=0.3307 | global_gate_abs=0.0896 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch24:32 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Hqql core/top-k separation after prior layer transformations

```python
# L0_ch24:32: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Hqql core/top-k separation
```

**Evidence:** class_grad:label_Wqq=0.7906, label_Hqql=0.3870, label_H4q=0.2608 | global_gate_abs=0.2271 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch32:40 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for W/Z two-prong-like separation after prior layer transformations

```python
# L0_ch32:40: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports W/Z two-prong-like separation
```

**Evidence:** class_grad:label_QCD=0.2724, label_Hcc=0.2370, label_Zqq=0.1604 | global_gate_abs=0.1125 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch40:48 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Hqql core/top-k separation after prior layer transformations

```python
# L0_ch40:48: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Hqql core/top-k separation
```

**Evidence:** class_grad:label_Wqq=1.1670, label_Zqq=0.9496, label_Hcc=0.9443 | global_gate_abs=0.7156 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch48:56 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L0_ch48:56: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Tbl leading-core signature
```

**Evidence:** class_grad:label_H4q=0.9793, label_QCD=0.8989, label_Tbl=0.8825 | global_gate_abs=0.3769 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch56:64 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Hqql core/top-k separation after prior layer transformations

```python
# L0_ch56:64: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Hqql core/top-k separation
```

**Evidence:** class_grad:label_Hqql=0.4484, label_H4q=0.3784, label_Zqq=0.2666 | global_gate_abs=0.0186 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L0_ch8:16 — early local edge/particle feature reader

**Input state:** raw particle kinematics/PID + KNN edge coordinates

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L0_ch8:16: early reader
for particle i:
    edge = knn_edges(i)
    local = read(pt, deltaR, PID, charge, neighbor_features)
    write_local_features(local)  # supports Tbl leading-core signature
```

**Evidence:** class_grad:label_Tbl=0.7731, label_Hcc=0.7574, label_Zqq=0.6469 | global_gate_abs=0.3577 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch0:16 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for Hqql core/top-k separation after prior layer transformations

```python
# L1_ch0:16: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely Hqql core/top-k separation
```

**Evidence:** class_grad:label_H4q=0.5761, label_Zqq=0.2802, label_Hcc=0.2169 | global_gate_abs=0.0146 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch112:128 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for H4q/multi-prong attractor separation after prior layer transformations

```python
# L1_ch112:128: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely H4q/multi-prong attractor separation
```

**Evidence:** class_grad:label_Hcc=1.2414, label_H4q=0.9725, label_Wqq=0.9042 | global_gate_abs=0.8689 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch16:32 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for H4q/multi-prong attractor separation after prior layer transformations

```python
# L1_ch16:32: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely H4q/multi-prong attractor separation
```

**Evidence:** class_grad:label_Wqq=1.6597, label_Zqq=1.0984, label_H4q=0.9520 | global_gate_abs=0.7480 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch32:48 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L1_ch32:48: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely Hqql/Tbl core-confusion axis
```

**Evidence:** class_grad:label_Tbl=1.3994, label_QCD=0.5415, label_Hqql=0.5251 | global_gate_abs=0.2108 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch48:64 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L1_ch48:64: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely Tbl leading-core signature
```

**Evidence:** class_grad:label_Hcc=0.1854, label_Tbl=0.1819, label_QCD=0.0978 | global_gate_abs=0.1366 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch64:80 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for H4q/multi-prong attractor separation after prior layer transformations

```python
# L1_ch64:80: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely H4q/multi-prong attractor separation
```

**Evidence:** class_grad:label_QCD=0.5339, label_Wqq=0.4825, label_Zqq=0.3464 | global_gate_abs=0.1835 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch80:96 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L1_ch80:96: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely Hqql/Tbl core-confusion axis
```

**Evidence:** class_grad:label_H4q=0.4375, label_Hqql=0.2887, label_Zqq=0.2790 | global_gate_abs=0.1692 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L1_ch96:112 — middle neighborhood/context relay

**Input state:** L0 local edge features already mixed into particle-neighborhood embeddings

**Meaning:** candidate mechanism for Hqql core/top-k separation after prior layer transformations

```python
# L1_ch96:112: middle relay
for particle/neighborhood i:
    core = read_topk_core_and_neighbors(i)
    context = mix(core, radial_shape, secondary_particles)
    route_evidence(context)  # likely Hqql core/top-k separation
```

**Evidence:** class_grad:label_QCD=0.5720, label_Hcc=0.4957, label_Hqql=0.4296 | global_gate_abs=0.0286 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch0:32 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L2_ch0:32: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Hqql/Tbl core-confusion axis
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_H4q=1.0545, label_Tbl=1.0411, label_Hqql=0.6474 | global_gate_abs=0.2611 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch128:160 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L2_ch128:160: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Hqql/Tbl core-confusion axis
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Hqql=1.8701, label_Tbl=1.5447, label_Wqq=0.1695 | global_gate_abs=0.3421 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch160:192 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L2_ch160:192: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Hqql/Tbl core-confusion axis
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Hqql=0.4768, label_QCD=0.2924, label_H4q=0.2516 | global_gate_abs=0.0423 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch192:224 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L2_ch192:224: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Tbl leading-core signature
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Wqq=0.3293, label_Tbl=0.2347, label_Hcc=0.1566 | global_gate_abs=0.0369 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch224:256 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for W/Z two-prong-like separation after prior layer transformations

```python
# L2_ch224:256: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # W/Z two-prong-like separation
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Wqq=1.1221, label_Zqq=1.0057, label_Hcc=0.7717 | global_gate_abs=0.7083 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch32:64 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L2_ch32:64: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Tbl leading-core signature
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Tbl=0.4565, label_Hcc=0.3231, label_QCD=0.1790 | global_gate_abs=0.1306 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch64:96 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Hqql/Tbl core-confusion axis after prior layer transformations

```python
# L2_ch64:96: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Hqql/Tbl core-confusion axis
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_QCD=0.9095, label_Hqql=0.4053, label_Tbl=0.4048 | global_gate_abs=0.3056 | relation_hits=2 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability

### L2_ch96:128 — late class-evidence aggregation/readout

**Input state:** L1 contextual neighborhood features, class-route evidence, core/top-k summaries

**Meaning:** candidate mechanism for Tbl leading-core signature after prior layer transformations

```python
# L2_ch96:128: late readout
for event:
    evidence = aggregate(core_context_heads)
    class_score += project(evidence)  # Tbl leading-core signature
    suppress_or_compete_with_nearby_classes()
```

**Evidence:** class_grad:label_Tbl=0.2700, label_Hcc=0.1736, label_QCD=0.1453 | global_gate_abs=0.0666 | relation_hits=3 | stream_hits=30

**Risks:** simple known-observable surrogate incomplete; semantic pseudocode, not literal model source

**Next test:** route-neighbor trace + heldout/per-file stability
