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
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3728 | 0.3728 | 128.2821 | 0.0373 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3087 | 0.3087 | 42.8085 | 0.0781 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1223 | 0.8043 | 129.3170 | 0.0018 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.2019 | 0.3923 | 308.4886 | 2.229e-04 |
| 5 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.2037 | 0.3847 | 262.8722 | 8.169e-05 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0909 | 0.7955 | 108.9801 | 8.231e-04 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0421 | 0.8633 | 135.1693 | 0.0017 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.1975 | 0.2017 | 153.6730 | 0.0319 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1565 | 0.3600 | 298.9579 | 1.650e-04 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1253 | 0.4694 | 131.1054 | 0.0016 |
| 11 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0236 | 0.7673 | 122.4922 | 0.0014 |
| 12 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0236 | 0.7673 | 130.6417 | 0.0017 |
| 13 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1026 | 0.3492 | 112.7470 | 0.0015 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0836 | 0.4213 | 124.1361 | 0.0012 |
| 15 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0836 | 0.4213 | 132.7159 | 0.0015 |
| 16 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1003 | 0.3389 | 103.5501 | 0.0013 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 18 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 19 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1094 | 0.2672 | 123.1559 | 0.0011 |
| 20 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0657 | 0.4406 | 109.8403 | 7.203e-04 |
| 21 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0393 | 0.4738 | 138.7621 | 0.0014 |
| 22 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.1030 | 0.2188 | 155.5532 | 7.872e-04 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1081 | 0.1190 | 47.8338 | 0.0605 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 26 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0765 | 0.2343 | 114.6783 | 7.526e-04 |
| 27 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0765 | 0.2343 | 121.5672 | 9.272e-04 |
| 28 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0560 | 0.3135 | 110.9119 | 0.0014 |
| 29 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0560 | 0.3135 | 103.8528 | 0.0011 |
| 30 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0441 | 0.3055 | 114.4019 | 0.0013 |
| 31 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0466 | 0.2673 | 96.7174 | 9.434e-04 |
| 32 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0466 | 0.2673 | 100.7414 | 0.0012 |
| 33 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0650 | 0.1882 | 157.8145 | 6.411e-04 |
| 34 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0352 | 0.3041 | 102.3519 | 0.0011 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0851 | 0.0972 | 151.9448 | 0.0323 |
| 36 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0605 | 0.1891 | 143.2139 | 5.408e-04 |
| 37 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0605 | 0.1891 | 153.1321 | 6.678e-04 |
| 38 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0325 | 0.2970 | 91.8748 | 6.593e-04 |
| 39 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0482 | 0.2344 | 101.7508 | 4.351e-04 |
| 40 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0613 | 0.1642 | 161.8836 | 1.901e-04 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | 0.0255 | 0.3028 | 88.6964 | 5.500e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0416 | 0.2328 | 124.9222 | 8.723e-04 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0471 | 0.2068 | 203.8861 | 5.142e-04 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0473 | 0.1875 | 122.9819 | 3.175e-04 |
| 45 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0379 | 0.1662 | 204.4560 | 3.838e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 1.618e-04 | 0.3078 | 293.2468 | 1.742e-04 |
| 47 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 1.618e-04 | 0.3078 | 281.0337 | 1.404e-04 |
| 48 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0166 | 0.1718 | 197.4753 | 4.113e-04 |
| 49 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0166 | 0.1718 | 184.7526 | 3.319e-04 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0140 | 0.0803 | 47.5756 | 0.0584 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3728 | 0.3728 | 128.2821 | 0.0373 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3087 | 0.3087 | 42.8085 | 0.0781 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.1975 | 0.2017 | 153.6730 | 0.0319 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1429 | 0.1429 | 46.8318 | 0.0596 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1081 | 0.1190 | 47.8338 | 0.0605 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1095 | 0.1103 | 152.0541 | 0.0326 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0851 | 0.0972 | 151.9448 | 0.0323 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0140 | 0.0803 | 47.5756 | 0.0584 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.4987 | 0.4987 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.4127 | 0.4127 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.4017 | 0.4017 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.3991 | 0.3991 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3728 | 0.3728 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.3415 | 0.3415 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.3405 | 0.3405 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3400 | 0.3400 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3398 | 0.3398 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3087 | 0.3087 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.2341 | 0.2341 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2265 | 0.2265 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.2136 | 0.2136 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.2131 | 0.2131 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.1975 | 0.2017 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.1880 | 0.1941 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1600 | 0.1600 |
| 18 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1600 | 0.1600 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1572 | 0.1572 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1468 | 0.1468 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1468 | 0.1468 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1433 | 0.1433 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1429 | 0.1429 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1429 | 0.1429 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1257 | 0.1260 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1257 | 0.1260 |
| 27 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | 0.1230 | 0.1230 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1131 | 0.1131 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1131 | 0.1131 |
| 30 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1081 | 0.1190 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1095 | 0.1103 |
| 32 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1095 | 0.1103 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1056 | 0.1056 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1056 | 0.1056 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.1013 | 0.1172 |
| 36 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | 0.1025 | 0.1025 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0926 | 0.0926 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0851 | 0.0972 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0858 | 0.0880 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0858 | 0.0880 |
| 41 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0849 | 0.0870 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0813 | 0.0873 |
| 43 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | 0.0780 | 0.0780 |
| 44 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0767 | 0.0801 |
| 45 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | 0.0662 | 0.0662 |
| 46 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0571 | 0.0571 |
| 47 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0561 | 0.0578 |
| 48 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0500 | 0.0500 |
| 49 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0496 | 0.0496 |
| 50 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0467 | 0.0467 |
| 51 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0464 | 0.0472 |
| 52 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0464 | 0.0472 |
| 53 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | 0.0439 | 0.0439 |
| 54 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0415 | 0.0415 |
| 55 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | 0.0402 | 0.0402 |
| 56 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | 0.0389 | 0.0389 |
| 57 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0309 | 0.0707 |
| 58 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0381 | 0.0381 |
| 59 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0376 | 0.0376 |
| 60 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0376 | 0.0376 |
| 61 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0278 | 0.0635 |
| 62 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0347 | 0.0347 |
| 63 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | -0.0335 | 0.0335 |
| 64 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | 0.0327 | 0.0327 |
| 65 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0305 | 0.0367 |
| 66 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0297 | 0.0297 |
| 67 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0294 | 0.0294 |
| 68 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0281 | 0.0281 |
| 69 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0281 | 0.0281 |
| 70 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0279 | 0.0279 |
| 71 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0140 | 0.0803 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0270 | 0.0270 |
| 73 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0270 | 0.0270 |
| 74 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0267 | 0.0267 |
| 75 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0232 | 0.0232 |
| 76 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | -0.0232 | 0.0232 |
| 77 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0077 | 0.0832 |
| 78 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0209 | 0.0283 |
| 79 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0209 | 0.0283 |
| 80 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0221 | 0.0235 |
| 81 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0221 | 0.0235 |
| 82 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0192 | 0.0276 |
| 83 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0208 | 0.0208 |
| 84 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0200 | 0.0200 |
| 85 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | -0.0200 | 0.0200 |
| 86 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0196 | 0.0196 |
| 87 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0375 |
| 88 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0375 |
| 89 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | -0.0182 | 0.0182 |
| 90 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0164 | 0.0226 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0154 | 0.0154 |
| 92 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | 0.0147 | 0.0147 |
| 93 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0136 | 0.0161 |
| 94 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0133 | 0.0133 |
| 95 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0099 | 0.0176 |
| 96 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0099 | 0.0176 |
| 97 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0103 | 0.0125 |
| 98 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0103 | 0.0125 |
| 99 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0083 | 0.0083 |
| 100 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0068 | 0.0092 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
