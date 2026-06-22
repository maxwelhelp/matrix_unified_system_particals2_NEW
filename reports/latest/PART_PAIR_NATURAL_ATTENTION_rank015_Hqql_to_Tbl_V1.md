# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9936**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1311 | -0.5465 | -0.7496 | -0.5465 | 0.9213 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1410 | -0.5568 | -0.6966 | -0.5568 | 0.9052 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.1212 | -0.5361 | -0.7077 | -0.5361 | 0.8900 |
| 4 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1231 | -0.2968 | -0.4043 | -0.2968 | 0.4989 |
| 5 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1133 | -0.3149 | -0.3228 | 0.4228 | 0.4763 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1184 | -0.2700 | -0.3929 | -0.2700 | 0.4664 |
| 7 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.1137 | -0.2432 | -0.3762 | -0.2432 | 0.4313 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.8323 | 0.0000 | 0.4162 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0831 | -0.1809 | -0.1819 | 0.3385 | 0.2719 |
| 10 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0981 | -0.1422 | -0.1661 | 0.1400 | 0.2253 |
| 11 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0775 | -0.0931 | -0.1054 | 0.5917 | 0.1458 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0698 | -0.0829 | -0.1011 | 0.1147 | 0.1335 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.2620 | 0.0000 | 0.1310 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.2375 | 0.0000 | 0.1187 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0646 | -0.0644 | -0.0724 | 0.3027 | 0.1006 |
| 16 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.2500 | 0.0229 | 0.1361 | 0.0229 | 0.0909 |
| 17 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0388 | -0.0590 | -0.0603 | -0.0436 | 0.0891 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.1754 | 0.0000 | 0.0877 |
| 19 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0733 | -0.0430 | -0.0631 | 0.2458 | 0.0745 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0419 | 0.0453 | 0.0509 | 0.0412 | 0.0708 |
| 21 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | -0.1344 | 0.0000 | 0.0672 |
| 22 | mod.cls_blocks.1.attn.h3 | CLS<-electron | 0.1818 | 0.0167 | 0.1004 | 0.0167 | 0.0668 |
| 23 | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0741 | -0.0321 | -0.0591 | -0.0321 | 0.0616 |
| 24 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0692 | -0.0300 | -0.0600 | -0.0300 | 0.0600 |
| 25 | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0643 | -0.0279 | -0.0605 | -0.0279 | 0.0582 |
| 26 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | 0.0000 | 0.0000 | 0.1156 | -0.0150 | 0.0578 |
| 27 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0000 | 0.0000 | 0.1058 | 0.0000 | 0.0529 |
| 28 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0636 | -0.0281 | -0.0459 | 0.1122 | 0.0511 |
| 29 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.1011 | 0.0000 | 0.0505 |
| 30 | mod.cls_blocks.0.attn.h1 | electron<-CLS | 0.0437 | -0.0266 | -0.0478 | -0.0266 | 0.0505 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.1070 | -0.4600 | -0.4600 | -0.4600 | 0.6900 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0795 | -0.2638 | -0.2638 | -0.2638 | 0.3957 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0795 | -0.2404 | -0.2404 | -0.2404 | 0.3605 |
| 4 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0968 | -0.2109 | -0.2109 | -0.2109 | 0.3163 |
| 5 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0659 | -0.1729 | -0.1729 | -0.1729 | 0.2593 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0688 | -0.1232 | -0.1232 | -0.1232 | 0.1849 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0691 | -0.1222 | -0.1222 | -0.1222 | 0.1833 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0565 | -0.0895 | -0.0895 | -0.0895 | 0.1342 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0388 | -0.0590 | -0.0590 | -0.0590 | 0.0885 |
| 10 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0419 | 0.0453 | 0.0453 | 0.0453 | 0.0679 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0436 | 0.0255 | 0.0255 | 0.0255 | 0.0382 |
| 12 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0366 | -0.0252 | -0.0252 | -0.0252 | 0.0379 |
| 13 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0556 | -0.0243 | -0.0243 | -0.0243 | 0.0364 |
| 14 | mod.cls_blocks.1.attn.h3 | photon<-neutral_hadron | 0.1429 | -0.0232 | -0.0232 | -0.0232 | 0.0348 |
| 15 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0378 | -0.0204 | -0.0204 | -0.0204 | 0.0305 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0398 | -0.0183 | -0.0183 | -0.0183 | 0.0274 |
| 17 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0791 | -0.0177 | -0.0177 | -0.0177 | 0.0266 |
| 18 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0422 | 0.0165 | 0.0165 | 0.0165 | 0.0247 |
| 19 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0479 | -0.0161 | -0.0161 | -0.0161 | 0.0242 |
| 20 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0471 | -0.0155 | -0.0155 | -0.0155 | 0.0232 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0386 | -0.0142 | -0.0142 | -0.0142 | 0.0213 |
| 22 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0323 | -0.0137 | -0.0137 | -0.0137 | 0.0206 |
| 23 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0575 | -0.0122 | -0.0122 | -0.0122 | 0.0183 |
| 24 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0447 | -0.0119 | -0.0119 | -0.0119 | 0.0179 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0387 | -0.0108 | -0.0108 | -0.0108 | 0.0162 |
| 26 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0581 | 0.0105 | 0.0105 | 0.0105 | 0.0157 |
| 27 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0332 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 28 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0355 | 0.0097 | 0.0097 | 0.0097 | 0.0145 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0295 | -0.0093 | -0.0093 | -0.0093 | 0.0140 |
| 30 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0279 | 0.0086 | 0.0086 | 0.0086 | 0.0128 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
