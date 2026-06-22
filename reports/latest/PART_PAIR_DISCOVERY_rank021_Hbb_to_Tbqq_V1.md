# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2160**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 6, 'B_Tbl_push_read_write': 3, 'weak_or_distributed': 2151}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank021_Hbb_to_Tbqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank021_Hbb_to_Tbqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1239 | -0.0619 | -0.0619 | 0.0619 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0619, value/write=-0.0619 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1089 | -0.0386 | -0.0386 | 0.0702 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0386, value/write=-0.0386 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0929 | -0.0459 | -0.0459 | 0.0471 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.0459, value/write=-0.0459 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0592 | 0.0296 | 0.0296 | 0.0296 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0296, value/write=0.0296 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0586 | -0.0293 | -0.0293 | 0.0293 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses charged_hadron<-muon; natural A×grad=-0.0293, value/write=-0.0293 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0503 | 0.0252 | 0.0252 | 0.0252 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0252, value/write=0.0252 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0464 | -0.0232 | -0.0232 | 0.0232 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0232, value/write=-0.0232 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0416 | 0.0208 | 0.0208 | 0.0208 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-muon; natural A×grad=0.0208, value/write=0.0208 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0407 | -0.0065 | -0.0065 | 0.0342 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0065, value/write=-0.0065 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0403 | -0.0202 | -0.0202 | 0.0202 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-muon; natural A×grad=-0.0202, value/write=-0.0202 so it resists Tbl / protective. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0352 | -0.0022 | -0.0022 | 0.0330 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0022, value/write=-0.0022 so it resists Tbl / protective. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0348 | -0.0165 | -0.0165 | 0.0184 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0165, value/write=-0.0165 so it resists Tbl / protective. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0298 | 0.0149 | 0.0149 | 0.0149 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-electron; natural A×grad=0.0149, value/write=0.0149 so it pushes B toward Tbl. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0288 | -0.0071 | -0.0071 | 0.0217 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0071, value/write=-0.0071 so it resists Tbl / protective. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0282 | 0.0077 | 0.0077 | 0.0205 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-muon; natural A×grad=0.0077, value/write=0.0077 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0273 | 0.0119 | 0.0119 | 0.0154 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0119, value/write=0.0119 so it pushes B toward Tbl. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0253 | 0.0127 | 0.0127 | 0.0127 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0127, value/write=0.0127 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0245 | 0.0117 | 0.0117 | 0.0128 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=0.0117, value/write=0.0117 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0244 | 0.0122 | 0.0122 | 0.0122 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-muon; natural A×grad=0.0122, value/write=0.0122 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0236 | 0.0118 | 0.0118 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0118, value/write=0.0118 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0234 | 0.0095 | 0.0095 | 0.0139 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=0.0095, value/write=0.0095 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0231 | -0.0030 | -0.0030 | 0.0201 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0030, value/write=-0.0030 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0224 | -0.0112 | -0.0112 | 0.0112 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=-0.0112, value/write=-0.0112 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0222 | 0.0014 | 0.0014 | 0.0208 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=0.0014, value/write=0.0014 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0213 | 0.0106 | 0.0106 | 0.0106 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0106, value/write=0.0106 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0206 | 0.0069 | 0.0069 | 0.0137 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0202 | 0.0062 | 0.0062 | 0.0140 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=0.0062, value/write=0.0062 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0197 | 0.0089 | 0.0089 | 0.0109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=0.0089, value/write=0.0089 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0167 | 0.0047 | 0.0047 | 0.0120 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-muon; natural A×grad=0.0047, value/write=0.0047 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0164 | -0.0080 | -0.0080 | 0.0084 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses CLS<-muon; natural A×grad=-0.0080, value/write=-0.0080 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0592 | 0.0296 | 0.0296 | 0.0296 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0296, value/write=0.0296 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0503 | 0.0252 | 0.0252 | 0.0252 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0252, value/write=0.0252 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0416 | 0.0208 | 0.0208 | 0.0208 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-muon; natural A×grad=0.0208, value/write=0.0208 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1239 | -0.0619 | -0.0619 | 0.0619 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0619, value/write=-0.0619 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1089 | -0.0386 | -0.0386 | 0.0702 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0386, value/write=-0.0386 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0929 | -0.0459 | -0.0459 | 0.0471 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.0459, value/write=-0.0459 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0586 | -0.0293 | -0.0293 | 0.0293 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses charged_hadron<-muon; natural A×grad=-0.0293, value/write=-0.0293 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0464 | -0.0232 | -0.0232 | 0.0232 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0232, value/write=-0.0232 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0403 | -0.0202 | -0.0202 | 0.0202 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-muon; natural A×grad=-0.0202, value/write=-0.0202 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
