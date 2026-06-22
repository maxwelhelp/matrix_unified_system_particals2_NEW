# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2176**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 25, 'B_Tbl_push_read_write': 2, 'weak_or_distributed': 2149}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank015_Hqql_to_Tbl_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank015_Hqql_to_Tbl_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 1.1137 | -0.5568 | -0.5568 | 0.5568 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=-0.5568, value/write=-0.5568 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.0930 | -0.5465 | -0.5465 | 0.5465 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.5465, value/write=-0.5465 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-CLS | 1.0723 | -0.5361 | -0.5361 | 0.5361 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-CLS; natural A×grad=-0.5361, value/write=-0.5361 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.9210 | -0.4600 | -0.4600 | 0.4610 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=-0.4600, value/write=-0.4600 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.5936 | -0.2968 | -0.2968 | 0.2968 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=-0.2968, value/write=-0.2968 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.5400 | -0.2700 | -0.2700 | 0.2700 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2700, value/write=-0.2700 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.5288 | -0.2638 | -0.2638 | 0.2650 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.2638, value/write=-0.2638 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.4864 | -0.2432 | -0.2432 | 0.2432 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-CLS; natural A×grad=-0.2432, value/write=-0.2432 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.4813 | -0.2404 | -0.2404 | 0.2409 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.2404, value/write=-0.2404 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.4217 | -0.2109 | -0.2109 | 0.2109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=-0.2109, value/write=-0.2109 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.3509 | -0.1729 | -0.1729 | 0.1780 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.1729, value/write=-0.1729 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.2479 | -0.1232 | -0.1232 | 0.1247 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.1232, value/write=-0.1232 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.2451 | -0.1222 | -0.1222 | 0.1229 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=-0.1222, value/write=-0.1222 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.2346 | -0.0590 | -0.0590 | 0.1756 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0590, value/write=-0.0590 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.1805 | -0.0895 | -0.0895 | 0.0910 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=-0.0895, value/write=-0.0895 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0958 | 0.0453 | 0.0453 | 0.0505 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0453, value/write=0.0453 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0733 | -0.0252 | -0.0252 | 0.0480 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=-0.0252, value/write=-0.0252 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0642 | -0.0321 | -0.0321 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=-0.0321, value/write=-0.0321 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0610 | 0.0255 | 0.0255 | 0.0355 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0255, value/write=0.0255 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0600 | -0.0300 | -0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0300, value/write=-0.0300 so it resists Tbl / protective. Routes:  |
| 21 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0558 | -0.0279 | -0.0279 | 0.0279 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-CLS; natural A×grad=-0.0279, value/write=-0.0279 so it resists Tbl / protective. Routes:  |
| 22 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | electron<-CLS | 0.0532 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses electron<-CLS; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0485 | -0.0243 | -0.0243 | 0.0243 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-muon; natural A×grad=-0.0243, value/write=-0.0243 so it resists Tbl / protective. Routes:  |
| 24 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0473 | -0.0237 | -0.0237 | 0.0237 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0237, value/write=-0.0237 so it resists Tbl / protective. Routes:  |
| 25 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.1.attn.h3 | photon<-neutral_hadron | 0.0463 | -0.0232 | -0.0232 | 0.0232 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h3 uses photon<-neutral_hadron; natural A×grad=-0.0232, value/write=-0.0232 so it resists Tbl / protective. Routes:  |
| 26 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | muon<-CLS | 0.0414 | -0.0207 | -0.0207 | 0.0207 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses muon<-CLS; natural A×grad=-0.0207, value/write=-0.0207 so it resists Tbl / protective. Routes:  |
| 27 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0407 | -0.0204 | -0.0204 | 0.0204 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses muon<-muon; natural A×grad=-0.0204, value/write=-0.0204 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | muon<-CLS | 0.0386 | -0.0193 | -0.0193 | 0.0193 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses muon<-CLS; natural A×grad=-0.0193, value/write=-0.0193 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0380 | -0.0183 | -0.0183 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0183, value/write=-0.0183 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0378 | -0.0189 | -0.0189 | 0.0189 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=-0.0189, value/write=-0.0189 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0958 | 0.0453 | 0.0453 | 0.0505 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0453, value/write=0.0453 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0610 | 0.0255 | 0.0255 | 0.0355 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0255, value/write=0.0255 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 1.1137 | -0.5568 | -0.5568 | 0.5568 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=-0.5568, value/write=-0.5568 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.0930 | -0.5465 | -0.5465 | 0.5465 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.5465, value/write=-0.5465 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-CLS | 1.0723 | -0.5361 | -0.5361 | 0.5361 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-CLS; natural A×grad=-0.5361, value/write=-0.5361 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.9210 | -0.4600 | -0.4600 | 0.4610 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=-0.4600, value/write=-0.4600 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.5936 | -0.2968 | -0.2968 | 0.2968 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=-0.2968, value/write=-0.2968 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.5400 | -0.2700 | -0.2700 | 0.2700 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2700, value/write=-0.2700 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.5288 | -0.2638 | -0.2638 | 0.2650 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.2638, value/write=-0.2638 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.4864 | -0.2432 | -0.2432 | 0.2432 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-CLS; natural A×grad=-0.2432, value/write=-0.2432 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.4813 | -0.2404 | -0.2404 | 0.2409 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.2404, value/write=-0.2404 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.4217 | -0.2109 | -0.2109 | 0.2109 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=-0.2109, value/write=-0.2109 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.3509 | -0.1729 | -0.1729 | 0.1780 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.1729, value/write=-0.1729 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.2479 | -0.1232 | -0.1232 | 0.1247 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.1232, value/write=-0.1232 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.2451 | -0.1222 | -0.1222 | 0.1229 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=-0.1222, value/write=-0.1222 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.2346 | -0.0590 | -0.0590 | 0.1756 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0590, value/write=-0.0590 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.1805 | -0.0895 | -0.0895 | 0.0910 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=-0.0895, value/write=-0.0895 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0733 | -0.0252 | -0.0252 | 0.0480 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=-0.0252, value/write=-0.0252 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0642 | -0.0321 | -0.0321 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=-0.0321, value/write=-0.0321 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0600 | -0.0300 | -0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0300, value/write=-0.0300 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0558 | -0.0279 | -0.0279 | 0.0279 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-CLS; natural A×grad=-0.0279, value/write=-0.0279 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | electron<-CLS | 0.0532 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses electron<-CLS; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
