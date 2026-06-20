# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2

Residual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.

- events: **128**
- rows: **1600**
- summary_rows: **50**
- kind_rows: `{'particle': 1280, 'cls': 320}`
- missed_rows: **0**

## Top residual block contributions
| rank | objective | module | kind | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3406 | 0.3407 | 40.2527 | 0.0536 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.3089 | 0.3089 | 40.6796 | 0.0514 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.2487 | 0.4936 | 118.8984 | 0.0011 |
| 4 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.1974 | 0.4680 | 93.2264 | 4.099e-04 |
| 5 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.2268 | 0.3093 | 308.3826 | 1.532e-04 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.2343 | 0.2343 | 136.3645 | 0.0209 |
| 7 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1795 | 0.2499 | 261.5821 | 5.995e-05 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.1905 | 0.1905 | 136.6642 | 0.0217 |
| 9 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.1484 | 0.2796 | 119.9726 | 9.829e-04 |
| 10 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.1444 | 0.2747 | 93.0151 | 3.589e-04 |
| 11 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.1197 | 0.2105 | 100.7126 | 9.086e-04 |
| 12 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0369 | 0.4572 | 116.6634 | 0.0012 |
| 13 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0369 | 0.4572 | 110.3314 | 9.749e-04 |
| 14 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0907 | 0.1916 | 78.1873 | 3.338e-04 |
| 15 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.0339 | 0.3839 | 119.4705 | 8.760e-04 |
| 16 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0650 | 0.1977 | 283.9998 | 1.079e-04 |
| 17 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.0650 | 0.1977 | 297.3597 | 1.317e-04 |
| 18 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0595 | 0.1955 | 98.4505 | 8.055e-04 |
| 19 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0714 | 0.1359 | 190.1267 | 3.197e-04 |
| 20 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0649 | 0.1311 | 147.1597 | 1.235e-04 |
| 21 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0345 | 0.2233 | 120.0289 | 7.598e-04 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0711 | 0.0711 | 156.0649 | 0.0197 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.0711 | 0.0711 | 156.0649 | 0.0197 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0671 | 0.0841 | 39.7854 | 0.0392 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.0671 | 0.0841 | 39.7854 | 0.0392 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0675 | 0.0746 | 41.8785 | 0.0375 |
| 27 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.0397 | 0.1781 | 305.8959 | 1.081e-04 |
| 28 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0120 | 0.2447 | 116.6646 | 0.0010 |
| 29 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0120 | 0.2447 | 110.4746 | 8.180e-04 |
| 30 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0304 | 0.1569 | 114.6988 | 6.761e-04 |
| 31 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0242 | 0.1782 | 93.7970 | 7.284e-04 |
| 32 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0242 | 0.1782 | 99.4886 | 9.057e-04 |
| 33 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0290 | 0.1359 | 94.1454 | 2.437e-04 |
| 34 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0161 | 0.1743 | 93.7317 | 6.182e-04 |
| 35 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0161 | 0.1743 | 97.1010 | 7.712e-04 |
| 36 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0249 | 0.1383 | 112.9178 | 6.314e-04 |
| 37 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0249 | 0.1383 | 107.6327 | 5.061e-04 |
| 38 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0143 | 0.1690 | 86.8325 | 2.875e-04 |
| 39 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0088 | 0.1698 | 101.5244 | 6.977e-04 |
| 40 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0190 | 0.1251 | 115.4203 | 4.997e-04 |
| 41 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0042 | 0.1479 | 99.0525 | 6.045e-04 |
| 42 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0168 | 0.0964 | 186.8479 | 2.371e-04 |
| 43 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0062 | 0.1305 | 142.5991 | 5.127e-04 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0275 | 0.0382 | 164.1318 | 0.0187 |
| 45 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0093 | 0.1104 | 112.6599 | 1.919e-04 |
| 46 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0055 | 0.1061 | 139.2195 | 4.692e-04 |
| 47 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0055 | 0.1061 | 131.4601 | 3.769e-04 |
| 48 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0075 | 0.0978 | 141.7128 | 3.754e-04 |
| 49 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0019 | 0.1071 | 172.7771 | 2.317e-04 |
| 50 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0019 | 0.1071 | 182.9139 | 2.853e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3406 | 0.3407 | 40.2527 | 0.0536 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.3089 | 0.3089 | 40.6796 | 0.0514 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.2343 | 0.2343 | 136.3645 | 0.0209 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.1905 | 0.1905 | 136.6642 | 0.0217 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0711 | 0.0711 | 156.0649 | 0.0197 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.0711 | 0.0711 | 156.0649 | 0.0197 |
| 7 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0671 | 0.0841 | 39.7854 | 0.0392 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.0671 | 0.0841 | 39.7854 | 0.0392 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0675 | 0.0746 | 41.8785 | 0.0375 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0275 | 0.0382 | 164.1318 | 0.0187 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.4183 | 0.4183 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.4072 | 0.4072 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.3744 | 0.3744 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3687 | 0.3687 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3406 | 0.3407 |
| 6 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.3126 | 0.3126 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.3089 | 0.3089 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.2937 | 0.2937 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.2910 | 0.2910 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.2876 | 0.2876 |
| 11 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2862 | 0.2862 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.2624 | 0.2624 |
| 13 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.2343 | 0.2343 |
| 14 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.2248 | 0.2248 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.1974 | 0.1974 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.1905 | 0.1905 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.1852 | 0.1852 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.1831 | 0.1831 |
| 19 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.1824 | 0.1824 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1665 | 0.1665 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.1665 | 0.1665 |
| 22 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1420 | 0.1420 |
| 23 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.1420 | 0.1420 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.1360 | 0.1360 |
| 25 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.1287 | 0.1287 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.1095 | 0.1112 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.1071 | 0.1071 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.0837 | 0.0837 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.0754 | 0.0754 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.0754 | 0.0754 |
| 31 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.0689 | 0.0944 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.0689 | 0.0944 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.0695 | 0.0865 |
| 34 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.0695 | 0.0865 |
| 35 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.0722 | 0.0722 |
| 36 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.0722 | 0.0722 |
| 37 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | muon | 0.0696 | 0.0804 |
| 38 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0711 | 0.0711 |
| 39 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.0711 | 0.0711 |
| 40 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0671 | 0.0841 |
| 41 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.0671 | 0.0841 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | 0.0692 | 0.0744 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0675 | 0.0746 |
| 44 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0574 | 0.0703 |
| 45 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.0538 | 0.0645 |
| 46 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0558 | 0.0558 |
| 47 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0463 | 0.0463 |
| 48 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0433 | 0.0433 |
| 49 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0433 | 0.0433 |
| 50 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0372 | 0.0410 |
| 51 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0359 | 0.0422 |
| 52 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0359 | 0.0422 |
| 53 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0348 | 0.0410 |
| 54 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0331 | 0.0452 |
| 55 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0336 | 0.0336 |
| 56 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0336 | 0.0336 |
| 57 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0281 | 0.0548 |
| 58 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | -0.0321 | 0.0380 |
| 59 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0275 | 0.0382 |
| 60 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | muon | -0.0245 | 0.0423 |
| 61 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0238 | 0.0384 |
| 62 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0238 | 0.0384 |
| 63 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0249 | 0.0306 |
| 64 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0209 | 0.0279 |
| 65 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0223 | 0.0223 |
| 66 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0212 | 0.0251 |
| 67 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0183 | 0.0350 |
| 68 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0187 | 0.0191 |
| 69 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0187 | 0.0187 |
| 70 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0175 | 0.0201 |
| 71 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0158 | 0.0217 |
| 72 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0143 | 0.0250 |
| 73 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0143 | 0.0250 |
| 74 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0149 | 0.0221 |
| 75 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0154 | 0.0154 |
| 76 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0128 | 0.0181 |
| 77 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0133 | 0.0150 |
| 78 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0084 | 0.0293 |
| 79 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0112 | 0.0170 |
| 80 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0098 | 0.0223 |
| 81 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0067 | 0.0338 |
| 82 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0102 | 0.0199 |
| 83 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0101 | 0.0190 |
| 84 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0093 | 0.0194 |
| 85 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0056 | 0.0339 |
| 86 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | -0.0096 | 0.0153 |
| 87 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | -0.0096 | 0.0153 |
| 88 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0062 | 0.0277 |
| 89 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0102 | 0.0112 |
| 90 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | charged_hadron | -0.0103 | 0.0108 |
| 91 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0084 | 0.0178 |
| 92 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0102 | 0.0102 |
| 93 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0081 | 0.0170 |
| 94 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0081 | 0.0170 |
| 95 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0096 | 0.0107 |
| 96 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0034 | 0.0344 |
| 97 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0034 | 0.0344 |
| 98 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0063 | 0.0226 |
| 99 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0093 | 0.0099 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0093 | 0.0099 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
