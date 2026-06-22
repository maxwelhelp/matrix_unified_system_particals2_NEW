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
| 1 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.6188 | 0.6762 | 256.5644 | 1.392e-04 |
| 2 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.4945 | 0.6483 | 332.9103 | 2.837e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.3142 | 1.0454 | 131.1305 | 0.0022 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.4435 | 0.4435 | 38.7420 | 0.1099 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1919 | 1.2656 | 132.6346 | 0.0028 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2685 | 0.8801 | 99.4952 | 8.256e-04 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3797 | 0.3797 | 127.5447 | 0.0451 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3772 | 0.3772 | 124.1126 | 0.0459 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.3095 | 0.4347 | 327.6777 | 2.449e-04 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2293 | 0.5569 | 98.9359 | 7.270e-04 |
| 11 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1759 | 0.6822 | 133.5150 | 0.0024 |
| 12 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.2594 | 0.3399 | 154.4873 | 2.643e-04 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.2551 | 0.2551 | 39.0524 | 0.1242 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.1660 | 0.6023 | 131.7672 | 0.0020 |
| 15 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.0265 | 1.1181 | 122.2819 | 0.0021 |
| 16 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | 0.0265 | 1.1181 | 127.3087 | 0.0024 |
| 17 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1814 | 0.3692 | 83.2890 | 6.863e-04 |
| 18 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1465 | 0.4828 | 103.9320 | 0.0019 |
| 19 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1332 | 0.5323 | 114.1249 | 0.0021 |
| 20 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.1855 | 0.3152 | 207.0647 | 5.845e-04 |
| 21 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.1586 | 0.3846 | 120.9973 | 0.0015 |
| 22 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.1586 | 0.3846 | 116.9248 | 0.0013 |
| 23 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.1245 | 0.4592 | 124.2668 | 0.0015 |
| 24 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0717 | 0.6207 | 127.8952 | 0.0021 |
| 25 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0717 | 0.6207 | 122.3675 | 0.0019 |
| 26 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.1354 | 0.3296 | 88.8183 | 6.032e-04 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0790 | 0.4307 | 113.1987 | 0.0018 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.1478 | 0.1478 | 141.9141 | 0.0419 |
| 29 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.1027 | 0.3195 | 155.9810 | 0.0011 |
| 30 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0653 | 0.4621 | 320.2430 | 2.587e-04 |
| 31 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0653 | 0.4621 | 310.2869 | 2.291e-04 |
| 32 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0706 | 0.4238 | 101.6715 | 0.0017 |
| 33 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0706 | 0.4238 | 98.7121 | 0.0015 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1352 | 0.1352 | 40.9518 | 0.0920 |
| 35 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0746 | 0.3199 | 200.7757 | 6.515e-04 |
| 36 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0746 | 0.3199 | 192.3868 | 5.618e-04 |
| 37 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0252 | 0.5002 | 111.1533 | 0.0019 |
| 38 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0252 | 0.5002 | 106.3581 | 0.0017 |
| 39 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0642 | 0.3384 | 151.8992 | 0.0011 |
| 40 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0642 | 0.3384 | 145.5603 | 9.420e-04 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0495 | 0.3770 | 103.4281 | 0.0016 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0534 | 0.3572 | 208.3810 | 6.720e-04 |
| 43 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0322 | 0.3518 | 123.9354 | 0.0013 |
| 44 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | 0.0244 | 0.2994 | 156.9288 | 9.651e-04 |
| 45 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0022 | 0.2881 | 97.1721 | 5.126e-04 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0022 | 0.2315 | 117.8791 | 3.964e-04 |
| 47 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0297 | 0.0893 | 137.2584 | 0.0435 |
| 48 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0297 | 0.0893 | 137.2584 | 0.0435 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0123 | 0.0920 | 40.1739 | 0.0926 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | -0.0123 | 0.0920 | 40.1739 | 0.0926 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.4435 | 0.4435 | 38.7420 | 0.1099 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3797 | 0.3797 | 127.5447 | 0.0451 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3772 | 0.3772 | 124.1126 | 0.0459 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.2551 | 0.2551 | 39.0524 | 0.1242 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.1478 | 0.1478 | 141.9141 | 0.0419 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1352 | 0.1352 | 40.9518 | 0.0920 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0297 | 0.0893 | 137.2584 | 0.0435 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0297 | 0.0893 | 137.2584 | 0.0435 |
| 9 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0123 | 0.0920 | 40.1739 | 0.0926 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | -0.0123 | 0.0920 | 40.1739 | 0.0926 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.4757 | 0.4757 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.4588 | 0.4588 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.4435 | 0.4435 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.4392 | 0.4392 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.4379 | 0.4379 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.4292 | 0.4292 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.3971 | 0.3971 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3797 | 0.3797 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3777 | 0.3777 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3772 | 0.3772 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.3681 | 0.3681 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3674 | 0.3674 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3551 | 0.3551 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.3518 | 0.3518 |
| 15 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.2834 | 0.2834 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.2811 | 0.2811 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.2551 | 0.2551 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.2538 | 0.2538 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.2276 | 0.2276 |
| 20 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.2081 | 0.2081 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.1625 | 0.1625 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.1559 | 0.1559 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1490 | 0.1490 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.1478 | 0.1478 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1454 | 0.1454 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1352 | 0.1352 |
| 27 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.1261 | 0.1261 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0958 | 0.0958 |
| 29 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0935 | 0.0935 |
| 30 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0808 | 0.0809 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0804 | 0.0804 |
| 32 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0804 | 0.0804 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | -0.0684 | 0.1271 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | -0.0684 | 0.1271 |
| 35 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0755 | 0.0839 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0698 | 0.0698 |
| 37 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0651 | 0.0651 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0651 | 0.0651 |
| 39 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | -0.0590 | 0.0590 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | -0.0590 | 0.0590 |
| 41 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0579 | 0.0579 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0567 | 0.0567 |
| 43 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0497 | 0.0775 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0497 | 0.0775 |
| 45 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0490 | 0.0742 |
| 46 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | -0.0490 | 0.0742 |
| 47 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | 0.0346 | 0.1311 |
| 48 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | 0.0346 | 0.1311 |
| 49 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0521 | 0.0574 |
| 50 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0521 | 0.0574 |
| 51 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0378 | 0.0954 |
| 52 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0378 | 0.0954 |
| 53 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0297 | 0.0893 |
| 54 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0297 | 0.0893 |
| 55 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0340 | 0.0340 |
| 56 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | 0.0339 | 0.0339 |
| 57 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | muon | 0.0339 | 0.0339 |
| 58 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0310 | 0.0393 |
| 59 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0286 | 0.0476 |
| 60 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0241 | 0.0539 |
| 61 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | -0.0241 | 0.0539 |
| 62 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.0298 | 0.0298 |
| 63 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0290 | 0.0298 |
| 64 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0287 | 0.0297 |
| 65 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0287 | 0.0297 |
| 66 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | -0.0123 | 0.0920 |
| 67 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | -0.0123 | 0.0920 |
| 68 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0266 | 0.0334 |
| 69 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0203 | 0.0558 |
| 70 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0203 | 0.0558 |
| 71 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0263 | 0.0263 |
| 72 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0262 | 0.0262 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0261 | 0.0261 |
| 74 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0085 | 0.0933 |
| 75 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | -0.0085 | 0.0933 |
| 76 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0107 | 0.0778 |
| 77 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0107 | 0.0778 |
| 78 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.0233 | 0.0233 |
| 79 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.0233 | 0.0233 |
| 80 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0195 | 0.0383 |
| 81 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0226 | 0.0226 |
| 82 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0196 | 0.0339 |
| 83 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0212 | 0.0261 |
| 84 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0172 | 0.0390 |
| 85 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0172 | 0.0390 |
| 86 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0215 | 0.0215 |
| 87 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0200 | 0.0264 |
| 88 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0200 | 0.0264 |
| 89 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0208 | 0.0227 |
| 90 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0170 | 0.0300 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0170 | 0.0300 |
| 92 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0163 | 0.0295 |
| 93 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0163 | 0.0295 |
| 94 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.0040 | 0.0775 |
| 95 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | photon | 0.0176 | 0.0176 |
| 96 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0153 | 0.0235 |
| 97 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0142 | 0.0269 |
| 98 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0142 | 0.0269 |
| 99 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | 0.0154 | 0.0217 |
| 100 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0159 | 0.0192 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
