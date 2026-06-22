# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **274**
- src_label: `label_Hbb`
- tgt_label: `label_H4q`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 2.2497 | 2.3120 | 12.6692 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 2.2497 | 2.3120 | 12.6692 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 2.1960 | 2.5757 | 5.3393 | 0.7167 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 2.1960 | 2.5757 | 5.3393 | 0.7167 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.7294 | 1.9924 | 3.8576 | 0.7167 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.7294 | 1.9924 | 3.8576 | 0.7167 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.6757 | 1.8102 | 11.2283 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.6757 | 1.8102 | 11.2283 | 0.3536 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4753 | 1.1764 | 3.1887 | 0.7167 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4753 | 1.1764 | 3.1887 | 0.7167 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4753 | 1.1764 | 3.1887 | 0.7167 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4753 | 1.1764 | 3.1887 | 0.7167 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4216 | 1.2152 | 10.5038 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4216 | 1.2152 | 10.5038 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.4216 | 1.2152 | 10.5038 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.4216 | 1.2152 | 10.5038 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3200 | 1.1550 | 10.9322 | 0.3536 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3200 | 1.1550 | 10.9322 | 0.3536 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.2663 | 1.1738 | 3.4428 | 0.7167 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.2663 | 1.1738 | 3.4428 | 0.7167 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | 1.3315 | 1.3315 | 5.3259 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 4 | 0.9182 | 0.9806 | -3.6730 | -0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 4 | 0.9182 | 0.9806 | -3.6730 | -0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.8087 | 0.8087 | 3.2350 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.8087 | 0.8087 | 3.2350 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | 0.8087 | 0.8087 | 3.2350 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 4 | 0.8087 | 0.8087 | 3.2350 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.7732 | 0.7732 | -2.1342 | -0.3623 |
| 12 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.7732 | 0.7732 | -2.1342 | -0.3623 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | 0.7024 | 0.7024 | 2.8094 | 0.2500 |
| 14 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | 0.7024 | 0.7024 | 2.8094 | 0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.6785 | 0.6785 | 3.2114 | 0.2113 |
| 16 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.6785 | 0.6785 | 3.2114 | 0.2113 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.5372 | 0.6030 | 1.4828 | 0.3623 |
| 18 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.5372 | 0.6030 | 1.4828 | 0.3623 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.4410 | 0.4410 | 1.3874 | 0.3178 |
| 20 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.4410 | 0.4410 | 1.3874 | 0.3178 |
| 21 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 4 | -0.3824 | 0.4526 | 1.5295 | -0.2500 |
| 22 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 4 | -0.3824 | 0.4526 | 1.5295 | -0.2500 |
| 23 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.3871 | 0.4064 | 1.5486 | -0.2500 |
| 24 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.3871 | 0.4064 | 1.5486 | -0.2500 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | -0.3871 | 0.4064 | 1.5486 | -0.2500 |
| 26 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | -0.3871 | 0.4064 | 1.5486 | -0.2500 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.3462 | 0.3476 | 1.6384 | 0.2113 |
| 28 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.3462 | 0.3476 | 1.6384 | 0.2113 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.3245 | 0.3327 | -1.2485 | -0.2599 |
| 30 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.3245 | 0.3327 | -1.2485 | -0.2599 |
| 31 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.3033 | 0.3066 | -0.8372 | -0.3623 |
| 32 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.3033 | 0.3066 | -0.8372 | -0.3623 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.3033 | 0.3066 | -0.8372 | -0.3623 |
| 34 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.3033 | 0.3066 | -0.8372 | -0.3623 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.2808 | 0.2835 | -0.8834 | -0.3178 |
| 36 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.2808 | 0.2835 | -0.8834 | -0.3178 |
| 37 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | 0.2494 | 0.3839 | -0.9976 | -0.2500 |
| 38 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | 0.2494 | 0.3839 | -0.9976 | -0.2500 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.2542 | 0.2542 | 0.9866 | 0.2577 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.2542 | 0.2542 | 0.9866 | 0.2577 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.1922 | 0.2288 | 0.7394 | 0.2599 |
| 42 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.1922 | 0.2288 | 0.7394 | 0.2599 |
| 43 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1605 | 0.2077 | 0.7595 | -0.2113 |
| 44 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1605 | 0.2077 | 0.7595 | -0.2113 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1605 | 0.2077 | 0.7595 | -0.2113 |
| 46 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1605 | 0.2077 | 0.7595 | -0.2113 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1641 | 0.1680 | 0.6368 | 0.2577 |
| 48 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1641 | 0.1680 | 0.6368 | 0.2577 |
| 49 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1641 | 0.1680 | 0.6368 | 0.2577 |
| 50 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1641 | 0.1680 | 0.6368 | 0.2577 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.1128 | 0.2371 | -0.3114 | 0.3623 |
| 52 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.1128 | 0.2371 | -0.3114 | 0.3623 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.1073 | 0.1173 | 0.8830 | 0.1215 |
| 54 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.1073 | 0.1173 | 0.8830 | 0.1215 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.1066 | 0.1066 | 0.8774 | 0.1215 |
| 56 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.1066 | 0.1066 | 0.8774 | 0.1215 |
| 57 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.1066 | 0.1066 | 0.8774 | 0.1215 |
| 58 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.1066 | 0.1066 | 0.8774 | 0.1215 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.1032 | 0.1196 | -0.4005 | -0.2577 |
| 60 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.1032 | 0.1196 | -0.4005 | -0.2577 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.0941 | 0.1006 | 0.2960 | 0.3178 |
| 62 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.0941 | 0.1006 | 0.2960 | 0.3178 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.0859 | 0.1085 | 1.3720 | 0.0626 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.0859 | 0.1085 | 1.3720 | 0.0626 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | -0.0857 | 0.0907 | 0.7059 | -0.1215 |
| 66 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | -0.0857 | 0.0907 | 0.7059 | -0.1215 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0585 | 0.1066 | -0.2251 | -0.2599 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0585 | 0.1066 | -0.2251 | -0.2599 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | -0.0542 | 0.0759 | 0.4460 | -0.1215 |
| 70 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | -0.0542 | 0.0759 | 0.4460 | -0.1215 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.0499 | 0.0860 | 0.1936 | -0.2577 |
| 72 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.0499 | 0.0860 | 0.1936 | -0.2577 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.0523 | 0.0560 | 0.8360 | 0.0626 |
| 74 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.0523 | 0.0560 | 0.8360 | 0.0626 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0512 | 0.0531 | 0.8180 | -0.0626 |
| 76 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0512 | 0.0531 | 0.8180 | -0.0626 |
| 77 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | -0.0512 | 0.0531 | 0.8180 | -0.0626 |
| 78 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | -0.0512 | 0.0531 | 0.8180 | -0.0626 |
| 79 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0401 | 0.1077 | -0.1263 | -0.3178 |
| 80 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0401 | 0.1077 | -0.1263 | -0.3178 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0401 | 0.1077 | -0.1263 | -0.3178 |
| 82 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0401 | 0.1077 | -0.1263 | -0.3178 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0466 | 0.0583 | -0.2581 | -0.1804 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0466 | 0.0583 | -0.2581 | -0.1804 |
| 85 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0370 | 0.0942 | 0.1425 | 0.2599 |
| 86 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0370 | 0.0942 | 0.1425 | 0.2599 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0370 | 0.0942 | 0.1425 | 0.2599 |
| 88 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0370 | 0.0942 | 0.1425 | 0.2599 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.0398 | 0.0622 | -0.2792 | -0.1425 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.0398 | 0.0622 | -0.2792 | -0.1425 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.0221 | 0.1469 | -0.1046 | -0.2113 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.0221 | 0.1469 | -0.1046 | -0.2113 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | -0.0315 | 0.0653 | -0.2214 | 0.1425 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | -0.0315 | 0.0653 | -0.2214 | 0.1425 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0322 | 0.0362 | 0.1786 | 0.1804 |
| 96 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0322 | 0.0362 | 0.1786 | 0.1804 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0170 | 0.0624 | -0.1196 | -0.1425 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0170 | 0.0624 | -0.1196 | -0.1425 |
| 99 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0170 | 0.0624 | -0.1196 | -0.1425 |
| 100 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0170 | 0.0624 | -0.1196 | -0.1425 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 8 | label_Hbb | label_H4q | -1.4492 | -0.2147 |
| 2 | mod.fc.0 | 57 | label_Hbb | label_H4q | -1.2713 | -0.2147 |
| 3 | mod.fc.0 | 121 | label_Hbb | label_H4q | 1.0397 | -0.2147 |
| 4 | mod.fc.0 | 10 | label_Hbb | label_H4q | 1.0307 | -0.2147 |
| 5 | mod.fc.0 | 79 | label_Hbb | label_H4q | -0.8452 | -0.2147 |
| 6 | mod.fc.0 | 45 | label_Hbb | label_H4q | 0.7216 | -0.2147 |
| 7 | mod.fc.0 | 76 | label_Hbb | label_H4q | -0.5701 | -0.2147 |
| 8 | mod.fc.0 | 3 | label_Hbb | label_H4q | 0.4859 | -0.2147 |
| 9 | mod.fc.0 | 2 | label_Hbb | label_H4q | 0.3812 | -0.2147 |
| 10 | mod.fc.0 | 23 | label_Hbb | label_H4q | 0.3016 | -0.2147 |
| 11 | mod.fc.0 | 124 | label_Hbb | label_H4q | -0.2827 | -0.2147 |
| 12 | mod.fc.0 | 91 | label_Hbb | label_H4q | -0.2561 | -0.2147 |
| 13 | mod.fc.0 | 103 | label_Hbb | label_H4q | -0.2504 | -0.2147 |
| 14 | mod.fc.0 | 82 | label_Hbb | label_H4q | 0.2109 | -0.2147 |
| 15 | mod.fc.0 | 123 | label_Hbb | label_H4q | 0.1526 | -0.2147 |
| 16 | mod.fc.0 | 96 | label_Hbb | label_H4q | 0.1324 | -0.2147 |
| 17 | mod.fc.0 | 54 | label_Hbb | label_H4q | 0.1174 | -0.2147 |
| 18 | mod.fc.0 | 58 | label_Hbb | label_H4q | -0.1028 | -0.2147 |
| 19 | mod.fc.0 | 66 | label_Hbb | label_H4q | 0.0744 | -0.2147 |
| 20 | mod.fc.0 | 6 | label_Hbb | label_H4q | -0.0421 | -0.2147 |
| 21 | mod.fc.0 | 34 | label_Hbb | label_H4q | -0.0271 | -0.2147 |
| 22 | mod.fc.0 | 18 | label_Hbb | label_H4q | 0.0230 | -0.2147 |
| 23 | mod.fc.0 | 80 | label_Hbb | label_H4q | 0.0150 | -0.2147 |
| 24 | mod.fc.0 | 78 | label_Hbb | label_H4q | 3.448e-04 | -0.2147 |
| 25 | mod.fc.0 | 115 | label_Hbb | label_H4q | 3.045e-04 | -0.2147 |
| 26 | mod.fc.0 | 110 | label_Hbb | label_H4q | 1.702e-04 | -0.2147 |
| 27 | mod.fc.0 | 38 | label_Hbb | label_H4q | -3.005e-05 | -0.2147 |
| 28 | mod.fc.0 | 49 | label_Hbb | label_H4q | -2.532e-05 | -0.2147 |
| 29 | mod.fc.0 | 11 | label_Hbb | label_H4q | -2.257e-05 | -0.2147 |
| 30 | mod.fc.0 | 119 | label_Hbb | label_H4q | 2.118e-05 | -0.2147 |
| 31 | mod.fc.0 | 20 | label_Hbb | label_H4q | 2.093e-05 | -0.2147 |
| 32 | mod.fc.0 | 4 | label_Hbb | label_H4q | 1.694e-05 | -0.2147 |
| 33 | mod.fc.0 | 118 | label_Hbb | label_H4q | 1.602e-05 | -0.2147 |
| 34 | mod.fc.0 | 46 | label_Hbb | label_H4q | -1.236e-05 | -0.2147 |
| 35 | mod.fc.0 | 19 | label_Hbb | label_H4q | -1.151e-05 | -0.2147 |
| 36 | mod.fc.0 | 127 | label_Hbb | label_H4q | -1.091e-05 | -0.2147 |
| 37 | mod.fc.0 | 40 | label_Hbb | label_H4q | -9.837e-06 | -0.2147 |
| 38 | mod.fc.0 | 92 | label_Hbb | label_H4q | 9.133e-06 | -0.2147 |
| 39 | mod.fc.0 | 94 | label_Hbb | label_H4q | -8.985e-06 | -0.2147 |
| 40 | mod.fc.0 | 87 | label_Hbb | label_H4q | 8.419e-06 | -0.2147 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
