# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2

Residual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.

- events: **64**
- rows: **800**
- summary_rows: **50**
- kind_rows: `{'particle': 640, 'cls': 160}`
- missed_rows: **0**

## Top residual block contributions
| rank | objective | module | kind | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.5416 | 0.5416 | 39.0524 | 0.0838 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.4528 | 0.4528 | 124.1126 | 0.0409 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2171 | 0.5748 | 96.9171 | 5.634e-04 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.2698 | 0.2698 | 149.6900 | 0.0332 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.2419 | 0.2419 | 49.7953 | 0.0637 |
| 6 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.2180 | 0.2721 | 255.3485 | 8.478e-05 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.2195 | 0.2195 | 42.6207 | 0.0720 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.2195 | 0.2195 | 42.6207 | 0.0720 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1800 | 0.1800 | 141.8127 | 0.0363 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1800 | 0.1800 | 141.8127 | 0.0363 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1041 | 0.4421 | 131.1386 | 0.0016 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1322 | 0.3208 | 97.6289 | 4.827e-04 |
| 13 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.1409 | 0.1763 | 148.8833 | 1.587e-04 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1461 | 0.1461 | 152.7344 | 0.0331 |
| 15 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1169 | 0.2567 | 81.9046 | 4.526e-04 |
| 16 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0143 | 0.6361 | 118.3460 | 0.0015 |
| 17 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0143 | 0.6361 | 125.5107 | 0.0018 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0396 | 0.5114 | 130.2367 | 0.0021 |
| 19 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.1054 | 0.1792 | 141.7775 | 5.528e-04 |
| 20 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.1054 | 0.1792 | 150.3916 | 6.623e-04 |
| 21 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0994 | 0.1981 | 118.0972 | 8.726e-04 |
| 22 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0994 | 0.1981 | 112.7448 | 7.289e-04 |
| 23 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0908 | 0.2274 | 305.0574 | 3.497e-04 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1178 | 0.1184 | 49.1468 | 0.0618 |
| 25 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0718 | 0.2425 | 287.8273 | 2.535e-04 |
| 26 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | -0.0718 | 0.2425 | 297.7767 | 3.023e-04 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0715 | 0.2351 | 112.7917 | 0.0015 |
| 28 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0888 | 0.1367 | 156.4577 | 8.010e-04 |
| 29 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0732 | 0.1482 | 156.8574 | 6.300e-04 |
| 30 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0651 | 0.1694 | 123.2512 | 8.222e-04 |
| 31 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0534 | 0.2114 | 85.9040 | 3.825e-04 |
| 32 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0438 | 0.2456 | 132.0454 | 0.0013 |
| 33 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0659 | 0.1378 | 199.9749 | 5.388e-04 |
| 34 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0516 | 0.1695 | 121.5631 | 0.0010 |
| 35 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0160 | 0.2860 | 130.4499 | 0.0017 |
| 36 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0015 | 0.3155 | 126.1710 | 0.0015 |
| 37 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0015 | 0.3155 | 118.8048 | 0.0012 |
| 38 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0352 | 0.1540 | 115.1937 | 2.502e-04 |
| 39 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0175 | 0.2218 | 101.1805 | 0.0010 |
| 40 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0175 | 0.2218 | 108.1853 | 0.0012 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0196 | 0.1925 | 102.5544 | 0.0013 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0272 | 0.1599 | 182.1498 | 3.740e-04 |
| 43 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0272 | 0.1599 | 193.7164 | 4.474e-04 |
| 44 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0197 | 0.1545 | 104.0169 | 9.767e-04 |
| 45 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.0052 | 0.1950 | 308.2119 | 2.773e-04 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | -0.0205 | 0.1304 | 206.9739 | 4.330e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0016 | 0.2033 | 99.2524 | 8.766e-04 |
| 48 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0016 | 0.2033 | 102.4188 | 0.0010 |
| 49 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0049 | 0.1887 | 113.4441 | 0.0011 |
| 50 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0035 | 0.1895 | 93.6346 | 3.176e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.5416 | 0.5416 | 39.0524 | 0.0838 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.4528 | 0.4528 | 124.1126 | 0.0409 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.2698 | 0.2698 | 149.6900 | 0.0332 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.2419 | 0.2419 | 49.7953 | 0.0637 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.2195 | 0.2195 | 42.6207 | 0.0720 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.2195 | 0.2195 | 42.6207 | 0.0720 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1800 | 0.1800 | 141.8127 | 0.0363 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1800 | 0.1800 | 141.8127 | 0.0363 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1461 | 0.1461 | 152.7344 | 0.0331 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1178 | 0.1184 | 49.1468 | 0.0618 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.5853 | 0.5853 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.5726 | 0.5726 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.5416 | 0.5416 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.4817 | 0.4817 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.4783 | 0.4783 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.4528 | 0.4528 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3690 | 0.3690 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.3614 | 0.3614 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.3443 | 0.3443 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.3402 | 0.3402 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.2901 | 0.2901 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.2740 | 0.2740 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.2698 | 0.2698 |
| 14 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.2568 | 0.2568 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.2568 | 0.2568 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2503 | 0.2503 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.2427 | 0.2427 |
| 18 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.2427 | 0.2427 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.2419 | 0.2419 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2328 | 0.2328 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.2312 | 0.2312 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.2195 | 0.2195 |
| 23 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.2195 | 0.2195 |
| 24 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.2164 | 0.2164 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.2067 | 0.2067 |
| 26 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.2067 | 0.2067 |
| 27 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1927 | 0.1927 |
| 28 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1927 | 0.1927 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1867 | 0.1867 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1800 | 0.1800 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1800 | 0.1800 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1691 | 0.1691 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1662 | 0.1662 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1587 | 0.1600 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1461 | 0.1461 |
| 36 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.1455 | 0.1455 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1223 | 0.1223 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1178 | 0.1184 |
| 39 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1094 | 0.1094 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1094 | 0.1094 |
| 41 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.1077 | 0.1077 |
| 42 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.1077 | 0.1077 |
| 43 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.1058 | 0.1058 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0814 | 0.0814 |
| 45 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0782 | 0.0782 |
| 46 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | -0.0757 | 0.0757 |
| 47 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0737 | 0.0737 |
| 48 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0737 | 0.0737 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0709 | 0.0709 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | 0.0652 | 0.0652 |
| 51 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0578 | 0.0578 |
| 52 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0532 | 0.0532 |
| 53 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0453 | 0.0527 |
| 54 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0395 | 0.0441 |
| 55 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0397 | 0.0397 |
| 56 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0389 | 0.0389 |
| 57 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0389 | 0.0389 |
| 58 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0383 | 0.0384 |
| 59 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0383 | 0.0383 |
| 60 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0378 | 0.0378 |
| 61 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0378 | 0.0378 |
| 62 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0376 | 0.0376 |
| 63 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0330 | 0.0330 |
| 64 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0330 | 0.0330 |
| 65 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0317 | 0.0317 |
| 66 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0297 | 0.0297 |
| 67 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0297 | 0.0297 |
| 68 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0268 | 0.0268 |
| 69 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0261 | 0.0261 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0259 | 0.0259 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0252 | 0.0252 |
| 72 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0252 | 0.0252 |
| 73 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0229 | 0.0257 |
| 74 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0222 | 0.0222 |
| 75 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0213 | 0.0234 |
| 76 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0170 | 0.0396 |
| 77 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0192 | 0.0192 |
| 78 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0192 | 0.0192 |
| 79 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0189 | 0.0189 |
| 80 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0160 | 0.0186 |
| 81 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0160 | 0.0186 |
| 82 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | 0.0147 | 0.0147 |
| 83 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0135 | 0.0135 |
| 84 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0135 | 0.0135 |
| 85 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0128 | 0.0160 |
| 86 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0133 | 0.0133 |
| 87 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | charged_hadron | -0.0123 | 0.0148 |
| 88 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | -0.0120 | 0.0147 |
| 89 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0106 | 0.0190 |
| 90 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0106 | 0.0190 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | -0.0114 | 0.0114 |
| 92 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | neutral_hadron | -0.0093 | 0.0104 |
| 93 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0089 | 0.0098 |
| 94 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0089 | 0.0098 |
| 95 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0084 | 0.0113 |
| 96 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0089 | 0.0089 |
| 97 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | -0.0079 | 0.0096 |
| 98 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0079 | 0.0079 |
| 99 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0079 | 0.0079 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | 0.0071 | 0.0106 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
