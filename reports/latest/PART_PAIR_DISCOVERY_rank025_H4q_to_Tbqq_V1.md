# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2048**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 6, 'B_Tbl_push_read_write': 3, 'weak_or_distributed': 2039}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank025_H4q_to_Tbqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank025_H4q_to_Tbqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.3471 | -0.6735 | -0.6735 | 0.6735 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.6735, value/write=-0.6735 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.7147 | -0.3573 | -0.3573 | 0.3573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.3573, value/write=-0.3573 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.6941 | -0.3326 | -0.3326 | 0.3615 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.3326, value/write=-0.3326 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3736 | -0.1868 | -0.1868 | 0.1868 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1868, value/write=-0.1868 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2155 | -0.1072 | -0.1072 | 0.1083 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1072, value/write=-0.1072 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2012 | -0.0917 | -0.0917 | 0.1094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0917, value/write=-0.0917 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1156 | 0.0578 | 0.0578 | 0.0578 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0578, value/write=0.0578 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0687 | 0.0343 | 0.0343 | 0.0343 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0343, value/write=0.0343 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0663 | -0.0155 | -0.0155 | 0.0509 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0155, value/write=-0.0155 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0462 | 0.0219 | 0.0219 | 0.0242 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0219, value/write=0.0219 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0397 | 0.0198 | 0.0198 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-muon; natural A×grad=0.0198, value/write=0.0198 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0397 | 0.0198 | 0.0198 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-muon; natural A×grad=0.0198, value/write=0.0198 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0390 | -0.0195 | -0.0195 | 0.0195 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0195, value/write=-0.0195 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0386 | 0.0131 | 0.0131 | 0.0255 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0131, value/write=0.0131 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0306 | -0.0061 | -0.0061 | 0.0245 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0061, value/write=-0.0061 so it resists Tbl / protective. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0290 | -0.0145 | -0.0145 | 0.0145 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-CLS; natural A×grad=-0.0145, value/write=-0.0145 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0281 | -0.0141 | -0.0141 | 0.0141 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0141, value/write=-0.0141 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0278 | 0.0132 | 0.0132 | 0.0146 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-electron; natural A×grad=0.0132, value/write=0.0132 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0276 | -0.0138 | -0.0138 | 0.0138 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0138, value/write=-0.0138 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0259 | 0.0117 | 0.0117 | 0.0143 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0117, value/write=0.0117 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0258 | -0.0129 | -0.0129 | 0.0129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=-0.0129, value/write=-0.0129 so it resists Tbl / protective. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0245 | 0.0085 | 0.0085 | 0.0161 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0085, value/write=0.0085 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0232 | -0.0033 | -0.0033 | 0.0199 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0033, value/write=-0.0033 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0228 | 0.0104 | 0.0104 | 0.0123 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0104, value/write=0.0104 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0228 | -0.0114 | -0.0114 | 0.0114 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0114, value/write=-0.0114 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0222 | -0.0111 | -0.0111 | 0.0111 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=-0.0111, value/write=-0.0111 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0211 | -0.0092 | -0.0092 | 0.0120 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0092, value/write=-0.0092 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0211 | -0.0106 | -0.0106 | 0.0106 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-electron; natural A×grad=-0.0106, value/write=-0.0106 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0208 | -0.0103 | -0.0103 | 0.0105 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0103, value/write=-0.0103 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0194 | 0.0072 | 0.0072 | 0.0122 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0072, value/write=0.0072 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1156 | 0.0578 | 0.0578 | 0.0578 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0578, value/write=0.0578 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0687 | 0.0343 | 0.0343 | 0.0343 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0343, value/write=0.0343 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0462 | 0.0219 | 0.0219 | 0.0242 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0219, value/write=0.0219 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.3471 | -0.6735 | -0.6735 | 0.6735 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.6735, value/write=-0.6735 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.7147 | -0.3573 | -0.3573 | 0.3573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.3573, value/write=-0.3573 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.6941 | -0.3326 | -0.3326 | 0.3615 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.3326, value/write=-0.3326 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3736 | -0.1868 | -0.1868 | 0.1868 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1868, value/write=-0.1868 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2155 | -0.1072 | -0.1072 | 0.1083 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1072, value/write=-0.1072 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2012 | -0.0917 | -0.0917 | 0.1094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0917, value/write=-0.0917 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
