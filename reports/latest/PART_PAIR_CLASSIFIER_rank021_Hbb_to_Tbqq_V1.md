# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **268**
- src_label: `label_Hbb`
- tgt_label: `label_Tbqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.9272 | 2.2140 | 4.1993 | 0.6883 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.9272 | 2.2140 | 4.1993 | 0.6883 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.8301 | 2.2652 | 10.8305 | 0.3536 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.8301 | 2.2652 | 10.8305 | 0.3536 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.7189 | 2.5317 | 5.3393 | 0.6883 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.7189 | 2.5317 | 5.3393 | 0.6883 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.8160 | 2.0169 | 12.6692 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.8160 | 2.0169 | 12.6692 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6129 | 1.6248 | 3.6604 | 0.6883 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6129 | 1.6248 | 3.6604 | 0.6883 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6129 | 1.6248 | 3.6604 | 0.6883 |
| 12 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6129 | 1.6248 | 3.6604 | 0.6883 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5158 | 1.4792 | 9.9963 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5158 | 1.4792 | 9.9963 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5158 | 1.4792 | 9.9963 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5158 | 1.4792 | 9.9963 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3157 | 1.6794 | 9.7176 | 0.3536 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3157 | 1.6794 | 9.7176 | 0.3536 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.2186 | 1.5531 | 3.9985 | 0.6883 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.2186 | 1.5531 | 3.9985 | 0.6883 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | 0.9976 | 0.9976 | 3.9903 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | 0.9976 | 0.9976 | 3.9903 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | 0.9817 | 0.9817 | 3.9270 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 8 | 0.9817 | 0.9817 | 3.9270 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | 0.9817 | 0.9817 | 3.9270 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 8 | 0.9817 | 0.9817 | 3.9270 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 8 | -0.6819 | 0.6819 | 2.7274 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 8 | -0.6819 | 0.6819 | 2.7274 | -0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.6800 | 0.6800 | 3.2114 | 0.2117 |
| 14 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.6800 | 0.6800 | 3.2114 | 0.2117 |
| 15 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.6603 | 0.6603 | -1.7046 | -0.3874 |
| 16 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.6603 | 0.6603 | -1.7046 | -0.3874 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.5744 | 0.6447 | 1.4828 | 0.3874 |
| 18 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.5744 | 0.6447 | 1.4828 | 0.3874 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 8 | 0.4845 | 0.6854 | -1.9380 | -0.2500 |
| 20 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 8 | 0.4845 | 0.6854 | -1.9380 | -0.2500 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.4659 | 0.4975 | 1.8638 | -0.2500 |
| 22 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.4659 | 0.4975 | 1.8638 | -0.2500 |
| 23 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.4659 | 0.4975 | 1.8638 | -0.2500 |
| 24 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.4659 | 0.4975 | 1.8638 | -0.2500 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.4146 | 0.4728 | 1.4172 | 0.2926 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.4146 | 0.4728 | 1.4172 | 0.2926 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.3961 | 0.3961 | -1.4905 | -0.2657 |
| 28 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.3961 | 0.3961 | -1.4905 | -0.2657 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.3326 | 0.3425 | 1.5709 | 0.2117 |
| 30 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.3326 | 0.3425 | 1.5709 | 0.2117 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2955 | 0.2977 | 1.3957 | -0.2117 |
| 32 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2955 | 0.2977 | 1.3957 | -0.2117 |
| 33 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2955 | 0.2977 | 1.3957 | -0.2117 |
| 34 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2955 | 0.2977 | 1.3957 | -0.2117 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2652 | 0.3717 | -0.6846 | -0.3874 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2652 | 0.3717 | -0.6846 | -0.3874 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.2652 | 0.3717 | -0.6846 | -0.3874 |
| 38 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.2652 | 0.3717 | -0.6846 | -0.3874 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.2494 | 0.2494 | -0.9386 | -0.2657 |
| 40 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.2494 | 0.2494 | -0.9386 | -0.2657 |
| 41 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.2494 | 0.2494 | -0.9386 | -0.2657 |
| 42 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.2494 | 0.2494 | -0.9386 | -0.2657 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.2450 | 0.2450 | -2.1118 | -0.1160 |
| 44 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.2450 | 0.2450 | -2.1118 | -0.1160 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.1567 | 0.3025 | 0.4046 | 0.3874 |
| 46 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.1567 | 0.3025 | 0.4046 | 0.3874 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | -0.1803 | 0.1823 | -1.5543 | 0.1160 |
| 48 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | -0.1803 | 0.1823 | -1.5543 | 0.1160 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.1495 | 0.2219 | 0.5110 | 0.2926 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.1495 | 0.2219 | 0.5110 | 0.2926 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 2 | 0.1573 | 0.1573 | 0.7461 | 0.2109 |
| 52 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 2 | 0.1573 | 0.1573 | 0.7461 | 0.2109 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.1459 | 0.2067 | -0.4987 | -0.2926 |
| 54 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.1459 | 0.2067 | -0.4987 | -0.2926 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1466 | 0.1837 | -0.6923 | -0.2117 |
| 56 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1466 | 0.1837 | -0.6923 | -0.2117 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.1500 | 0.1500 | -1.2929 | -0.1160 |
| 58 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.1500 | 0.1500 | -1.2929 | -0.1160 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.1500 | 0.1500 | -1.2929 | -0.1160 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.1500 | 0.1500 | -1.2929 | -0.1160 |
| 61 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | -0.1144 | 0.3207 | 0.4576 | -0.2500 |
| 62 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | -0.1144 | 0.3207 | 0.4576 | -0.2500 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | -0.1448 | 0.1485 | -1.2485 | 0.1160 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | -0.1448 | 0.1485 | -1.2485 | 0.1160 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.1389 | 0.1389 | 1.4786 | 0.0939 |
| 66 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.1389 | 0.1389 | 1.4786 | 0.0939 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.1185 | 0.1660 | 0.4460 | 0.2657 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.1185 | 0.1660 | 0.4460 | 0.2657 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.1121 | 0.1121 | -0.7770 | -0.1443 |
| 70 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.1121 | 0.1121 | -0.7770 | -0.1443 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.0977 | 0.0977 | 1.0402 | 0.0939 |
| 72 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.0977 | 0.0977 | 1.0402 | 0.0939 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | -0.0962 | 0.0962 | -0.6666 | 0.1443 |
| 74 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | -0.0962 | 0.0962 | -0.6666 | 0.1443 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0945 | 0.0945 | -0.6545 | -0.1443 |
| 76 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0945 | 0.0945 | -0.6545 | -0.1443 |
| 77 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0945 | 0.0945 | -0.6545 | -0.1443 |
| 78 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0945 | 0.0945 | -0.6545 | -0.1443 |
| 79 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0831 | 0.0923 | 1.0290 | 0.0807 |
| 80 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0831 | 0.0923 | 1.0290 | 0.0807 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0831 | 0.0923 | 1.0290 | 0.0807 |
| 82 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0831 | 0.0923 | 1.0290 | 0.0807 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0786 | 0.0786 | 0.3726 | 0.2109 |
| 84 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0786 | 0.0786 | 0.3726 | 0.2109 |
| 85 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0786 | 0.0786 | 0.3726 | 0.2109 |
| 86 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0786 | 0.0786 | 0.3726 | 0.2109 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | -0.0785 | 0.0785 | 0.3722 | -0.2109 |
| 88 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | -0.0785 | 0.0785 | 0.3722 | -0.2109 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | -0.0694 | 0.0906 | 0.7390 | -0.0939 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | -0.0694 | 0.0906 | 0.7390 | -0.0939 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0728 | 0.0728 | 2.1824 | -0.0333 |
| 92 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0728 | 0.0728 | 2.1824 | -0.0333 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0638 | 0.0777 | 0.6789 | -0.0939 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0638 | 0.0777 | 0.6789 | -0.0939 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0638 | 0.0777 | 0.6789 | -0.0939 |
| 96 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0638 | 0.0777 | 0.6789 | -0.0939 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0654 | 0.0670 | 0.8106 | 0.0807 |
| 98 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0654 | 0.0670 | 0.8106 | 0.0807 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | -0.0604 | 0.0732 | -0.4182 | 0.1443 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | -0.0604 | 0.0732 | -0.4182 | 0.1443 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 8 | label_Hbb | label_Tbqq | -1.5495 | -0.3884 |
| 2 | mod.fc.0 | 34 | label_Hbb | label_Tbqq | -1.1703 | -0.3884 |
| 3 | mod.fc.0 | 3 | label_Hbb | label_Tbqq | -1.0628 | -0.3884 |
| 4 | mod.fc.0 | 79 | label_Hbb | label_Tbqq | -0.8470 | -0.3884 |
| 5 | mod.fc.0 | 2 | label_Hbb | label_Tbqq | 0.8435 | -0.3884 |
| 6 | mod.fc.0 | 66 | label_Hbb | label_Tbqq | -0.5774 | -0.3884 |
| 7 | mod.fc.0 | 121 | label_Hbb | label_Tbqq | -0.4641 | -0.3884 |
| 8 | mod.fc.0 | 57 | label_Hbb | label_Tbqq | -0.3757 | -0.3884 |
| 9 | mod.fc.0 | 123 | label_Hbb | label_Tbqq | 0.3455 | -0.3884 |
| 10 | mod.fc.0 | 124 | label_Hbb | label_Tbqq | -0.3345 | -0.3884 |
| 11 | mod.fc.0 | 76 | label_Hbb | label_Tbqq | 0.3230 | -0.3884 |
| 12 | mod.fc.0 | 45 | label_Hbb | label_Tbqq | 0.2798 | -0.3884 |
| 13 | mod.fc.0 | 23 | label_Hbb | label_Tbqq | 0.2783 | -0.3884 |
| 14 | mod.fc.0 | 54 | label_Hbb | label_Tbqq | 0.1449 | -0.3884 |
| 15 | mod.fc.0 | 103 | label_Hbb | label_Tbqq | 0.1333 | -0.3884 |
| 16 | mod.fc.0 | 96 | label_Hbb | label_Tbqq | 0.1072 | -0.3884 |
| 17 | mod.fc.0 | 18 | label_Hbb | label_Tbqq | 0.0893 | -0.3884 |
| 18 | mod.fc.0 | 58 | label_Hbb | label_Tbqq | 0.0625 | -0.3884 |
| 19 | mod.fc.0 | 82 | label_Hbb | label_Tbqq | 0.0610 | -0.3884 |
| 20 | mod.fc.0 | 6 | label_Hbb | label_Tbqq | -0.0469 | -0.3884 |
| 21 | mod.fc.0 | 10 | label_Hbb | label_Tbqq | -0.0425 | -0.3884 |
| 22 | mod.fc.0 | 110 | label_Hbb | label_Tbqq | -0.0187 | -0.3884 |
| 23 | mod.fc.0 | 80 | label_Hbb | label_Tbqq | -0.0099 | -0.3884 |
| 24 | mod.fc.0 | 91 | label_Hbb | label_Tbqq | -0.0091 | -0.3884 |
| 25 | mod.fc.0 | 115 | label_Hbb | label_Tbqq | 9.346e-04 | -0.3884 |
| 26 | mod.fc.0 | 38 | label_Hbb | label_Tbqq | -4.709e-05 | -0.3884 |
| 27 | mod.fc.0 | 4 | label_Hbb | label_Tbqq | 2.971e-05 | -0.3884 |
| 28 | mod.fc.0 | 40 | label_Hbb | label_Tbqq | -1.975e-05 | -0.3884 |
| 29 | mod.fc.0 | 106 | label_Hbb | label_Tbqq | 1.970e-05 | -0.3884 |
| 30 | mod.fc.0 | 49 | label_Hbb | label_Tbqq | -1.919e-05 | -0.3884 |
| 31 | mod.fc.0 | 78 | label_Hbb | label_Tbqq | -1.859e-05 | -0.3884 |
| 32 | mod.fc.0 | 22 | label_Hbb | label_Tbqq | 1.777e-05 | -0.3884 |
| 33 | mod.fc.0 | 109 | label_Hbb | label_Tbqq | -1.758e-05 | -0.3884 |
| 34 | mod.fc.0 | 77 | label_Hbb | label_Tbqq | 1.583e-05 | -0.3884 |
| 35 | mod.fc.0 | 118 | label_Hbb | label_Tbqq | 1.313e-05 | -0.3884 |
| 36 | mod.fc.0 | 29 | label_Hbb | label_Tbqq | -1.211e-05 | -0.3884 |
| 37 | mod.fc.0 | 108 | label_Hbb | label_Tbqq | 1.189e-05 | -0.3884 |
| 38 | mod.fc.0 | 15 | label_Hbb | label_Tbqq | -1.158e-05 | -0.3884 |
| 39 | mod.fc.0 | 46 | label_Hbb | label_Tbqq | -1.052e-05 | -0.3884 |
| 40 | mod.fc.0 | 94 | label_Hbb | label_Tbqq | 9.935e-06 | -0.3884 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
