# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2032**
- diagnosis_counts: `{'B_Tbl_push_read_write': 5, 'B_Tbl_resist_or_protective_read_write': 2, 'weak_or_distributed': 2025}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank016_H4q_to_Hcc_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank016_H4q_to_Hcc_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2246 | 0.1123 | 0.1123 | 0.1123 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1123, value/write=0.1123 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1617 | 0.0809 | 0.0809 | 0.0809 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0809, value/write=0.0809 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1408 | 0.0704 | 0.0704 | 0.0704 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.0704, value/write=0.0704 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1172 | 0.0586 | 0.0586 | 0.0586 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.0586, value/write=0.0586 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0863 | -0.0432 | -0.0432 | 0.0432 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.0432, value/write=-0.0432 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0751 | -0.0347 | -0.0347 | 0.0403 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0347, value/write=-0.0347 so it resists Tbl / protective. Routes:  |
| 7 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0648 | -0.0177 | -0.0177 | 0.0470 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.0177, value/write=-0.0177 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0469 | 0.0234 | 0.0234 | 0.0234 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-muon; natural A×grad=0.0234, value/write=0.0234 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0275 | 0.0103 | 0.0103 | 0.0172 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0103, value/write=0.0103 so it pushes B toward Tbl. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0259 | 0.0129 | 0.0129 | 0.0129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=0.0129, value/write=0.0129 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0197 | 0.0098 | 0.0098 | 0.0098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0098, value/write=0.0098 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0190 | -0.0095 | -0.0095 | 0.0095 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0095, value/write=-0.0095 so it resists Tbl / protective. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0185 | 0.0093 | 0.0093 | 0.0093 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0093, value/write=0.0093 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0182 | 0.0091 | 0.0091 | 0.0091 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0091, value/write=0.0091 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0168 | 0.0031 | 0.0031 | 0.0136 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0031, value/write=0.0031 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0165 | -0.0083 | -0.0083 | 0.0083 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0083, value/write=-0.0083 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.1.attn.h2 | photon<-CLS | 0.0164 | 0.0082 | 0.0082 | 0.0082 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h2 uses photon<-CLS; natural A×grad=0.0082, value/write=0.0082 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0163 | 0.0069 | 0.0069 | 0.0094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-charged_hadron; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0157 | -0.0036 | -0.0036 | 0.0121 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0036, value/write=-0.0036 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0153 | -0.0065 | -0.0065 | 0.0088 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0065, value/write=-0.0065 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0148 | -0.0029 | -0.0029 | 0.0119 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=-0.0029, value/write=-0.0029 so it resists Tbl / protective. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0146 | 0.0060 | 0.0060 | 0.0086 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0060, value/write=0.0060 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h3 | neutral_hadron<-muon | 0.0136 | -0.0068 | -0.0068 | 0.0068 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses neutral_hadron<-muon; natural A×grad=-0.0068, value/write=-0.0068 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.1.attn.h0 | neutral_hadron<-muon | 0.0131 | 0.0065 | 0.0065 | 0.0065 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h0 uses neutral_hadron<-muon; natural A×grad=0.0065, value/write=0.0065 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0127 | -0.0033 | -0.0033 | 0.0094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0033, value/write=-0.0033 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.1.attn.h2 | CLS<-CLS | 0.0123 | 0.0061 | 0.0061 | 0.0062 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h2 uses CLS<-CLS; natural A×grad=0.0061, value/write=0.0061 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0112 | 0.0045 | 0.0045 | 0.0068 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-charged_hadron; natural A×grad=0.0045, value/write=0.0045 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0112 | -0.0056 | -0.0056 | 0.0056 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-electron; natural A×grad=-0.0056, value/write=-0.0056 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0112 | 0.0048 | 0.0048 | 0.0063 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0048, value/write=0.0048 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.blocks.3.attn.h0 | electron<-muon | 0.0111 | -0.0055 | -0.0055 | 0.0056 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h0 uses electron<-muon; natural A×grad=-0.0055, value/write=-0.0055 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2246 | 0.1123 | 0.1123 | 0.1123 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1123, value/write=0.1123 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1617 | 0.0809 | 0.0809 | 0.0809 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0809, value/write=0.0809 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1408 | 0.0704 | 0.0704 | 0.0704 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.0704, value/write=0.0704 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1172 | 0.0586 | 0.0586 | 0.0586 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.0586, value/write=0.0586 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0469 | 0.0234 | 0.0234 | 0.0234 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-muon; natural A×grad=0.0234, value/write=0.0234 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0863 | -0.0432 | -0.0432 | 0.0432 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.0432, value/write=-0.0432 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0751 | -0.0347 | -0.0347 | 0.0403 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0347, value/write=-0.0347 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
