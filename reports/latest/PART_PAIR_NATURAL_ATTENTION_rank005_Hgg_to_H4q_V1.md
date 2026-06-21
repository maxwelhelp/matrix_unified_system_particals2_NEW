# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7248**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0705 | 0.1364 | 0.3367 | 0.1364 | 0.3047 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0714 | 0.1111 | 0.3122 | 0.1111 | 0.2673 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0723 | 0.0859 | 0.2759 | 0.0859 | 0.2238 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0601 | 0.0692 | 0.1518 | 0.0692 | 0.1452 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0601 | 0.0496 | 0.1326 | 0.0496 | 0.1159 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.2219 | 0.0000 | 0.1109 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0601 | 0.0300 | 0.1136 | 0.0300 | 0.0868 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | 0.0844 | 0.0000 | 0.0422 |
| 9 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0437 | 0.0128 | 0.0211 | 0.0128 | 0.0233 |
| 10 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0397 | 0.0125 | 0.0207 | 0.0125 | 0.0229 |
| 11 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0357 | 0.0123 | 0.0200 | 0.0123 | 0.0223 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0248 | 0.0099 | 0.0126 | -0.0086 | 0.0162 |
| 13 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0412 | 0.0068 | 0.0136 | 0.0068 | 0.0137 |
| 14 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0372 | 0.0069 | 0.0133 | 0.0069 | 0.0135 |
| 15 | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0331 | 0.0069 | 0.0129 | 0.0069 | 0.0133 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0249 | 0.0052 | 0.0073 | 0.0052 | 0.0088 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0239 | 0.0045 | 0.0071 | 0.0045 | 0.0081 |
| 18 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0184 | -0.0020 | -0.0100 | -5.918e-04 | 0.0070 |
| 19 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0230 | 0.0039 | 0.0060 | 0.0039 | 0.0069 |
| 20 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0189 | -0.0024 | -0.0068 | -0.0017 | 0.0058 |
| 21 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0150 | -0.0029 | -0.0052 | -0.0023 | 0.0054 |
| 22 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0000 | 0.0000 | 0.0107 | 0.0000 | 0.0053 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0154 | -0.0028 | -0.0050 | -0.0013 | 0.0053 |
| 24 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0510 | -0.0034 | -0.0035 | -0.0130 | 0.0052 |
| 25 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0510 | -0.0034 | -0.0034 | -0.0229 | 0.0052 |
| 26 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0155 | -0.0018 | -0.0067 | 0.0012 | 0.0051 |
| 27 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0209 | 0.0033 | 0.0034 | -0.0020 | 0.0049 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0161 | -0.0026 | -0.0044 | 5.793e-04 | 0.0048 |
| 29 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0165 | -0.0018 | -0.0056 | 0.0037 | 0.0047 |
| 30 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0143 | -0.0017 | -0.0057 | -0.0013 | 0.0045 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0268 | 0.0161 | 0.0161 | 0.0161 | 0.0241 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0253 | 0.0053 | 0.0053 | 0.0053 | 0.0079 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0223 | 0.0043 | 0.0043 | 0.0043 | 0.0065 |
| 4 | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0270 | 0.0036 | 0.0036 | 0.0036 | 0.0053 |
| 5 | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0253 | 0.0035 | 0.0035 | 0.0035 | 0.0053 |
| 6 | mod.cls_blocks.1.attn.h5 | CLS<-electron | 0.0510 | -0.0034 | -0.0034 | -0.0034 | 0.0052 |
| 7 | mod.cls_blocks.1.attn.h5 | charged_hadron<-electron | 0.0510 | -0.0034 | -0.0034 | -0.0034 | 0.0052 |
| 8 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0212 | 0.0034 | 0.0034 | 0.0034 | 0.0051 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0153 | -0.0033 | -0.0033 | -0.0033 | 0.0050 |
| 10 | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0158 | -0.0032 | -0.0032 | -0.0032 | 0.0047 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0163 | -0.0030 | -0.0030 | -0.0030 | 0.0045 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0163 | -0.0030 | -0.0030 | -0.0030 | 0.0045 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0169 | -0.0029 | -0.0029 | -0.0029 | 0.0043 |
| 14 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0163 | -0.0024 | -0.0024 | -0.0024 | 0.0036 |
| 15 | mod.cls_blocks.0.attn.h3 | neutral_hadron<-neutral_hadron | 0.0187 | 0.0022 | 0.0022 | 0.0022 | 0.0034 |
| 16 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0217 | 0.0021 | 0.0021 | 0.0021 | 0.0032 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0146 | -0.0021 | -0.0021 | -0.0021 | 0.0032 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0177 | -0.0020 | -0.0020 | -0.0020 | 0.0031 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0138 | -0.0020 | -0.0020 | -0.0020 | 0.0030 |
| 20 | mod.cls_blocks.0.attn.h1 | charged_hadron<-charged_hadron | 0.0190 | 0.0020 | 0.0020 | 0.0020 | 0.0030 |
| 21 | mod.cls_blocks.0.attn.h1 | CLS<-charged_hadron | 0.0190 | 0.0019 | 0.0019 | 0.0019 | 0.0029 |
| 22 | mod.cls_blocks.0.attn.h3 | CLS<-neutral_hadron | 0.0203 | 0.0019 | 0.0019 | 0.0019 | 0.0029 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0165 | -0.0018 | -0.0018 | -0.0018 | 0.0028 |
| 24 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | 0.0165 | -0.0018 | -0.0018 | -0.0018 | 0.0028 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0187 | 0.0018 | 0.0018 | 0.0018 | 0.0027 |
| 26 | mod.cls_blocks.0.attn.h3 | charged_hadron<-neutral_hadron | 0.0209 | 0.0018 | 0.0018 | 0.0018 | 0.0026 |
| 27 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0198 | 0.0016 | 0.0016 | 0.0016 | 0.0024 |
| 28 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0181 | -0.0015 | -0.0015 | -0.0015 | 0.0023 |
| 29 | mod.cls_blocks.1.attn.h5 | neutral_hadron<-neutral_hadron | 0.0167 | 0.0015 | 0.0015 | 0.0015 | 0.0023 |
| 30 | mod.blocks.2.attn.h4 | electron<-electron | 0.1854 | 0.0015 | 0.0015 | 0.0015 | 0.0023 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
