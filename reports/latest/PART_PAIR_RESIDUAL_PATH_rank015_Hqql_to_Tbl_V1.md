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
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.7712 | 0.7712 | 39.2950 | 0.1164 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.6055 | 0.6055 | 40.7081 | 0.0963 |
| 3 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.4979 | 1.0283 | 119.2013 | 0.0025 |
| 4 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.5364 | 0.7087 | 313.3275 | 3.390e-04 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.5124 | 0.5124 | 130.6261 | 0.0432 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.2816 | 0.8690 | 94.1115 | 7.655e-04 |
| 7 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.3438 | 0.6002 | 120.1807 | 0.0021 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3875 | 0.3875 | 140.9830 | 0.0423 |
| 9 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.3391 | 0.4887 | 263.1187 | 1.141e-04 |
| 10 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.2726 | 0.4432 | 101.9894 | 0.0019 |
| 11 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.2036 | 0.5020 | 93.4292 | 6.678e-04 |
| 12 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | -0.1232 | 0.7344 | 129.1276 | 0.0020 |
| 13 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0268 | 0.9971 | 114.2490 | 0.0021 |
| 14 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0268 | 0.9971 | 119.9582 | 0.0026 |
| 15 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.1884 | 0.2980 | 192.6078 | 6.971e-04 |
| 16 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.1832 | 0.1969 | 42.2553 | 0.0772 |
| 17 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.1371 | 0.3283 | 77.7230 | 6.150e-04 |
| 18 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1205 | 0.3940 | 316.3225 | 2.693e-04 |
| 19 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1205 | 0.3940 | 304.2197 | 2.204e-04 |
| 20 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.1162 | 0.4091 | 99.7285 | 0.0017 |
| 21 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | 0.1244 | 0.3514 | 327.1911 | 2.482e-04 |
| 22 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0889 | 0.4170 | 99.6807 | 0.0017 |
| 23 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0889 | 0.4170 | 96.5843 | 0.0013 |
| 24 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | -0.0750 | 0.4435 | 130.2830 | 0.0017 |
| 25 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1408 | 0.1675 | 39.4086 | 0.0789 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1408 | 0.1675 | 39.4086 | 0.0789 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1442 | 0.1442 | 154.2432 | 0.0397 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1442 | 0.1442 | 154.2432 | 0.0397 |
| 29 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | -0.0798 | 0.3172 | 115.0764 | 0.0014 |
| 30 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0162 | 0.5524 | 114.3143 | 0.0017 |
| 31 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | 0.0162 | 0.5524 | 119.8542 | 0.0022 |
| 32 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0534 | 0.3898 | 96.9972 | 0.0016 |
| 33 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0534 | 0.3898 | 102.2559 | 0.0019 |
| 34 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0891 | 0.2219 | 146.3628 | 2.344e-04 |
| 35 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0560 | 0.3275 | 112.5721 | 0.0011 |
| 36 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | -0.0560 | 0.3275 | 117.1678 | 0.0014 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0835 | 0.1119 | 165.0186 | 0.0373 |
| 38 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | 0.0617 | 0.1910 | 204.3970 | 5.329e-04 |
| 39 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | -0.0381 | 0.2618 | 143.5329 | 0.0011 |
| 40 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | -0.0382 | 0.2226 | 113.6565 | 3.606e-04 |
| 41 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | -0.0147 | 0.3109 | 109.8273 | 0.0016 |
| 42 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0168 | 0.2924 | 87.1138 | 5.310e-04 |
| 43 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | 0.0305 | 0.2278 | 123.3697 | 0.0011 |
| 44 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0254 | 0.2310 | 144.3529 | 0.0010 |
| 45 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | -0.0254 | 0.2310 | 137.1034 | 8.206e-04 |
| 46 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0202 | 0.2486 | 94.2933 | 4.560e-04 |
| 47 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | 0.0107 | 0.2775 | 103.6900 | 0.0014 |
| 48 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0125 | 0.2321 | 183.3398 | 5.022e-04 |
| 49 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | -0.0125 | 0.2321 | 192.2804 | 6.130e-04 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0189 | 0.1957 | 153.8905 | 8.383e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.7712 | 0.7712 | 39.2950 | 0.1164 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.6055 | 0.6055 | 40.7081 | 0.0963 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.5124 | 0.5124 | 130.6261 | 0.0432 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3875 | 0.3875 | 140.9830 | 0.0423 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.1832 | 0.1969 | 42.2553 | 0.0772 |
| 6 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1408 | 0.1675 | 39.4086 | 0.0789 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1408 | 0.1675 | 39.4086 | 0.0789 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1442 | 0.1442 | 154.2432 | 0.0397 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1442 | 0.1442 | 154.2432 | 0.0397 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0835 | 0.1119 | 165.0186 | 0.0373 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 1.0371 | 1.0371 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.9046 | 0.9046 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.7937 | 0.7937 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | electron | 0.7790 | 0.7790 |
| 5 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.7712 | 0.7712 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.6543 | 0.6543 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.6145 | 0.6145 |
| 8 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.6055 | 0.6055 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | electron | 0.5909 | 0.5909 |
| 10 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.5789 | 0.5789 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.5284 | 0.5284 |
| 12 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.5124 | 0.5124 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | muon | 0.4778 | 0.4778 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.4758 | 0.4758 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | electron | -0.4600 | 0.4600 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.3958 | 0.3958 |
| 17 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | electron | -0.3879 | 0.3879 |
| 18 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3875 | 0.3875 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3589 | 0.3589 |
| 20 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.3527 | 0.3527 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.3177 | 0.3177 |
| 22 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | muon | -0.3130 | 0.3130 |
| 23 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.2806 | 0.2806 |
| 24 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.2066 | 0.2066 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | muon | 0.2066 | 0.2066 |
| 26 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | electron | 0.1958 | 0.2142 |
| 27 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | muon | 0.1866 | 0.1866 |
| 28 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.1832 | 0.1969 |
| 29 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.1791 | 0.1791 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | muon | -0.1791 | 0.1791 |
| 31 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.1675 | 0.1675 |
| 32 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1561 | 0.1561 |
| 33 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.1561 | 0.1561 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1408 | 0.1675 |
| 35 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1408 | 0.1675 |
| 36 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1442 | 0.1442 |
| 37 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1442 | 0.1442 |
| 38 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.1339 | 0.1339 |
| 39 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | electron | -0.1339 | 0.1339 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.1225 | 0.1225 |
| 41 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | -0.1115 | 0.1252 |
| 42 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.0957 | 0.1773 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | electron | 0.0957 | 0.1773 |
| 44 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | electron | -0.1041 | 0.1243 |
| 45 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1051 | 0.1051 |
| 46 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.1051 | 0.1051 |
| 47 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0945 | 0.0951 |
| 48 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0835 | 0.1119 |
| 49 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0866 | 0.0866 |
| 50 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.0866 | 0.0866 |
| 51 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | muon | -0.0721 | 0.1037 |
| 52 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0479 | 0.1215 |
| 53 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0587 | 0.0712 |
| 54 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | muon | -0.0481 | 0.0901 |
| 55 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0525 | 0.0669 |
| 56 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | 0.0525 | 0.0669 |
| 57 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | muon | -0.0504 | 0.0707 |
| 58 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | 0.0513 | 0.0513 |
| 59 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0502 | 0.0507 |
| 60 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0441 | 0.0657 |
| 61 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0410 | 0.0603 |
| 62 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | 0.0410 | 0.0603 |
| 63 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0420 | 0.0420 |
| 64 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | -0.0359 | 0.0621 |
| 65 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0379 | 0.0402 |
| 66 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0379 | 0.0402 |
| 67 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | -0.0361 | 0.0361 |
| 68 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0322 | 0.0447 |
| 69 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0303 | 0.0461 |
| 70 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0298 | 0.0481 |
| 71 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | muon | 0.0324 | 0.0324 |
| 72 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | muon | 0.0324 | 0.0324 |
| 73 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | muon | -0.0279 | 0.0473 |
| 74 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | charged_hadron | -0.0310 | 0.0310 |
| 75 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | -0.0285 | 0.0359 |
| 76 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0289 | 0.0330 |
| 77 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0167 | 0.0753 |
| 78 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0201 | 0.0597 |
| 79 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0174 | 0.0706 |
| 80 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0214 | 0.0507 |
| 81 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0253 | 0.0271 |
| 82 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | -0.0253 | 0.0271 |
| 83 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | -0.0233 | 0.0328 |
| 84 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | 0.0218 | 0.0335 |
| 85 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | electron | -0.0217 | 0.0281 |
| 86 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | photon | 0.0226 | 0.0227 |
| 87 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | 0.0220 | 0.0220 |
| 88 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | muon | -0.0195 | 0.0308 |
| 89 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | muon | 0.0216 | 0.0216 |
| 90 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0073 | 0.0726 |
| 91 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0153 | 0.0385 |
| 92 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | muon | -0.0153 | 0.0385 |
| 93 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0170 | 0.0303 |
| 94 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0068 | 0.0653 |
| 95 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | muon | -0.0068 | 0.0653 |
| 96 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | charged_hadron | 0.0177 | 0.0201 |
| 97 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | muon | 0.0137 | 0.0339 |
| 98 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | charged_hadron | -0.0167 | 0.0171 |
| 99 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0156 | 0.0203 |
| 100 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | muon | -0.0156 | 0.0203 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
