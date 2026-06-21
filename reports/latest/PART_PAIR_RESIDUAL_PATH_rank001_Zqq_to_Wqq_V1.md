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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.1018 | 0.6104 | 96.9171 | 6.962e-04 |
| 2 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1282 | 0.2951 | 97.6289 | 5.555e-04 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.0980 | 0.3818 | 126.1881 | 0.0015 |
| 4 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.1342 | 0.1970 | 93.6346 | 3.163e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1460 | 0.1460 | 154.6844 | 0.0269 |
| 6 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1172 | 0.2565 | 81.9046 | 4.848e-04 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1438 | 0.1438 | 50.8918 | 0.0465 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0992 | 0.2914 | 131.4871 | 0.0015 |
| 9 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0297 | 0.5556 | 130.2134 | 0.0019 |
| 10 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0995 | 0.2172 | 85.9040 | 3.871e-04 |
| 11 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.1070 | 0.1732 | 115.1937 | 2.525e-04 |
| 12 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0851 | 0.1904 | 123.7140 | 8.999e-04 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1036 | 0.1036 | 49.9678 | 0.0485 |
| 14 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1036 | 0.1036 | 49.9678 | 0.0485 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1036 | 0.1036 | 150.2727 | 0.0277 |
| 16 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1036 | 0.1036 | 150.2727 | 0.0277 |
| 17 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0182 | 0.4215 | 132.2929 | 0.0017 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0182 | 0.4215 | 123.0197 | 0.0014 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.0614 | 0.2458 | 255.3485 | 1.146e-04 |
| 20 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0806 | 0.1556 | 156.3908 | 7.021e-04 |
| 21 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0543 | 0.2231 | 103.3731 | 0.0011 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.0844 | 0.0903 | 149.6900 | 0.0279 |
| 23 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0710 | 0.1225 | 114.4745 | 6.500e-04 |
| 24 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0710 | 0.1225 | 121.9741 | 8.059e-04 |
| 25 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0586 | 0.1112 | 117.9251 | 6.655e-04 |
| 26 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0261 | 0.2341 | 318.4889 | 3.121e-04 |
| 27 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0364 | 0.1762 | 126.9488 | 0.0012 |
| 28 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0538 | 0.1019 | 146.0175 | 5.205e-04 |
| 29 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0538 | 0.1019 | 156.3204 | 6.456e-04 |
| 30 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0220 | 0.2218 | 111.4164 | 0.0014 |
| 31 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0495 | 0.1081 | 192.3109 | 3.515e-04 |
| 32 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0495 | 0.1081 | 206.9867 | 4.384e-04 |
| 33 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0531 | 0.0903 | 196.8568 | 3.688e-04 |
| 34 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0326 | 0.1587 | 302.8277 | 2.238e-04 |
| 35 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0326 | 0.1587 | 316.7226 | 2.856e-04 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.0325 | 0.1481 | 302.0735 | 2.474e-04 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0415 | 0.1000 | 152.0129 | 5.405e-04 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.0451 | 0.0734 | 49.7953 | 0.0568 |
| 39 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0242 | 0.1567 | 112.6805 | 0.0012 |
| 40 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 0.0242 | 0.1567 | 104.2718 | 9.779e-04 |
| 41 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0053 | 0.2004 | 133.8216 | 0.0014 |
| 42 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0053 | 0.2004 | 124.4409 | 0.0011 |
| 43 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0141 | 0.1468 | 148.8833 | 1.726e-04 |
| 44 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0125 | 0.1238 | 202.8836 | 4.736e-04 |
| 45 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | 0.0042 | 0.1320 | 101.5682 | 7.977e-04 |
| 46 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0052 | 0.1207 | 109.2348 | 9.817e-04 |
| 47 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0043 | 0.1192 | 101.4929 | 9.847e-04 |
| 48 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | 0.0043 | 0.1192 | 97.1256 | 7.965e-04 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0194 | 0.0512 | 162.5002 | 0.0256 |
| 50 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | -0.0060 | 0.0544 | 52.8696 | 0.0490 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1460 | 0.1460 | 154.6844 | 0.0269 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1438 | 0.1438 | 50.8918 | 0.0465 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1036 | 0.1036 | 49.9678 | 0.0485 |
| 4 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1036 | 0.1036 | 49.9678 | 0.0485 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1036 | 0.1036 | 150.2727 | 0.0277 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1036 | 0.1036 | 150.2727 | 0.0277 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.0844 | 0.0903 | 149.6900 | 0.0279 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.0451 | 0.0734 | 49.7953 | 0.0568 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0194 | 0.0512 | 162.5002 | 0.0256 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | -0.0060 | 0.0544 | 52.8696 | 0.0490 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.1834 | 0.1834 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1799 | 0.1799 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.1547 | 0.1547 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1460 | 0.1460 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1438 | 0.1438 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.1406 | 0.1406 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1364 | 0.1364 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.1328 | 0.1328 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1308 | 0.1308 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1243 | 0.1243 |
| 11 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1243 | 0.1243 |
| 12 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | muon | -0.1239 | 0.1239 |
| 13 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | muon | -0.1218 | 0.1218 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1161 | 0.1161 |
| 15 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1161 | 0.1161 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1077 | 0.1077 |
| 17 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1077 | 0.1077 |
| 18 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | muon | -0.1066 | 0.1066 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1036 | 0.1036 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1036 | 0.1036 |
| 21 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1036 | 0.1036 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1036 | 0.1036 |
| 23 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0866 | 0.1059 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0889 | 0.0889 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0889 | 0.0889 |
| 26 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.0844 | 0.0903 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0845 | 0.0845 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0845 | 0.0845 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.0833 | 0.0861 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.0806 | 0.0873 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0813 | 0.0813 |
| 32 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0736 | 0.0999 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.0738 | 0.0839 |
| 34 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0711 | 0.0907 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0700 | 0.0700 |
| 36 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0687 | 0.0687 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.0641 | 0.0837 |
| 38 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0661 | 0.0661 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0661 | 0.0661 |
| 40 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | -0.0564 | 0.0564 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0553 | 0.0553 |
| 42 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0543 | 0.0543 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.0412 | 0.0931 |
| 44 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0513 | 0.0513 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.0451 | 0.0734 |
| 46 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | muon | -0.0489 | 0.0491 |
| 47 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0447 | 0.0598 |
| 48 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | -0.0474 | 0.0480 |
| 49 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0446 | 0.0488 |
| 50 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0443 | 0.0443 |
| 51 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0408 | 0.0408 |
| 52 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.0340 | 0.0597 |
| 53 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0321 | 0.0498 |
| 54 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0263 | 0.0542 |
| 55 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0310 | 0.0310 |
| 56 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0258 | 0.0302 |
| 57 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0261 | 0.0261 |
| 58 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0261 | 0.0261 |
| 59 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0194 | 0.0512 |
| 60 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | 0.0233 | 0.0357 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | electron | -0.0245 | 0.0245 |
| 62 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | 0.0242 | 0.0242 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0228 | 0.0260 |
| 64 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0193 | 0.0381 |
| 65 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0220 | 0.0220 |
| 66 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0139 | 0.0354 |
| 67 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0182 | 0.0182 |
| 68 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | 0.0182 | 0.0182 |
| 69 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | 0.0177 | 0.0177 |
| 70 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0089 | 0.0469 |
| 71 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | -0.0159 | 0.0159 |
| 72 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | -0.0060 | 0.0544 |
| 73 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0140 | 0.0144 |
| 74 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0140 | 0.0144 |
| 75 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0134 | 0.0166 |
| 76 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0134 | 0.0166 |
| 77 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | muon | -0.0133 | 0.0133 |
| 78 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0128 | 0.0128 |
| 79 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0124 | 0.0124 |
| 80 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0102 | 0.0186 |
| 81 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0102 | 0.0186 |
| 82 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | neutral_hadron | -0.0082 | 0.0161 |
| 83 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0069 | 0.0153 |
| 84 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0077 | 0.0077 |
| 85 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0074 | 0.0074 |
| 86 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0074 | 0.0074 |
| 87 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | neutral_hadron | -0.0056 | 0.0138 |
| 88 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | -0.0066 | 0.0098 |
| 89 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0063 | 0.0098 |
| 90 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0063 | 0.0098 |
| 91 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0064 | 0.0085 |
| 92 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0062 | 0.0084 |
| 93 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | 8.507e-04 | 0.0285 |
| 94 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | photon | -0.0062 | 0.0065 |
| 95 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0060 | 0.0060 |
| 96 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | charged_hadron | -0.0055 | 0.0057 |
| 97 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0050 | 0.0075 |
| 98 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0050 | 0.0075 |
| 99 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0055 | 0.0055 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0055 | 0.0055 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
