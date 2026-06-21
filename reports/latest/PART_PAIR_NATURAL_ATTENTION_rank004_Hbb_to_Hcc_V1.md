# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9744**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0776 | 0.1649 | 0.2894 | 0.1649 | 0.3096 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0834 | -0.1000 | 0.1923 | -0.1000 | 0.1961 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.0000 | 0.0000 | 0.3795 | 0.0000 | 0.1898 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0675 | 0.0804 | 0.1775 | 0.0804 | 0.1692 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0910 | -0.0337 | 0.2296 | -0.0337 | 0.1486 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0845 | 0.0365 | 0.1934 | 0.0365 | 0.1332 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0768 | 0.0389 | 0.1867 | 0.0389 | 0.1322 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0857 | -6.446e-04 | 0.2395 | -6.446e-04 | 0.1204 |
| 9 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0599 | 0.0618 | 0.1002 | 0.0618 | 0.1119 |
| 10 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1325 | 0.0494 | 0.1187 | 0.0494 | 0.1088 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0556 | 0.0509 | 0.0912 | 0.0509 | 0.0964 |
| 12 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.0000 | 0.0000 | 0.1910 | 0.0000 | 0.0955 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0592 | 0.0506 | 0.0895 | 0.0506 | 0.0954 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0707 | 0.0020 | 0.1698 | 0.0020 | 0.0869 |
| 15 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.1671 | 0.0000 | 0.0836 |
| 16 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0441 | 0.0404 | 0.0828 | 0.0404 | 0.0818 |
| 17 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.1432 | 0.0000 | 0.0716 |
| 18 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0000 | 0.0000 | -0.1235 | 0.0000 | 0.0617 |
| 19 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0700 | 0.0243 | 0.0297 | 0.0154 | 0.0391 |
| 20 | mod.cls_blocks.1.attn.h3 | photon<-muon | 1.647e-04 | -7.155e-07 | -0.0766 | -7.155e-07 | 0.0383 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0469 | 0.0166 | 0.0432 | 0.0106 | 0.0382 |
| 22 | mod.cls_blocks.1.attn.h3 | electron<-electron | 0.0000 | 0.0000 | -0.0755 | 0.0000 | 0.0377 |
| 23 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0429 | 0.0157 | 0.0260 | 0.0157 | 0.0287 |
| 24 | mod.cls_blocks.1.attn.h3 | neutral_hadron<-muon | 0.9196 | 0.0177 | 0.0184 | 0.0177 | 0.0269 |
| 25 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0000 | 0.0000 | -0.0536 | -0.0579 | 0.0268 |
| 26 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0202 | 0.0168 | 0.0195 | 0.0168 | 0.0265 |
| 27 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-muon | 0.1100 | 0.0108 | -0.0301 | 0.0108 | 0.0258 |
| 28 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0168 | -0.0034 | -0.0417 | -0.0115 | 0.0243 |
| 29 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0308 | 0.0125 | 0.0234 | 0.0125 | 0.0242 |
| 30 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0741 | -0.0095 | -0.0292 | -0.0095 | 0.0240 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0764 | -0.0407 | -0.0407 | -0.0407 | 0.0611 |
| 2 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0510 | -0.0233 | -0.0233 | -0.0233 | 0.0350 |
| 3 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0241 | -0.0136 | -0.0136 | -0.0136 | 0.0205 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0350 | 0.0124 | 0.0124 | 0.0124 | 0.0185 |
| 5 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0337 | -0.0111 | -0.0111 | -0.0111 | 0.0167 |
| 6 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0290 | 0.0102 | 0.0102 | 0.0102 | 0.0153 |
| 7 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0268 | 0.0094 | 0.0094 | 0.0094 | 0.0140 |
| 8 | mod.blocks.1.attn.h5 | muon<-electron | 0.3002 | -0.0088 | -0.0088 | -0.0088 | 0.0132 |
| 9 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-muon | 0.0718 | -0.0085 | -0.0085 | -0.0085 | 0.0128 |
| 10 | mod.cls_blocks.0.attn.h5 | neutral_hadron<-electron | 0.0427 | -0.0084 | -0.0084 | -0.0084 | 0.0127 |
| 11 | mod.blocks.1.attn.h4 | electron<-muon | 0.2144 | -0.0080 | -0.0080 | -0.0080 | 0.0121 |
| 12 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0279 | -0.0080 | -0.0080 | -0.0080 | 0.0120 |
| 13 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0347 | 0.0072 | 0.0072 | 0.0072 | 0.0108 |
| 14 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0374 | 0.0065 | 0.0065 | 0.0065 | 0.0098 |
| 15 | mod.blocks.3.attn.h4 | electron<-muon | 0.8758 | 0.0063 | 0.0063 | 0.0063 | 0.0095 |
| 16 | mod.blocks.3.attn.h4 | muon<-electron | 0.2794 | 0.0063 | 0.0063 | 0.0063 | 0.0094 |
| 17 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0324 | 0.0062 | 0.0062 | 0.0062 | 0.0093 |
| 18 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0172 | 0.0061 | 0.0061 | 0.0061 | 0.0092 |
| 19 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0244 | 0.0051 | 0.0051 | 0.0051 | 0.0077 |
| 20 | mod.cls_blocks.0.attn.h1 | photon<-charged_hadron | 0.0241 | 0.0051 | 0.0051 | 0.0051 | 0.0077 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0251 | 0.0049 | 0.0049 | 0.0049 | 0.0074 |
| 22 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0150 | -0.0049 | -0.0049 | -0.0049 | 0.0074 |
| 23 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0282 | -0.0049 | -0.0049 | -0.0049 | 0.0074 |
| 24 | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0273 | -0.0049 | -0.0049 | -0.0049 | 0.0073 |
| 25 | mod.cls_blocks.0.attn.h1 | photon<-photon | 0.0205 | 0.0049 | 0.0049 | 0.0049 | 0.0073 |
| 26 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0258 | 0.0048 | 0.0048 | 0.0048 | 0.0072 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0517 | -0.0047 | -0.0047 | -0.0047 | 0.0071 |
| 28 | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0294 | -0.0047 | -0.0047 | -0.0047 | 0.0070 |
| 29 | mod.cls_blocks.0.attn.h3 | charged_hadron<-muon | 0.0804 | 0.0044 | 0.0044 | 0.0044 | 0.0066 |
| 30 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-photon | 0.0258 | -0.0043 | -0.0043 | -0.0043 | 0.0064 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
