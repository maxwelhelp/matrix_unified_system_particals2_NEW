# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **268**
- src_label: `label_Hcc`
- tgt_label: `label_Tbqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 2.3365 | 2.3447 | 14.5730 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 2.3365 | 2.3447 | 14.5730 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 2.2034 | 2.7075 | 5.5365 | 0.7020 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 2.2034 | 2.7075 | 5.5365 | 0.7020 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 2.1016 | 2.3266 | 4.1993 | 0.7020 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 2.1016 | 2.3266 | 4.1993 | 0.7020 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.9685 | 2.0974 | 10.8305 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.9685 | 2.0974 | 10.8305 | 0.3536 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6206 | 1.8246 | 3.6159 | 0.7020 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6206 | 1.8246 | 3.6159 | 0.7020 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.6206 | 1.8246 | 3.6159 | 0.7020 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.6206 | 1.8246 | 3.6159 | 0.7020 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4874 | 1.4572 | 9.6706 | 0.3536 |
| 14 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4874 | 1.4572 | 9.6706 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4874 | 1.4572 | 9.6706 | 0.3536 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4874 | 1.4572 | 9.6706 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.4517 | 1.1945 | 10.6928 | 0.3536 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.4517 | 1.1945 | 10.6928 | 0.3536 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3185 | 1.5785 | 3.4565 | 0.7020 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3185 | 1.5785 | 3.4565 | 0.7020 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 8 | 1.9445 | 1.9445 | 7.7780 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 8 | 1.2032 | 1.2113 | -4.8126 | -0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 8 | 1.2032 | 1.2113 | -4.8126 | -0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 7 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | 0.9521 | 0.9521 | 3.8083 | 0.2500 |
| 8 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 8 | 0.9521 | 0.9521 | 3.8083 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 8 | 0.9521 | 0.9521 | 3.8083 | 0.2500 |
| 10 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 8 | 0.9521 | 0.9521 | 3.8083 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.9070 | 0.9070 | 3.7199 | 0.2438 |
| 12 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.9070 | 0.9070 | 3.7199 | 0.2438 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.7962 | 0.8119 | -2.5646 | -0.3105 |
| 14 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.7962 | 0.8119 | -2.5646 | -0.3105 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | 0.6983 | 0.6983 | 2.7933 | 0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | 0.6983 | 0.6983 | 2.7933 | 0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.6007 | 0.6007 | -2.1118 | -0.2844 |
| 18 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.6007 | 0.6007 | -2.1118 | -0.2844 |
| 19 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.4647 | 0.5052 | 1.8587 | -0.2500 |
| 20 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.4647 | 0.5052 | 1.8587 | -0.2500 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.4647 | 0.5052 | 1.8587 | -0.2500 |
| 22 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.4647 | 0.5052 | 1.8587 | -0.2500 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.4096 | 0.4096 | 1.6801 | 0.2438 |
| 24 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.4096 | 0.4096 | 1.6801 | 0.2438 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.3481 | 0.3622 | 1.3701 | 0.2540 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.3481 | 0.3622 | 1.3701 | 0.2540 |
| 27 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.3228 | 0.3228 | -1.1350 | -0.2844 |
| 28 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.3228 | 0.3228 | -1.1350 | -0.2844 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.3228 | 0.3228 | -1.1350 | -0.2844 |
| 30 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.3228 | 0.3228 | -1.1350 | -0.2844 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.3193 | 0.3193 | -1.9131 | -0.1669 |
| 32 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.3193 | 0.3193 | -1.9131 | -0.1669 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.3193 | 0.3193 | -1.9131 | -0.1669 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.3193 | 0.3193 | -1.9131 | -0.1669 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.3157 | 0.3157 | -1.4905 | -0.2118 |
| 36 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.3157 | 0.3157 | -1.4905 | -0.2118 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.3087 | 0.3087 | -1.8496 | 0.1669 |
| 38 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.3087 | 0.3087 | -1.8496 | 0.1669 |
| 39 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2812 | 0.3867 | 1.1531 | -0.2438 |
| 40 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2812 | 0.3867 | 1.1531 | -0.2438 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.2812 | 0.3867 | 1.1531 | -0.2438 |
| 42 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.2812 | 0.3867 | 1.1531 | -0.2438 |
| 43 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 8 | -0.2467 | 0.4962 | 0.9866 | -0.2500 |
| 44 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 8 | -0.2467 | 0.4962 | 0.9866 | -0.2500 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.2845 | 0.2845 | -1.7046 | -0.1669 |
| 46 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.2845 | 0.2845 | -1.7046 | -0.1669 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.2699 | 0.2988 | 0.8694 | 0.3105 |
| 48 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.2699 | 0.2988 | 0.8694 | 0.3105 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.1810 | 0.2150 | 0.7123 | 0.2540 |
| 50 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.1810 | 0.2150 | 0.7123 | 0.2540 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.1688 | 0.2115 | -0.6923 | -0.2438 |
| 52 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.1688 | 0.2115 | -0.6923 | -0.2438 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 2 | 0.1705 | 0.1705 | 0.7461 | 0.2286 |
| 54 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 2 | 0.1705 | 0.1705 | 0.7461 | 0.2286 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.1450 | 0.2007 | -0.4671 | -0.3105 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.1450 | 0.2007 | -0.4671 | -0.3105 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.1267 | 0.1795 | -0.4987 | -0.2540 |
| 58 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.1267 | 0.1795 | -0.4987 | -0.2540 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.1236 | 0.1374 | -0.5835 | -0.2118 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.1236 | 0.1374 | -0.5835 | -0.2118 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.1236 | 0.1374 | -0.5835 | -0.2118 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.1236 | 0.1374 | -0.5835 | -0.2118 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.0976 | 0.0976 | -0.7770 | -0.1256 |
| 64 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.0976 | 0.0976 | -0.7770 | -0.1256 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | -0.0747 | 0.1494 | -0.4474 | 0.1669 |
| 66 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | -0.0747 | 0.1494 | -0.4474 | 0.1669 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0747 | 0.1347 | 0.2626 | 0.2844 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0747 | 0.1347 | 0.2626 | 0.2844 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0714 | 0.0879 | 0.3125 | 0.2286 |
| 70 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0714 | 0.0879 | 0.3125 | 0.2286 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0714 | 0.0879 | 0.3125 | 0.2286 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0714 | 0.0879 | 0.3125 | 0.2286 |
| 73 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0682 | 0.0682 | -0.5430 | -0.1256 |
| 74 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0682 | 0.0682 | -0.5430 | -0.1256 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0682 | 0.0682 | -0.5430 | -0.1256 |
| 76 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0682 | 0.0682 | -0.5430 | -0.1256 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | -0.0545 | 0.0881 | -0.2572 | 0.2118 |
| 78 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | -0.0545 | 0.0881 | -0.2572 | 0.2118 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.0579 | 0.0579 | 1.2162 | 0.0476 |
| 80 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.0579 | 0.0579 | 1.2162 | 0.0476 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0550 | 0.0550 | 1.1556 | 0.0476 |
| 82 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0550 | 0.0550 | 1.1556 | 0.0476 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 2 | 0.0538 | 0.0587 | -0.2352 | -0.2286 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 2 | 0.0538 | 0.0587 | -0.2352 | -0.2286 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | -0.0519 | 0.0589 | -0.4133 | 0.1256 |
| 86 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | -0.0519 | 0.0589 | -0.4133 | 0.1256 |
| 87 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | 0.0239 | 0.1529 | -0.0958 | -0.2500 |
| 88 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | 0.0239 | 0.1529 | -0.0958 | -0.2500 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | -0.0437 | 0.0437 | 0.9173 | -0.0476 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | -0.0437 | 0.0437 | 0.9173 | -0.0476 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | 0.0386 | 0.0417 | 0.5371 | 0.0719 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | 0.0386 | 0.0417 | 0.5371 | 0.0719 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 2 | -0.0370 | 0.0478 | 0.1618 | -0.2286 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 2 | -0.0370 | 0.0478 | 0.1618 | -0.2286 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 2.514e-04 | 0.2219 | 8.097e-04 | 0.3105 |
| 96 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 2.514e-04 | 0.2219 | 8.097e-04 | 0.3105 |
| 97 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 2.514e-04 | 0.2219 | 8.097e-04 | 0.3105 |
| 98 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 2.514e-04 | 0.2219 | 8.097e-04 | 0.3105 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | -0.0274 | 0.0838 | -0.1295 | 0.2118 |
| 100 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | -0.0274 | 0.0838 | -0.1295 | 0.2118 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 103 | label_Hcc | label_Tbqq | 1.2418 | -0.5327 |
| 2 | mod.fc.0 | 121 | label_Hcc | label_Tbqq | -1.1377 | -0.5327 |
| 3 | mod.fc.0 | 34 | label_Hcc | label_Tbqq | -1.0162 | -0.5327 |
| 4 | mod.fc.0 | 79 | label_Hcc | label_Tbqq | -0.9753 | -0.5327 |
| 5 | mod.fc.0 | 2 | label_Hcc | label_Tbqq | 0.9143 | -0.5327 |
| 6 | mod.fc.0 | 3 | label_Hcc | label_Tbqq | -0.8471 | -0.5327 |
| 7 | mod.fc.0 | 8 | label_Hcc | label_Tbqq | -0.6676 | -0.5327 |
| 8 | mod.fc.0 | 66 | label_Hcc | label_Tbqq | -0.5024 | -0.5327 |
| 9 | mod.fc.0 | 124 | label_Hcc | label_Tbqq | -0.4570 | -0.5327 |
| 10 | mod.fc.0 | 123 | label_Hcc | label_Tbqq | 0.4547 | -0.5327 |
| 11 | mod.fc.0 | 54 | label_Hcc | label_Tbqq | 0.3020 | -0.5327 |
| 12 | mod.fc.0 | 18 | label_Hcc | label_Tbqq | 0.2875 | -0.5327 |
| 13 | mod.fc.0 | 45 | label_Hcc | label_Tbqq | -0.2593 | -0.5327 |
| 14 | mod.fc.0 | 58 | label_Hcc | label_Tbqq | -0.2500 | -0.5327 |
| 15 | mod.fc.0 | 82 | label_Hcc | label_Tbqq | 0.2095 | -0.5327 |
| 16 | mod.fc.0 | 76 | label_Hcc | label_Tbqq | -0.1903 | -0.5327 |
| 17 | mod.fc.0 | 96 | label_Hcc | label_Tbqq | 0.0605 | -0.5327 |
| 18 | mod.fc.0 | 10 | label_Hcc | label_Tbqq | 0.0603 | -0.5327 |
| 19 | mod.fc.0 | 23 | label_Hcc | label_Tbqq | 0.0534 | -0.5327 |
| 20 | mod.fc.0 | 6 | label_Hcc | label_Tbqq | -0.0485 | -0.5327 |
| 21 | mod.fc.0 | 91 | label_Hcc | label_Tbqq | 0.0216 | -0.5327 |
| 22 | mod.fc.0 | 80 | label_Hcc | label_Tbqq | -0.0194 | -0.5327 |
| 23 | mod.fc.0 | 57 | label_Hcc | label_Tbqq | -0.0192 | -0.5327 |
| 24 | mod.fc.0 | 110 | label_Hcc | label_Tbqq | -0.0111 | -0.5327 |
| 25 | mod.fc.0 | 115 | label_Hcc | label_Tbqq | 3.943e-04 | -0.5327 |
| 26 | mod.fc.0 | 78 | label_Hcc | label_Tbqq | -8.162e-05 | -0.5327 |
| 27 | mod.fc.0 | 118 | label_Hcc | label_Tbqq | 3.223e-05 | -0.5327 |
| 28 | mod.fc.0 | 4 | label_Hcc | label_Tbqq | 2.922e-05 | -0.5327 |
| 29 | mod.fc.0 | 81 | label_Hcc | label_Tbqq | 2.660e-05 | -0.5327 |
| 30 | mod.fc.0 | 89 | label_Hcc | label_Tbqq | 1.793e-05 | -0.5327 |
| 31 | mod.fc.0 | 19 | label_Hcc | label_Tbqq | 1.685e-05 | -0.5327 |
| 32 | mod.fc.0 | 20 | label_Hcc | label_Tbqq | -1.630e-05 | -0.5327 |
| 33 | mod.fc.0 | 22 | label_Hcc | label_Tbqq | 1.608e-05 | -0.5327 |
| 34 | mod.fc.0 | 40 | label_Hcc | label_Tbqq | -1.589e-05 | -0.5327 |
| 35 | mod.fc.0 | 48 | label_Hcc | label_Tbqq | -1.555e-05 | -0.5327 |
| 36 | mod.fc.0 | 119 | label_Hcc | label_Tbqq | -1.487e-05 | -0.5327 |
| 37 | mod.fc.0 | 106 | label_Hcc | label_Tbqq | 1.435e-05 | -0.5327 |
| 38 | mod.fc.0 | 52 | label_Hcc | label_Tbqq | -1.430e-05 | -0.5327 |
| 39 | mod.fc.0 | 64 | label_Hcc | label_Tbqq | 1.419e-05 | -0.5327 |
| 40 | mod.fc.0 | 11 | label_Hcc | label_Tbqq | 1.228e-05 | -0.5327 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
