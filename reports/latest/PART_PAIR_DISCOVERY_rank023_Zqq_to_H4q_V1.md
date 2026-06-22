# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2064**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 18, 'weak_or_distributed': 2045, 'B_Tbl_push_read_write': 1}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank023_Zqq_to_H4q_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank023_Zqq_to_H4q_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.8946 | -0.9473 | -0.9473 | 0.9473 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.9473, value/write=-0.9473 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.2159 | -0.6079 | -0.6079 | 0.6079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.6079, value/write=-0.6079 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.0056 | -0.5028 | -0.5028 | 0.5028 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.5028, value/write=-0.5028 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.9578 | -0.4789 | -0.4789 | 0.4789 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.4789, value/write=-0.4789 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.5068 | -0.2534 | -0.2534 | 0.2534 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.2534, value/write=-0.2534 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.4374 | -0.2187 | -0.2187 | 0.2187 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2187, value/write=-0.2187 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.4372 | -0.2186 | -0.2186 | 0.2186 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.2186, value/write=-0.2186 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3683 | -0.1842 | -0.1842 | 0.1842 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1842, value/write=-0.1842 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.2716 | -0.1034 | -0.1034 | 0.1682 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1034, value/write=-0.1034 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0990 | -0.0495 | -0.0495 | 0.0495 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0495, value/write=-0.0495 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0874 | -0.0382 | -0.0382 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0382, value/write=-0.0382 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0697 | -0.0232 | -0.0232 | 0.0466 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0232, value/write=-0.0232 so it resists Tbl / protective. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0684 | -0.0167 | -0.0167 | 0.0517 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0167, value/write=-0.0167 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0670 | -0.0335 | -0.0335 | 0.0335 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0335, value/write=-0.0335 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0642 | 0.0321 | 0.0321 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-electron; natural A×grad=0.0321, value/write=0.0321 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0579 | -0.0290 | -0.0290 | 0.0290 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0290, value/write=-0.0290 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0570 | -0.0109 | -0.0109 | 0.0461 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0109, value/write=-0.0109 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0552 | -0.0276 | -0.0276 | 0.0276 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0276, value/write=-0.0276 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0543 | -0.0272 | -0.0272 | 0.0272 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0272, value/write=-0.0272 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0533 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |
| 21 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0442 | -0.0221 | -0.0221 | 0.0221 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0330 | -4.023e-04 | -4.023e-04 | 0.0326 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-4.023e-04, value/write=-4.023e-04 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0314 | 0.0157 | 0.0157 | 0.0157 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-muon; natural A×grad=0.0157, value/write=0.0157 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0314 | 0.0157 | 0.0157 | 0.0157 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=0.0157, value/write=0.0157 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0310 | 0.0118 | 0.0118 | 0.0192 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0118, value/write=0.0118 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0304 | 0.0106 | 0.0106 | 0.0199 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=0.0106, value/write=0.0106 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0277 | 0.0087 | 0.0087 | 0.0190 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0087, value/write=0.0087 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0258 | 0.0129 | 0.0129 | 0.0129 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-electron; natural A×grad=0.0129, value/write=0.0129 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0257 | 0.0062 | 0.0062 | 0.0195 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=0.0062, value/write=0.0062 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0257 | -0.0128 | -0.0128 | 0.0128 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0128, value/write=-0.0128 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0642 | 0.0321 | 0.0321 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-electron; natural A×grad=0.0321, value/write=0.0321 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.8946 | -0.9473 | -0.9473 | 0.9473 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.9473, value/write=-0.9473 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.2159 | -0.6079 | -0.6079 | 0.6079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.6079, value/write=-0.6079 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.0056 | -0.5028 | -0.5028 | 0.5028 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.5028, value/write=-0.5028 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.9578 | -0.4789 | -0.4789 | 0.4789 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.4789, value/write=-0.4789 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.5068 | -0.2534 | -0.2534 | 0.2534 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.2534, value/write=-0.2534 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.4374 | -0.2187 | -0.2187 | 0.2187 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2187, value/write=-0.2187 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.4372 | -0.2186 | -0.2186 | 0.2186 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.2186, value/write=-0.2186 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3683 | -0.1842 | -0.1842 | 0.1842 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.1842, value/write=-0.1842 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.2716 | -0.1034 | -0.1034 | 0.1682 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1034, value/write=-0.1034 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0990 | -0.0495 | -0.0495 | 0.0495 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0495, value/write=-0.0495 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0874 | -0.0382 | -0.0382 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0382, value/write=-0.0382 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0697 | -0.0232 | -0.0232 | 0.0466 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0232, value/write=-0.0232 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0670 | -0.0335 | -0.0335 | 0.0335 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0335, value/write=-0.0335 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0579 | -0.0290 | -0.0290 | 0.0290 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0290, value/write=-0.0290 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0552 | -0.0276 | -0.0276 | 0.0276 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0276, value/write=-0.0276 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0543 | -0.0272 | -0.0272 | 0.0272 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0272, value/write=-0.0272 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0533 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0442 | -0.0221 | -0.0221 | 0.0221 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
