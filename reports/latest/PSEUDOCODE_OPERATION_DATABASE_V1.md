# Pseudocode Operation Database v1

Full semantic pseudocode database: one row per pseudo-head/channel group.

## Top candidates
| head | stage | axis | confidence | gate | class_grad |
| --- | --- | --- | --- | --- | --- |
| L0_ch40:48 | L0 early local reader | W/Z structured-prong axis | HIGH_CANDIDATE | 0.7156 | 1.1670 |
| L0_ch0:8 | L0 early local reader | Hqql/Tbl core-confusion axis | HIGH_CANDIDATE | 0.2042 | 1.1571 |
| L0_ch48:56 | L0 early local reader | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.3769 | 0.9793 |
| L0_ch16:24 | L0 early local reader | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.0896 | 0.9509 |
| L0_ch24:32 | L0 early local reader | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.2271 | 0.7906 |
| L0_ch8:16 | L0 early local reader | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.3577 | 0.7731 |
| L0_ch56:64 | L0 early local reader | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.0186 | 0.4484 |
| L0_ch32:40 | L0 early local reader | W/Z structured-prong axis | LOW_NEEDS_MORE_EVIDENCE | 0.1125 | 0.2724 |
| L1_ch16:32 | L1 middle context relay | W/Z structured-prong axis | HIGH_CANDIDATE | 0.7480 | 1.6597 |
| L1_ch32:48 | L1 middle context relay | Hqql/Tbl core-confusion axis | HIGH_CANDIDATE | 0.2108 | 1.3994 |
| L1_ch112:128 | L1 middle context relay | W/Z structured-prong axis | HIGH_CANDIDATE | 0.8689 | 1.2414 |
| L1_ch0:16 | L1 middle context relay | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.0146 | 0.5761 |
| L1_ch96:112 | L1 middle context relay | W/Z structured-prong axis | MEDIUM_CANDIDATE | 0.0286 | 0.5720 |
| L1_ch64:80 | L1 middle context relay | W/Z structured-prong axis | MEDIUM_CANDIDATE | 0.1835 | 0.5339 |
| L1_ch80:96 | L1 middle context relay | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.1692 | 0.4375 |
| L1_ch48:64 | L1 middle context relay | Hqql/Tbl core-confusion axis | LOW_NEEDS_MORE_EVIDENCE | 0.1366 | 0.1854 |
| L2_ch128:160 | L2 late readout | Hqql/Tbl core-confusion axis | HIGH_CANDIDATE | 0.3421 | 1.8701 |
| L2_ch224:256 | L2 late readout | W/Z structured-prong axis | HIGH_CANDIDATE | 0.7083 | 1.1221 |
| L2_ch0:32 | L2 late readout | Hqql/Tbl core-confusion axis | HIGH_CANDIDATE | 0.2611 | 1.0545 |
| L2_ch64:96 | L2 late readout | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.3056 | 0.9095 |
| L2_ch160:192 | L2 late readout | Hqql/Tbl core-confusion axis | MEDIUM_CANDIDATE | 0.0423 | 0.4768 |
| L2_ch32:64 | L2 late readout | W/Z structured-prong axis | MEDIUM_CANDIDATE | 0.1306 | 0.4565 |
| L2_ch192:224 | L2 late readout | W/Z structured-prong axis | LOW_NEEDS_MORE_EVIDENCE | 0.0369 | 0.3293 |
| L2_ch96:128 | L2 late readout | W/Z structured-prong axis | LOW_NEEDS_MORE_EVIDENCE | 0.0666 | 0.2700 |

## Full pseudocode

### L0_ch40:48 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: W/Z structured-prong axis

```python
# L0_ch40:48
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_Wqq=1.1670, label_Zqq=0.9496, label_Hcc=0.9443 | global_gate_abs=0.7156 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.1670, label_Zqq:0.9496, label_Hcc:0.9443, label_H4q:0.8881, label_QCD:0.6787

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch0:8 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch0:8
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_H4q=1.1571, label_Hqql=0.5866, label_QCD=0.5120 | global_gate_abs=0.2042 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:1.1571, label_Hqql:0.5866, label_QCD:0.5120, label_Tbl:0.3306, label_Hcc:0.3104

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch48:56 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch48:56
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_H4q=0.9793, label_QCD=0.8989, label_Tbl=0.8825 | global_gate_abs=0.3769 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:0.9793, label_QCD:0.8989, label_Tbl:0.8825, label_Hqql:0.4893, label_Hcc:0.4175

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch16:24 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch16:24
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_H4q=0.9509, label_Tbl=0.3513, label_Hcc=0.3307 | global_gate_abs=0.0896 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:0.9509, label_Tbl:0.3513, label_Hcc:0.3307, label_Zqq:0.2983, label_Hqql:0.2765

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch24:32 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch24:32
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_Wqq=0.7906, label_Hqql=0.3870, label_H4q=0.2608 | global_gate_abs=0.2271 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:0.7906, label_Hqql:0.3870, label_H4q:0.2608, label_Tbl:0.2569, label_Hcc:0.2532

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch8:16 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch8:16
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_Tbl=0.7731, label_Hcc=0.7574, label_Zqq=0.6469 | global_gate_abs=0.3577 | relation_hits=2 | stream_hits=30 | class_grads=label_Tbl:0.7731, label_Hcc:0.7574, label_Zqq:0.6469, label_Wqq:0.5422, label_Hqql:0.2834

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch56:64 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: Hqql/Tbl core-confusion axis

```python
# L0_ch56:64
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_Hqql=0.4484, label_H4q=0.3784, label_Zqq=0.2666 | global_gate_abs=0.0186 | relation_hits=3 | stream_hits=30 | class_grads=label_Hqql:0.4484, label_H4q:0.3784, label_Zqq:0.2666, label_Tbl:0.1801, label_Hcc:0.0961

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L0_ch32:40 — L0 early local reader

Pre-layer state: raw particles + KNN edge coordinates

Reads: pt/energy, deltaR, PID/charge, neighbor edge differences

Steps: build KNN edge features -> detect local core/radial/PID pattern -> write local evidence

Writes: local particle-edge features for L1

Axis: W/Z structured-prong axis

```python
# L0_ch32:40
for particle i:
    nb = knn(i)
    local = read(pt_energy, deltaR, pid_charge, edge(i, nb))
    write_local(local, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_QCD=0.2724, label_Hcc=0.2370, label_Zqq=0.1604 | global_gate_abs=0.1125 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.2724, label_Hcc:0.2370, label_Zqq:0.1604, label_Hqql:0.0554, label_Wqq:0.0495

Confidence: LOW_NEEDS_MORE_EVIDENCE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch16:32 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: W/Z structured-prong axis

```python
# L1_ch16:32
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_Wqq=1.6597, label_Zqq=1.0984, label_H4q=0.9520 | global_gate_abs=0.7480 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.6597, label_Zqq:1.0984, label_H4q:0.9520, label_Hcc:0.8966, label_QCD:0.6487

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch32:48 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: Hqql/Tbl core-confusion axis

```python
# L1_ch32:48
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_Tbl=1.3994, label_QCD=0.5415, label_Hqql=0.5251 | global_gate_abs=0.2108 | relation_hits=2 | stream_hits=30 | class_grads=label_Tbl:1.3994, label_QCD:0.5415, label_Hqql:0.5251, label_H4q:0.5031, label_Zqq:0.2462

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch112:128 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: W/Z structured-prong axis

```python
# L1_ch112:128
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_Hcc=1.2414, label_H4q=0.9725, label_Wqq=0.9042 | global_gate_abs=0.8689 | relation_hits=2 | stream_hits=30 | class_grads=label_Hcc:1.2414, label_H4q:0.9725, label_Wqq:0.9042, label_Zqq:0.8062, label_Tbl:0.8018

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch0:16 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: Hqql/Tbl core-confusion axis

```python
# L1_ch0:16
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_H4q=0.5761, label_Zqq=0.2802, label_Hcc=0.2169 | global_gate_abs=0.0146 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:0.5761, label_Zqq:0.2802, label_Hcc:0.2169, label_Tbl:0.1700, label_Hqql:0.1143

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch96:112 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: W/Z structured-prong axis

```python
# L1_ch96:112
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_QCD=0.5720, label_Hcc=0.4957, label_Hqql=0.4296 | global_gate_abs=0.0286 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.5720, label_Hcc:0.4957, label_Hqql:0.4296, label_Zqq:0.2820, label_H4q:0.2214

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch64:80 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: W/Z structured-prong axis

```python
# L1_ch64:80
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='W/Z structured-prong axis')
```

Evidence: class_grad:label_QCD=0.5339, label_Wqq=0.4825, label_Zqq=0.3464 | global_gate_abs=0.1835 | relation_hits=3 | stream_hits=30 | class_grads=label_QCD:0.5339, label_Wqq:0.4825, label_Zqq:0.3464, label_H4q:0.3362, label_Hqql:0.2216

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch80:96 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: Hqql/Tbl core-confusion axis

```python
# L1_ch80:96
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_H4q=0.4375, label_Hqql=0.2887, label_Zqq=0.2790 | global_gate_abs=0.1692 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:0.4375, label_Hqql:0.2887, label_Zqq:0.2790, label_Wqq:0.2236, label_Hcc:0.1581

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L1_ch48:64 — L1 middle context relay

Pre-layer state: L0 local edge features already mixed

Reads: L0 local features, top-k core, neighbor context, wide particles

Steps: read L0 evidence -> mix core with neighborhood/secondary context -> route class evidence

Writes: core+context vectors for L2

Axis: Hqql/Tbl core-confusion axis

```python
# L1_ch48:64
for neighborhood i:
    local = read_L0(i)
    context = mix(topk_core(i), neighbors(i), secondary_context(i))
    write_context(context, axis='Hqql/Tbl core-confusion axis')
```

Evidence: class_grad:label_Hcc=0.1854, label_Tbl=0.1819, label_QCD=0.0978 | global_gate_abs=0.1366 | relation_hits=2 | stream_hits=30 | class_grads=label_Hcc:0.1854, label_Tbl:0.1819, label_QCD:0.0978, label_Zqq:0.0743, label_Hqql:0.0677

Confidence: LOW_NEEDS_MORE_EVIDENCE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch128:160 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: Hqql/Tbl core-confusion axis

```python
# L2_ch128:160
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='Hqql/Tbl core-confusion axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Hqql=1.8701, label_Tbl=1.5447, label_Wqq=0.1695 | global_gate_abs=0.3421 | relation_hits=2 | stream_hits=30 | class_grads=label_Hqql:1.8701, label_Tbl:1.5447, label_Wqq:0.1695, label_Hcc:0.1494, label_QCD:0.1342

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch224:256 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: W/Z structured-prong axis

```python
# L2_ch224:256
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='W/Z structured-prong axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Wqq=1.1221, label_Zqq=1.0057, label_Hcc=0.7717 | global_gate_abs=0.7083 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.1221, label_Zqq:1.0057, label_Hcc:0.7717, label_Tbl:0.6898, label_H4q:0.6133

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch0:32 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: Hqql/Tbl core-confusion axis

```python
# L2_ch0:32
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='Hqql/Tbl core-confusion axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_H4q=1.0545, label_Tbl=1.0411, label_Hqql=0.6474 | global_gate_abs=0.2611 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:1.0545, label_Tbl:1.0411, label_Hqql:0.6474, label_Hcc:0.3019, label_QCD:0.2690

Confidence: HIGH_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch64:96 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: Hqql/Tbl core-confusion axis

```python
# L2_ch64:96
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='Hqql/Tbl core-confusion axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_QCD=0.9095, label_Hqql=0.4053, label_Tbl=0.4048 | global_gate_abs=0.3056 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.9095, label_Hqql:0.4053, label_Tbl:0.4048, label_Wqq:0.3195, label_Zqq:0.2910

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch160:192 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: Hqql/Tbl core-confusion axis

```python
# L2_ch160:192
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='Hqql/Tbl core-confusion axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Hqql=0.4768, label_QCD=0.2924, label_H4q=0.2516 | global_gate_abs=0.0423 | relation_hits=3 | stream_hits=30 | class_grads=label_Hqql:0.4768, label_QCD:0.2924, label_H4q:0.2516, label_Zqq:0.1109, label_Hcc:0.1041

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch32:64 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: W/Z structured-prong axis

```python
# L2_ch32:64
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='W/Z structured-prong axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Tbl=0.4565, label_Hcc=0.3231, label_QCD=0.1790 | global_gate_abs=0.1306 | relation_hits=3 | stream_hits=30 | class_grads=label_Tbl:0.4565, label_Hcc:0.3231, label_QCD:0.1790, label_Wqq:0.1683, label_Zqq:0.1380

Confidence: MEDIUM_CANDIDATE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch192:224 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: W/Z structured-prong axis

```python
# L2_ch192:224
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='W/Z structured-prong axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Wqq=0.3293, label_Tbl=0.2347, label_Hcc=0.1566 | global_gate_abs=0.0369 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:0.3293, label_Tbl:0.2347, label_Hcc:0.1566, label_Zqq:0.0772, label_H4q:0.0406

Confidence: LOW_NEEDS_MORE_EVIDENCE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2

### L2_ch96:128 — L2 late readout

Pre-layer state: L1 context and class-route evidence already mixed

Reads: L1 context, class-evidence summaries, core/secondary competition

Steps: read L1 context -> aggregate class evidence -> write classifier support/competition

Writes: class evidence and class-competition support

Axis: W/Z structured-prong axis

```python
# L2_ch96:128
for event:
    context = collect_L1_context()
    evidence = aggregate(context, axis='W/Z structured-prong axis')
    write_class_evidence(evidence)
```

Evidence: class_grad:label_Tbl=0.2700, label_Hcc=0.1736, label_QCD=0.1453 | global_gate_abs=0.0666 | relation_hits=3 | stream_hits=30 | class_grads=label_Tbl:0.2700, label_Hcc:0.1736, label_QCD:0.1453, label_H4q:0.0713, label_Wqq:0.0673

Confidence: LOW_NEEDS_MORE_EVIDENCE

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

Next: route-neighbor trace; head-pair synergy; per-file heldout; residual v2
