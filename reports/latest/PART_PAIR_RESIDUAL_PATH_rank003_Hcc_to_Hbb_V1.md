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
| 1 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1517 | 0.5356 | 114.4578 | 8.236e-04 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.1923 | 0.1923 | 39.0524 | 0.0356 |
| 3 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.1672 | 0.2488 | 286.7757 | 7.806e-05 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1577 | 0.2202 | 256.5644 | 4.855e-05 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.1595 | 0.1595 | 42.8085 | 0.0336 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0999 | 0.3914 | 128.7833 | 9.599e-04 |
| 7 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0923 | 0.4067 | 99.4951 | 4.056e-04 |
| 8 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1060 | 0.3215 | 114.2446 | 7.298e-04 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.1402 | 0.1402 | 124.1126 | 0.0165 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.1253 | 0.1253 | 128.2821 | 0.0156 |
| 11 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0913 | 0.2551 | 98.9359 | 3.587e-04 |
| 12 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0914 | 0.2487 | 98.7145 | 6.842e-04 |
| 13 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0712 | 0.2212 | 96.6219 | 5.734e-04 |
| 14 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0157 | 0.4379 | 103.6675 | 4.415e-04 |
| 15 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0157 | 0.4379 | 126.7873 | 9.688e-04 |
| 16 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0730 | 0.1760 | 287.6276 | 9.768e-05 |
| 17 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0730 | 0.1760 | 255.5024 | 4.508e-05 |
| 18 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0579 | 0.2245 | 128.6508 | 8.483e-04 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0655 | 0.1815 | 311.2688 | 1.050e-04 |
| 20 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0686 | 0.1413 | 154.4873 | 1.082e-04 |
| 21 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0642 | 0.1537 | 179.4532 | 1.920e-04 |
| 22 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0592 | 0.1725 | 83.2890 | 3.335e-04 |
| 23 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0475 | 0.1626 | 110.3247 | 4.552e-04 |
| 24 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0187 | 0.2309 | 102.2466 | 3.847e-04 |
| 25 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0187 | 0.2309 | 127.6843 | 8.438e-04 |
| 26 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0318 | 0.1725 | 110.7453 | 7.797e-04 |
| 27 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0462 | 0.1088 | 117.8791 | 1.776e-04 |
| 28 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0569 | 0.0569 | 42.6181 | 0.0285 |
| 29 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0569 | 0.0569 | 42.6181 | 0.0285 |
| 30 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0330 | 0.1475 | 88.8183 | 2.831e-04 |
| 31 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0370 | 0.1151 | 200.2302 | 2.481e-04 |
| 32 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0380 | 0.1004 | 152.8992 | 4.136e-04 |
| 33 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0277 | 0.1394 | 118.8058 | 5.064e-04 |
| 34 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0277 | 0.1394 | 99.4204 | 2.315e-04 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0500 | 0.0500 | 139.8983 | 0.0147 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0500 | 0.0500 | 139.8983 | 0.0147 |
| 37 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0278 | 0.1339 | 136.8924 | 3.313e-04 |
| 38 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0432 | 0.0487 | 43.1525 | 0.0285 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0168 | 0.1521 | 101.8223 | 6.732e-04 |
| 40 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0124 | 0.1602 | 99.5773 | 6.435e-04 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0124 | 0.1602 | 88.5189 | 2.940e-04 |
| 42 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0379 | 0.0432 | 142.8148 | 0.0144 |
| 43 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | 6.492e-04 | 0.1623 | 86.0668 | 3.540e-04 |
| 44 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | 6.491e-04 | 0.1623 | 107.9099 | 7.760e-04 |
| 45 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0157 | 0.0966 | 191.2977 | 2.276e-04 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0157 | 0.0966 | 153.0208 | 1.043e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | 0.0050 | 0.1194 | 97.1721 | 2.368e-04 |
| 48 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 7.287e-04 | 0.1225 | 120.8565 | 5.540e-04 |
| 49 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0039 | 0.1034 | 148.4712 | 3.761e-04 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0039 | 0.1034 | 119.5033 | 1.721e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.1923 | 0.1923 | 39.0524 | 0.0356 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.1595 | 0.1595 | 42.8085 | 0.0336 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.1402 | 0.1402 | 124.1126 | 0.0165 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.1253 | 0.1253 | 128.2821 | 0.0156 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0569 | 0.0569 | 42.6181 | 0.0285 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0569 | 0.0569 | 42.6181 | 0.0285 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0500 | 0.0500 | 139.8983 | 0.0147 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0500 | 0.0500 | 139.8983 | 0.0147 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0432 | 0.0487 | 43.1525 | 0.0285 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0379 | 0.0432 | 142.8148 | 0.0144 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.2115 | 0.2115 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.2023 | 0.2023 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.1953 | 0.1953 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.1945 | 0.1945 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.1927 | 0.1927 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.1923 | 0.1923 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1819 | 0.1819 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.1595 | 0.1595 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.1570 | 0.1570 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.1562 | 0.1562 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.1521 | 0.1521 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.1493 | 0.1493 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.1466 | 0.1466 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.1419 | 0.1419 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.1402 | 0.1402 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.1383 | 0.1383 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.1266 | 0.1266 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.1253 | 0.1253 |
| 19 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.1218 | 0.1218 |
| 20 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.1218 | 0.1218 |
| 21 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.1130 | 0.1130 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.1130 | 0.1130 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1109 | 0.1109 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.1059 | 0.1059 |
| 25 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.0630 | 0.0630 |
| 26 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | 0.0630 | 0.0630 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0590 | 0.0590 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0576 | 0.0576 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.0576 | 0.0576 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0569 | 0.0569 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0569 | 0.0569 |
| 32 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0539 | 0.0539 |
| 33 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | muon | -0.0539 | 0.0539 |
| 34 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0519 | 0.0519 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0519 | 0.0519 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.0505 | 0.0505 |
| 37 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0500 | 0.0500 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0500 | 0.0500 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.0481 | 0.0481 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0470 | 0.0470 |
| 41 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0470 | 0.0470 |
| 42 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0469 | 0.0469 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0432 | 0.0487 |
| 44 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0434 | 0.0434 |
| 45 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0434 | 0.0434 |
| 46 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0431 | 0.0431 |
| 47 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0424 | 0.0424 |
| 48 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | muon | 0.0424 | 0.0424 |
| 49 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0415 | 0.0415 |
| 50 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | 0.0415 | 0.0415 |
| 51 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0395 | 0.0421 |
| 52 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0387 | 0.0439 |
| 53 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0394 | 0.0406 |
| 54 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0375 | 0.0463 |
| 55 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0392 | 0.0392 |
| 56 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0392 | 0.0392 |
| 57 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0379 | 0.0432 |
| 58 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0336 | 0.0413 |
| 59 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | muon | 0.0324 | 0.0324 |
| 60 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0298 | 0.0371 |
| 61 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0300 | 0.0300 |
| 62 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0290 | 0.0290 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0235 | 0.0248 |
| 64 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0235 | 0.0235 |
| 65 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0235 | 0.0235 |
| 66 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0233 | 0.0233 |
| 67 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0221 | 0.0221 |
| 68 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0214 | 0.0219 |
| 69 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0212 | 0.0212 |
| 70 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | muon | 0.0212 | 0.0212 |
| 71 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0212 | 0.0212 |
| 72 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | 0.0154 | 0.0420 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0205 | 0.0205 |
| 74 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0197 | 0.0197 |
| 75 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0176 | 0.0271 |
| 76 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0182 | 0.0215 |
| 77 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0182 | 0.0215 |
| 78 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0173 | 0.0245 |
| 79 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0173 | 0.0245 |
| 80 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0309 |
| 81 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0309 |
| 82 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0143 | 0.0275 |
| 83 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0167 | 0.0167 |
| 84 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0160 | 0.0161 |
| 85 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0160 | 0.0160 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0221 |
| 87 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0144 | 0.0221 |
| 88 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | muon | -0.0158 | 0.0158 |
| 89 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0153 | 0.0153 |
| 90 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0150 | 0.0150 |
| 91 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | 0.0144 | 0.0152 |
| 92 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0127 | 0.0208 |
| 93 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0115 | 0.0162 |
| 94 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | electron | -0.0122 | 0.0122 |
| 95 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0080 | 0.0274 |
| 96 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | muon | 0.0118 | 0.0118 |
| 97 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0085 | 0.0246 |
| 98 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0085 | 0.0246 |
| 99 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0106 | 0.0152 |
| 100 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | muon | 0.0114 | 0.0114 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
