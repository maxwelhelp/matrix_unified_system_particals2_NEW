# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2048**
- diagnosis_counts: `{'B_Tbl_push_read_write': 11, 'weak_or_distributed': 2037}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank011_Hgg_to_Hcc_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank011_Hgg_to_Hcc_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3207 | 0.1604 | 0.1604 | 0.1604 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1604, value/write=0.1604 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3147 | 0.1573 | 0.1573 | 0.1573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1573, value/write=0.1573 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2984 | 0.1492 | 0.1492 | 0.1492 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1492, value/write=0.1492 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2416 | 0.1208 | 0.1208 | 0.1208 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1208, value/write=0.1208 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2353 | 0.1176 | 0.1176 | 0.1176 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1176, value/write=0.1176 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2258 | 0.1129 | 0.1129 | 0.1129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.1129, value/write=0.1129 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0990 | 0.0495 | 0.0495 | 0.0495 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0495, value/write=0.0495 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0744 | 0.0372 | 0.0372 | 0.0372 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0372, value/write=0.0372 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0670 | 0.0289 | 0.0289 | 0.0381 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0289, value/write=0.0289 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0533 | 0.0266 | 0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0266, value/write=0.0266 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0515 | 0.0258 | 0.0258 | 0.0258 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0258, value/write=0.0258 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0402 | 0.0165 | 0.0165 | 0.0238 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0165, value/write=0.0165 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0296 | 0.0148 | 0.0148 | 0.0148 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0148, value/write=0.0148 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0273 | 0.0071 | 0.0071 | 0.0202 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0071, value/write=0.0071 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0258 | 0.0124 | 0.0124 | 0.0133 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-neutral_hadron; natural A×grad=0.0124, value/write=0.0124 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0250 | 0.0125 | 0.0125 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0125, value/write=0.0125 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0242 | -0.0121 | -0.0121 | 0.0121 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-muon; natural A×grad=-0.0121, value/write=-0.0121 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0218 | 0.0022 | 0.0022 | 0.0196 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=0.0022, value/write=0.0022 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0217 | -0.0066 | -0.0066 | 0.0152 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-charged_hadron; natural A×grad=-0.0066, value/write=-0.0066 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0215 | -0.0093 | -0.0093 | 0.0122 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-photon; natural A×grad=-0.0093, value/write=-0.0093 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0197 | -0.0059 | -0.0059 | 0.0138 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-photon; natural A×grad=-0.0059, value/write=-0.0059 so it resists Tbl / protective. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0197 | 0.0072 | 0.0072 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0072, value/write=0.0072 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0194 | -0.0073 | -0.0073 | 0.0121 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-electron; natural A×grad=-0.0073, value/write=-0.0073 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0186 | -0.0073 | -0.0073 | 0.0113 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-photon; natural A×grad=-0.0073, value/write=-0.0073 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0185 | 0.0027 | 0.0027 | 0.0159 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-charged_hadron; natural A×grad=0.0027, value/write=0.0027 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0169 | 0.0022 | 0.0022 | 0.0148 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0022, value/write=0.0022 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0168 | -0.0031 | -0.0031 | 0.0137 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-neutral_hadron; natural A×grad=-0.0031, value/write=-0.0031 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.blocks.3.attn.h4 | electron<-electron | 0.0164 | -0.0082 | -0.0082 | 0.0082 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h4 uses electron<-electron; natural A×grad=-0.0082, value/write=-0.0082 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.blocks.1.attn.h4 | electron<-electron | 0.0158 | -0.0079 | -0.0079 | 0.0079 | n/a | 0 | n/a | n/a | mod.blocks.1.attn.h4 uses electron<-electron; natural A×grad=-0.0079, value/write=-0.0079 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0155 | -0.0078 | -0.0078 | 0.0078 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-muon; natural A×grad=-0.0078, value/write=-0.0078 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3207 | 0.1604 | 0.1604 | 0.1604 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1604, value/write=0.1604 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3147 | 0.1573 | 0.1573 | 0.1573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1573, value/write=0.1573 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2984 | 0.1492 | 0.1492 | 0.1492 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1492, value/write=0.1492 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2416 | 0.1208 | 0.1208 | 0.1208 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1208, value/write=0.1208 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2353 | 0.1176 | 0.1176 | 0.1176 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1176, value/write=0.1176 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2258 | 0.1129 | 0.1129 | 0.1129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.1129, value/write=0.1129 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0990 | 0.0495 | 0.0495 | 0.0495 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0495, value/write=0.0495 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0744 | 0.0372 | 0.0372 | 0.0372 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0372, value/write=0.0372 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0670 | 0.0289 | 0.0289 | 0.0381 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0289, value/write=0.0289 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0533 | 0.0266 | 0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0266, value/write=0.0266 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0515 | 0.0258 | 0.0258 | 0.0258 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0258, value/write=0.0258 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
_No rows._

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
