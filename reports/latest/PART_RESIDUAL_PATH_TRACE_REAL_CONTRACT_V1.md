# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V1

Residual path composition trace. For every `mod.blocks.N` and `mod.cls_blocks.N`, it computes `delta = block_out - block_in` and contribution `dot(delta, dJ/dblock_out)`, grouped by analysis group and particle roles. This starts connecting particle blocks → CLS blocks → logits.

- events: **128**
- rows: **1280**
- summary_rows: **40**

## Top residual block contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | -0.2487 | 0.4936 | 118.8984 | 0.0011 |
| 2 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | -0.1974 | 0.4680 | 93.2264 | 4.099e-04 |
| 3 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | 0.2268 | 0.3093 | 308.3826 | 1.532e-04 |
| 4 | signed_hqql_tbl | mod.blocks.7 | A_Hqql_correct | 0.1795 | 0.2499 | 261.5821 | 5.995e-05 |
| 5 | signed_hqql_tbl | mod.blocks.1 | C_Tbl_correct | -0.1484 | 0.2796 | 119.9726 | 9.829e-04 |
| 6 | signed_hqql_tbl | mod.blocks.1 | A_Hqql_correct | -0.1444 | 0.2747 | 93.0151 | 3.589e-04 |
| 7 | signed_hqql_tbl | mod.blocks.2 | C_Tbl_correct | -0.1197 | 0.2105 | 100.7126 | 9.086e-04 |
| 8 | B_tbl_minus_hqql | mod.blocks.0 | B_Hqql_to_Tbl | -0.0369 | 0.4572 | 116.6634 | 0.0012 |
| 9 | signed_hqql_tbl | mod.blocks.0 | B_Hqql_to_Tbl | -0.0369 | 0.4572 | 110.3314 | 9.749e-04 |
| 10 | signed_hqql_tbl | mod.blocks.2 | A_Hqql_correct | -0.0907 | 0.1916 | 78.1873 | 3.338e-04 |
| 11 | signed_hqql_tbl | mod.blocks.0 | D_Tbl_to_Hqql | -0.0339 | 0.3839 | 119.4705 | 8.760e-04 |
| 12 | signed_hqql_tbl | mod.blocks.7 | B_Hqql_to_Tbl | 0.0650 | 0.1977 | 283.9998 | 1.079e-04 |
| 13 | B_tbl_minus_hqql | mod.blocks.7 | B_Hqql_to_Tbl | 0.0650 | 0.1977 | 297.3597 | 1.317e-04 |
| 14 | signed_hqql_tbl | mod.blocks.3 | C_Tbl_correct | -0.0595 | 0.1955 | 98.4505 | 8.055e-04 |
| 15 | signed_hqql_tbl | mod.blocks.6 | C_Tbl_correct | 0.0714 | 0.1359 | 190.1267 | 3.197e-04 |
| 16 | signed_hqql_tbl | mod.blocks.6 | A_Hqql_correct | 0.0649 | 0.1311 | 147.1597 | 1.235e-04 |
| 17 | signed_hqql_tbl | mod.blocks.1 | D_Tbl_to_Hqql | -0.0345 | 0.2233 | 120.0289 | 7.598e-04 |
| 18 | signed_hqql_tbl | mod.blocks.7 | D_Tbl_to_Hqql | 0.0397 | 0.1781 | 305.8959 | 1.081e-04 |
| 19 | B_tbl_minus_hqql | mod.blocks.1 | B_Hqql_to_Tbl | -0.0120 | 0.2447 | 116.6646 | 0.0010 |
| 20 | signed_hqql_tbl | mod.blocks.1 | B_Hqql_to_Tbl | -0.0120 | 0.2447 | 110.4746 | 8.180e-04 |
| 21 | signed_hqql_tbl | mod.blocks.4 | C_Tbl_correct | -0.0304 | 0.1569 | 114.6988 | 6.761e-04 |
| 22 | signed_hqql_tbl | mod.blocks.2 | B_Hqql_to_Tbl | -0.0242 | 0.1782 | 93.7970 | 7.284e-04 |
| 23 | B_tbl_minus_hqql | mod.blocks.2 | B_Hqql_to_Tbl | -0.0242 | 0.1782 | 99.4886 | 9.057e-04 |
| 24 | signed_hqql_tbl | mod.blocks.4 | A_Hqql_correct | -0.0290 | 0.1359 | 94.1454 | 2.437e-04 |
| 25 | signed_hqql_tbl | mod.blocks.3 | B_Hqql_to_Tbl | -0.0161 | 0.1743 | 93.7317 | 6.182e-04 |
| 26 | B_tbl_minus_hqql | mod.blocks.3 | B_Hqql_to_Tbl | -0.0161 | 0.1743 | 97.1010 | 7.712e-04 |
| 27 | B_tbl_minus_hqql | mod.blocks.4 | B_Hqql_to_Tbl | -0.0249 | 0.1383 | 112.9178 | 6.314e-04 |
| 28 | signed_hqql_tbl | mod.blocks.4 | B_Hqql_to_Tbl | -0.0249 | 0.1383 | 107.6327 | 5.061e-04 |
| 29 | signed_hqql_tbl | mod.blocks.3 | A_Hqql_correct | -0.0143 | 0.1690 | 86.8325 | 2.875e-04 |
| 30 | signed_hqql_tbl | mod.blocks.2 | D_Tbl_to_Hqql | -0.0088 | 0.1698 | 101.5244 | 6.977e-04 |
| 31 | signed_hqql_tbl | mod.blocks.4 | D_Tbl_to_Hqql | 0.0190 | 0.1251 | 115.4203 | 4.997e-04 |
| 32 | signed_hqql_tbl | mod.blocks.3 | D_Tbl_to_Hqql | 0.0042 | 0.1479 | 99.0525 | 6.045e-04 |
| 33 | signed_hqql_tbl | mod.blocks.6 | D_Tbl_to_Hqql | 0.0168 | 0.0964 | 186.8479 | 2.371e-04 |
| 34 | signed_hqql_tbl | mod.blocks.5 | C_Tbl_correct | -0.0062 | 0.1305 | 142.5991 | 5.127e-04 |
| 35 | signed_hqql_tbl | mod.blocks.5 | A_Hqql_correct | -0.0093 | 0.1104 | 112.6599 | 1.919e-04 |
| 36 | B_tbl_minus_hqql | mod.blocks.5 | B_Hqql_to_Tbl | -0.0055 | 0.1061 | 139.2195 | 4.692e-04 |
| 37 | signed_hqql_tbl | mod.blocks.5 | B_Hqql_to_Tbl | -0.0055 | 0.1061 | 131.4601 | 3.769e-04 |
| 38 | signed_hqql_tbl | mod.blocks.5 | D_Tbl_to_Hqql | -0.0075 | 0.0978 | 141.7128 | 3.754e-04 |
| 39 | signed_hqql_tbl | mod.blocks.6 | B_Hqql_to_Tbl | 0.0019 | 0.1071 | 172.7771 | 2.317e-04 |
| 40 | B_tbl_minus_hqql | mod.blocks.6 | B_Hqql_to_Tbl | 0.0019 | 0.1071 | 182.9139 | 2.853e-04 |

## Top role-level residual contributions
| rank | objective | module | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | muon | -0.0574 | 0.0703 |
| 2 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | electron | -0.0538 | 0.0645 |
| 3 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | electron | -0.0372 | 0.0410 |
| 4 | signed_hqql_tbl | mod.blocks.1 | A_Hqql_correct | muon | -0.0348 | 0.0410 |
| 5 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | muon | -0.0281 | 0.0548 |
| 6 | B_tbl_minus_hqql | mod.blocks.0 | B_Hqql_to_Tbl | electron | 0.0238 | 0.0384 |
| 7 | signed_hqql_tbl | mod.blocks.0 | B_Hqql_to_Tbl | electron | 0.0238 | 0.0384 |
| 8 | signed_hqql_tbl | mod.blocks.1 | C_Tbl_correct | muon | -0.0249 | 0.0306 |
| 9 | signed_hqql_tbl | mod.blocks.1 | C_Tbl_correct | electron | -0.0209 | 0.0279 |
| 10 | signed_hqql_tbl | mod.blocks.2 | C_Tbl_correct | muon | -0.0212 | 0.0251 |
| 11 | signed_hqql_tbl | mod.blocks.0 | D_Tbl_to_Hqql | electron | -0.0183 | 0.0350 |
| 12 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | charged_hadron | -0.0187 | 0.0191 |
| 13 | signed_hqql_tbl | mod.blocks.6 | A_Hqql_correct | muon | 0.0187 | 0.0187 |
| 14 | signed_hqql_tbl | mod.blocks.6 | A_Hqql_correct | electron | 0.0175 | 0.0201 |
| 15 | signed_hqql_tbl | mod.blocks.1 | A_Hqql_correct | electron | -0.0158 | 0.0217 |
| 16 | B_tbl_minus_hqql | mod.blocks.1 | B_Hqql_to_Tbl | electron | 0.0143 | 0.0250 |
| 17 | signed_hqql_tbl | mod.blocks.1 | B_Hqql_to_Tbl | electron | 0.0143 | 0.0250 |
| 18 | signed_hqql_tbl | mod.blocks.2 | A_Hqql_correct | muon | -0.0149 | 0.0221 |
| 19 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | charged_hadron | 0.0154 | 0.0154 |
| 20 | signed_hqql_tbl | mod.blocks.7 | A_Hqql_correct | electron | 0.0128 | 0.0181 |
| 21 | signed_hqql_tbl | mod.blocks.7 | A_Hqql_correct | muon | 0.0133 | 0.0150 |
| 22 | signed_hqql_tbl | mod.blocks.2 | A_Hqql_correct | electron | -0.0112 | 0.0170 |
| 23 | signed_hqql_tbl | mod.blocks.3 | A_Hqql_correct | muon | 0.0098 | 0.0223 |
| 24 | signed_hqql_tbl | mod.blocks.3 | C_Tbl_correct | muon | -0.0067 | 0.0338 |
| 25 | signed_hqql_tbl | mod.blocks.2 | C_Tbl_correct | electron | -0.0102 | 0.0199 |
| 26 | signed_hqql_tbl | mod.blocks.1 | D_Tbl_to_Hqql | electron | -0.0101 | 0.0190 |
| 27 | signed_hqql_tbl | mod.blocks.4 | C_Tbl_correct | muon | -0.0093 | 0.0194 |
| 28 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | muon | 0.0056 | 0.0339 |
| 29 | B_tbl_minus_hqql | mod.blocks.7 | B_Hqql_to_Tbl | electron | -0.0096 | 0.0153 |
| 30 | signed_hqql_tbl | mod.blocks.7 | B_Hqql_to_Tbl | electron | -0.0096 | 0.0153 |
| 31 | signed_hqql_tbl | mod.blocks.3 | C_Tbl_correct | electron | -0.0062 | 0.0277 |
| 32 | signed_hqql_tbl | mod.blocks.4 | A_Hqql_correct | muon | 0.0102 | 0.0112 |
| 33 | signed_hqql_tbl | mod.blocks.1 | C_Tbl_correct | charged_hadron | -0.0103 | 0.0108 |
| 34 | signed_hqql_tbl | mod.blocks.4 | C_Tbl_correct | electron | -0.0084 | 0.0178 |
| 35 | signed_hqql_tbl | mod.blocks.7 | D_Tbl_to_Hqql | electron | 0.0102 | 0.0102 |
| 36 | B_tbl_minus_hqql | mod.blocks.7 | B_Hqql_to_Tbl | muon | -0.0081 | 0.0170 |
| 37 | signed_hqql_tbl | mod.blocks.7 | B_Hqql_to_Tbl | muon | -0.0081 | 0.0170 |
| 38 | signed_hqql_tbl | mod.blocks.7 | A_Hqql_correct | charged_hadron | 0.0096 | 0.0107 |
| 39 | B_tbl_minus_hqql | mod.blocks.0 | B_Hqql_to_Tbl | muon | -0.0034 | 0.0344 |
| 40 | signed_hqql_tbl | mod.blocks.0 | B_Hqql_to_Tbl | muon | -0.0034 | 0.0344 |
| 41 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | electron | 0.0063 | 0.0226 |
| 42 | B_tbl_minus_hqql | mod.blocks.6 | B_Hqql_to_Tbl | electron | -0.0093 | 0.0099 |
| 43 | signed_hqql_tbl | mod.blocks.6 | B_Hqql_to_Tbl | electron | -0.0093 | 0.0099 |
| 44 | signed_hqql_tbl | mod.blocks.7 | D_Tbl_to_Hqql | muon | 0.0085 | 0.0126 |
| 45 | signed_hqql_tbl | mod.blocks.0 | D_Tbl_to_Hqql | muon | -0.0047 | 0.0275 |
| 46 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | photon | 0.0090 | 0.0090 |
| 47 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | neutral_hadron | -0.0073 | 0.0122 |
| 48 | signed_hqql_tbl | mod.blocks.5 | D_Tbl_to_Hqql | muon | -0.0073 | 0.0119 |
| 49 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | charged_hadron | -0.0075 | 0.0101 |
| 50 | B_tbl_minus_hqql | mod.blocks.6 | B_Hqql_to_Tbl | muon | -0.0075 | 0.0098 |
| 51 | signed_hqql_tbl | mod.blocks.6 | B_Hqql_to_Tbl | muon | -0.0075 | 0.0098 |
| 52 | signed_hqql_tbl | mod.blocks.1 | A_Hqql_correct | charged_hadron | -0.0077 | 0.0084 |
| 53 | signed_hqql_tbl | mod.blocks.2 | B_Hqql_to_Tbl | electron | 0.0070 | 0.0109 |
| 54 | B_tbl_minus_hqql | mod.blocks.2 | B_Hqql_to_Tbl | electron | 0.0070 | 0.0109 |
| 55 | signed_hqql_tbl | mod.blocks.3 | A_Hqql_correct | electron | 0.0054 | 0.0161 |
| 56 | signed_hqql_tbl | mod.blocks.3 | B_Hqql_to_Tbl | electron | -0.0055 | 0.0158 |
| 57 | B_tbl_minus_hqql | mod.blocks.3 | B_Hqql_to_Tbl | electron | -0.0055 | 0.0158 |
| 58 | signed_hqql_tbl | mod.blocks.6 | D_Tbl_to_Hqql | electron | 0.0072 | 0.0082 |
| 59 | signed_hqql_tbl | mod.blocks.5 | A_Hqql_correct | electron | -0.0062 | 0.0102 |
| 60 | signed_hqql_tbl | mod.blocks.6 | D_Tbl_to_Hqql | muon | 0.0064 | 0.0089 |
| 61 | signed_hqql_tbl | mod.blocks.7 | A_Hqql_correct | photon | 0.0066 | 0.0071 |
| 62 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | photon | -0.0061 | 0.0088 |
| 63 | signed_hqql_tbl | mod.blocks.0 | A_Hqql_correct | neutral_hadron | -0.0051 | 0.0116 |
| 64 | signed_hqql_tbl | mod.blocks.2 | C_Tbl_correct | charged_hadron | -0.0062 | 0.0070 |
| 65 | signed_hqql_tbl | mod.blocks.6 | C_Tbl_correct | muon | -0.0044 | 0.0129 |
| 66 | signed_hqql_tbl | mod.blocks.0 | C_Tbl_correct | photon | -0.0054 | 0.0084 |
| 67 | signed_hqql_tbl | mod.blocks.2 | A_Hqql_correct | charged_hadron | -0.0058 | 0.0067 |
| 68 | signed_hqql_tbl | mod.blocks.5 | C_Tbl_correct | electron | 0.0046 | 0.0114 |
| 69 | signed_hqql_tbl | mod.blocks.1 | A_Hqql_correct | photon | -0.0056 | 0.0072 |
| 70 | signed_hqql_tbl | mod.blocks.5 | A_Hqql_correct | muon | -0.0051 | 0.0090 |
| 71 | signed_hqql_tbl | mod.blocks.7 | C_Tbl_correct | neutral_hadron | 0.0055 | 0.0065 |
| 72 | signed_hqql_tbl | mod.blocks.3 | D_Tbl_to_Hqql | muon | 0.0037 | 0.0133 |
| 73 | signed_hqql_tbl | mod.blocks.6 | C_Tbl_correct | charged_hadron | 0.0054 | 0.0059 |
| 74 | signed_hqql_tbl | mod.blocks.4 | D_Tbl_to_Hqql | electron | 0.0047 | 0.0069 |
| 75 | signed_hqql_tbl | mod.blocks.2 | B_Hqql_to_Tbl | neutral_hadron | -0.0049 | 0.0058 |
| 76 | B_tbl_minus_hqql | mod.blocks.2 | B_Hqql_to_Tbl | neutral_hadron | -0.0049 | 0.0058 |
| 77 | B_tbl_minus_hqql | mod.blocks.3 | B_Hqql_to_Tbl | muon | 0.0030 | 0.0128 |
| 78 | signed_hqql_tbl | mod.blocks.3 | B_Hqql_to_Tbl | muon | 0.0030 | 0.0128 |
| 79 | signed_hqql_tbl | mod.blocks.2 | D_Tbl_to_Hqql | electron | -0.0029 | 0.0134 |
| 80 | signed_hqql_tbl | mod.blocks.7 | B_Hqql_to_Tbl | photon | 0.0047 | 0.0057 |

## Formula

```text
R_l = block_l(X_l) - X_l
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
