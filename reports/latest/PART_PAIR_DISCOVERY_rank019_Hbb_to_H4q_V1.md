# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2144**
- diagnosis_counts: `{'B_Tbl_push_read_write': 13, 'B_Tbl_resist_or_protective_read_write': 4, 'weak_or_distributed': 2127}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank019_Hbb_to_H4q_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank019_Hbb_to_H4q_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.4134 | 0.7067 | 0.7067 | 0.7067 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.7067, value/write=0.7067 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.8210 | 0.4105 | 0.4105 | 0.4105 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.4105, value/write=0.4105 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3467 | 0.1692 | 0.1692 | 0.1775 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.1692, value/write=0.1692 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.2753 | -0.1377 | -0.1377 | 0.1377 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses neutral_hadron<-electron; natural A×grad=-0.1377, value/write=-0.1377 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.2286 | 0.1143 | 0.1143 | 0.1143 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1143, value/write=0.1143 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1855 | 0.0768 | 0.0768 | 0.1087 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0768, value/write=0.0768 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1007 | 0.0450 | 0.0450 | 0.0558 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0450, value/write=0.0450 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0953 | 0.0477 | 0.0477 | 0.0477 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0477, value/write=0.0477 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0809 | 0.0405 | 0.0405 | 0.0405 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0405, value/write=0.0405 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0758 | -0.0379 | -0.0379 | 0.0379 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=-0.0379, value/write=-0.0379 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0666 | 0.0333 | 0.0333 | 0.0333 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0333, value/write=0.0333 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0640 | 0.0320 | 0.0320 | 0.0320 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0320, value/write=0.0320 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0587 | -0.0292 | -0.0292 | 0.0294 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses CLS<-electron; natural A×grad=-0.0292, value/write=-0.0292 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0553 | -0.0155 | -0.0155 | 0.0398 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0155, value/write=-0.0155 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0543 | -0.0272 | -0.0272 | 0.0272 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-electron; natural A×grad=-0.0272, value/write=-0.0272 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0542 | 0.0271 | 0.0271 | 0.0271 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0271, value/write=0.0271 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0511 | 0.0255 | 0.0255 | 0.0255 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0255, value/write=0.0255 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0444 | 0.0222 | 0.0222 | 0.0222 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0222, value/write=0.0222 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0393 | 0.0150 | 0.0150 | 0.0243 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0150, value/write=0.0150 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0385 | 0.0193 | 0.0193 | 0.0193 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=0.0193, value/write=0.0193 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0280 | 0.0112 | 0.0112 | 0.0168 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0112, value/write=0.0112 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0260 | 0.0130 | 0.0130 | 0.0130 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=0.0130, value/write=0.0130 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0225 | 0.0040 | 0.0040 | 0.0185 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0040, value/write=0.0040 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.0225 | -0.0112 | -0.0112 | 0.0112 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-electron; natural A×grad=-0.0112, value/write=-0.0112 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0221 | 0.0109 | 0.0109 | 0.0112 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h5 uses charged_hadron<-electron; natural A×grad=0.0109, value/write=0.0109 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0219 | -0.0104 | -0.0104 | 0.0115 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-electron; natural A×grad=-0.0104, value/write=-0.0104 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0206 | -0.0078 | -0.0078 | 0.0127 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0078, value/write=-0.0078 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0198 | -0.0068 | -0.0068 | 0.0130 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-electron; natural A×grad=-0.0068, value/write=-0.0068 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0193 | -0.0087 | -0.0087 | 0.0106 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0087, value/write=-0.0087 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0190 | -0.0091 | -0.0091 | 0.0100 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0091, value/write=-0.0091 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.4134 | 0.7067 | 0.7067 | 0.7067 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.7067, value/write=0.7067 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.8210 | 0.4105 | 0.4105 | 0.4105 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.4105, value/write=0.4105 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3467 | 0.1692 | 0.1692 | 0.1775 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.1692, value/write=0.1692 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.2286 | 0.1143 | 0.1143 | 0.1143 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1143, value/write=0.1143 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1855 | 0.0768 | 0.0768 | 0.1087 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0768, value/write=0.0768 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1007 | 0.0450 | 0.0450 | 0.0558 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0450, value/write=0.0450 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0953 | 0.0477 | 0.0477 | 0.0477 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0477, value/write=0.0477 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0809 | 0.0405 | 0.0405 | 0.0405 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0405, value/write=0.0405 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0666 | 0.0333 | 0.0333 | 0.0333 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0333, value/write=0.0333 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0640 | 0.0320 | 0.0320 | 0.0320 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0320, value/write=0.0320 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0542 | 0.0271 | 0.0271 | 0.0271 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0271, value/write=0.0271 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0511 | 0.0255 | 0.0255 | 0.0255 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0255, value/write=0.0255 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0444 | 0.0222 | 0.0222 | 0.0222 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0222, value/write=0.0222 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.2753 | -0.1377 | -0.1377 | 0.1377 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses neutral_hadron<-electron; natural A×grad=-0.1377, value/write=-0.1377 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0758 | -0.0379 | -0.0379 | 0.0379 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=-0.0379, value/write=-0.0379 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | CLS<-electron | 0.0587 | -0.0292 | -0.0292 | 0.0294 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses CLS<-electron; natural A×grad=-0.0292, value/write=-0.0292 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0543 | -0.0272 | -0.0272 | 0.0272 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-electron; natural A×grad=-0.0272, value/write=-0.0272 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
