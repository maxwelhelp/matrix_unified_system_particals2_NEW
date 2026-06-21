# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **1840**
- diagnosis_counts: `{'B_Tbl_push_read_write': 6, 'weak_or_distributed': 1834}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank005_Hgg_to_H4q_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank005_Hgg_to_H4q_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.2727 | 0.1364 | 0.1364 | 0.1364 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1364, value/write=0.1364 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2223 | 0.1111 | 0.1111 | 0.1111 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1111, value/write=0.1111 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1718 | 0.0859 | 0.0859 | 0.0859 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0859, value/write=0.0859 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1385 | 0.0692 | 0.0692 | 0.0692 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0692, value/write=0.0692 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0992 | 0.0496 | 0.0496 | 0.0496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0496, value/write=0.0496 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0600 | 0.0300 | 0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0300, value/write=0.0300 so it pushes B toward Tbl. Routes:  |
| 7 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0359 | 0.0161 | 0.0161 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0161, value/write=0.0161 so it pushes B toward Tbl. Routes:  |
| 8 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0255 | 0.0128 | 0.0128 | 0.0128 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0128, value/write=0.0128 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0251 | 0.0125 | 0.0125 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0125, value/write=0.0125 so it pushes B toward Tbl. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0246 | 0.0123 | 0.0123 | 0.0123 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0123, value/write=0.0123 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0151 | 0.0053 | 0.0053 | 0.0098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0053, value/write=0.0053 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0137 | 0.0069 | 0.0069 | 0.0069 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0137 | 0.0069 | 0.0069 | 0.0069 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0137 | 0.0068 | 0.0068 | 0.0068 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0068, value/write=0.0068 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0129 | 0.0043 | 0.0043 | 0.0085 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0043, value/write=0.0043 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0104 | 0.0052 | 0.0052 | 0.0052 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0091 | 0.0045 | 0.0045 | 0.0045 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0045, value/write=0.0045 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0087 | 0.0036 | 0.0036 | 0.0051 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-neutral_hadron; natural A×grad=0.0036, value/write=0.0036 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0086 | 0.0016 | 0.0016 | 0.0069 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0016, value/write=0.0016 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0083 | 0.0035 | 0.0035 | 0.0048 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-neutral_hadron; natural A×grad=0.0035, value/write=0.0035 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0078 | 0.0039 | 0.0039 | 0.0039 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0039, value/write=0.0039 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0075 | 7.989e-04 | 7.989e-04 | 0.0067 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=7.989e-04, value/write=7.989e-04 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0074 | -0.0029 | -0.0029 | 0.0046 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-photon; natural A×grad=-0.0029, value/write=-0.0029 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0074 | 0.0034 | 0.0034 | 0.0040 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0034, value/write=0.0034 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0073 | -0.0032 | -0.0032 | 0.0041 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-photon; natural A×grad=-0.0032, value/write=-0.0032 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0072 | -0.0033 | -0.0033 | 0.0039 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-photon; natural A×grad=-0.0033, value/write=-0.0033 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0069 | -0.0034 | -0.0034 | 0.0034 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h5 uses CLS<-electron; natural A×grad=-0.0034, value/write=-0.0034 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0069 | -0.0034 | -0.0034 | 0.0034 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h5 uses charged_hadron<-electron; natural A×grad=-0.0034, value/write=-0.0034 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0067 | 7.288e-04 | 7.288e-04 | 0.0060 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=7.288e-04, value/write=7.288e-04 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0065 | -0.0020 | -0.0020 | 0.0045 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0020, value/write=-0.0020 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.2727 | 0.1364 | 0.1364 | 0.1364 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1364, value/write=0.1364 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2223 | 0.1111 | 0.1111 | 0.1111 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1111, value/write=0.1111 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1718 | 0.0859 | 0.0859 | 0.0859 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.0859, value/write=0.0859 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1385 | 0.0692 | 0.0692 | 0.0692 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0692, value/write=0.0692 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0992 | 0.0496 | 0.0496 | 0.0496 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0496, value/write=0.0496 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0600 | 0.0300 | 0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0300, value/write=0.0300 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
_No rows._

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
