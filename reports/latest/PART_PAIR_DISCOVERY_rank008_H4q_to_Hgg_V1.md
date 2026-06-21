# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **1840**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 6, 'B_Tbl_push_read_write': 1, 'weak_or_distributed': 1833}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank008_H4q_to_Hgg_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank008_H4q_to_Hgg_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3504 | -0.1752 | -0.1752 | 0.1752 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.1752, value/write=-0.1752 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2730 | -0.1365 | -0.1365 | 0.1365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1365, value/write=-0.1365 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1274 | -0.0637 | -0.0637 | 0.0637 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0637, value/write=-0.0637 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1057 | -0.0528 | -0.0528 | 0.0528 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0528, value/write=-0.0528 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0705 | 0.0352 | 0.0352 | 0.0352 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-electron; natural A×grad=0.0352, value/write=0.0352 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0408 | -0.0204 | -0.0204 | 0.0204 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.0204, value/write=-0.0204 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0404 | -0.0202 | -0.0202 | 0.0202 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.0202, value/write=-0.0202 so it resists Tbl / protective. Routes:  |
| 8 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0313 | -0.0134 | -0.0134 | 0.0179 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0134, value/write=-0.0134 so it resists Tbl / protective. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0263 | -0.0131 | -0.0131 | 0.0131 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0131, value/write=-0.0131 so it resists Tbl / protective. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0249 | 0.0124 | 0.0124 | 0.0124 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=0.0124, value/write=0.0124 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0249 | 0.0124 | 0.0124 | 0.0124 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-muon; natural A×grad=0.0124, value/write=0.0124 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0235 | 0.0113 | 0.0113 | 0.0122 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-electron; natural A×grad=0.0113, value/write=0.0113 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0219 | -0.0109 | -0.0109 | 0.0109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0109, value/write=-0.0109 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.blocks.0.attn.h3 | electron<-electron | 0.0203 | 0.0087 | 0.0087 | 0.0116 | n/a | 0 | n/a | n/a | mod.blocks.0.attn.h3 uses electron<-electron; natural A×grad=0.0087, value/write=0.0087 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0195 | 0.0098 | 0.0098 | 0.0098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-electron; natural A×grad=0.0098, value/write=0.0098 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0171 | 0.0085 | 0.0085 | 0.0085 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-electron; natural A×grad=0.0085, value/write=0.0085 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0152 | -0.0076 | -0.0076 | 0.0076 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0076, value/write=-0.0076 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0151 | -0.0060 | -0.0060 | 0.0091 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0060, value/write=-0.0060 so it resists Tbl / protective. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0142 | -0.0071 | -0.0071 | 0.0071 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=-0.0071, value/write=-0.0071 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0142 | -0.0033 | -0.0033 | 0.0109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0033, value/write=-0.0033 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0138 | 0.0069 | 0.0069 | 0.0069 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0135 | -0.0019 | -0.0019 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0019, value/write=-0.0019 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0124 | -0.0062 | -0.0062 | 0.0062 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=-0.0062, value/write=-0.0062 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0116 | 0.0045 | 0.0045 | 0.0071 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=0.0045, value/write=0.0045 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0115 | -0.0025 | -0.0025 | 0.0090 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0025, value/write=-0.0025 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0114 | -0.0056 | -0.0056 | 0.0058 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0056, value/write=-0.0056 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0114 | 0.0052 | 0.0052 | 0.0061 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0095 | -0.0041 | -0.0041 | 0.0054 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=-0.0041, value/write=-0.0041 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0094 | 0.0047 | 0.0047 | 0.0047 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0047, value/write=0.0047 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.blocks.2.attn.h3 | muon<-muon | 0.0093 | 0.0047 | 0.0047 | 0.0047 | n/a | 0 | n/a | n/a | mod.blocks.2.attn.h3 uses muon<-muon; natural A×grad=0.0047, value/write=0.0047 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0705 | 0.0352 | 0.0352 | 0.0352 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-electron; natural A×grad=0.0352, value/write=0.0352 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3504 | -0.1752 | -0.1752 | 0.1752 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.1752, value/write=-0.1752 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2730 | -0.1365 | -0.1365 | 0.1365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1365, value/write=-0.1365 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1274 | -0.0637 | -0.0637 | 0.0637 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0637, value/write=-0.0637 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1057 | -0.0528 | -0.0528 | 0.0528 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0528, value/write=-0.0528 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0408 | -0.0204 | -0.0204 | 0.0204 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.0204, value/write=-0.0204 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0404 | -0.0202 | -0.0202 | 0.0202 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.0202, value/write=-0.0202 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
