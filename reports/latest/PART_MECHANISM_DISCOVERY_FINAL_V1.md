# PART_MECHANISM_DISCOVERY_FINAL_V1

Final frozen mechanism-discovery report for current ParT Hqql/Tbl interpretation pass. This report summarizes the matrix decoder formula, validated mechanisms, evidence chain, and remaining work needed for full-model interpretation.

## Status

- **Current claim:** model is not fully decompiled end-to-end, but the Hqql/Tbl decision region now has validated matrix-program mechanisms.
- **Validated scope:** read routes, value/write contribution, head-level gradients, pair-level interventions, and Hqql/Tbl margin/flips.
- **Not yet full-model scope:** all residual paths, all MLP/classifier terms, every head/pair over all classes, and cross-layer path composition.

## Matrix decoder formula

For one attention head `h`:

```text
Q_h = X W_Q^h
K_h = X W_K^h
V_h = X W_V^h
S_h = Q_h K_h^T / sqrt(d) + mask
A_h = softmax(S_h)
C_h = A_h V_h
Y_h = C_h W_O^h
J = logit_Tbl - logit_Hqql  (or signed per group)
READ(h, q<-k)  = mean_{q in role_q, k in role_k} A_h[q,k] * dJ/dA_h[q,k]
WRITE(h, q<-k) = mean_{q in role_q, k in role_k} A_h[q,k] * dot(V_h[k], dJ/dC_h[q])
PATCH(h, q<-k) = S_h[q,k] += beta; measure Δ(logit_Tbl-logit_Hqql), ΔTbl_pred_rate
```

## Evidence pipeline

```text
real replay groups
→ all-head differentiable supertrace
→ natural attention A×grad
→ value/write A*dot(V,grad_C)
→ discovery candidates
→ exact head+role-pair causal validation
→ final mechanism report
```

## Input report sizes / counts

| source | count/status |
| --- | --- |
| discovery_candidates | 2176 |
| balanced_validation_rows | 24 |
| validated_strong_rows | 13 |
| natural_attention_rows | 4240 |
| value_write_rows | 4240 |
| allhead_events | 256 |
| matrix_heads | 80 |

## Diagnosis counts

| diagnosis | discovery_count | validation_count |
| --- | --- | --- |
| B_Tbl_push_read_write | 6 | 6 |
| B_Tbl_resist_or_protective_read_write | 17 | 6 |
| causal_candidate | 100 | 6 |
| high_gradient_write_node | 4 | 6 |
| rule_supported_weak_write | 475 | 0 |
| weak_or_distributed | 1574 | 0 |

## Mechanism 1: CLS h4 lepton self-route protective mechanism

Interpretation: `mod.cls_blocks.0.attn.h4` reads lepton self/CLS-lepton routes and writes a protective signal that suppresses erroneous Tbl-like margin in Hqql→Tbl cases.

| rank | head | pair | action | B_delta | B_flip | A_damage | C_damage | B_write | Agrad | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | up | -1.1925 | -0.3750 | 0.9901 | 1.9078 | -0.4598 | -0.4598 | 1.2180 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-electron | up | -1.0486 | -0.4062 | 1.3805 | 1.6979 | -0.3289 | -0.3289 | 1.0916 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-muon | up | -1.1249 | -0.3438 | 0.6201 | 3.3142 | -0.4664 | -0.4664 | 0.8288 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-muon | down | 1.0003 | 0.0000 | 0.8061 | 0.8141 | -0.4664 | -0.4664 | 0.5953 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-electron | down | 0.9589 | 0.0000 | 1.3631 | 0.7772 | -0.4598 | -0.4598 | 0.4238 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-electron | down | 0.9461 | 0.0000 | 1.3714 | 0.7233 | -0.3289 | -0.3289 | 0.4224 |

Pseudocode:

```text
HEAD mod.cls_blocks.0.attn.h4
IF CLS/electron/muon self-evidence is strong
THEN write anti-Tbl / Hqql-protective evidence into the decision stream
EVIDENCE: boosting these routes drives B_Hqql_to_Tbl margin downward and causes Tbl prediction-rate drops.
```

## Mechanism 2: CLS h4 photon/hadron Tbl-push mechanism

Interpretation: a smaller set of `mod.cls_blocks.0.attn.h4` photon/hadron routes pushes B examples toward Tbl-like margin.

| rank | head | pair | action | B_delta | B_flip | A_damage | C_damage | B_write | Agrad | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | up | 0.3823 | 0.0000 | 0.0277 | 0.0460 | 0.0261 | 0.0261 | 0.3639 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | down | -0.1109 | -0.0625 | 0.0114 | 0.1530 | 0.0261 | 0.0261 | 0.1948 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-muon | up | 0.1421 | 0.0000 | 5.960e-08 | 0.2789 | 0.0209 | 0.0209 | 0.0724 |

Pseudocode:

```text
HEAD mod.cls_blocks.0.attn.h4
IF photon reads charged/neutral hadron context
THEN increase Tbl-like evidence
EVIDENCE: boosting push routes increases B Tbl-Hqql margin; suppressing can reduce margin/flips.
```

## Mechanism 3: blocks.7 h3 charged-hadron/lepton causal route

Interpretation: `mod.blocks.7.attn.h3` is a weaker but rule-supported particle-block route. It links charged-hadron/lepton relations before CLS aggregation.

| rank | head | pair | action | B_delta | B_flip | A_damage | C_damage | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.blocks.7.attn.h3 | charged_hadron<-electron | up | -0.0682 | 0.0000 | 0.0546 | 0.1019 | -6.774e-04 | -6.774e-04 | 2 | 0.0291 |

Pseudocode:

```text
HEAD mod.blocks.7.attn.h3
IF charged_hadron attends to electron/muon route
THEN modify later Hqql/Tbl decision evidence
EVIDENCE: exact pair patch changes B margin in predicted direction; route has compiled rule support.
```

## Additional high-gradient validated nodes

| rank | head | pair | action | B_delta | B_flip | B_write | Agrad | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | up | 0.2301 | 0.0000 | 0.0173 | 0.0173 | 0.2140 |
| 2 | mod.cls_blocks.0.attn.h1 | charged_hadron<-photon | up | 0.0554 | 0.0000 | 0.0167 | 0.0167 | 0.0124 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | down | 0.0564 | 0.0000 | -0.0089 | -0.0089 | 0.0064 |

## What is already interpretable

- The Hqql/Tbl region has validated read/write mechanisms, not just saliency.
- For selected heads/pairs we know real attention route (`A×grad`), value/write direction (`A*dot(V,grad_C)`), causal direction, margin change, and prediction-flip change.
- The strongest currently validated node is `mod.cls_blocks.0.attn.h4`, especially lepton self/CLS-lepton routes.

## What remains for full-model interpretation

1. **All heads/all pairs sweep:** run balanced validation over every high-score pair, not only top 12 short mode.
2. **Residual path composition:** connect particle-block outputs → CLS blocks → classifier logits with per-layer residual contribution.
3. **MLP/classifier decoder:** decompose final classifier and any FFN/MLP residual terms into class directions.
4. **Cross-class expansion:** repeat beyond Hqql/Tbl for all JetClass class pairs.
5. **Stability:** rerun candidates at 128/256/512 events and multiple strengths; keep only stable mechanisms.
6. **Program compiler:** emit one machine-readable pseudocode graph: nodes=head/pair/write, edges=residual/CLS/classifier, weights=validated causal effects.

## Final claim

```text
Current project state:
  Not a full end-to-end decompiler of the whole ParT model yet.
  But it is a working matrix-program mechanism decoder for Hqql/Tbl.
  It has validated read→write→margin→causal-patch mechanisms.
Next goal:
  Extend from validated Hqql/Tbl mechanisms to full-model program graph.
```
