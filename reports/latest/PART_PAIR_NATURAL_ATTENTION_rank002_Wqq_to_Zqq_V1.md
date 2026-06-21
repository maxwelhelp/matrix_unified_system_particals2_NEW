# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **8352**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0980 | -0.7573 | -1.1384 | -0.7573 | 1.3265 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1125 | -0.7030 | -1.0860 | -0.7030 | 1.2460 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1270 | -0.6487 | -0.7810 | -0.6487 | 1.0392 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0806 | -0.1906 | -0.2801 | -0.1906 | 0.3306 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | -0.5753 | 0.0000 | 0.2876 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0946 | -0.1589 | -0.2462 | -0.1589 | 0.2820 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1086 | -0.1273 | -0.1561 | -0.1273 | 0.2053 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0463 | -0.1423 | -0.1256 | -0.0077 | 0.2050 |
| 9 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0972 | 0.0613 | 0.0613 | 0.0613 | 0.0919 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0328 | -0.0653 | -0.0518 | -0.0107 | 0.0912 |
| 11 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0567 | -0.0438 | -0.0651 | -0.0438 | 0.0764 |
| 12 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0268 | -0.0370 | -0.0618 | -0.0370 | 0.0679 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0638 | -0.0360 | -0.0593 | -0.0360 | 0.0656 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0308 | -0.0348 | -0.0602 | -0.0348 | 0.0649 |
| 15 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0000 | 0.0000 | -0.1262 | 0.0000 | 0.0631 |
| 16 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0349 | -0.0326 | -0.0437 | -0.0326 | 0.0545 |
| 17 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0876 | 0.0348 | 0.0348 | 0.0658 | 0.0522 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0385 | -0.0342 | -0.0331 | 0.0022 | 0.0508 |
| 19 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0709 | -0.0281 | -0.0435 | -0.0281 | 0.0499 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0572 | -0.0266 | -0.0266 | -0.0266 | 0.0399 |
| 21 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0309 | 0.0235 | 0.0247 | 0.0142 | 0.0359 |
| 22 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0191 | 0.0167 | 0.0247 | 0.0051 | 0.0291 |
| 23 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0210 | -0.0225 | -0.0114 | 0.0551 | 0.0282 |
| 24 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0572 | 0.0185 | 0.0185 | 0.0185 | 0.0278 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0248 | 0.0185 | 0.0179 | 0.0042 | 0.0274 |
| 26 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0214 | 0.0144 | 0.0223 | 0.0310 | 0.0256 |
| 27 | mod.cls_blocks.0.attn.h1 | charged_hadron<-electron | 0.0186 | -0.0026 | -0.0455 | -0.0026 | 0.0253 |
| 28 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.0168 | -0.0168 | 0.5235 | 0.0252 |
| 29 | mod.cls_blocks.0.attn.h1 | CLS<-electron | 0.0159 | -0.0020 | -0.0424 | -0.0122 | 0.0232 |
| 30 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0485 | -0.0149 | -0.0149 | -0.0149 | 0.0223 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0490 | -0.1879 | -0.1879 | -0.1879 | 0.2819 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0342 | -0.0838 | -0.0838 | -0.0838 | 0.1257 |
| 3 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.0972 | 0.0613 | 0.0613 | 0.0613 | 0.0919 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0453 | -0.0430 | -0.0430 | -0.0430 | 0.0644 |
| 5 | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0876 | 0.0348 | 0.0348 | 0.0348 | 0.0522 |
| 6 | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0572 | -0.0266 | -0.0266 | -0.0266 | 0.0399 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0277 | -0.0241 | -0.0241 | -0.0241 | 0.0361 |
| 8 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0313 | 0.0228 | 0.0228 | 0.0228 | 0.0342 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0210 | -0.0225 | -0.0225 | -0.0225 | 0.0337 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0259 | 0.0201 | 0.0201 | 0.0201 | 0.0301 |
| 11 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0572 | 0.0185 | 0.0185 | 0.0185 | 0.0278 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0333 | -0.0184 | -0.0184 | -0.0184 | 0.0275 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0201 | 0.0169 | 0.0169 | 0.0169 | 0.0254 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0434 | -0.0168 | -0.0168 | -0.0168 | 0.0252 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0224 | 0.0151 | 0.0151 | 0.0151 | 0.0227 |
| 16 | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0485 | -0.0149 | -0.0149 | -0.0149 | 0.0223 |
| 17 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0353 | -0.0132 | -0.0132 | -0.0132 | 0.0198 |
| 18 | mod.cls_blocks.0.attn.h1 | photon<-muon | 0.0220 | -0.0116 | -0.0116 | -0.0116 | 0.0174 |
| 19 | mod.blocks.0.attn.h6 | muon<-electron | 0.1521 | 0.0109 | 0.0109 | 0.0109 | 0.0164 |
| 20 | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0419 | 0.0101 | 0.0101 | 0.0101 | 0.0151 |
| 21 | mod.cls_blocks.0.attn.h1 | photon<-photon | 0.0149 | 0.0100 | 0.0100 | 0.0100 | 0.0150 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-muon | 0.0371 | -0.0090 | -0.0090 | -0.0090 | 0.0135 |
| 23 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0780 | 0.0083 | 0.0083 | 0.0083 | 0.0124 |
| 24 | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.0296 | -0.0082 | -0.0082 | -0.0082 | 0.0123 |
| 25 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0305 | -0.0082 | -0.0082 | -0.0082 | 0.0122 |
| 26 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0359 | -0.0078 | -0.0078 | -0.0078 | 0.0118 |
| 27 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-charged_hadron | 0.0355 | 0.0077 | 0.0077 | 0.0077 | 0.0115 |
| 28 | mod.blocks.6.attn.h1 | electron<-muon | 0.2340 | -0.0076 | -0.0076 | -0.0076 | 0.0114 |
| 29 | mod.cls_blocks.0.attn.h6 | photon<-muon | 0.0221 | -0.0074 | -0.0074 | -0.0074 | 0.0111 |
| 30 | mod.blocks.6.attn.h1 | muon<-electron | 0.2276 | 0.0073 | 0.0073 | 0.0073 | 0.0110 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
