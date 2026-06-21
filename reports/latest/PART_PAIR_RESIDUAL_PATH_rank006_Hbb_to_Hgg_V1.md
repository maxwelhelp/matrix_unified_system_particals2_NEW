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
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3728 | 0.3728 | 128.2821 | 0.0373 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3087 | 0.3087 | 42.8085 | 0.0781 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.1223 | 0.8043 | 102.9025 | 8.027e-04 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.2019 | 0.3923 | 265.7897 | 9.696e-05 |
| 5 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.2037 | 0.3847 | 299.4730 | 1.600e-04 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0909 | 0.7955 | 133.2286 | 0.0016 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0421 | 0.8633 | 128.8211 | 0.0014 |
| 8 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0421 | 0.8633 | 135.1693 | 0.0017 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1975 | 0.2017 | 153.6730 | 0.0319 |
| 10 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1565 | 0.3600 | 291.4624 | 1.419e-04 |
| 11 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1565 | 0.3600 | 298.9579 | 1.650e-04 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1253 | 0.4694 | 102.6035 | 7.071e-04 |
| 13 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0236 | 0.7673 | 130.6417 | 0.0017 |
| 14 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1026 | 0.3492 | 88.0831 | 6.543e-04 |
| 15 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0836 | 0.4213 | 132.7159 | 0.0015 |
| 16 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1003 | 0.3389 | 90.8134 | 5.627e-04 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 18 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.1094 | 0.2672 | 100.3251 | 4.597e-04 |
| 19 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0657 | 0.4406 | 135.6455 | 0.0014 |
| 20 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0393 | 0.4738 | 132.1758 | 0.0012 |
| 21 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0393 | 0.4738 | 138.7621 | 0.0014 |
| 22 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.1030 | 0.2188 | 122.1807 | 3.425e-04 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1081 | 0.1190 | 47.8338 | 0.0605 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 25 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0765 | 0.2343 | 121.5672 | 9.272e-04 |
| 26 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0560 | 0.3135 | 110.9119 | 0.0014 |
| 27 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0441 | 0.3055 | 114.4019 | 0.0013 |
| 28 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0441 | 0.3055 | 108.6794 | 0.0011 |
| 29 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0466 | 0.2673 | 100.7414 | 0.0012 |
| 30 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0650 | 0.1882 | 157.8145 | 6.411e-04 |
| 31 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0650 | 0.1882 | 149.9416 | 5.531e-04 |
| 32 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0352 | 0.3041 | 99.6156 | 9.500e-04 |
| 33 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0352 | 0.3041 | 102.3519 | 0.0011 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0851 | 0.0972 | 151.9449 | 0.0323 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0851 | 0.0972 | 151.9448 | 0.0323 |
| 36 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0605 | 0.1891 | 153.1321 | 6.678e-04 |
| 37 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0325 | 0.2970 | 112.8805 | 0.0013 |
| 38 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0482 | 0.2344 | 123.3645 | 8.558e-04 |
| 39 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0613 | 0.1642 | 203.4189 | 3.733e-04 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | 0.0255 | 0.3028 | 100.9367 | 0.0011 |
| 41 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0416 | 0.2328 | 124.9222 | 8.723e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0416 | 0.2328 | 119.8857 | 7.505e-04 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0471 | 0.2068 | 159.8869 | 2.235e-04 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0473 | 0.1875 | 155.1264 | 6.246e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0379 | 0.1662 | 194.6084 | 3.299e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0379 | 0.1662 | 204.4560 | 3.838e-04 |
| 47 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 1.618e-04 | 0.3078 | 293.2468 | 1.742e-04 |
| 48 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0166 | 0.1718 | 197.4753 | 4.113e-04 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0140 | 0.0803 | 47.5756 | 0.0584 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0140 | 0.0803 | 47.5756 | 0.0584 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3728 | 0.3728 | 128.2821 | 0.0373 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3087 | 0.3087 | 42.8085 | 0.0781 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1975 | 0.2017 | 153.6730 | 0.0319 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1081 | 0.1190 | 47.8338 | 0.0605 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0851 | 0.0972 | 151.9449 | 0.0323 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0851 | 0.0972 | 151.9448 | 0.0323 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0140 | 0.0803 | 47.5756 | 0.0584 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0140 | 0.0803 | 47.5756 | 0.0584 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.4987 | 0.4987 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.4127 | 0.4127 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.4017 | 0.4017 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3991 | 0.3991 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3728 | 0.3728 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.3415 | 0.3415 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.3405 | 0.3405 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.3400 | 0.3400 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3398 | 0.3398 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3087 | 0.3087 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.2341 | 0.2341 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2265 | 0.2265 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.2136 | 0.2136 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2131 | 0.2131 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1975 | 0.2017 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.1880 | 0.1941 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1600 | 0.1600 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1572 | 0.1572 |
| 19 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1572 | 0.1572 |
| 20 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1468 | 0.1468 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1433 | 0.1433 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1429 | 0.1429 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1257 | 0.1260 |
| 24 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.1230 | 0.1230 |
| 25 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.1230 | 0.1230 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.1131 | 0.1131 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1081 | 0.1190 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1095 | 0.1103 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1056 | 0.1056 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1013 | 0.1172 |
| 31 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.1025 | 0.1025 |
| 32 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.1025 | 0.1025 |
| 33 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.0926 | 0.0926 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0851 | 0.0972 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0851 | 0.0972 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0858 | 0.0880 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0849 | 0.0870 |
| 38 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0849 | 0.0870 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0813 | 0.0873 |
| 40 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0813 | 0.0873 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | 0.0780 | 0.0780 |
| 42 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | 0.0780 | 0.0780 |
| 43 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0767 | 0.0801 |
| 44 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0767 | 0.0801 |
| 45 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0662 | 0.0662 |
| 46 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0662 | 0.0662 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 0.0571 | 0.0571 |
| 48 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0561 | 0.0578 |
| 49 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0500 | 0.0500 |
| 50 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0496 | 0.0496 |
| 51 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0467 | 0.0467 |
| 52 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0467 | 0.0467 |
| 53 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.0464 | 0.0472 |
| 54 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0439 | 0.0439 |
| 55 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0439 | 0.0439 |
| 56 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0415 | 0.0415 |
| 57 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | 0.0402 | 0.0402 |
| 58 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | 0.0402 | 0.0402 |
| 59 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | 0.0389 | 0.0389 |
| 60 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | 0.0389 | 0.0389 |
| 61 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0309 | 0.0707 |
| 62 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0309 | 0.0707 |
| 63 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0381 | 0.0381 |
| 64 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0376 | 0.0376 |
| 65 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0278 | 0.0635 |
| 66 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0278 | 0.0635 |
| 67 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0347 | 0.0347 |
| 68 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0335 | 0.0335 |
| 69 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0335 | 0.0335 |
| 70 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | 0.0327 | 0.0327 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | 0.0327 | 0.0327 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0305 | 0.0367 |
| 73 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0297 | 0.0297 |
| 74 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | 0.0294 | 0.0294 |
| 75 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | 0.0294 | 0.0294 |
| 76 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0281 | 0.0281 |
| 77 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0279 | 0.0279 |
| 78 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0140 | 0.0803 |
| 79 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0140 | 0.0803 |
| 80 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0270 | 0.0270 |
| 81 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0267 | 0.0267 |
| 82 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0232 | 0.0232 |
| 83 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0077 | 0.0832 |
| 84 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0077 | 0.0832 |
| 85 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0209 | 0.0283 |
| 86 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0221 | 0.0235 |
| 87 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0192 | 0.0276 |
| 88 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0208 | 0.0208 |
| 89 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0200 | 0.0200 |
| 90 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | 0.0196 | 0.0196 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0144 | 0.0375 |
| 92 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | -0.0182 | 0.0182 |
| 93 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | -0.0182 | 0.0182 |
| 94 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0164 | 0.0226 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0154 | 0.0154 |
| 96 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | 0.0147 | 0.0147 |
| 97 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0136 | 0.0161 |
| 98 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0133 | 0.0133 |
| 99 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0099 | 0.0176 |
| 100 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0103 | 0.0125 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
