# PART_MATRIX_DECODER_FIRST_ATLAS_V1

Decoder-first interpretation atlas. Pair atlas is used only to select validated mechanisms; final interpretation is the matrix-program / pseudocode / physics binding.

- mechanisms: **116**
- status_counts: `{'PARTIAL_DECODE': 116}`
- min_abs_weight: **0.001**

## Concrete decoded mechanisms

### 1. rank013 label_Hbb -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-2.5652**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hbb->label_Zqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Hbb)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hbb->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 2. rank013 label_Hbb -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `CLS<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-2.4556**
- causal_B_flip: **0.0**
- query_role: `CLS`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, CLS<-neutral_hadron, label_Hbb->label_Zqq] = READ_ROUTE(CLS<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Hbb)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hbb->label_Zqq: route uses CLS aggregation. Likely global event summary/readout rather than a local particle-pair operator.

### 3. rank022 label_Hcc -> label_Tbqq / `mod.cls_blocks.0.attn.h6` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-1.4327**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h6, muon<-muon, label_Hcc->label_Tbqq] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Tbqq: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 4. rank015 label_Hqql -> label_Tbl / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-1.4079**
- causal_B_flip: **-0.375**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Hqql->label_Tbl] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbl-label_Hqql)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hqql->label_Tbl: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 5. rank015 label_Hqql -> label_Tbl / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **1.2846**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Hqql->label_Tbl] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbl-label_Hqql)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hqql->label_Tbl: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 6. rank007 label_Hcc -> label_Hgg / `mod.cls_blocks.0.attn.h6` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.9907**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h6, neutral_hadron<-neutral_hadron, label_Hcc->label_Hgg] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hgg-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Hgg: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 7. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `electron<-electron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.9290**
- causal_B_flip: **-0.1875**
- query_role: `electron`
- key_role: `electron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, electron<-electron, label_Tbl->label_Hqql] = READ_ROUTE(electron<-electron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 8. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `CLS<-electron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.9261**
- causal_B_flip: **-0.1875**
- query_role: `CLS`
- key_role: `electron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, CLS<-electron, label_Tbl->label_Hqql] = READ_ROUTE(CLS<-electron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 9. rank021 label_Hbb -> label_Tbqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.8494**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hbb->label_Tbqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_Hbb)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hbb->label_Tbqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 10. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `CLS<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.8186**
- causal_B_flip: **-0.3125**
- query_role: `CLS`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, CLS<-muon, label_Tbl->label_Hqql] = READ_ROUTE(CLS<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 11. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.8177**
- causal_B_flip: **-0.3125**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Tbl->label_Hqql] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 12. rank022 label_Hcc -> label_Tbqq / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.7682**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Hcc->label_Tbqq] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Tbqq: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 13. rank018 label_Zqq -> label_Hcc / `mod.cls_blocks.0.attn.h4` / `photon<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.7533**
- causal_B_flip: **0.0**
- query_role: `photon`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, photon<-neutral_hadron, label_Zqq->label_Hcc] = READ_ROUTE(photon<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hcc-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hcc: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 14. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.7199**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-charged_hadron, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 15. rank018 label_Zqq -> label_Hcc / `mod.cls_blocks.0.attn.h4` / `photon<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.7186**
- causal_B_flip: **0.0**
- query_role: `photon`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, photon<-charged_hadron, label_Zqq->label_Hcc] = READ_ROUTE(photon<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hcc-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hcc: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 16. rank007 label_Hcc -> label_Hgg / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.6870**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hcc->label_Hgg] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hgg-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Hgg: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 17. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.6431**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 18. rank012 label_Hcc -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.6378**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hcc->label_Zqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 19. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-photon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.6279**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `photon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-photon, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-photon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 20. rank017 label_Zqq -> label_Hbb / `mod.cls_blocks.0.attn.h4` / `charged_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.6068**
- causal_B_flip: **0.0**
- query_role: `charged_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, charged_hadron<-neutral_hadron, label_Zqq->label_Hbb] = READ_ROUTE(charged_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hbb: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 21. rank020 label_Tbqq -> label_H4q / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.6067**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Tbqq->label_H4q] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_H4q-label_Tbqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbqq->label_H4q: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 22. rank022 label_Hcc -> label_Tbqq / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5805**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Hcc->label_Tbqq] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Tbqq: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 23. rank019 label_Hbb -> label_H4q / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.5688**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hbb->label_H4q] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_H4q-label_Hbb)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hbb->label_H4q: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 24. rank022 label_Hcc -> label_Tbqq / `mod.cls_blocks.0.attn.h4` / `muon<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5550**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-charged_hadron, label_Hcc->label_Tbqq] = READ_ROUTE(muon<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Tbqq: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 25. rank013 label_Hbb -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5487**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Hbb->label_Zqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Hbb)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hbb->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 26. rank017 label_Zqq -> label_Hbb / `mod.cls_blocks.0.attn.h4` / `photon<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5397**
- causal_B_flip: **0.0**
- query_role: `photon`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, photon<-neutral_hadron, label_Zqq->label_Hbb] = READ_ROUTE(photon<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hbb: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 27. rank025 label_H4q -> label_Tbqq / `mod.cls_blocks.0.attn.h4` / `photon<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5120**
- causal_B_flip: **0.0**
- query_role: `photon`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, photon<-neutral_hadron, label_H4q->label_Tbqq] = READ_ROUTE(photon<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Tbqq-label_H4q)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_H4q->label_Tbqq: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 28. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `electron<-electron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.5042**
- causal_B_flip: **0.0**
- query_role: `electron`
- key_role: `electron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, electron<-electron, label_Tbl->label_Hqql] = READ_ROUTE(electron<-electron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 29. rank017 label_Zqq -> label_Hbb / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.4713**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-charged_hadron, label_Zqq->label_Hbb] = READ_ROUTE(neutral_hadron<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hbb: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 30. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-photon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.4671**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `photon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-photon, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-photon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 31. rank017 label_Zqq -> label_Hbb / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.4614**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-charged_hadron, label_Zqq->label_Hbb] = READ_ROUTE(neutral_hadron<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hbb: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 32. rank003 label_Hcc -> label_Hbb / `mod.cls_blocks.0.attn.h4` / `electron<-electron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.4486**
- causal_B_flip: **0.0**
- query_role: `electron`
- key_role: `electron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, electron<-electron, label_Hcc->label_Hbb] = READ_ROUTE(electron<-electron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Hcc)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hcc->label_Hbb: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 33. rank018 label_Zqq -> label_Hcc / `mod.cls_blocks.0.attn.h4` / `photon<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.4441**
- causal_B_flip: **0.0**
- query_role: `photon`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, photon<-charged_hadron, label_Zqq->label_Hcc] = READ_ROUTE(photon<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hcc-label_Zqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Zqq->label_Hcc: head reads photon-hadron coupling. Likely uses electromagnetic fraction / neutral pion related shower structure as a class-evidence axis.

### 34. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-charged_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.4370**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `charged_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-charged_hadron, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-charged_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 35. rank002 label_Wqq -> label_Zqq / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.4240**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_Wqq->label_Zqq] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Zqq-label_Wqq)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Wqq->label_Zqq: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 36. rank008 label_H4q -> label_Hgg / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **-0.3685**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_H4q->label_Hgg] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hgg-label_H4q)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_H4q->label_Hgg: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 37. rank010 label_Hgg -> label_Hbb / `mod.cls_blocks.0.attn.h6` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.3615**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h6, neutral_hadron<-neutral_hadron, label_Hgg->label_Hbb] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hbb-label_Hgg)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Hgg->label_Hbb: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 38. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `CLS<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.3601**
- causal_B_flip: **0.0**
- query_role: `CLS`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, CLS<-muon, label_Tbl->label_Hqql] = READ_ROUTE(CLS<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

### 39. rank016 label_H4q -> label_Hcc / `mod.cls_blocks.0.attn.h4` / `neutral_hadron<-neutral_hadron`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.3384**
- causal_B_flip: **0.0**
- query_role: `neutral_hadron`
- key_role: `neutral_hadron`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, neutral_hadron<-neutral_hadron, label_H4q->label_Hcc] = READ_ROUTE(neutral_hadron<-neutral_hadron) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hcc-label_H4q)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_H4q->label_Hcc: head reads hadron-hadron topology. Likely computes jet-substructure, neutral/charged energy flow, prong geometry, or fragmentation pattern used to separate hadronic classes.

### 40. rank014 label_Tbl -> label_Hqql / `mod.cls_blocks.0.attn.h4` / `muon<-muon`

- decode_status: **PARTIAL_DECODE**
- missing: `compiled_route_rule;route_aware_or_refined_pseudocode`
- causal_B_delta: **0.3378**
- causal_B_flip: **0.0**
- query_role: `muon`
- key_role: `muon`
- full_trace_diagnosis: `high_gradient_weak_ablation`
- operation_db_role: ``

**What it computes**

read particle/context via attention head -> write residual channel slice -> shift Hqql/Tbl margin -> top particle roles/compiled routes/causal ablation evidence

**Compiled matrix route**

```text
PROGRAM[mod.cls_blocks.0.attn.h4, muon<-muon, label_Tbl->label_Hqql] = READ_ROUTE(muon<-muon) -> WRITE_RESIDUAL(head_slice) -> PROJECT_LOGIT(label_Hqql-label_Tbl)
```

**Pseudocode**

```python
# MISSING_PSEUDOCODE
```

**Physics interpretation / hypothesis**

label_Tbl->label_Hqql: head reads lepton-linked route. Likely detects semileptonic decay proxy, heavy-flavor/top contamination, or lepton-in-jet evidence.

## Rule

A mechanism is final only when it is DECODED or explicitly marked with the missing decoder fields. Gradients/patches/residual paths are evidence, not the interpretation itself.
