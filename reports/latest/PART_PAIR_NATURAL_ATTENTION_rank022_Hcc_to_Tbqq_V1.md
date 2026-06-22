# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **9680**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0834 | -0.7200 | -0.7151 | -0.5129 | 1.0776 |
| 2 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0716 | -0.2745 | -0.2746 | -0.1690 | 0.4118 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0430 | -0.2666 | -0.2805 | -0.2615 | 0.4068 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0881 | -0.0949 | -0.3521 | -0.0949 | 0.2709 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0432 | -0.1004 | -0.1802 | -0.0945 | 0.1905 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.3737 | 0.0000 | 0.1869 |
| 7 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | -0.3705 | 0.0000 | 0.1852 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0881 | -0.0949 | -0.1784 | -0.0949 | 0.1841 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0869 | -0.0684 | -0.1869 | -0.0684 | 0.1618 |
| 10 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0821 | -0.0966 | -0.0966 | -0.0966 | 0.1448 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0869 | -0.0684 | -0.1499 | -0.0684 | 0.1433 |
| 12 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0689 | -0.0914 | -0.0914 | -0.0914 | 0.1370 |
| 13 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | -0.1700 | 0.0000 | 0.0850 |
| 14 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0134 | 0.0029 | -0.1564 | -0.0125 | 0.0811 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | -0.1426 | 0.0000 | 0.0713 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0323 | -0.0464 | -0.0470 | -0.0425 | 0.0699 |
| 17 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0513 | -0.0417 | -0.0407 | -0.0353 | 0.0620 |
| 18 | mod.cls_blocks.1.attn.h2 | neutral_hadron<-CLS | 0.0000 | 0.0000 | -0.1171 | 0.0000 | 0.0585 |
| 19 | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0218 | -0.0087 | -0.0916 | -0.0186 | 0.0545 |
| 20 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0508 | -0.0184 | -0.0580 | -0.0184 | 0.0474 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0264 | 0.0312 | 0.0312 | 0.0312 | 0.0468 |
| 22 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0508 | -0.0184 | -0.0526 | -0.0184 | 0.0448 |
| 23 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0309 | -0.0188 | -0.0498 | -0.0262 | 0.0437 |
| 24 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0121 | 0.0288 | 0.0288 | 0.0229 | 0.0432 |
| 25 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0256 | 0.0230 | 0.0364 | 0.0200 | 0.0412 |
| 26 | mod.cls_blocks.0.attn.h7 | photon<-muon | 0.0542 | 0.0256 | 0.0256 | 0.0253 | 0.0384 |
| 27 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0528 | -0.0245 | -0.0245 | -0.0251 | 0.0368 |
| 28 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0345 | 0.0235 | 0.0228 | -0.0069 | 0.0349 |
| 29 | mod.blocks.6.attn.h1 | muon<-electron | 0.4971 | 0.0210 | 0.0210 | 0.0208 | 0.0314 |
| 30 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0287 | 0.0205 | 0.0205 | 0.0205 | 0.0308 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.0834 | -0.7200 | -0.7200 | -0.7200 | 1.0801 |
| 2 | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.0716 | -0.2745 | -0.2745 | -0.2745 | 0.4117 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.2645 | -0.2645 | -0.2645 | 0.3967 |
| 4 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0359 | -0.1010 | -0.1010 | -0.1010 | 0.1515 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.0821 | -0.0966 | -0.0966 | -0.0966 | 0.1448 |
| 6 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0689 | -0.0914 | -0.0914 | -0.0914 | 0.1370 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0323 | -0.0464 | -0.0464 | -0.0464 | 0.0696 |
| 8 | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0513 | -0.0417 | -0.0417 | -0.0417 | 0.0626 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0264 | 0.0312 | 0.0312 | 0.0312 | 0.0468 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0121 | 0.0288 | 0.0288 | 0.0288 | 0.0432 |
| 11 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0345 | 0.0235 | 0.0235 | 0.0235 | 0.0352 |
| 12 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0256 | 0.0230 | 0.0230 | 0.0230 | 0.0345 |
| 13 | mod.blocks.6.attn.h1 | muon<-electron | 0.4971 | 0.0210 | 0.0210 | 0.0210 | 0.0314 |
| 14 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0287 | 0.0205 | 0.0205 | 0.0205 | 0.0308 |
| 15 | mod.blocks.3.attn.h0 | muon<-electron | 0.5002 | -0.0203 | -0.0203 | -0.0203 | 0.0304 |
| 16 | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0310 | 0.0199 | 0.0199 | 0.0199 | 0.0298 |
| 17 | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0309 | -0.0188 | -0.0188 | -0.0188 | 0.0282 |
| 18 | mod.cls_blocks.0.attn.h1 | muon<-neutral_hadron | 0.0519 | -0.0186 | -0.0186 | -0.0186 | 0.0279 |
| 19 | mod.cls_blocks.0.attn.h6 | muon<-neutral_hadron | 0.0392 | 0.0184 | 0.0184 | 0.0184 | 0.0276 |
| 20 | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0589 | -0.0179 | -0.0179 | -0.0179 | 0.0268 |
| 21 | mod.cls_blocks.0.attn.h7 | electron<-charged_hadron | 0.0261 | 0.0177 | 0.0177 | 0.0177 | 0.0266 |
| 22 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0300 | -0.0176 | -0.0176 | -0.0176 | 0.0264 |
| 23 | mod.blocks.4.attn.h7 | electron<-muon | 0.2239 | -0.0169 | -0.0169 | -0.0169 | 0.0254 |
| 24 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0294 | -0.0159 | -0.0159 | -0.0159 | 0.0238 |
| 25 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0243 | -0.0151 | -0.0151 | -0.0151 | 0.0227 |
| 26 | mod.cls_blocks.0.attn.h4 | muon<-photon | 0.0187 | 0.0148 | 0.0148 | 0.0148 | 0.0222 |
| 27 | mod.cls_blocks.0.attn.h7 | muon<-muon | 0.0301 | -0.0145 | -0.0145 | -0.0145 | 0.0218 |
| 28 | mod.blocks.7.attn.h3 | muon<-electron | 0.9526 | 0.0131 | 0.0131 | 0.0131 | 0.0197 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0398 | -0.0123 | -0.0123 | -0.0123 | 0.0185 |
| 30 | mod.cls_blocks.0.attn.h1 | electron<-neutral_hadron | 0.0396 | -0.0122 | -0.0122 | -0.0122 | 0.0184 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
