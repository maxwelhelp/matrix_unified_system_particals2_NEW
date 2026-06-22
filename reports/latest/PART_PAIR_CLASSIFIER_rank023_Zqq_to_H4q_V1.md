# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **264**
- src_label: `label_Zqq`
- tgt_label: `label_H4q`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.7398 | 1.8723 | 12.2446 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.7398 | 1.8723 | 12.2446 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.6565 | 2.2520 | 4.2863 | 0.7775 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.6565 | 2.2520 | 4.2863 | 0.7775 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.5744 | 1.9772 | 3.8576 | 0.7775 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.5744 | 1.9772 | 3.8576 | 0.7775 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.4910 | 1.6211 | 11.2283 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.4910 | 1.6211 | 11.2283 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.6155 | 1.0897 | 10.8086 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.6155 | 1.0897 | 10.8086 | 0.3536 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.5322 | 1.4156 | 3.2536 | 0.7775 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.5322 | 1.4156 | 3.2536 | 0.7775 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4450 | 1.4912 | 3.2597 | 0.7775 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4450 | 1.4912 | 3.2597 | 0.7775 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4450 | 1.4912 | 3.2597 | 0.7775 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4450 | 1.4912 | 3.2597 | 0.7775 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3617 | 1.1828 | 11.3000 | 0.3536 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3617 | 1.1828 | 11.3000 | 0.3536 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3617 | 1.1828 | 11.3000 | 0.3536 |
| 20 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3617 | 1.1828 | 11.3000 | 0.3536 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 4 | 0.8022 | 0.9346 | -3.2086 | -0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 4 | 0.8022 | 0.9346 | -3.2086 | -0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.8113 | 0.8113 | -2.1342 | -0.3801 |
| 8 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.8113 | 0.8113 | -2.1342 | -0.3801 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.7493 | 0.7493 | 2.9971 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.7493 | 0.7493 | 2.9971 | 0.2500 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.7493 | 0.7493 | 2.9971 | 0.2500 |
| 12 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.7493 | 0.7493 | 2.9971 | 0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.6412 | 0.6807 | 1.6867 | 0.3801 |
| 14 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.6412 | 0.6807 | 1.6867 | 0.3801 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | 0.6458 | 0.6458 | 2.5831 | 0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | 0.6458 | 0.6458 | 2.5831 | 0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.5697 | 0.5697 | -2.2187 | -0.2568 |
| 18 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.5697 | 0.5697 | -2.2187 | -0.2568 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.4501 | 0.4600 | -1.1841 | -0.3801 |
| 20 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.4501 | 0.4600 | -1.1841 | -0.3801 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.4501 | 0.4600 | -1.1841 | -0.3801 |
| 22 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.4501 | 0.4600 | -1.1841 | -0.3801 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.4440 | 0.4456 | -1.7290 | -0.2568 |
| 24 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.4440 | 0.4456 | -1.7290 | -0.2568 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.3876 | 0.4335 | 1.5504 | -0.2500 |
| 26 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.3876 | 0.4335 | 1.5504 | -0.2500 |
| 27 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | -0.3876 | 0.4335 | 1.5504 | -0.2500 |
| 28 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | -0.3876 | 0.4335 | 1.5504 | -0.2500 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.2424 | 0.2650 | 0.8830 | 0.2745 |
| 30 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.2424 | 0.2650 | 0.8830 | 0.2745 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.1922 | 0.2786 | -0.7483 | 0.2568 |
| 32 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.1922 | 0.2786 | -0.7483 | 0.2568 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.1922 | 0.2786 | -0.7483 | 0.2568 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.1922 | 0.2786 | -0.7483 | 0.2568 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.1980 | 0.2357 | 0.7394 | 0.2678 |
| 36 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.1980 | 0.2357 | 0.7394 | 0.2678 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.1660 | 0.2241 | -0.6199 | -0.2678 |
| 38 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.1660 | 0.2241 | -0.6199 | -0.2678 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1334 | 0.1334 | -0.9510 | -0.1403 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1334 | 0.1334 | -0.9510 | -0.1403 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.1314 | 0.1314 | -0.6128 | -0.2145 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.1314 | 0.1314 | -0.6128 | -0.2145 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.1154 | 0.1226 | -0.8231 | -0.1403 |
| 44 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.1154 | 0.1226 | -0.8231 | -0.1403 |
| 45 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.1154 | 0.1226 | -0.8231 | -0.1403 |
| 46 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.1154 | 0.1226 | -0.8231 | -0.1403 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | -0.1087 | 0.1247 | -0.7747 | 0.1403 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | -0.1087 | 0.1247 | -0.7747 | 0.1403 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0696 | 0.3169 | 0.1830 | 0.3801 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0696 | 0.3169 | 0.1830 | 0.3801 |
| 51 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 4 | -0.0302 | 0.4439 | 0.1210 | -0.2500 |
| 52 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 4 | -0.0302 | 0.4439 | 0.1210 | -0.2500 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | -0.0946 | 0.0995 | -0.4413 | 0.2145 |
| 54 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | -0.0946 | 0.0995 | -0.4413 | 0.2145 |
| 55 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | -0.0946 | 0.0995 | -0.4413 | 0.2145 |
| 56 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | -0.0946 | 0.0995 | -0.4413 | 0.2145 |
| 57 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | 0.0647 | 0.1948 | -0.2589 | -0.2500 |
| 58 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | 0.0647 | 0.1948 | -0.2589 | -0.2500 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0749 | 0.1244 | 0.2730 | 0.2745 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0749 | 0.1244 | 0.2730 | 0.2745 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0749 | 0.1244 | 0.2730 | 0.2745 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0749 | 0.1244 | 0.2730 | 0.2745 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.0629 | 0.1393 | -0.2292 | -0.2745 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.0629 | 0.1393 | -0.2292 | -0.2745 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | 0.0728 | 0.0839 | -0.3395 | -0.2145 |
| 66 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | 0.0728 | 0.0839 | -0.3395 | -0.2145 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.0705 | 0.0857 | -0.3878 | -0.1817 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.0705 | 0.0857 | -0.3878 | -0.1817 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0460 | 0.1308 | -0.1674 | -0.2745 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0460 | 0.1308 | -0.1674 | -0.2745 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | -0.0369 | 0.1755 | -0.1438 | 0.2568 |
| 72 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | -0.0369 | 0.1755 | -0.1438 | 0.2568 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.0574 | 0.0642 | 0.3157 | 0.1817 |
| 74 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.0574 | 0.0642 | 0.3157 | 0.1817 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0527 | 0.0845 | -0.2903 | 0.1817 |
| 76 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0527 | 0.0845 | -0.2903 | 0.1817 |
| 77 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0527 | 0.0845 | -0.2903 | 0.1817 |
| 78 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0527 | 0.0845 | -0.2903 | 0.1817 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0484 | 0.1037 | 0.1806 | 0.2678 |
| 80 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0484 | 0.1037 | 0.1806 | 0.2678 |
| 81 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0484 | 0.1037 | 0.1806 | 0.2678 |
| 82 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0484 | 0.1037 | 0.1806 | 0.2678 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0517 | 0.0693 | -0.3123 | -0.1656 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0517 | 0.0693 | -0.3123 | -0.1656 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | -0.0526 | 0.0526 | 0.5276 | -0.0996 |
| 86 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | -0.0526 | 0.0526 | 0.5276 | -0.0996 |
| 87 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | -0.0526 | 0.0526 | 0.5276 | -0.0996 |
| 88 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | -0.0526 | 0.0526 | 0.5276 | -0.0996 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0486 | 0.0486 | 0.2462 | 0.1974 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0486 | 0.0486 | 0.2462 | 0.1974 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0486 | 0.0486 | 0.4877 | 0.0996 |
| 92 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0486 | 0.0486 | 0.4877 | 0.0996 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0440 | 0.0674 | -0.3012 | -0.1460 |
| 94 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0440 | 0.0674 | -0.3012 | -0.1460 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | 0.0454 | 0.0454 | 0.4557 | 0.0996 |
| 96 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | 0.0454 | 0.0454 | 0.4557 | 0.0996 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.0408 | 0.0408 | 1.1692 | -0.0349 |
| 98 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.0408 | 0.0408 | 1.1692 | -0.0349 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0371 | 0.0586 | -0.1881 | -0.1974 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0371 | 0.0586 | -0.1881 | -0.1974 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 8 | label_Zqq | label_H4q | -1.5206 | -0.3334 |
| 2 | mod.fc.0 | 3 | label_Zqq | label_H4q | 1.0979 | -0.3334 |
| 3 | mod.fc.0 | 121 | label_Zqq | label_H4q | 1.0711 | -0.3334 |
| 4 | mod.fc.0 | 103 | label_Zqq | label_H4q | 1.0272 | -0.3334 |
| 5 | mod.fc.0 | 66 | label_Zqq | label_H4q | 0.8579 | -0.3334 |
| 6 | mod.fc.0 | 45 | label_Zqq | label_H4q | 0.7896 | -0.3334 |
| 7 | mod.fc.0 | 18 | label_Zqq | label_H4q | 0.7268 | -0.3334 |
| 8 | mod.fc.0 | 82 | label_Zqq | label_H4q | 0.6622 | -0.3334 |
| 9 | mod.fc.0 | 76 | label_Zqq | label_H4q | -0.5838 | -0.3334 |
| 10 | mod.fc.0 | 57 | label_Zqq | label_H4q | -0.5611 | -0.3334 |
| 11 | mod.fc.0 | 54 | label_Zqq | label_H4q | 0.5277 | -0.3334 |
| 12 | mod.fc.0 | 91 | label_Zqq | label_H4q | -0.4830 | -0.3334 |
| 13 | mod.fc.0 | 124 | label_Zqq | label_H4q | -0.4042 | -0.3334 |
| 14 | mod.fc.0 | 2 | label_Zqq | label_H4q | -0.3984 | -0.3334 |
| 15 | mod.fc.0 | 23 | label_Zqq | label_H4q | -0.2544 | -0.3334 |
| 16 | mod.fc.0 | 96 | label_Zqq | label_H4q | -0.1415 | -0.3334 |
| 17 | mod.fc.0 | 10 | label_Zqq | label_H4q | 0.1396 | -0.3334 |
| 18 | mod.fc.0 | 58 | label_Zqq | label_H4q | -0.1301 | -0.3334 |
| 19 | mod.fc.0 | 34 | label_Zqq | label_H4q | 0.0790 | -0.3334 |
| 20 | mod.fc.0 | 6 | label_Zqq | label_H4q | -0.0619 | -0.3334 |
| 21 | mod.fc.0 | 79 | label_Zqq | label_H4q | 0.0395 | -0.3334 |
| 22 | mod.fc.0 | 123 | label_Zqq | label_H4q | 0.0384 | -0.3334 |
| 23 | mod.fc.0 | 80 | label_Zqq | label_H4q | 0.0337 | -0.3334 |
| 24 | mod.fc.0 | 110 | label_Zqq | label_H4q | 0.0242 | -0.3334 |
| 25 | mod.fc.0 | 78 | label_Zqq | label_H4q | 7.383e-04 | -0.3334 |
| 26 | mod.fc.0 | 118 | label_Zqq | label_H4q | 4.511e-05 | -0.3334 |
| 27 | mod.fc.0 | 38 | label_Zqq | label_H4q | -3.120e-05 | -0.3334 |
| 28 | mod.fc.0 | 115 | label_Zqq | label_H4q | -2.936e-05 | -0.3334 |
| 29 | mod.fc.0 | 119 | label_Zqq | label_H4q | 2.261e-05 | -0.3334 |
| 30 | mod.fc.0 | 51 | label_Zqq | label_H4q | 2.230e-05 | -0.3334 |
| 31 | mod.fc.0 | 4 | label_Zqq | label_H4q | -2.074e-05 | -0.3334 |
| 32 | mod.fc.0 | 109 | label_Zqq | label_H4q | 1.528e-05 | -0.3334 |
| 33 | mod.fc.0 | 49 | label_Zqq | label_H4q | -1.511e-05 | -0.3334 |
| 34 | mod.fc.0 | 46 | label_Zqq | label_H4q | -1.294e-05 | -0.3334 |
| 35 | mod.fc.0 | 127 | label_Zqq | label_H4q | -1.196e-05 | -0.3334 |
| 36 | mod.fc.0 | 98 | label_Zqq | label_H4q | 1.046e-05 | -0.3334 |
| 37 | mod.fc.0 | 89 | label_Zqq | label_H4q | -1.009e-05 | -0.3334 |
| 38 | mod.fc.0 | 106 | label_Zqq | label_H4q | -9.833e-06 | -0.3334 |
| 39 | mod.fc.0 | 68 | label_Zqq | label_H4q | -9.786e-06 | -0.3334 |
| 40 | mod.fc.0 | 105 | label_Zqq | label_H4q | 9.671e-06 | -0.3334 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
