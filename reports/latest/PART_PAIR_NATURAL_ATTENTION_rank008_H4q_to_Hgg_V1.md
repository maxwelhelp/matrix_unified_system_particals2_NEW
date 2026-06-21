# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7792**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0701 | -0.1752 | -0.2008 | -0.1752 | 0.2756 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0649 | -0.1365 | -0.1906 | -0.1365 | 0.2318 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0635 | -0.0637 | -0.0563 | -0.0637 | 0.0919 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0493 | -0.0204 | -0.1398 | -0.0204 | 0.0903 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0576 | -0.0528 | -0.0617 | -0.0528 | 0.0837 |
| 6 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0399 | -0.0202 | -0.0660 | -0.0202 | 0.0532 |
| 7 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.1136 | 0.0352 | 0.0352 | 0.0352 | 0.0528 |
| 8 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0397 | -0.0131 | -0.0286 | -0.0131 | 0.0274 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.0529 | 0.0000 | 0.0264 |
| 10 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0371 | -0.0109 | -0.0269 | -0.0109 | 0.0244 |
| 11 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0670 | 0.0127 | 0.0126 | 0.0141 | 0.0190 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0228 | -0.0127 | -0.0107 | 0.0291 | 0.0180 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0832 | 0.0084 | 0.0175 | 0.0084 | 0.0171 |
| 14 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0218 | -0.0076 | -0.0161 | -0.0076 | 0.0157 |
| 15 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0294 | -0.0043 | -0.0223 | -0.0043 | 0.0155 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0492 | 0.0098 | 0.0105 | 0.0098 | 0.0150 |
| 17 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0338 | -0.0071 | -0.0120 | -0.0071 | 0.0131 |
| 18 | mod.blocks.0.attn.h3 | electron<-electron | 0.2307 | 0.0087 | 0.0085 | 0.0088 | 0.0130 |
| 19 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0832 | 0.0084 | 0.0084 | 0.0084 | 0.0125 |
| 20 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0308 | -0.0062 | -0.0121 | -0.0062 | 0.0122 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0214 | -0.0056 | -0.0128 | -0.0056 | 0.0120 |
| 22 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0694 | 0.0042 | 0.0144 | 0.0042 | 0.0114 |
| 23 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0486 | -0.0050 | 0.0127 | -0.0050 | 0.0113 |
| 24 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0641 | 0.0069 | 0.0075 | 0.0069 | 0.0106 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0676 | 0.0051 | 0.0105 | 0.0049 | 0.0103 |
| 26 | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.8221 | -0.0019 | 0.0151 | -0.0019 | 0.0095 |
| 27 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0234 | 0.0049 | 0.0084 | 0.0089 | 0.0091 |
| 28 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0218 | -0.0035 | -0.0109 | -0.0035 | 0.0090 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.0000 | 0.0000 | 0.0177 | 0.0000 | 0.0088 |
| 30 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0606 | 0.0017 | 0.0138 | 0.0017 | 0.0086 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | 0.1136 | 0.0352 | 0.0352 | 0.0352 | 0.0529 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0244 | -0.0134 | -0.0134 | -0.0134 | 0.0201 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0263 | 0.0124 | 0.0124 | 0.0124 | 0.0187 |
| 4 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0263 | 0.0124 | 0.0124 | 0.0124 | 0.0187 |
| 5 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0467 | 0.0113 | 0.0113 | 0.0113 | 0.0169 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0492 | 0.0098 | 0.0098 | 0.0098 | 0.0146 |
| 7 | mod.blocks.0.attn.h3 | electron<-electron | 0.2307 | 0.0087 | 0.0087 | 0.0087 | 0.0131 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0278 | 0.0085 | 0.0085 | 0.0085 | 0.0128 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0641 | 0.0069 | 0.0069 | 0.0069 | 0.0103 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0226 | -0.0060 | -0.0060 | -0.0060 | 0.0089 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0260 | 0.0052 | 0.0052 | 0.0052 | 0.0079 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0241 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 13 | mod.blocks.2.attn.h3 | muon<-muon | 0.0889 | 0.0047 | 0.0047 | 0.0047 | 0.0070 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0201 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 15 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-electron | 0.0567 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 16 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0266 | -0.0041 | -0.0041 | -0.0041 | 0.0062 |
| 17 | mod.cls_blocks.1.attn.h5 | photon<-neutral_hadron | 0.0404 | -0.0035 | -0.0035 | -0.0035 | 0.0052 |
| 18 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0128 | 0.0035 | 0.0035 | 0.0035 | 0.0052 |
| 19 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0219 | -0.0033 | -0.0033 | -0.0033 | 0.0049 |
| 20 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0185 | 0.0031 | 0.0031 | 0.0031 | 0.0046 |
| 21 | mod.cls_blocks.0.attn.h3 | photon<-neutral_hadron | 0.0225 | -0.0030 | -0.0030 | -0.0030 | 0.0045 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0204 | 0.0029 | 0.0029 | 0.0029 | 0.0044 |
| 23 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0204 | 0.0029 | 0.0029 | 0.0029 | 0.0044 |
| 24 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0141 | 0.0028 | 0.0028 | 0.0028 | 0.0042 |
| 25 | mod.blocks.0.attn.h4 | electron<-electron | 0.0698 | 0.0028 | 0.0028 | 0.0028 | 0.0042 |
| 26 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0215 | -0.0027 | -0.0027 | -0.0027 | 0.0040 |
| 27 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0131 | 0.0026 | 0.0026 | 0.0026 | 0.0039 |
| 28 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0161 | -0.0025 | -0.0025 | -0.0025 | 0.0038 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0233 | -0.0025 | -0.0025 | -0.0025 | 0.0037 |
| 30 | mod.cls_blocks.0.attn.h3 | CLS<-neutral_hadron | 0.0199 | -0.0024 | -0.0024 | -0.0024 | 0.0036 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
