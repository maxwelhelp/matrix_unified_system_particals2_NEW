# PART_NATURAL_ATTENTION_MANUAL_GRAD_REAL_CONTRACT_V1

Natural attention A×grad trace using manual legacy MHA forward. This computes real QK softmax attention `A`, retains `grad_A`, and aggregates `A`, `grad_A`, `A*grad_A` by physical role-pairs. No synthetic route gate is inserted.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **7120**

## Top natural attention role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0849 | 1.4209 | 2.6267 | 1.4209 | 2.7342 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0871 | 1.0000 | 1.5290 | 1.0000 | 1.7645 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0711 | 0.7485 | 1.2407 | 0.7485 | 1.3688 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.0710 | 0.4621 | 0.8849 | 0.4621 | 0.9045 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1075 | 0.4098 | 0.6225 | 0.4098 | 0.7210 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0720 | 0.3567 | 0.6093 | 0.3567 | 0.6614 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0628 | 0.2723 | 0.5086 | 0.2723 | 0.5266 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0832 | 0.2305 | 0.4288 | 0.2305 | 0.4449 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0433 | 0.1635 | 0.1633 | 0.0484 | 0.2451 |
| 10 | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0422 | 0.0625 | 0.1204 | 0.0625 | 0.1227 |
| 11 | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0268 | 0.0597 | 0.1135 | 0.0597 | 0.1165 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0363 | 0.0719 | 0.0722 | 0.0141 | 0.1080 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0423 | 0.0390 | 0.0621 | 0.0390 | 0.0701 |
| 14 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0263 | 0.0390 | 0.0571 | 0.0390 | 0.0675 |
| 15 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1477 | 0.0449 | 0.0423 | 0.0418 | 0.0661 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0300 | 0.0414 | 0.0406 | -0.0075 | 0.0617 |
| 17 | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0223 | 0.0323 | 0.0472 | 0.0323 | 0.0559 |
| 18 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0219 | -0.0240 | -0.0490 | -0.0181 | 0.0485 |
| 19 | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0289 | 0.0197 | 0.0388 | 0.0197 | 0.0391 |
| 20 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0466 | -0.0223 | -0.0307 | -0.0194 | 0.0377 |
| 21 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0304 | 0.0182 | 0.0384 | 0.0182 | 0.0374 |
| 22 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0927 | 0.0262 | 0.0206 | 0.0223 | 0.0366 |
| 23 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0237 | -0.0214 | -0.0253 | -0.0114 | 0.0341 |
| 24 | mod.cls_blocks.1.attn.h3 | photon<-electron | 0.9895 | 0.0228 | 0.0210 | 0.0227 | 0.0333 |
| 25 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0290 | -0.0166 | -0.0242 | -0.0048 | 0.0287 |
| 26 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0235 | -0.0182 | -0.0146 | -0.0188 | 0.0255 |
| 27 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0264 | -0.0146 | -0.0207 | -0.0040 | 0.0249 |
| 28 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0289 | -0.0122 | -0.0252 | -0.0074 | 0.0248 |
| 29 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0544 | 0.0129 | 0.0233 | 0.0129 | 0.0246 |
| 30 | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0300 | 0.0137 | 0.0203 | 0.0137 | 0.0239 |

## Top natural attention role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_AxGrad | B-A | B-C | support |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0445 | 0.1836 | 0.1836 | 0.1836 | 0.2753 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0421 | 0.0830 | 0.0830 | 0.0830 | 0.1245 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.0327 | -0.0787 | -0.0787 | -0.0787 | 0.1180 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0304 | 0.0386 | 0.0386 | 0.0386 | 0.0579 |
| 5 | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.1241 | -0.0365 | -0.0365 | -0.0365 | 0.0547 |
| 6 | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.1152 | 0.0353 | 0.0353 | 0.0353 | 0.0530 |
| 7 | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0892 | 0.0348 | 0.0348 | 0.0348 | 0.0523 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0229 | -0.0302 | -0.0302 | -0.0302 | 0.0453 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0185 | 0.0292 | 0.0292 | 0.0292 | 0.0439 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0250 | -0.0221 | -0.0221 | -0.0221 | 0.0331 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0224 | -0.0209 | -0.0209 | -0.0209 | 0.0314 |
| 12 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0291 | 0.0185 | 0.0185 | 0.0185 | 0.0278 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0220 | -0.0185 | -0.0185 | -0.0185 | 0.0278 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0274 | -0.0177 | -0.0177 | -0.0177 | 0.0266 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0252 | 0.0175 | 0.0175 | 0.0175 | 0.0262 |
| 16 | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0919 | -0.0175 | -0.0175 | -0.0175 | 0.0262 |
| 17 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0288 | -0.0158 | -0.0158 | -0.0158 | 0.0237 |
| 18 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0269 | -0.0157 | -0.0157 | -0.0157 | 0.0236 |
| 19 | mod.cls_blocks.0.attn.h6 | photon<-electron | 0.0242 | -0.0152 | -0.0152 | -0.0152 | 0.0228 |
| 20 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0169 | -0.0132 | -0.0132 | -0.0132 | 0.0198 |
| 21 | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0187 | -0.0129 | -0.0129 | -0.0129 | 0.0194 |
| 22 | mod.cls_blocks.0.attn.h7 | CLS<-electron | 0.0531 | -0.0126 | -0.0126 | -0.0126 | 0.0189 |
| 23 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0385 | 0.0119 | 0.0119 | 0.0119 | 0.0178 |
| 24 | mod.cls_blocks.0.attn.h5 | CLS<-electron | 0.0519 | 0.0118 | 0.0118 | 0.0118 | 0.0177 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0505 | 0.0117 | 0.0117 | 0.0117 | 0.0175 |
| 26 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0280 | -0.0112 | -0.0112 | -0.0112 | 0.0168 |
| 27 | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0217 | -0.0102 | -0.0102 | -0.0102 | 0.0152 |
| 28 | mod.cls_blocks.0.attn.h4 | charged_hadron<-electron | 0.0239 | -0.0086 | -0.0086 | -0.0086 | 0.0128 |
| 29 | mod.cls_blocks.0.attn.h3 | photon<-electron | 0.0394 | 0.0082 | 0.0082 | 0.0082 | 0.0123 |
| 30 | mod.cls_blocks.0.attn.h2 | neutral_hadron<-electron | 0.0490 | -0.0077 | -0.0077 | -0.0077 | 0.0115 |

## Interpretation

- `mean_A`: natural attention mass on this role-link.
- `mean_AxGrad`: attention mass times objective gradient. Active links with large |A×grad| are real attention links that matter for Hqql/Tbl.
- For `B_tbl_minus_hqql`, positive B_AxGrad pushes Hqql mistakes toward Tbl; negative resists Tbl.
- This fixes the previous `rows=0` issue by manually computing the attention graph instead of relying on returned PyTorch weights.
