# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2144**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 8, 'weak_or_distributed': 2136}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank006_Hbb_to_Hgg_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank006_Hbb_to_Hgg_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.9097 | -0.4548 | -0.4548 | 0.4548 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.4548, value/write=-0.4548 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.6538 | -0.3269 | -0.3269 | 0.3269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.3269, value/write=-0.3269 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.5296 | -0.2648 | -0.2648 | 0.2648 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.2648, value/write=-0.2648 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4156 | -0.2078 | -0.2078 | 0.2078 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.2078, value/write=-0.2078 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3082 | -0.1541 | -0.1541 | 0.1541 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1541, value/write=-0.1541 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2943 | -0.1471 | -0.1471 | 0.1471 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1471, value/write=-0.1471 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2775 | -0.1388 | -0.1388 | 0.1388 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1388, value/write=-0.1388 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2267 | -0.1133 | -0.1133 | 0.1133 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1133, value/write=-0.1133 so it resists Tbl / protective. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0398 | -0.0156 | -0.0156 | 0.0242 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0156, value/write=-0.0156 so it resists Tbl / protective. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0319 | -0.0098 | -0.0098 | 0.0221 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0098, value/write=-0.0098 so it resists Tbl / protective. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0286 | 0.0143 | 0.0143 | 0.0143 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0143, value/write=0.0143 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0279 | 0.0139 | 0.0139 | 0.0139 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0139, value/write=0.0139 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0269 | 0.0134 | 0.0134 | 0.0134 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0134, value/write=0.0134 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0251 | 0.0125 | 0.0125 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-electron; natural A×grad=0.0125, value/write=0.0125 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0232 | 0.0116 | 0.0116 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0116, value/write=0.0116 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0231 | 0.0116 | 0.0116 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0116, value/write=0.0116 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0230 | 0.0115 | 0.0115 | 0.0115 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-muon; natural A×grad=0.0115, value/write=0.0115 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0217 | 0.0109 | 0.0109 | 0.0109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0109, value/write=0.0109 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0217 | 0.0109 | 0.0109 | 0.0109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0109, value/write=0.0109 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0197 | -0.0056 | -0.0056 | 0.0141 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0056, value/write=-0.0056 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0189 | 0.0094 | 0.0094 | 0.0094 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0094, value/write=0.0094 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0183 | -0.0017 | -0.0017 | 0.0167 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=-0.0017, value/write=-0.0017 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0182 | 0.0091 | 0.0091 | 0.0091 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=0.0091, value/write=0.0091 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0180 | 0.0025 | 0.0025 | 0.0156 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=0.0025, value/write=0.0025 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0180 | 0.0056 | 0.0056 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-neutral_hadron; natural A×grad=0.0056, value/write=0.0056 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0178 | 0.0089 | 0.0089 | 0.0089 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0089, value/write=0.0089 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0170 | 0.0067 | 0.0067 | 0.0103 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-neutral_hadron; natural A×grad=0.0067, value/write=0.0067 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0162 | 0.0071 | 0.0071 | 0.0091 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-photon; natural A×grad=0.0071, value/write=0.0071 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0160 | 0.0054 | 0.0054 | 0.0106 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-photon; natural A×grad=0.0054, value/write=0.0054 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0156 | -0.0041 | -0.0041 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0041, value/write=-0.0041 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
_No rows._

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.9097 | -0.4548 | -0.4548 | 0.4548 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.4548, value/write=-0.4548 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.6538 | -0.3269 | -0.3269 | 0.3269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.3269, value/write=-0.3269 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.5296 | -0.2648 | -0.2648 | 0.2648 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.2648, value/write=-0.2648 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4156 | -0.2078 | -0.2078 | 0.2078 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.2078, value/write=-0.2078 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3082 | -0.1541 | -0.1541 | 0.1541 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1541, value/write=-0.1541 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2943 | -0.1471 | -0.1471 | 0.1471 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1471, value/write=-0.1471 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2775 | -0.1388 | -0.1388 | 0.1388 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1388, value/write=-0.1388 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2267 | -0.1133 | -0.1133 | 0.1133 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1133, value/write=-0.1133 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
