# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **268**
- src_label: `label_H4q`
- tgt_label: `label_Hgg`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.1019 | 1.7682 | 11.2283 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.1019 | 1.7682 | 11.2283 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.1437 | 1.5122 | 3.8576 | 0.6178 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.1437 | 1.5122 | 3.8576 | 0.6178 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.8212 | 1.4482 | 12.3908 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.8212 | 1.4482 | 12.3908 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 0.7794 | 1.1928 | 3.8859 | 0.6178 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 0.7794 | 1.1928 | 3.8859 | 0.6178 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2724 | 1.6203 | 11.6977 | 0.3536 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2724 | 1.6203 | 11.6977 | 0.3536 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.2724 | 1.6203 | 11.6977 | 0.3536 |
| 12 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.2724 | 1.6203 | 11.6977 | 0.3536 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.2275 | 1.8341 | 11.5010 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.2275 | 1.8341 | 11.5010 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.2693 | 1.0650 | 3.3927 | 0.6178 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.2693 | 1.0650 | 3.3927 | 0.6178 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2306 | 1.0880 | 3.5350 | 0.6178 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2306 | 1.0880 | 3.5350 | 0.6178 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2306 | 1.0880 | 3.5350 | 0.6178 |
| 20 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2306 | 1.0880 | 3.5350 | 0.6178 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 4 | 1.0308 | 1.0308 | 4.1232 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 4 | 1.0308 | 1.0308 | 4.1232 | 0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | 0.9463 | 0.9463 | 3.7854 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 3 | 0.9463 | 0.9463 | 3.7854 | 0.2500 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | 0.9463 | 0.9463 | 3.7854 | 0.2500 |
| 10 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 3 | 0.9463 | 0.9463 | 3.7854 | 0.2500 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 3 | -0.8033 | 0.8033 | 3.2132 | -0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 3 | -0.8033 | 0.8033 | 3.2132 | -0.2500 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | -0.6739 | 0.6739 | 2.6957 | -0.2500 |
| 14 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 4 | -0.6739 | 0.6739 | 2.6957 | -0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | -0.6739 | 0.6739 | 2.6957 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 4 | -0.6739 | 0.6739 | 2.6957 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.5212 | 0.5212 | -2.1342 | -0.2442 |
| 18 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.5212 | 0.5212 | -2.1342 | -0.2442 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.4926 | 0.4926 | 2.3474 | 0.2098 |
| 20 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.4926 | 0.4926 | 2.3474 | 0.2098 |
| 21 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.3995 | 0.3995 | 1.9041 | 0.2098 |
| 22 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.3995 | 0.3995 | 1.9041 | 0.2098 |
| 23 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.3995 | 0.3995 | 1.9041 | 0.2098 |
| 24 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.3995 | 0.3995 | 1.9041 | 0.2098 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.3423 | 0.3423 | -1.4016 | -0.2442 |
| 26 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.3423 | 0.3423 | -1.4016 | -0.2442 |
| 27 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 3 | -0.3244 | 0.3419 | 1.2976 | -0.2500 |
| 28 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 3 | -0.3244 | 0.3419 | 1.2976 | -0.2500 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.3191 | 0.3489 | 0.8830 | 0.3614 |
| 30 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.3191 | 0.3489 | 0.8830 | 0.3614 |
| 31 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 4 | -0.2485 | 0.3785 | 0.9939 | -0.2500 |
| 32 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 4 | -0.2485 | 0.3785 | 0.9939 | -0.2500 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.2295 | 0.2295 | 0.9866 | 0.2327 |
| 34 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.2295 | 0.2295 | 0.9866 | 0.2327 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.2167 | 0.2289 | -0.8875 | 0.2442 |
| 36 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.2167 | 0.2289 | -0.8875 | 0.2442 |
| 37 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.2167 | 0.2289 | -0.8875 | 0.2442 |
| 38 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.2167 | 0.2289 | -0.8875 | 0.2442 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | -0.2113 | 0.2187 | 1.0071 | -0.2098 |
| 40 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | -0.2113 | 0.2187 | 1.0071 | -0.2098 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.1547 | 0.1938 | -0.4279 | -0.3614 |
| 42 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.1547 | 0.1938 | -0.4279 | -0.3614 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.1312 | 0.1312 | 0.5639 | 0.2327 |
| 44 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.1312 | 0.1312 | 0.5639 | 0.2327 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | -0.1061 | 0.1061 | -1.1208 | 0.0947 |
| 46 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | -0.1061 | 0.1061 | -1.1208 | 0.0947 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1021 | 0.1021 | -1.0786 | -0.0947 |
| 48 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1021 | 0.1021 | -1.0786 | -0.0947 |
| 49 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0910 | 0.0910 | -0.9608 | -0.0947 |
| 50 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0910 | 0.0910 | -0.9608 | -0.0947 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0910 | 0.0910 | -0.9608 | -0.0947 |
| 52 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0910 | 0.0910 | -0.9608 | -0.0947 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | -0.0901 | 0.0901 | -0.9510 | 0.0947 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | -0.0901 | 0.0901 | -0.9510 | 0.0947 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0750 | 0.1157 | 0.2075 | 0.3614 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0750 | 0.1157 | 0.2075 | 0.3614 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0210 | 0.1372 | -0.1001 | -0.2098 |
| 58 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0210 | 0.1372 | -0.1001 | -0.2098 |
| 59 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0316 | 0.0830 | 0.1360 | -0.2327 |
| 60 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0316 | 0.0830 | 0.1360 | -0.2327 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | -0.0316 | 0.0830 | 0.1360 | -0.2327 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | -0.0316 | 0.0830 | 0.1360 | -0.2327 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 45 | 0.0375 | 0.0421 | 0.1786 | 0.2100 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 45 | 0.0375 | 0.0421 | 0.1786 | 0.2100 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.0141 | 0.1585 | 0.0577 | 0.2442 |
| 66 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.0141 | 0.1585 | 0.0577 | 0.2442 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.0381 | 0.0381 | 1.9006 | 0.0200 |
| 68 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.0381 | 0.0381 | 1.9006 | 0.0200 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.0371 | 0.0371 | 1.8521 | 0.0200 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.0371 | 0.0371 | 1.8521 | 0.0200 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | -0.0369 | 0.0369 | 1.8421 | -0.0200 |
| 72 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | -0.0369 | 0.0369 | 1.8421 | -0.0200 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0367 | 0.0367 | 1.1757 | 0.0312 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0367 | 0.0367 | 1.1757 | 0.0312 |
| 75 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0367 | 0.0367 | 1.1757 | 0.0312 |
| 76 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0367 | 0.0367 | 1.1757 | 0.0312 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.0362 | 0.0377 | 1.1607 | 0.0312 |
| 78 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.0362 | 0.0377 | 1.1607 | 0.0312 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0362 | 0.0362 | -0.1723 | -0.2100 |
| 80 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0362 | 0.0362 | -0.1723 | -0.2100 |
| 81 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0346 | 0.0346 | 1.7282 | -0.0200 |
| 82 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0346 | 0.0346 | 1.7282 | -0.0200 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0346 | 0.0346 | 1.7282 | -0.0200 |
| 84 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0346 | 0.0346 | 1.7282 | -0.0200 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | -0.0234 | 0.0709 | 0.1005 | -0.2327 |
| 86 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | -0.0234 | 0.0709 | 0.1005 | -0.2327 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 18 | 0.0253 | 0.0299 | 0.2861 | 0.0883 |
| 88 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 18 | 0.0253 | 0.0299 | 0.2861 | 0.0883 |
| 89 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0044 | 0.1297 | -0.0121 | -0.3614 |
| 90 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0044 | 0.1297 | -0.0121 | -0.3614 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | 0.0044 | 0.1297 | -0.0121 | -0.3614 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | 0.0044 | 0.1297 | -0.0121 | -0.3614 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0215 | 0.0273 | 0.6885 | -0.0312 |
| 94 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0215 | 0.0273 | 0.6885 | -0.0312 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0185 | 0.0264 | 0.2098 | -0.0883 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0185 | 0.0264 | 0.2098 | -0.0883 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | -0.0185 | 0.0264 | 0.2098 | -0.0883 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | -0.0185 | 0.0264 | 0.2098 | -0.0883 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0169 | 0.0188 | 0.2269 | 0.0744 |
| 100 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0169 | 0.0188 | 0.2269 | 0.0744 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 3 | label_H4q | label_Hgg | -1.4458 | 0.1672 |
| 2 | mod.fc.0 | 8 | label_H4q | label_Hgg | 0.9769 | 0.1672 |
| 3 | mod.fc.0 | 10 | label_H4q | label_Hgg | -0.9306 | 0.1672 |
| 4 | mod.fc.0 | 45 | label_H4q | label_Hgg | -0.8398 | 0.1672 |
| 5 | mod.fc.0 | 79 | label_H4q | label_Hgg | 0.8393 | 0.1672 |
| 6 | mod.fc.0 | 57 | label_H4q | label_Hgg | -0.3788 | 0.1672 |
| 7 | mod.fc.0 | 18 | label_H4q | label_Hgg | -0.3531 | 0.1672 |
| 8 | mod.fc.0 | 124 | label_H4q | label_Hgg | 0.3457 | 0.1672 |
| 9 | mod.fc.0 | 58 | label_H4q | label_Hgg | 0.3305 | 0.1672 |
| 10 | mod.fc.0 | 54 | label_H4q | label_Hgg | -0.3205 | 0.1672 |
| 11 | mod.fc.0 | 66 | label_H4q | label_Hgg | 0.2978 | 0.1672 |
| 12 | mod.fc.0 | 91 | label_H4q | label_Hgg | 0.2277 | 0.1672 |
| 13 | mod.fc.0 | 103 | label_H4q | label_Hgg | 0.1248 | 0.1672 |
| 14 | mod.fc.0 | 76 | label_H4q | label_Hgg | 0.0979 | 0.1672 |
| 15 | mod.fc.0 | 34 | label_H4q | label_Hgg | -0.0802 | 0.1672 |
| 16 | mod.fc.0 | 2 | label_H4q | label_Hgg | -0.0740 | 0.1672 |
| 17 | mod.fc.0 | 23 | label_H4q | label_Hgg | 0.0649 | 0.1672 |
| 18 | mod.fc.0 | 96 | label_H4q | label_Hgg | -0.0572 | 0.1672 |
| 19 | mod.fc.0 | 121 | label_H4q | label_Hgg | 0.0465 | 0.1672 |
| 20 | mod.fc.0 | 82 | label_H4q | label_Hgg | 0.0124 | 0.1672 |
| 21 | mod.fc.0 | 110 | label_H4q | label_Hgg | -0.0105 | 0.1672 |
| 22 | mod.fc.0 | 123 | label_H4q | label_Hgg | -0.0051 | 0.1672 |
| 23 | mod.fc.0 | 80 | label_H4q | label_Hgg | 0.0022 | 0.1672 |
| 24 | mod.fc.0 | 6 | label_H4q | label_Hgg | 0.0015 | 0.1672 |
| 25 | mod.fc.0 | 115 | label_H4q | label_Hgg | 3.494e-04 | 0.1672 |
| 26 | mod.fc.0 | 118 | label_H4q | label_Hgg | -4.682e-05 | 0.1672 |
| 27 | mod.fc.0 | 4 | label_H4q | label_Hgg | 3.224e-05 | 0.1672 |
| 28 | mod.fc.0 | 20 | label_H4q | label_Hgg | -2.288e-05 | 0.1672 |
| 29 | mod.fc.0 | 38 | label_H4q | label_Hgg | 2.076e-05 | 0.1672 |
| 30 | mod.fc.0 | 78 | label_H4q | label_Hgg | -2.032e-05 | 0.1672 |
| 31 | mod.fc.0 | 119 | label_H4q | label_Hgg | -2.020e-05 | 0.1672 |
| 32 | mod.fc.0 | 11 | label_H4q | label_Hgg | -1.592e-05 | 0.1672 |
| 33 | mod.fc.0 | 106 | label_H4q | label_Hgg | 1.565e-05 | 0.1672 |
| 34 | mod.fc.0 | 109 | label_H4q | label_Hgg | -1.537e-05 | 0.1672 |
| 35 | mod.fc.0 | 22 | label_H4q | label_Hgg | 1.416e-05 | 0.1672 |
| 36 | mod.fc.0 | 87 | label_H4q | label_Hgg | -1.356e-05 | 0.1672 |
| 37 | mod.fc.0 | 89 | label_H4q | label_Hgg | 1.163e-05 | 0.1672 |
| 38 | mod.fc.0 | 15 | label_H4q | label_Hgg | -1.114e-05 | 0.1672 |
| 39 | mod.fc.0 | 94 | label_H4q | label_Hgg | 1.062e-05 | 0.1672 |
| 40 | mod.fc.0 | 127 | label_H4q | label_Hgg | 1.040e-05 | 0.1672 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
