# Pseudocode Operation Database v2

This version merges semantic pseudocode with corrected code alignment and actual pseudo-head output trace.

## Top output-aware rows
| head | module | slice | output_role | top_class | lead_match | logit_corr |
| --- | --- | --- | --- | --- | --- | --- |
| L0_ch40:48 | edge_convs.0 | output[:, 40:48, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.1648 | label_Tbqq:0.1292 |
| L0_ch32:40 | edge_convs.0 | output[:, 32:40, :] | early local/context feature builder over non-leading neighbor particles | label_QCD | 0.1195 | label_Hqql:-0.3183 |
| L0_ch24:32 | edge_convs.0 | output[:, 24:32, :] | early local/context feature builder over non-leading neighbor particles | label_QCD | 0.0797 | label_H4q:-0.1225 |
| L0_ch48:56 | edge_convs.0 | output[:, 48:56, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0461 | label_Tbqq:0.1998 |
| L0_ch16:24 | edge_convs.0 | output[:, 16:24, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0195 | label_Tbqq:0.2299 |
| L0_ch8:16 | edge_convs.0 | output[:, 8:16, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0078 | label_Tbqq:0.2794 |
| L0_ch0:8 | edge_convs.0 | output[:, 0:8, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0031 | label_Hqql:-0.2814 |
| L0_ch56:64 | edge_convs.0 | output[:, 56:64, :] | early local/context feature builder over non-leading neighbor particles | label_Tbqq | 0.0031 | label_Tbqq:0.2599 |
| L1_ch0:16 | edge_convs.1 | output[:, 0:16, :] | middle relay mixing context with some core alignment | label_Tbl | 0.3016 | label_H4q:-0.3682 |
| L1_ch112:128 | edge_convs.1 | output[:, 112:128, :] | middle context relay mostly away from literal leading particle | label_Tbl | 0.1727 | label_Wqq:-0.2462 |
| L1_ch96:112 | edge_convs.1 | output[:, 96:112, :] | middle context relay mostly away from literal leading particle | label_QCD | 0.1289 | label_H4q:-0.1061 |
| L1_ch48:64 | edge_convs.1 | output[:, 48:64, :] | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0969 | label_Tbqq:0.2433 |
| L1_ch32:48 | edge_convs.1 | output[:, 32:48, :] | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0656 | label_Hqql:-0.2501 |
| L1_ch80:96 | edge_convs.1 | output[:, 80:96, :] | middle context relay mostly away from literal leading particle | label_Tbl | 0.0414 | label_Tbl:0.1208 |
| L1_ch16:32 | edge_convs.1 | output[:, 16:32, :] | middle context relay mostly away from literal leading particle | label_QCD | 0.0383 | label_QCD:0.1070 |
| L1_ch64:80 | edge_convs.1 | output[:, 64:80, :] | middle context relay mostly away from literal leading particle | label_Tbqq | 0.0000 | label_Tbqq:0.2741 |
| L2_ch224:256 | edge_convs.2 | output[:, 224:256, :] | late readout strongly anchored on particle0/leading-pT core | label_Tbl | 0.7180 | label_Hgg:-0.6442 |
| L2_ch0:32 | edge_convs.2 | output[:, 0:32, :] | late readout moderately core-aligned | label_Hqql | 0.4227 | label_Hbb:-0.3352 |
| L2_ch128:160 | edge_convs.2 | output[:, 128:160, :] | late readout moderately core-aligned | label_Tbl | 0.3852 | label_Tbl:0.6627 |
| L2_ch32:64 | edge_convs.2 | output[:, 32:64, :] | late readout moderately core-aligned | label_Tbl | 0.3812 | label_QCD:-0.5493 |
| L2_ch192:224 | edge_convs.2 | output[:, 192:224, :] | late readout moderately core-aligned | label_Tbqq | 0.3055 | label_QCD:-0.3177 |
| L2_ch160:192 | edge_convs.2 | output[:, 160:192, :] | late readout with distributed/non-core particle evidence | label_Tbl | 0.2477 | label_Tbl:0.5801 |
| L2_ch64:96 | edge_convs.2 | output[:, 64:96, :] | late readout with distributed/non-core particle evidence | label_Tbl | 0.2336 | label_QCD:-0.5693 |
| L2_ch96:128 | edge_convs.2 | output[:, 96:128, :] | late readout with distributed/non-core particle evidence | label_Hbb | 0.2094 | label_Wqq:-0.1734 |

## Full refined pseudocode

### L0_ch40:48 — L0 early local reader

Code: `edge_convs.0` / `output[:, 40:48, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.1648, lead_match=0.1648, logit_corr=label_Tbqq:0.1292

```python
# L0_ch40:48: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.16
```

Evidence: class_grad:label_Wqq=1.1670, label_Zqq=0.9496, label_Hcc=0.9443 | global_gate_abs=0.7156 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.1670, label_Zqq:0.9496, label_Hcc:0.9443, label_H4q:0.8881, label_QCD:0.6787

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch32:40 — L0 early local reader

Code: `edge_convs.0` / `output[:, 32:40, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_QCD, particle0_top=0.1195, lead_match=0.1195, logit_corr=label_Hqql:-0.3183

```python
# L0_ch32:40: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_QCD; lead_match=0.12
```

Evidence: class_grad:label_QCD=0.2724, label_Hcc=0.2370, label_Zqq=0.1604 | global_gate_abs=0.1125 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.2724, label_Hcc:0.2370, label_Zqq:0.1604, label_Hqql:0.0554, label_Wqq:0.0495

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch24:32 — L0 early local reader

Code: `edge_convs.0` / `output[:, 24:32, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_QCD, particle0_top=0.0797, lead_match=0.0797, logit_corr=label_H4q:-0.1225

```python
# L0_ch24:32: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_QCD; lead_match=0.08
```

Evidence: class_grad:label_Wqq=0.7906, label_Hqql=0.3870, label_H4q=0.2608 | global_gate_abs=0.2271 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:0.7906, label_Hqql:0.3870, label_H4q:0.2608, label_Tbl:0.2569, label_Hcc:0.2532

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch48:56 — L0 early local reader

Code: `edge_convs.0` / `output[:, 48:56, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.0461, lead_match=0.0461, logit_corr=label_Tbqq:0.1998

```python
# L0_ch48:56: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.05
```

Evidence: class_grad:label_H4q=0.9793, label_QCD=0.8989, label_Tbl=0.8825 | global_gate_abs=0.3769 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:0.9793, label_QCD:0.8989, label_Tbl:0.8825, label_Hqql:0.4893, label_Hcc:0.4175

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch16:24 — L0 early local reader

Code: `edge_convs.0` / `output[:, 16:24, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.0195, lead_match=0.0195, logit_corr=label_Tbqq:0.2299

```python
# L0_ch16:24: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.02
```

Evidence: class_grad:label_H4q=0.9509, label_Tbl=0.3513, label_Hcc=0.3307 | global_gate_abs=0.0896 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:0.9509, label_Tbl:0.3513, label_Hcc:0.3307, label_Zqq:0.2983, label_Hqql:0.2765

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch8:16 — L0 early local reader

Code: `edge_convs.0` / `output[:, 8:16, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.0078, lead_match=0.0078, logit_corr=label_Tbqq:0.2794

```python
# L0_ch8:16: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.01
```

Evidence: class_grad:label_Tbl=0.7731, label_Hcc=0.7574, label_Zqq=0.6469 | global_gate_abs=0.3577 | relation_hits=2 | stream_hits=30 | class_grads=label_Tbl:0.7731, label_Hcc:0.7574, label_Zqq:0.6469, label_Wqq:0.5422, label_Hqql:0.2834

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch0:8 — L0 early local reader

Code: `edge_convs.0` / `output[:, 0:8, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.0031, lead_match=0.0031, logit_corr=label_Hqql:-0.2814

```python
# L0_ch0:8: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.00
```

Evidence: class_grad:label_H4q=1.1571, label_Hqql=0.5866, label_QCD=0.5120 | global_gate_abs=0.2042 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:1.1571, label_Hqql:0.5866, label_QCD:0.5120, label_Tbl:0.3306, label_Hcc:0.3104

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L0_ch56:64 — L0 early local reader

Code: `edge_convs.0` / `output[:, 56:64, :]` / shape `[160, 64, 128]`

Output role: **early local/context feature builder over non-leading neighbor particles**

Output: top_class=label_Tbqq, particle0_top=0.0031, lead_match=0.0031, logit_corr=label_Tbqq:0.2599

```python
# L0_ch56:64: L0 output-aware pseudocode
for particle i:
    nb = knn(i)
    local = read_raw_edge_features(i, nb)
    score = detect_local_pattern(local)
    write_L0_channels(score)  # output role: early local/context feature builder over non-leading neighbor particles; top_class=label_Tbqq; lead_match=0.00
```

Evidence: class_grad:label_Hqql=0.4484, label_H4q=0.3784, label_Zqq=0.2666 | global_gate_abs=0.0186 | relation_hits=3 | stream_hits=30 | class_grads=label_Hqql:0.4484, label_H4q:0.3784, label_Zqq:0.2666, label_Tbl:0.1801, label_Hcc:0.0961

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch0:16 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 0:16, :]` / shape `[160, 128, 128]`

Output role: **middle relay mixing context with some core alignment**

Output: top_class=label_Tbl, particle0_top=0.3016, lead_match=0.3016, logit_corr=label_H4q:-0.3682

```python
# L1_ch0:16: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle relay mixing context with some core alignment; particle0_top=0.30; top_class=label_Tbl
```

Evidence: class_grad:label_H4q=0.5761, label_Zqq=0.2802, label_Hcc=0.2169 | global_gate_abs=0.0146 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:0.5761, label_Zqq:0.2802, label_Hcc:0.2169, label_Tbl:0.1700, label_Hqql:0.1143

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch112:128 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 112:128, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_Tbl, particle0_top=0.1727, lead_match=0.1727, logit_corr=label_Wqq:-0.2462

```python
# L1_ch112:128: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.17; top_class=label_Tbl
```

Evidence: class_grad:label_Hcc=1.2414, label_H4q=0.9725, label_Wqq=0.9042 | global_gate_abs=0.8689 | relation_hits=2 | stream_hits=30 | class_grads=label_Hcc:1.2414, label_H4q:0.9725, label_Wqq:0.9042, label_Zqq:0.8062, label_Tbl:0.8018

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch96:112 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 96:112, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_QCD, particle0_top=0.1289, lead_match=0.1289, logit_corr=label_H4q:-0.1061

```python
# L1_ch96:112: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.13; top_class=label_QCD
```

Evidence: class_grad:label_QCD=0.5720, label_Hcc=0.4957, label_Hqql=0.4296 | global_gate_abs=0.0286 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.5720, label_Hcc:0.4957, label_Hqql:0.4296, label_Zqq:0.2820, label_H4q:0.2214

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch48:64 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 48:64, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_Tbqq, particle0_top=0.0969, lead_match=0.0969, logit_corr=label_Tbqq:0.2433

```python
# L1_ch48:64: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.10; top_class=label_Tbqq
```

Evidence: class_grad:label_Hcc=0.1854, label_Tbl=0.1819, label_QCD=0.0978 | global_gate_abs=0.1366 | relation_hits=2 | stream_hits=30 | class_grads=label_Hcc:0.1854, label_Tbl:0.1819, label_QCD:0.0978, label_Zqq:0.0743, label_Hqql:0.0677

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch32:48 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 32:48, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_Tbqq, particle0_top=0.0656, lead_match=0.0656, logit_corr=label_Hqql:-0.2501

```python
# L1_ch32:48: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.07; top_class=label_Tbqq
```

Evidence: class_grad:label_Tbl=1.3994, label_QCD=0.5415, label_Hqql=0.5251 | global_gate_abs=0.2108 | relation_hits=2 | stream_hits=30 | class_grads=label_Tbl:1.3994, label_QCD:0.5415, label_Hqql:0.5251, label_H4q:0.5031, label_Zqq:0.2462

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch80:96 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 80:96, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_Tbl, particle0_top=0.0414, lead_match=0.0414, logit_corr=label_Tbl:0.1208

```python
# L1_ch80:96: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.04; top_class=label_Tbl
```

Evidence: class_grad:label_H4q=0.4375, label_Hqql=0.2887, label_Zqq=0.2790 | global_gate_abs=0.1692 | relation_hits=3 | stream_hits=30 | class_grads=label_H4q:0.4375, label_Hqql:0.2887, label_Zqq:0.2790, label_Wqq:0.2236, label_Hcc:0.1581

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch16:32 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 16:32, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_QCD, particle0_top=0.0383, lead_match=0.0383, logit_corr=label_QCD:0.1070

```python
# L1_ch16:32: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.04; top_class=label_QCD
```

Evidence: class_grad:label_Wqq=1.6597, label_Zqq=1.0984, label_H4q=0.9520 | global_gate_abs=0.7480 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.6597, label_Zqq:1.0984, label_H4q:0.9520, label_Hcc:0.8966, label_QCD:0.6487

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L1_ch64:80 — L1 middle context relay

Code: `edge_convs.1` / `output[:, 64:80, :]` / shape `[160, 128, 128]`

Output role: **middle context relay mostly away from literal leading particle**

Output: top_class=label_Tbqq, particle0_top=0.0000, lead_match=0.0000, logit_corr=label_Tbqq:0.2741

```python
# L1_ch64:80: L1 output-aware pseudocode
for particle/neighborhood i:
    l0 = read_L0_local_features(i)
    ctx = mix_neighbors_core_and_secondary(l0)
    write_L1_context(ctx)  # output role: middle context relay mostly away from literal leading particle; particle0_top=0.00; top_class=label_Tbqq
```

Evidence: class_grad:label_QCD=0.5339, label_Wqq=0.4825, label_Zqq=0.3464 | global_gate_abs=0.1835 | relation_hits=3 | stream_hits=30 | class_grads=label_QCD:0.5339, label_Wqq:0.4825, label_Zqq:0.3464, label_H4q:0.3362, label_Hqql:0.2216

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch224:256 — L2 late readout

Code: `edge_convs.2` / `output[:, 224:256, :]` / shape `[160, 256, 128]`

Output role: **late readout strongly anchored on particle0/leading-pT core**

Output: top_class=label_Tbl, particle0_top=0.7180, lead_match=0.7180, logit_corr=label_Hgg:-0.6442

```python
# L2_ch224:256: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.72):
        logits += project_core_readout(evidence)
    # output role: late readout strongly anchored on particle0/leading-pT core; top_class=label_Tbl; corr=label_Hgg:-0.6442
```

Evidence: class_grad:label_Wqq=1.1221, label_Zqq=1.0057, label_Hcc=0.7717 | global_gate_abs=0.7083 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:1.1221, label_Zqq:1.0057, label_Hcc:0.7717, label_Tbl:0.6898, label_H4q:0.6133

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch0:32 — L2 late readout

Code: `edge_convs.2` / `output[:, 0:32, :]` / shape `[160, 256, 128]`

Output role: **late readout moderately core-aligned**

Output: top_class=label_Hqql, particle0_top=0.4227, lead_match=0.4227, logit_corr=label_Hbb:-0.3352

```python
# L2_ch0:32: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.42):
        logits += project_core_readout(evidence)
    # output role: late readout moderately core-aligned; top_class=label_Hqql; corr=label_Hbb:-0.3352
```

Evidence: class_grad:label_H4q=1.0545, label_Tbl=1.0411, label_Hqql=0.6474 | global_gate_abs=0.2611 | relation_hits=2 | stream_hits=30 | class_grads=label_H4q:1.0545, label_Tbl:1.0411, label_Hqql:0.6474, label_Hcc:0.3019, label_QCD:0.2690

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch128:160 — L2 late readout

Code: `edge_convs.2` / `output[:, 128:160, :]` / shape `[160, 256, 128]`

Output role: **late readout moderately core-aligned**

Output: top_class=label_Tbl, particle0_top=0.3852, lead_match=0.3852, logit_corr=label_Tbl:0.6627

```python
# L2_ch128:160: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.39):
        logits += project_core_readout(evidence)
    # output role: late readout moderately core-aligned; top_class=label_Tbl; corr=label_Tbl:0.6627
```

Evidence: class_grad:label_Hqql=1.8701, label_Tbl=1.5447, label_Wqq=0.1695 | global_gate_abs=0.3421 | relation_hits=2 | stream_hits=30 | class_grads=label_Hqql:1.8701, label_Tbl:1.5447, label_Wqq:0.1695, label_Hcc:0.1494, label_QCD:0.1342

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch32:64 — L2 late readout

Code: `edge_convs.2` / `output[:, 32:64, :]` / shape `[160, 256, 128]`

Output role: **late readout moderately core-aligned**

Output: top_class=label_Tbl, particle0_top=0.3812, lead_match=0.3812, logit_corr=label_QCD:-0.5493

```python
# L2_ch32:64: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.38):
        logits += project_core_readout(evidence)
    # output role: late readout moderately core-aligned; top_class=label_Tbl; corr=label_QCD:-0.5493
```

Evidence: class_grad:label_Tbl=0.4565, label_Hcc=0.3231, label_QCD=0.1790 | global_gate_abs=0.1306 | relation_hits=3 | stream_hits=30 | class_grads=label_Tbl:0.4565, label_Hcc:0.3231, label_QCD:0.1790, label_Wqq:0.1683, label_Zqq:0.1380

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch192:224 — L2 late readout

Code: `edge_convs.2` / `output[:, 192:224, :]` / shape `[160, 256, 128]`

Output role: **late readout moderately core-aligned**

Output: top_class=label_Tbqq, particle0_top=0.3055, lead_match=0.3055, logit_corr=label_QCD:-0.3177

```python
# L2_ch192:224: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.31):
        logits += project_core_readout(evidence)
    # output role: late readout moderately core-aligned; top_class=label_Tbqq; corr=label_QCD:-0.3177
```

Evidence: class_grad:label_Wqq=0.3293, label_Tbl=0.2347, label_Hcc=0.1566 | global_gate_abs=0.0369 | relation_hits=2 | stream_hits=30 | class_grads=label_Wqq:0.3293, label_Tbl:0.2347, label_Hcc:0.1566, label_Zqq:0.0772, label_H4q:0.0406

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch160:192 — L2 late readout

Code: `edge_convs.2` / `output[:, 160:192, :]` / shape `[160, 256, 128]`

Output role: **late readout with distributed/non-core particle evidence**

Output: top_class=label_Tbl, particle0_top=0.2477, lead_match=0.2477, logit_corr=label_Tbl:0.5801

```python
# L2_ch160:192: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.25):
        logits += project_core_readout(evidence)
    # output role: late readout with distributed/non-core particle evidence; top_class=label_Tbl; corr=label_Tbl:0.5801
```

Evidence: class_grad:label_Hqql=0.4768, label_QCD=0.2924, label_H4q=0.2516 | global_gate_abs=0.0423 | relation_hits=3 | stream_hits=30 | class_grads=label_Hqql:0.4768, label_QCD:0.2924, label_H4q:0.2516, label_Zqq:0.1109, label_Hcc:0.1041

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch64:96 — L2 late readout

Code: `edge_convs.2` / `output[:, 64:96, :]` / shape `[160, 256, 128]`

Output role: **late readout with distributed/non-core particle evidence**

Output: top_class=label_Tbl, particle0_top=0.2336, lead_match=0.2336, logit_corr=label_QCD:-0.5693

```python
# L2_ch64:96: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.23):
        logits += project_core_readout(evidence)
    # output role: late readout with distributed/non-core particle evidence; top_class=label_Tbl; corr=label_QCD:-0.5693
```

Evidence: class_grad:label_QCD=0.9095, label_Hqql=0.4053, label_Tbl=0.4048 | global_gate_abs=0.3056 | relation_hits=2 | stream_hits=30 | class_grads=label_QCD:0.9095, label_Hqql:0.4053, label_Tbl:0.4048, label_Wqq:0.3195, label_Zqq:0.2910

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model

### L2_ch96:128 — L2 late readout

Code: `edge_convs.2` / `output[:, 96:128, :]` / shape `[160, 256, 128]`

Output role: **late readout with distributed/non-core particle evidence**

Output: top_class=label_Hbb, particle0_top=0.2094, lead_match=0.2094, logit_corr=label_Wqq:-0.1734

```python
# L2_ch96:128: L2 output-aware pseudocode
for event:
    ctx = collect_L1_context()
    evidence = aggregate_class_evidence(ctx)
    if top_particle_is_core_or_particle0(rate=0.21):
        logits += project_core_readout(evidence)
    # output role: late readout with distributed/non-core particle evidence; top_class=label_Hbb; corr=label_Wqq:-0.1734
```

Evidence: class_grad:label_Tbl=0.2700, label_Hcc=0.1736, label_QCD=0.1453 | global_gate_abs=0.0666 | relation_hits=3 | stream_hits=30 | class_grads=label_Tbl:0.2700, label_Hcc:0.1736, label_QCD:0.1453, label_H4q:0.0713, label_Wqq:0.0673

Risks: semantic pseudocode; needs route trace, residual v2, heldout/cross-model
