# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **250**
- src_label: `label_Tbqq`
- tgt_label: `label_H4q`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 2.2636 | 2.4506 | 4.1993 | 0.7853 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 2.2636 | 2.4506 | 4.1993 | 0.7853 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 2.2202 | 2.4497 | 10.8305 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 2.2202 | 2.4497 | 10.8305 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.6779 | 1.8044 | 11.2283 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.6779 | 1.8044 | 11.2283 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.6344 | 2.0214 | 3.8576 | 0.7853 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.6344 | 2.0214 | 3.8576 | 0.7853 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.4730 | 1.4354 | 8.2772 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.4730 | 1.4354 | 8.2772 | 0.3536 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5212 | 1.1504 | 9.8965 | 0.3536 |
| 12 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5212 | 1.1504 | 9.8965 | 0.3536 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5212 | 1.1504 | 9.8965 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5212 | 1.1504 | 9.8965 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.5164 | 1.1032 | 2.8226 | 0.7853 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.5164 | 1.1032 | 2.8226 | 0.7853 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4778 | 1.1081 | 3.0569 | 0.7853 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4778 | 1.1081 | 3.0569 | 0.7853 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4778 | 1.1081 | 3.0569 | 0.7853 |
| 20 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4778 | 1.1081 | 3.0569 | 0.7853 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 8 | 0.9408 | 0.9408 | 3.7633 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 8 | 0.9408 | 0.9408 | 3.7633 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.7939 | 0.7939 | -2.1118 | -0.3759 |
| 8 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.7939 | 0.7939 | -2.1118 | -0.3759 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.7913 | 0.7913 | 3.1653 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.7913 | 0.7913 | 3.1653 | 0.2500 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.7913 | 0.7913 | 3.1653 | 0.2500 |
| 12 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.7913 | 0.7913 | 3.1653 | 0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.5771 | 0.5771 | -1.4905 | -0.3872 |
| 14 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.5771 | 0.5771 | -1.4905 | -0.3872 |
| 15 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.5432 | 0.5432 | 1.9006 | 0.2858 |
| 16 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.5432 | 0.5432 | 1.9006 | 0.2858 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 4 | -0.4679 | 0.4946 | 1.8715 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 4 | -0.4679 | 0.4946 | 1.8715 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.3660 | 0.3660 | 1.2807 | 0.2858 |
| 20 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.3660 | 0.3660 | 1.2807 | 0.2858 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.3660 | 0.3660 | 1.2807 | 0.2858 |
| 22 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.3660 | 0.3660 | 1.2807 | 0.2858 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.3419 | 0.3738 | 0.8830 | 0.3872 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.3419 | 0.3738 | 0.8830 | 0.3872 |
| 25 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 4 | 0.2756 | 0.5052 | -1.1026 | -0.2500 |
| 26 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 4 | 0.2756 | 0.5052 | -1.1026 | -0.2500 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.2780 | 0.3309 | 0.7394 | 0.3759 |
| 28 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.2780 | 0.3309 | 0.7394 | 0.3759 |
| 29 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | -0.2701 | 0.3590 | 1.0804 | -0.2500 |
| 30 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 8 | -0.2701 | 0.3590 | 1.0804 | -0.2500 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | -0.2701 | 0.3590 | 1.0804 | -0.2500 |
| 32 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 8 | -0.2701 | 0.3590 | 1.0804 | -0.2500 |
| 33 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 8 | 0.2516 | 0.3781 | -1.0063 | -0.2500 |
| 34 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 8 | 0.2516 | 0.3781 | -1.0063 | -0.2500 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.2647 | 0.2647 | 0.9866 | 0.2683 |
| 36 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.2647 | 0.2647 | 0.9866 | 0.2683 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.2214 | 0.2360 | -0.5890 | -0.3759 |
| 38 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.2214 | 0.2360 | -0.5890 | -0.3759 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1978 | 0.1997 | -0.8834 | -0.2239 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1978 | 0.1997 | -0.8834 | -0.2239 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.1810 | 0.1854 | 0.8106 | 0.2233 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.1810 | 0.1854 | 0.8106 | 0.2233 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.1660 | 0.1940 | -0.4287 | -0.3872 |
| 44 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.1660 | 0.1940 | -0.4287 | -0.3872 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.1551 | 0.2023 | 0.6928 | 0.2239 |
| 46 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.1551 | 0.2023 | 0.6928 | 0.2239 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.1425 | 0.2019 | -0.4987 | -0.2858 |
| 48 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.1425 | 0.2019 | -0.4987 | -0.2858 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.1266 | 0.1266 | -0.7770 | -0.1629 |
| 50 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.1266 | 0.1266 | -0.7770 | -0.1629 |
| 51 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1124 | 0.1331 | 0.4189 | 0.2683 |
| 52 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1124 | 0.1331 | 0.4189 | 0.2683 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1124 | 0.1331 | 0.4189 | 0.2683 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1124 | 0.1331 | 0.4189 | 0.2683 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0907 | 0.1152 | -0.4050 | -0.2239 |
| 56 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0907 | 0.1152 | -0.4050 | -0.2239 |
| 57 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0907 | 0.1152 | -0.4050 | -0.2239 |
| 58 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0907 | 0.1152 | -0.4050 | -0.2239 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0875 | 0.1152 | 0.3921 | 0.2233 |
| 60 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0875 | 0.1152 | 0.3921 | 0.2233 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0862 | 0.0862 | 0.7461 | 0.1156 |
| 62 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0862 | 0.0862 | 0.7461 | 0.1156 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.0828 | 0.0982 | 0.8626 | 0.0959 |
| 64 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.0828 | 0.0982 | 0.8626 | 0.0959 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.0834 | 0.0923 | 0.8694 | 0.0959 |
| 66 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.0834 | 0.0923 | 0.8694 | 0.0959 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0751 | 0.1321 | 0.2629 | -0.2858 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0751 | 0.1321 | 0.2629 | -0.2858 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0623 | 0.0974 | -0.2792 | -0.2233 |
| 70 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0623 | 0.0974 | -0.2792 | -0.2233 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.0617 | 0.0789 | 0.2299 | -0.2683 |
| 72 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.0617 | 0.0789 | 0.2299 | -0.2683 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0453 | 0.0963 | -0.1688 | -0.2683 |
| 74 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0453 | 0.0963 | -0.1688 | -0.2683 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | -0.0535 | 0.0535 | -2.1342 | 0.0251 |
| 76 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | -0.0535 | 0.0535 | -2.1342 | 0.0251 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0488 | 0.0488 | -1.9447 | 0.0251 |
| 78 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0488 | 0.0488 | -1.9447 | 0.0251 |
| 79 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.0488 | 0.0488 | -1.9447 | 0.0251 |
| 80 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.0488 | 0.0488 | -1.9447 | 0.0251 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0461 | 0.0484 | -0.2829 | -0.1629 |
| 82 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0461 | 0.0484 | -0.2829 | -0.1629 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0435 | 0.0435 | -1.7352 | -0.0251 |
| 84 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0435 | 0.0435 | -1.7352 | -0.0251 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0427 | 0.0427 | -1.7046 | -0.0251 |
| 86 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0427 | 0.0427 | -1.7046 | -0.0251 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | 0.0408 | 0.0408 | 0.3532 | 0.1156 |
| 88 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | 0.0408 | 0.0408 | 0.3532 | 0.1156 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | -0.0402 | 0.0402 | 0.3482 | -0.1156 |
| 90 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | -0.0402 | 0.0402 | 0.3482 | -0.1156 |
| 91 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | -0.0402 | 0.0402 | 0.3482 | -0.1156 |
| 92 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | -0.0402 | 0.0402 | 0.3482 | -0.1156 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0210 | 0.1290 | 0.0542 | 0.3872 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0210 | 0.1290 | 0.0542 | 0.3872 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0210 | 0.1290 | 0.0542 | 0.3872 |
| 96 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0210 | 0.1290 | 0.0542 | 0.3872 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0299 | 0.0654 | 0.1339 | -0.2233 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0299 | 0.0654 | 0.1339 | -0.2233 |
| 99 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0299 | 0.0654 | 0.1339 | -0.2233 |
| 100 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0299 | 0.0654 | 0.1339 | -0.2233 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 3 | label_Tbqq | label_H4q | 1.5487 | 0.1737 |
| 2 | mod.fc.0 | 121 | label_Tbqq | label_H4q | 1.5038 | 0.1737 |
| 3 | mod.fc.0 | 34 | label_Tbqq | label_H4q | 1.1432 | 0.1737 |
| 4 | mod.fc.0 | 10 | label_Tbqq | label_H4q | 1.0732 | 0.1737 |
| 5 | mod.fc.0 | 57 | label_Tbqq | label_H4q | -0.8956 | 0.1737 |
| 6 | mod.fc.0 | 76 | label_Tbqq | label_H4q | -0.8931 | 0.1737 |
| 7 | mod.fc.0 | 66 | label_Tbqq | label_H4q | 0.6517 | 0.1737 |
| 8 | mod.fc.0 | 2 | label_Tbqq | label_H4q | -0.4622 | 0.1737 |
| 9 | mod.fc.0 | 45 | label_Tbqq | label_H4q | 0.4417 | 0.1737 |
| 10 | mod.fc.0 | 103 | label_Tbqq | label_H4q | -0.3838 | 0.1737 |
| 11 | mod.fc.0 | 91 | label_Tbqq | label_H4q | -0.2471 | 0.1737 |
| 12 | mod.fc.0 | 123 | label_Tbqq | label_H4q | -0.1929 | 0.1737 |
| 13 | mod.fc.0 | 58 | label_Tbqq | label_H4q | -0.1652 | 0.1737 |
| 14 | mod.fc.0 | 82 | label_Tbqq | label_H4q | 0.1499 | 0.1737 |
| 15 | mod.fc.0 | 8 | label_Tbqq | label_H4q | 0.1003 | 0.1737 |
| 16 | mod.fc.0 | 18 | label_Tbqq | label_H4q | -0.0663 | 0.1737 |
| 17 | mod.fc.0 | 124 | label_Tbqq | label_H4q | 0.0518 | 0.1737 |
| 18 | mod.fc.0 | 54 | label_Tbqq | label_H4q | -0.0274 | 0.1737 |
| 19 | mod.fc.0 | 96 | label_Tbqq | label_H4q | 0.0252 | 0.1737 |
| 20 | mod.fc.0 | 80 | label_Tbqq | label_H4q | 0.0249 | 0.1737 |
| 21 | mod.fc.0 | 23 | label_Tbqq | label_H4q | 0.0233 | 0.1737 |
| 22 | mod.fc.0 | 110 | label_Tbqq | label_H4q | 0.0189 | 0.1737 |
| 23 | mod.fc.0 | 6 | label_Tbqq | label_H4q | 0.0048 | 0.1737 |
| 24 | mod.fc.0 | 79 | label_Tbqq | label_H4q | 0.0018 | 0.1737 |
| 25 | mod.fc.0 | 115 | label_Tbqq | label_H4q | -6.301e-04 | 0.1737 |
| 26 | mod.fc.0 | 78 | label_Tbqq | label_H4q | 3.634e-04 | 0.1737 |
| 27 | mod.fc.0 | 11 | label_Tbqq | label_H4q | -2.885e-05 | 0.1737 |
| 28 | mod.fc.0 | 106 | label_Tbqq | label_H4q | -2.467e-05 | 0.1737 |
| 29 | mod.fc.0 | 22 | label_Tbqq | label_H4q | -2.444e-05 | 0.1737 |
| 30 | mod.fc.0 | 119 | label_Tbqq | label_H4q | 2.199e-05 | 0.1737 |
| 31 | mod.fc.0 | 20 | label_Tbqq | label_H4q | 2.117e-05 | 0.1737 |
| 32 | mod.fc.0 | 94 | label_Tbqq | label_H4q | -1.892e-05 | 0.1737 |
| 33 | mod.fc.0 | 38 | label_Tbqq | label_H4q | 1.704e-05 | 0.1737 |
| 34 | mod.fc.0 | 109 | label_Tbqq | label_H4q | 1.285e-05 | 0.1737 |
| 35 | mod.fc.0 | 4 | label_Tbqq | label_H4q | -1.277e-05 | 0.1737 |
| 36 | mod.fc.0 | 77 | label_Tbqq | label_H4q | -1.078e-05 | 0.1737 |
| 37 | mod.fc.0 | 81 | label_Tbqq | label_H4q | -1.002e-05 | 0.1737 |
| 38 | mod.fc.0 | 40 | label_Tbqq | label_H4q | 9.911e-06 | 0.1737 |
| 39 | mod.fc.0 | 89 | label_Tbqq | label_H4q | -9.742e-06 | 0.1737 |
| 40 | mod.fc.0 | 19 | label_Tbqq | label_H4q | -9.369e-06 | 0.1737 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
