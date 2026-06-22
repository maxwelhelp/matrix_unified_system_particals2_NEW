# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **262**
- src_label: `label_Hqql`
- tgt_label: `label_Tbl`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 2.3647 | 5.1216 | 17.3872 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 2.3647 | 5.1216 | 17.3872 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 2.5323 | 2.6776 | 5.4525 | 0.8304 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 2.5323 | 2.6776 | 5.4525 | 0.8304 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.7242 | 4.4175 | 14.8894 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.7242 | 4.4175 | 14.8894 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.5566 | 2.1558 | 4.8828 | 0.8304 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.5566 | 2.1558 | 4.8828 | 0.8304 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.5242 | 4.3669 | 13.3469 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.5242 | 4.3669 | 13.3469 | 0.3536 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4439 | 4.4621 | 13.9217 | 0.3536 |
| 12 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4439 | 4.4621 | 13.9217 | 0.3536 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4439 | 4.4621 | 13.9217 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4439 | 4.4621 | 13.9217 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6114 | 1.2690 | 3.9826 | 0.8304 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6114 | 1.2690 | 3.9826 | 0.8304 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6114 | 1.2690 | 3.9826 | 0.8304 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6114 | 1.2690 | 3.9826 | 0.8304 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3567 | 1.2878 | 3.9812 | 0.8304 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3567 | 1.2878 | 3.9812 | 0.8304 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 9 | 3.7369 | 3.7369 | 14.9478 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 9 | 3.7369 | 3.7369 | 14.9478 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 5 | 3.0286 | 3.0286 | 12.1144 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 5 | 3.0286 | 3.0286 | 12.1144 | 0.2500 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 9 | 2.4530 | 2.4530 | 9.8119 | 0.2500 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 9 | 2.4530 | 2.4530 | 9.8119 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 9 | 2.4530 | 2.4530 | 9.8119 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 9 | 2.4530 | 2.4530 | 9.8119 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 5 | 2.4456 | 2.4456 | 9.7823 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 5 | 2.4456 | 2.4456 | 9.7823 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 5 | -2.0091 | 2.0091 | 8.0365 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 5 | -2.0091 | 2.0091 | 8.0365 | -0.2500 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 5 | -2.0091 | 2.0091 | 8.0365 | -0.2500 |
| 14 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 5 | -2.0091 | 2.0091 | 8.0365 | -0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 9 | -1.9213 | 1.9213 | 7.6853 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 9 | -1.9213 | 1.9213 | 7.6853 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 5 | -1.3722 | 1.3847 | 5.4888 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 5 | -1.3722 | 1.3847 | 5.4888 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 9 | -1.3044 | 1.3889 | 5.2177 | -0.2500 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 9 | -1.3044 | 1.3889 | 5.2177 | -0.2500 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.7079 | 0.7079 | -2.2626 | -0.3129 |
| 22 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.7079 | 0.7079 | -2.2626 | -0.3129 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.5899 | 0.5899 | 1.8853 | 0.3129 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.5899 | 0.5899 | 1.8853 | 0.3129 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.5700 | 0.5700 | -1.6118 | -0.3536 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.5700 | 0.5700 | -1.6118 | -0.3536 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.4271 | 0.5014 | 1.2077 | 0.3536 |
| 28 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.4271 | 0.5014 | 1.2077 | 0.3536 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 54 | 0.3825 | 0.3825 | -0.9018 | -0.4241 |
| 30 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 54 | 0.3825 | 0.3825 | -0.9018 | -0.4241 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.3503 | 0.3826 | -0.9906 | -0.3536 |
| 32 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.3503 | 0.3826 | -0.9906 | -0.3536 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.3211 | 0.3211 | -1.0125 | -0.3172 |
| 34 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.3211 | 0.3211 | -1.0125 | -0.3172 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.2217 | 0.2328 | -0.7086 | -0.3129 |
| 36 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.2217 | 0.2328 | -0.7086 | -0.3129 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.2080 | 0.2080 | 0.8513 | 0.2444 |
| 38 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.2080 | 0.2080 | 0.8513 | 0.2444 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1878 | 0.1878 | 1.5916 | 0.1180 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1878 | 0.1878 | 1.5916 | 0.1180 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1784 | 0.1784 | -0.5624 | -0.3172 |
| 42 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1784 | 0.1784 | -0.5624 | -0.3172 |
| 43 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.1784 | 0.1784 | -0.5624 | -0.3172 |
| 44 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.1784 | 0.1784 | -0.5624 | -0.3172 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.1670 | 0.1837 | 0.5264 | 0.3172 |
| 46 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.1670 | 0.1837 | 0.5264 | 0.3172 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 54 | 0.1519 | 0.1519 | 0.3581 | 0.4241 |
| 48 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 54 | 0.1519 | 0.1519 | 0.3581 | 0.4241 |
| 49 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 54 | 0.1506 | 0.1506 | -0.3551 | -0.4241 |
| 50 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 54 | 0.1506 | 0.1506 | -0.3551 | -0.4241 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 54 | 0.1506 | 0.1506 | -0.3551 | -0.4241 |
| 52 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 54 | 0.1506 | 0.1506 | -0.3551 | -0.4241 |
| 53 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.1362 | 0.1423 | 0.5573 | 0.2444 |
| 54 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.1362 | 0.1423 | 0.5573 | 0.2444 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.1362 | 0.1423 | 0.5573 | 0.2444 |
| 56 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.1362 | 0.1423 | 0.5573 | 0.2444 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.1133 | 0.1133 | -2.6541 | -0.0427 |
| 58 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.1133 | 0.1133 | -2.6541 | -0.0427 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0894 | 0.2058 | -0.2857 | 0.3129 |
| 60 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0894 | 0.2058 | -0.2857 | 0.3129 |
| 61 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0894 | 0.2058 | -0.2857 | 0.3129 |
| 62 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0894 | 0.2058 | -0.2857 | 0.3129 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | -0.1013 | 0.1013 | -2.3721 | 0.0427 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | -0.1013 | 0.1013 | -2.3721 | 0.0427 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0968 | 0.0968 | 1.6642 | 0.0582 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0968 | 0.0968 | 1.6642 | 0.0582 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0965 | 0.0965 | -2.2615 | 0.0427 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0965 | 0.0965 | -2.2615 | 0.0427 |
| 69 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0929 | 0.0929 | -2.1763 | -0.0427 |
| 70 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0929 | 0.0929 | -2.1763 | -0.0427 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0929 | 0.0929 | -2.1763 | -0.0427 |
| 72 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0929 | 0.0929 | -2.1763 | -0.0427 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0791 | 0.1606 | -0.2236 | 0.3536 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0791 | 0.1606 | -0.2236 | 0.3536 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0791 | 0.1606 | -0.2236 | 0.3536 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0791 | 0.1606 | -0.2236 | 0.3536 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0880 | 0.1091 | -0.3603 | -0.2444 |
| 78 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0880 | 0.1091 | -0.3603 | -0.2444 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | -0.0870 | 0.1011 | 0.3560 | -0.2444 |
| 80 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | -0.0870 | 0.1011 | 0.3560 | -0.2444 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.0840 | 0.0840 | -0.9637 | -0.0872 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.0840 | 0.0840 | -0.9637 | -0.0872 |
| 83 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0734 | 0.0734 | 0.6220 | 0.1180 |
| 84 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0734 | 0.0734 | 0.6220 | 0.1180 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0734 | 0.0734 | 0.6220 | 0.1180 |
| 86 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0734 | 0.0734 | 0.6220 | 0.1180 |
| 87 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0703 | 0.0838 | 1.2083 | 0.0582 |
| 88 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0703 | 0.0838 | 1.2083 | 0.0582 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.0703 | 0.0838 | 1.2083 | 0.0582 |
| 90 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.0703 | 0.0838 | 1.2083 | 0.0582 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0637 | 0.0637 | -0.7309 | -0.0872 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0637 | 0.0637 | -0.7309 | -0.0872 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.0637 | 0.0637 | -0.7309 | -0.0872 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.0637 | 0.0637 | -0.7309 | -0.0872 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.0612 | 0.0622 | -0.7012 | 0.0872 |
| 96 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.0612 | 0.0622 | -0.7012 | 0.0872 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0589 | 0.0589 | -0.4889 | -0.1205 |
| 98 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0589 | 0.0589 | -0.4889 | -0.1205 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0588 | 0.0588 | 0.4880 | 0.1205 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0588 | 0.0588 | 0.4880 | 0.1205 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 54 | label_Hqql | label_Tbl | -1.6964 | -0.6703 |
| 2 | mod.fc.0 | 76 | label_Hqql | label_Tbl | 1.4146 | -0.6703 |
| 3 | mod.fc.0 | 18 | label_Hqql | label_Tbl | -1.2686 | -0.6703 |
| 4 | mod.fc.0 | 103 | label_Hqql | label_Tbl | 1.2515 | -0.6703 |
| 5 | mod.fc.0 | 121 | label_Hqql | label_Tbl | 0.9775 | -0.6703 |
| 6 | mod.fc.0 | 96 | label_Hqql | label_Tbl | -0.7730 | -0.6703 |
| 7 | mod.fc.0 | 58 | label_Hqql | label_Tbl | 0.5745 | -0.6703 |
| 8 | mod.fc.0 | 23 | label_Hqql | label_Tbl | 0.5696 | -0.6703 |
| 9 | mod.fc.0 | 45 | label_Hqql | label_Tbl | -0.4822 | -0.6703 |
| 10 | mod.fc.0 | 57 | label_Hqql | label_Tbl | 0.4719 | -0.6703 |
| 11 | mod.fc.0 | 10 | label_Hqql | label_Tbl | -0.3489 | -0.6703 |
| 12 | mod.fc.0 | 8 | label_Hqql | label_Tbl | 0.2327 | -0.6703 |
| 13 | mod.fc.0 | 2 | label_Hqql | label_Tbl | 0.2039 | -0.6703 |
| 14 | mod.fc.0 | 91 | label_Hqql | label_Tbl | 0.1842 | -0.6703 |
| 15 | mod.fc.0 | 34 | label_Hqql | label_Tbl | -0.1708 | -0.6703 |
| 16 | mod.fc.0 | 79 | label_Hqql | label_Tbl | -0.1077 | -0.6703 |
| 17 | mod.fc.0 | 6 | label_Hqql | label_Tbl | 0.0887 | -0.6703 |
| 18 | mod.fc.0 | 66 | label_Hqql | label_Tbl | 0.0838 | -0.6703 |
| 19 | mod.fc.0 | 3 | label_Hqql | label_Tbl | 0.0658 | -0.6703 |
| 20 | mod.fc.0 | 80 | label_Hqql | label_Tbl | -0.0510 | -0.6703 |
| 21 | mod.fc.0 | 110 | label_Hqql | label_Tbl | -0.0399 | -0.6703 |
| 22 | mod.fc.0 | 123 | label_Hqql | label_Tbl | 0.0129 | -0.6703 |
| 23 | mod.fc.0 | 124 | label_Hqql | label_Tbl | 0.0039 | -0.6703 |
| 24 | mod.fc.0 | 82 | label_Hqql | label_Tbl | 0.0031 | -0.6703 |
| 25 | mod.fc.0 | 78 | label_Hqql | label_Tbl | -0.0022 | -0.6703 |
| 26 | mod.fc.0 | 115 | label_Hqql | label_Tbl | -3.447e-04 | -0.6703 |
| 27 | mod.fc.0 | 49 | label_Hqql | label_Tbl | -2.977e-05 | -0.6703 |
| 28 | mod.fc.0 | 118 | label_Hqql | label_Tbl | 2.434e-05 | -0.6703 |
| 29 | mod.fc.0 | 87 | label_Hqql | label_Tbl | 2.198e-05 | -0.6703 |
| 30 | mod.fc.0 | 74 | label_Hqql | label_Tbl | -1.706e-05 | -0.6703 |
| 31 | mod.fc.0 | 125 | label_Hqql | label_Tbl | 1.705e-05 | -0.6703 |
| 32 | mod.fc.0 | 111 | label_Hqql | label_Tbl | 1.638e-05 | -0.6703 |
| 33 | mod.fc.0 | 70 | label_Hqql | label_Tbl | -1.551e-05 | -0.6703 |
| 34 | mod.fc.0 | 50 | label_Hqql | label_Tbl | 1.345e-05 | -0.6703 |
| 35 | mod.fc.0 | 15 | label_Hqql | label_Tbl | -1.341e-05 | -0.6703 |
| 36 | mod.fc.0 | 81 | label_Hqql | label_Tbl | -1.294e-05 | -0.6703 |
| 37 | mod.fc.0 | 38 | label_Hqql | label_Tbl | -1.277e-05 | -0.6703 |
| 38 | mod.fc.0 | 108 | label_Hqql | label_Tbl | 1.259e-05 | -0.6703 |
| 39 | mod.fc.0 | 29 | label_Hqql | label_Tbl | 1.211e-05 | -0.6703 |
| 40 | mod.fc.0 | 61 | label_Hqql | label_Tbl | 1.161e-05 | -0.6703 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
