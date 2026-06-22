# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10032**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1099 | 0.5395 | 1.0377 | 0.5395 | 1.0583 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1160 | 0.4769 | 0.8721 | 0.4769 | 0.9130 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1342 | 0.2892 | 1.0797 | 0.2892 | 0.8290 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0939 | 0.2061 | 0.3434 | 0.2061 | 0.3778 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1006 | 0.1701 | 0.2916 | 0.1701 | 0.3160 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0473 | 0.1866 | 0.1853 | 0.0949 | 0.2793 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.4475 | 0.0000 | 0.2238 |
| 8 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1207 | 0.0623 | 0.2450 | 0.0623 | 0.1848 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.3266 | 0.0000 | 0.1633 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0420 | 0.1083 | 0.1088 | 0.0693 | 0.1627 |
| 11 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0600 | 0.0694 | 0.0866 | 0.0694 | 0.1127 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0404 | 0.0621 | 0.0617 | 0.0268 | 0.0930 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.1803 | 0.0000 | 0.0901 |
| 14 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0565 | 0.0535 | 0.0703 | 0.0535 | 0.0887 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.1607 | 0.0000 | 0.0804 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0643 | -0.0353 | -0.0605 | -0.0353 | 0.0656 |
| 17 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.2349 | 0.0357 | 0.0588 | 0.0357 | 0.0651 |
| 18 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1109 | 0.0370 | 0.0476 | 0.0363 | 0.0608 |
| 19 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0299 | 0.0352 | 0.0496 | 0.0352 | 0.0600 |
| 20 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0364 | 0.0370 | 0.0375 | 0.0228 | 0.0558 |
| 21 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0453 | 0.0411 | 0.0245 | 0.0343 | 0.0533 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0305 | 0.0300 | 0.0424 | 0.0300 | 0.0512 |
| 23 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0350 | 0.0303 | 0.0191 | 0.0501 |
| 24 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0988 | 0.0000 | 0.0494 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0293 | -0.0268 | -0.0429 | -0.0153 | 0.0482 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0373 | -0.0152 | -0.0467 | -0.4142 | 0.0386 |
| 27 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0975 | 0.0218 | 0.0326 | 0.0030 | 0.0381 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0345 | -0.0257 | -0.0245 | -0.0257 | 0.0380 |
| 29 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0000 | 0.0000 | -0.0715 | 0.0000 | 0.0357 |
| 30 | mod.cls_blocks.0.attn.h1 | electron<-CLS | 0.0321 | 0.0143 | 0.0412 | 0.0143 | 0.0349 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.1342 | 0.2892 | 0.2892 | 0.2892 | 0.4338 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0518 | 0.2288 | 0.2288 | 0.2288 | 0.3432 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0450 | 0.1340 | 0.1340 | 0.1340 | 0.2010 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0464 | 0.0782 | 0.0782 | 0.0782 | 0.1173 |
| 5 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1207 | 0.0623 | 0.0623 | 0.0623 | 0.0935 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0402 | 0.0469 | 0.0469 | 0.0469 | 0.0703 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0453 | 0.0411 | 0.0411 | 0.0411 | 0.0616 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0643 | -0.0353 | -0.0353 | -0.0353 | 0.0530 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0350 | 0.0350 | 0.0350 | 0.0524 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0373 | 0.0290 | 0.0290 | 0.0290 | 0.0435 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0345 | -0.0257 | -0.0257 | -0.0257 | 0.0386 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0288 | -0.0254 | -0.0254 | -0.0254 | 0.0381 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0400 | 0.0204 | 0.0204 | 0.0204 | 0.0306 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0450 | -0.0195 | -0.0195 | -0.0195 | 0.0293 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0314 | -0.0193 | -0.0193 | -0.0193 | 0.0289 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0225 | -0.0186 | -0.0186 | -0.0186 | 0.0279 |
| 17 | mod.cls_blocks.0.attn.h5 | charged_hadron<-electron | 0.0756 | -0.0153 | -0.0153 | -0.0153 | 0.0230 |
| 18 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0316 | -0.0153 | -0.0153 | -0.0153 | 0.0229 |
| 19 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0468 | -0.0147 | -0.0147 | -0.0147 | 0.0220 |
| 20 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0321 | 0.0143 | 0.0143 | 0.0143 | 0.0214 |
| 21 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0324 | 0.0141 | 0.0141 | 0.0141 | 0.0212 |
| 22 | mod.cls_blocks.0.attn.h4 | electron<-neutral_hadron | 0.0349 | -0.0132 | -0.0132 | -0.0132 | 0.0197 |
| 23 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0449 | 0.0131 | 0.0131 | 0.0131 | 0.0197 |
| 24 | mod.cls_blocks.0.attn.h4 | electron<-charged_hadron | 0.0429 | -0.0129 | -0.0129 | -0.0129 | 0.0194 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-neutral_hadron | 0.0361 | 0.0120 | 0.0120 | 0.0120 | 0.0180 |
| 26 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0346 | 0.0114 | 0.0114 | 0.0114 | 0.0171 |
| 27 | mod.blocks.3.attn.h5 | electron<-muon | 0.2032 | -0.0102 | -0.0102 | -0.0102 | 0.0153 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0311 | -0.0096 | -0.0096 | -0.0096 | 0.0145 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0339 | -0.0093 | -0.0093 | -0.0093 | 0.0140 |
| 30 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0250 | -0.0092 | -0.0092 | -0.0092 | 0.0138 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
