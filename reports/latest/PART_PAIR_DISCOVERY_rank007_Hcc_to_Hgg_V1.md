# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2064**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 6, 'B_Tbl_push_read_write': 2, 'weak_or_distributed': 2056}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank007_Hcc_to_Hgg_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank007_Hcc_to_Hgg_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.3667 | -0.1833 | -0.1833 | 0.1833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1833, value/write=-0.1833 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3667 | -0.1833 | -0.1833 | 0.1833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.1833, value/write=-0.1833 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2991 | -0.1496 | -0.1496 | 0.1496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1496, value/write=-0.1496 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2991 | -0.1496 | -0.1496 | 0.1496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1496, value/write=-0.1496 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0700 | 0.0350 | 0.0350 | 0.0350 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-electron; natural A×grad=0.0350, value/write=0.0350 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0599 | -0.0251 | -0.0251 | 0.0347 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0251, value/write=-0.0251 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0578 | -0.0240 | -0.0240 | 0.0338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0240, value/write=-0.0240 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0452 | 0.0226 | 0.0226 | 0.0226 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0226, value/write=0.0226 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0329 | -0.0165 | -0.0165 | 0.0165 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0165, value/write=-0.0165 so it resists Tbl / protective. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0329 | -0.0165 | -0.0165 | 0.0165 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0165, value/write=-0.0165 so it resists Tbl / protective. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0232 | 0.0116 | 0.0116 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-electron; natural A×grad=0.0116, value/write=0.0116 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0210 | 0.0093 | 0.0093 | 0.0117 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-photon; natural A×grad=0.0093, value/write=0.0093 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0209 | -0.0055 | -0.0055 | 0.0153 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0055, value/write=-0.0055 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-electron | 0.0204 | 0.0102 | 0.0102 | 0.0102 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-electron; natural A×grad=0.0102, value/write=0.0102 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0196 | 0.0086 | 0.0086 | 0.0110 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-photon; natural A×grad=0.0086, value/write=0.0086 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0195 | -6.933e-04 | -6.933e-04 | 0.0189 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-charged_hadron; natural A×grad=-6.933e-04, value/write=-6.933e-04 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0187 | -0.0032 | -0.0032 | 0.0155 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=-0.0032, value/write=-0.0032 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0169 | 0.0079 | 0.0079 | 0.0090 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=0.0079, value/write=0.0079 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0164 | 0.0070 | 0.0070 | 0.0094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-photon; natural A×grad=0.0070, value/write=0.0070 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-charged_hadron | 0.0162 | 7.293e-04 | 7.293e-04 | 0.0155 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-charged_hadron; natural A×grad=7.293e-04, value/write=7.293e-04 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0152 | 3.424e-04 | 3.424e-04 | 0.0149 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=3.424e-04, value/write=3.424e-04 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0152 | -0.0033 | -0.0033 | 0.0119 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0033, value/write=-0.0033 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0146 | 0.0073 | 0.0073 | 0.0073 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0073, value/write=0.0073 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.blocks.3.attn.h5 | muon<-muon | 0.0138 | -0.0058 | -0.0058 | 0.0080 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h5 uses muon<-muon; natural A×grad=-0.0058, value/write=-0.0058 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0132 | 0.0037 | 0.0037 | 0.0096 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-neutral_hadron; natural A×grad=0.0037, value/write=0.0037 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0126 | 0.0049 | 0.0049 | 0.0077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0049, value/write=0.0049 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0117 | 0.0055 | 0.0055 | 0.0062 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=0.0055, value/write=0.0055 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0114 | 0.0043 | 0.0043 | 0.0071 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-charged_hadron; natural A×grad=0.0043, value/write=0.0043 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0110 | 0.0031 | 0.0031 | 0.0079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=0.0031, value/write=0.0031 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.0110 | 0.0031 | 0.0031 | 0.0079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-muon; natural A×grad=0.0031, value/write=0.0031 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0700 | 0.0350 | 0.0350 | 0.0350 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-electron; natural A×grad=0.0350, value/write=0.0350 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0452 | 0.0226 | 0.0226 | 0.0226 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0226, value/write=0.0226 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.3667 | -0.1833 | -0.1833 | 0.1833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1833, value/write=-0.1833 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3667 | -0.1833 | -0.1833 | 0.1833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.1833, value/write=-0.1833 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2991 | -0.1496 | -0.1496 | 0.1496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1496, value/write=-0.1496 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2991 | -0.1496 | -0.1496 | 0.1496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1496, value/write=-0.1496 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0599 | -0.0251 | -0.0251 | 0.0347 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0251, value/write=-0.0251 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0578 | -0.0240 | -0.0240 | 0.0338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0240, value/write=-0.0240 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
