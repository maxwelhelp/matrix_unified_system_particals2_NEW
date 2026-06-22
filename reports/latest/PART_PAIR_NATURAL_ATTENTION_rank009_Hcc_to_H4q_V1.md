# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9024**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0753 | 0.2539 | 0.4906 | 0.2539 | 0.4992 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0834 | 0.0909 | 0.2914 | 0.0909 | 0.2366 |
| 3 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0861 | -0.1378 | -0.1079 | -0.1378 | 0.1918 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0659 | -0.0992 | -0.1461 | -0.0992 | 0.1722 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0958 | -0.1002 | 0.1328 | -0.1002 | 0.1666 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0874 | -0.0439 | 0.1345 | -0.0439 | 0.1112 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0118 | -0.0012 | -0.2032 | -0.0012 | 0.1028 |
| 8 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.2001 | 0.0000 | 0.1000 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0694 | -0.0506 | -0.0729 | -0.0506 | 0.0871 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0118 | -0.0012 | -0.1321 | -0.0023 | 0.0672 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0374 | 0.0037 | -0.0752 | 0.0010 | 0.0413 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0374 | 0.0037 | -0.0752 | 0.0018 | 0.0413 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0627 | 0.0172 | -0.0440 | 0.0172 | 0.0392 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0551 | -0.0182 | -0.0402 | -0.0186 | 0.0383 |
| 15 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0551 | -0.0182 | -0.0402 | -0.0197 | 0.0383 |
| 16 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0463 | -0.0116 | -0.0379 | -0.0116 | 0.0305 |
| 17 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0000 | 0.0000 | -0.0602 | 0.0000 | 0.0301 |
| 18 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0000 | 0.0000 | -0.0599 | 0.0000 | 0.0300 |
| 19 | mod.cls_blocks.1.attn.h3 | charged_hadron<-muon | 0.0061 | 2.361e-05 | 0.0562 | 2.361e-05 | 0.0281 |
| 20 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0217 | 0.0139 | 0.0267 | 0.0139 | 0.0272 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0247 | -0.0098 | -0.0345 | -0.0108 | 0.0270 |
| 22 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0248 | 0.0132 | 0.0203 | 0.0132 | 0.0234 |
| 23 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0283 | 0.0128 | 0.0205 | 0.0128 | 0.0231 |
| 24 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0276 | 0.0122 | 0.0182 | 0.0122 | 0.0213 |
| 25 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0448 | 0.0069 | -0.0279 | 0.0069 | 0.0209 |
| 26 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0568 | -0.0053 | -0.0284 | -0.0053 | 0.0195 |
| 27 | mod.cls_blocks.1.attn.h3 | muon<-muon | 0.0000 | 0.0000 | -0.0386 | 0.0000 | 0.0193 |
| 28 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0286 | -0.0135 | 0.0066 | -0.0207 | 0.0168 |
| 29 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0185 | -0.0066 | -0.0175 | -0.0039 | 0.0153 |
| 30 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0482 | -7.570e-04 | -0.0251 | -7.570e-04 | 0.0133 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0341 | 0.0207 | 0.0207 | 0.0207 | 0.0311 |
| 2 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0247 | -0.0098 | -0.0098 | -0.0098 | 0.0147 |
| 3 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0247 | -0.0098 | -0.0098 | -0.0098 | 0.0147 |
| 4 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0678 | 0.0097 | 0.0097 | 0.0097 | 0.0146 |
| 5 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0678 | 0.0097 | 0.0097 | 0.0097 | 0.0146 |
| 6 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0351 | 0.0075 | 0.0075 | 0.0075 | 0.0113 |
| 7 | mod.cls_blocks.0.attn.h2 | CLS<-muon | 0.0360 | -0.0071 | -0.0071 | -0.0071 | 0.0106 |
| 8 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | 0.0360 | -0.0071 | -0.0071 | -0.0071 | 0.0106 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0279 | 0.0052 | 0.0052 | 0.0052 | 0.0078 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0279 | 0.0052 | 0.0052 | 0.0052 | 0.0078 |
| 11 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0191 | 0.0052 | 0.0052 | 0.0052 | 0.0077 |
| 12 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0191 | 0.0052 | 0.0052 | 0.0052 | 0.0077 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0270 | 0.0045 | 0.0045 | 0.0045 | 0.0067 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0293 | -0.0041 | -0.0041 | -0.0041 | 0.0061 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0141 | -0.0028 | -0.0028 | -0.0028 | 0.0043 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0280 | 0.0027 | 0.0027 | 0.0027 | 0.0040 |
| 17 | mod.cls_blocks.0.attn.h5 | CLS<-muon | 0.0291 | -0.0026 | -0.0026 | -0.0026 | 0.0039 |
| 18 | mod.cls_blocks.0.attn.h5 | charged_hadron<-muon | 0.0291 | -0.0026 | -0.0026 | -0.0026 | 0.0039 |
| 19 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0166 | 0.0025 | 0.0025 | 0.0025 | 0.0038 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0177 | 0.0024 | 0.0024 | 0.0024 | 0.0035 |
| 21 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0287 | 0.0023 | 0.0023 | 0.0023 | 0.0035 |
| 22 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0245 | 0.0022 | 0.0022 | 0.0022 | 0.0033 |
| 23 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0245 | 0.0022 | 0.0022 | 0.0022 | 0.0033 |
| 24 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0097 | -0.0021 | -0.0021 | -0.0021 | 0.0032 |
| 25 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0097 | -0.0021 | -0.0021 | -0.0021 | 0.0032 |
| 26 | mod.cls_blocks.0.attn.h6 | charged_hadron<-neutral_hadron | 0.0238 | 0.0021 | 0.0021 | 0.0021 | 0.0032 |
| 27 | mod.cls_blocks.0.attn.h3 | CLS<-electron | 0.0141 | 0.0019 | 0.0019 | 0.0019 | 0.0029 |
| 28 | mod.cls_blocks.0.attn.h3 | charged_hadron<-electron | 0.0141 | 0.0019 | 0.0019 | 0.0019 | 0.0029 |
| 29 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-photon | 0.0160 | -0.0019 | -0.0019 | -0.0019 | 0.0029 |
| 30 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0167 | 0.0018 | 0.0018 | 0.0018 | 0.0028 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
