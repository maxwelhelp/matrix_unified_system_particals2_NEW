# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2128**
- diagnosis_counts: `{'B_Tbl_push_read_write': 3, 'weak_or_distributed': 2124, 'B_Tbl_resist_or_protective_read_write': 1}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank001_Zqq_to_Wqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank001_Zqq_to_Wqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.2823 | 0.0989 | 0.0989 | 0.1834 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0989, value/write=0.0989 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0712 | 0.0267 | 0.0267 | 0.0445 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0267, value/write=0.0267 so it pushes B toward Tbl. Routes:  |
| 3 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0682 | 0.0079 | 0.0079 | 0.0603 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0079, value/write=0.0079 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0654 | 0.0259 | 0.0259 | 0.0395 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0259, value/write=0.0259 so it pushes B toward Tbl. Routes:  |
| 5 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0623 | 0.0190 | 0.0190 | 0.0433 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0190, value/write=0.0190 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0592 | -0.0263 | -0.0263 | 0.0329 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0263, value/write=-0.0263 so it resists Tbl / protective. Routes:  |
| 7 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0405 | 0.0151 | 0.0151 | 0.0254 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0151, value/write=0.0151 so it pushes B toward Tbl. Routes:  |
| 8 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0346 | 0.0059 | 0.0059 | 0.0287 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=0.0059, value/write=0.0059 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0329 | -0.0118 | -0.0118 | 0.0211 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0118, value/write=-0.0118 so it resists Tbl / protective. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0282 | 0.0141 | 0.0141 | 0.0141 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-electron; natural A×grad=0.0141, value/write=0.0141 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0251 | -0.0091 | -0.0091 | 0.0159 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0091, value/write=-0.0091 so it resists Tbl / protective. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0243 | -0.0051 | -0.0051 | 0.0193 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=-0.0051, value/write=-0.0051 so it resists Tbl / protective. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0236 | -0.0118 | -0.0118 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.0118, value/write=-0.0118 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0236 | -0.0118 | -0.0118 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-muon; natural A×grad=-0.0118, value/write=-0.0118 so it resists Tbl / protective. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0213 | 0.0020 | 0.0020 | 0.0194 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0020, value/write=0.0020 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0212 | 0.0050 | 0.0050 | 0.0162 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0050, value/write=0.0050 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0209 | -0.0077 | -0.0077 | 0.0133 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=-0.0077, value/write=-0.0077 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0204 | 8.372e-04 | 8.372e-04 | 0.0195 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-neutral_hadron; natural A×grad=8.372e-04, value/write=8.372e-04 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0189 | -0.0019 | -0.0019 | 0.0170 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0019, value/write=-0.0019 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0180 | -0.0046 | -0.0046 | 0.0133 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=-0.0046, value/write=-0.0046 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.0164 | -0.0080 | -0.0080 | 0.0083 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses neutral_hadron<-electron; natural A×grad=-0.0080, value/write=-0.0080 so it resists Tbl / protective. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0163 | 0.0082 | 0.0082 | 0.0082 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-electron; natural A×grad=0.0082, value/write=0.0082 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0163 | 0.0046 | 0.0046 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-charged_hadron; natural A×grad=0.0046, value/write=0.0046 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0161 | 0.0058 | 0.0058 | 0.0102 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=0.0058, value/write=0.0058 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0157 | 4.895e-04 | 4.895e-04 | 0.0152 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-charged_hadron; natural A×grad=4.895e-04, value/write=4.895e-04 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0156 | 0.0059 | 0.0059 | 0.0097 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-electron; natural A×grad=0.0059, value/write=0.0059 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0154 | -0.0077 | -0.0077 | 0.0077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-electron; natural A×grad=-0.0077, value/write=-0.0077 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0147 | 0.0060 | 0.0060 | 0.0087 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0060, value/write=0.0060 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0137 | 6.339e-04 | 6.339e-04 | 0.0131 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-charged_hadron; natural A×grad=6.339e-04, value/write=6.339e-04 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0135 | 0.0011 | 0.0011 | 0.0124 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-charged_hadron; natural A×grad=0.0011, value/write=0.0011 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.2823 | 0.0989 | 0.0989 | 0.1834 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0989, value/write=0.0989 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0712 | 0.0267 | 0.0267 | 0.0445 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0267, value/write=0.0267 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0654 | 0.0259 | 0.0259 | 0.0395 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0259, value/write=0.0259 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0592 | -0.0263 | -0.0263 | 0.0329 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0263, value/write=-0.0263 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
