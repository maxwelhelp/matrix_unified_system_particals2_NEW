# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2048**
- diagnosis_counts: `{'B_Tbl_push_read_write': 3, 'B_Tbl_resist_or_protective_read_write': 5, 'weak_or_distributed': 2040}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank009_Hcc_to_H4q_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank009_Hcc_to_H4q_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.5079 | 0.2539 | 0.2539 | 0.2539 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.2539, value/write=0.2539 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2756 | -0.1378 | -0.1378 | 0.1378 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1378, value/write=-0.1378 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2539 | 0.0909 | 0.0909 | 0.1630 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.0909, value/write=0.0909 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2004 | -0.1002 | -0.1002 | 0.1002 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1002, value/write=-0.1002 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1983 | -0.0992 | -0.0992 | 0.0992 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0992, value/write=-0.0992 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1249 | -0.0506 | -0.0506 | 0.0743 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0506, value/write=-0.0506 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0879 | -0.0439 | -0.0439 | 0.0439 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0439, value/write=-0.0439 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0784 | 0.0207 | 0.0207 | 0.0577 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0207, value/write=0.0207 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0473 | 0.0172 | 0.0172 | 0.0301 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0172, value/write=0.0172 so it pushes B toward Tbl. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0277 | 0.0139 | 0.0139 | 0.0139 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0139, value/write=0.0139 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0264 | 0.0132 | 0.0132 | 0.0132 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0132, value/write=0.0132 so it pushes B toward Tbl. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0257 | 0.0128 | 0.0128 | 0.0128 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0128, value/write=0.0128 so it pushes B toward Tbl. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0244 | 0.0122 | 0.0122 | 0.0122 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0122, value/write=0.0122 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0231 | -0.0116 | -0.0116 | 0.0116 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0116, value/write=-0.0116 so it resists Tbl / protective. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0197 | 0.0097 | 0.0097 | 0.0100 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h5 uses CLS<-electron; natural A×grad=0.0097, value/write=0.0097 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0197 | 0.0097 | 0.0097 | 0.0100 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h5 uses charged_hadron<-electron; natural A×grad=0.0097, value/write=0.0097 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0195 | -0.0098 | -0.0098 | 0.0098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=-0.0098, value/write=-0.0098 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0195 | -0.0098 | -0.0098 | 0.0098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-muon; natural A×grad=-0.0098, value/write=-0.0098 so it resists Tbl / protective. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0187 | 0.0045 | 0.0045 | 0.0142 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0045, value/write=0.0045 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0170 | -0.0041 | -0.0041 | 0.0129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0041, value/write=-0.0041 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0151 | 0.0075 | 0.0075 | 0.0075 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=0.0075, value/write=0.0075 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0150 | 0.0069 | 0.0069 | 0.0081 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0141 | -0.0071 | -0.0071 | 0.0071 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses CLS<-muon; natural A×grad=-0.0071, value/write=-0.0071 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0141 | -0.0071 | -0.0071 | 0.0071 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses charged_hadron<-muon; natural A×grad=-0.0071, value/write=-0.0071 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0129 | 0.0052 | 0.0052 | 0.0077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-electron; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0129 | 0.0052 | 0.0052 | 0.0077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-electron; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0123 | 0.0052 | 0.0052 | 0.0072 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0123 | 0.0052 | 0.0052 | 0.0072 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-electron; natural A×grad=0.0052, value/write=0.0052 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0110 | 0.0055 | 0.0055 | 0.0055 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0055, value/write=0.0055 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0109 | 0.0027 | 0.0027 | 0.0082 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0027, value/write=0.0027 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.5079 | 0.2539 | 0.2539 | 0.2539 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.2539, value/write=0.2539 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2539 | 0.0909 | 0.0909 | 0.1630 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.0909, value/write=0.0909 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0784 | 0.0207 | 0.0207 | 0.0577 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0207, value/write=0.0207 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2756 | -0.1378 | -0.1378 | 0.1378 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1378, value/write=-0.1378 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2004 | -0.1002 | -0.1002 | 0.1002 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1002, value/write=-0.1002 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1983 | -0.0992 | -0.0992 | 0.0992 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0992, value/write=-0.0992 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1249 | -0.0506 | -0.0506 | 0.0743 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0506, value/write=-0.0506 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0879 | -0.0439 | -0.0439 | 0.0439 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0439, value/write=-0.0439 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
