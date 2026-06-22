# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **280**
- src_label: `label_H4q`
- tgt_label: `label_Hcc`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 2.2103 | 2.2103 | 14.5730 | 0.3536 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 2.2103 | 2.2103 | 14.5730 | 0.3536 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 2.1206 | 2.5908 | 5.5365 | 0.6580 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 2.1206 | 2.5908 | 5.5365 | 0.6580 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.2223 | 1.6172 | 3.8576 | 0.6580 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.2223 | 1.6172 | 3.8576 | 0.6580 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.1326 | 1.7827 | 11.2283 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.1326 | 1.7827 | 11.2283 | 0.3536 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.5946 | 1.4646 | 3.7567 | 0.6580 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.5946 | 1.4646 | 3.7567 | 0.6580 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.5048 | 1.6253 | 11.8503 | 0.3536 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.5048 | 1.6253 | 11.8503 | 0.3536 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3071 | 1.1590 | 11.7499 | 0.3536 |
| 14 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3071 | 1.1590 | 11.7499 | 0.3536 |
| 15 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.3071 | 1.1590 | 11.7499 | 0.3536 |
| 16 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.3071 | 1.1590 | 11.7499 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2174 | 1.4354 | 3.6212 | 0.6580 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2174 | 1.4354 | 3.6212 | 0.6580 |
| 19 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.2174 | 1.4354 | 3.6212 | 0.6580 |
| 20 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.2174 | 1.4354 | 3.6212 | 0.6580 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 4 | 1.4263 | 1.4263 | 5.7052 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | 1.1334 | 1.1334 | 4.5335 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 4 | 1.0769 | 1.0769 | -4.3077 | -0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 4 | 1.0769 | 1.0769 | -4.3077 | -0.2500 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 4 | 1.0639 | 1.0639 | 4.2558 | 0.2500 |
| 8 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 4 | 1.0639 | 1.0639 | 4.2558 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | 0.9053 | 0.9053 | 3.7199 | 0.2434 |
| 10 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | 0.9053 | 0.9053 | 3.7199 | 0.2434 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.7240 | 0.7240 | 2.8960 | 0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.7240 | 0.7240 | 2.8960 | 0.2500 |
| 13 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | 0.7240 | 0.7240 | 2.8960 | 0.2500 |
| 14 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | 0.7240 | 0.7240 | 2.8960 | 0.2500 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | -0.5591 | 0.5614 | 2.2364 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | -0.5591 | 0.5614 | 2.2364 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.5502 | 0.5610 | -2.5646 | -0.2145 |
| 18 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.5502 | 0.5610 | -2.5646 | -0.2145 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.4758 | 0.4758 | 1.9551 | 0.2434 |
| 20 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.4758 | 0.4758 | 1.9551 | 0.2434 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | 0.4758 | 0.4758 | 1.9551 | 0.2434 |
| 22 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | 0.4758 | 0.4758 | 1.9551 | 0.2434 |
| 23 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | -0.4169 | 0.4350 | 1.6675 | -0.2500 |
| 24 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 4 | -0.4169 | 0.4350 | 1.6675 | -0.2500 |
| 25 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 4 | -0.4169 | 0.4350 | 1.6675 | -0.2500 |
| 26 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 4 | -0.4169 | 0.4350 | 1.6675 | -0.2500 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 76 | 0.3137 | 0.3137 | 1.1582 | 0.2709 |
| 28 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 76 | 0.3137 | 0.3137 | 1.1582 | 0.2709 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.3083 | 0.3083 | -2.1735 | -0.1418 |
| 30 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.3083 | 0.3083 | -2.1735 | -0.1418 |
| 31 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | -0.2937 | 0.3564 | 1.1747 | -0.2500 |
| 32 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | -0.2937 | 0.3564 | 1.1747 | -0.2500 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.3027 | 0.3027 | -2.1342 | -0.1418 |
| 34 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.3027 | 0.3027 | -2.1342 | -0.1418 |
| 35 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.2796 | 0.2796 | 0.9866 | 0.2834 |
| 36 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.2796 | 0.2796 | 0.9866 | 0.2834 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | -0.2707 | 0.3136 | 1.1123 | -0.2434 |
| 38 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | -0.2707 | 0.3136 | 1.1123 | -0.2434 |
| 39 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.2327 | 0.2327 | -1.6408 | 0.1418 |
| 40 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.2327 | 0.2327 | -1.6408 | 0.1418 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | -0.2327 | 0.2327 | -1.6408 | 0.1418 |
| 42 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | -0.2327 | 0.2327 | -1.6408 | 0.1418 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.2175 | 0.2175 | -0.9510 | -0.2287 |
| 44 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.2175 | 0.2175 | -0.9510 | -0.2287 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.2141 | 0.2179 | -0.7554 | -0.2834 |
| 46 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.2141 | 0.2179 | -0.7554 | -0.2834 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.1654 | 0.2003 | 0.7232 | 0.2287 |
| 48 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.1654 | 0.2003 | 0.7232 | 0.2287 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1640 | 0.2021 | -0.7645 | -0.2145 |
| 50 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1640 | 0.2021 | -0.7645 | -0.2145 |
| 51 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.1640 | 0.2021 | -0.7645 | -0.2145 |
| 52 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.1640 | 0.2021 | -0.7645 | -0.2145 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 3 | 0.1549 | 0.1693 | 0.8830 | 0.1754 |
| 54 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 3 | 0.1549 | 0.1693 | 0.8830 | 0.1754 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.1270 | 0.1270 | -0.5552 | -0.2287 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.1270 | 0.1270 | -0.5552 | -0.2287 |
| 57 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | 0.1229 | 0.1337 | 0.4339 | 0.2834 |
| 58 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | 0.1229 | 0.1337 | 0.4339 | 0.2834 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.1034 | 0.1263 | 0.5897 | 0.1754 |
| 60 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.1034 | 0.1263 | 0.5897 | 0.1754 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.0756 | 0.1181 | -0.2792 | -0.2709 |
| 62 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.0756 | 0.1181 | -0.2792 | -0.2709 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0697 | 0.1038 | 0.2573 | 0.2709 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0697 | 0.1038 | 0.2573 | 0.2709 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | 0.0697 | 0.1038 | 0.2573 | 0.2709 |
| 66 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | 0.0697 | 0.1038 | 0.2573 | 0.2709 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | -0.0635 | 0.1269 | -0.4474 | 0.1418 |
| 68 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | -0.0635 | 0.1269 | -0.4474 | 0.1418 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0677 | 0.0805 | 0.7394 | 0.0915 |
| 70 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0677 | 0.0805 | 0.7394 | 0.0915 |
| 71 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | -0.0666 | 0.0793 | 0.3796 | -0.1754 |
| 72 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | -0.0666 | 0.0793 | 0.3796 | -0.1754 |
| 73 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | -0.0666 | 0.0793 | 0.3796 | -0.1754 |
| 74 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 3 | -0.0666 | 0.0793 | 0.3796 | -0.1754 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.0638 | 0.0671 | 0.6973 | 0.0915 |
| 76 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.0638 | 0.0671 | 0.6973 | 0.0915 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | 0.0613 | 0.0613 | 1.9306 | 0.0318 |
| 78 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | 0.0613 | 0.0613 | 1.9306 | 0.0318 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | 0.0604 | 0.0604 | 1.9006 | 0.0318 |
| 80 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | 0.0604 | 0.0604 | 1.9006 | 0.0318 |
| 81 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0583 | 0.0583 | 1.8355 | -0.0318 |
| 82 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0583 | 0.0583 | 1.8355 | -0.0318 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | -0.0583 | 0.0583 | 1.8355 | -0.0318 |
| 84 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | -0.0583 | 0.0583 | 1.8355 | -0.0318 |
| 85 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.0301 | 0.1573 | 0.1401 | 0.2145 |
| 86 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.0301 | 0.1573 | 0.1401 | 0.2145 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | -0.0309 | 0.1466 | -0.1438 | 0.2145 |
| 88 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | -0.0309 | 0.1466 | -0.1438 | 0.2145 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0254 | 0.1692 | -0.1046 | -0.2434 |
| 90 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0254 | 0.1692 | -0.1046 | -0.2434 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | -0.0485 | 0.0505 | 1.5276 | -0.0318 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | -0.0485 | 0.0505 | 1.5276 | -0.0318 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0438 | 0.0701 | -0.1915 | 0.2287 |
| 94 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0438 | 0.0701 | -0.1915 | 0.2287 |
| 95 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.0438 | 0.0701 | -0.1915 | 0.2287 |
| 96 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.0438 | 0.0701 | -0.1915 | 0.2287 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0355 | 0.0558 | 0.3875 | -0.0915 |
| 98 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0355 | 0.0558 | 0.3875 | -0.0915 |
| 99 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | -0.0355 | 0.0558 | 0.3875 | -0.0915 |
| 100 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | -0.0355 | 0.0558 | 0.3875 | -0.0915 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 10 | label_H4q | label_Hcc | -1.1334 | 0.3590 |
| 2 | mod.fc.0 | 76 | label_H4q | label_Hcc | 1.0834 | 0.3590 |
| 3 | mod.fc.0 | 79 | label_H4q | label_Hcc | 0.9735 | 0.3590 |
| 4 | mod.fc.0 | 57 | label_H4q | label_Hcc | 0.9148 | 0.3590 |
| 5 | mod.fc.0 | 103 | label_H4q | label_Hcc | -0.8581 | 0.3590 |
| 6 | mod.fc.0 | 3 | label_H4q | label_Hcc | -0.7016 | 0.3590 |
| 7 | mod.fc.0 | 8 | label_H4q | label_Hcc | 0.5673 | 0.3590 |
| 8 | mod.fc.0 | 2 | label_H4q | label_Hcc | -0.4520 | 0.3590 |
| 9 | mod.fc.0 | 58 | label_H4q | label_Hcc | 0.4152 | 0.3590 |
| 10 | mod.fc.0 | 124 | label_H4q | label_Hcc | 0.4052 | 0.3590 |
| 11 | mod.fc.0 | 121 | label_H4q | label_Hcc | -0.3661 | 0.3590 |
| 12 | mod.fc.0 | 82 | label_H4q | label_Hcc | -0.3594 | 0.3590 |
| 13 | mod.fc.0 | 54 | label_H4q | label_Hcc | -0.2746 | 0.3590 |
| 14 | mod.fc.0 | 123 | label_H4q | label_Hcc | -0.2618 | 0.3590 |
| 15 | mod.fc.0 | 91 | label_H4q | label_Hcc | 0.2254 | 0.3590 |
| 16 | mod.fc.0 | 18 | label_H4q | label_Hcc | -0.2212 | 0.3590 |
| 17 | mod.fc.0 | 45 | label_H4q | label_Hcc | -0.1824 | 0.3590 |
| 18 | mod.fc.0 | 66 | label_H4q | label_Hcc | -0.1494 | 0.3590 |
| 19 | mod.fc.0 | 34 | label_H4q | label_Hcc | -0.1270 | 0.3590 |
| 20 | mod.fc.0 | 96 | label_H4q | label_Hcc | -0.0857 | 0.3590 |
| 21 | mod.fc.0 | 23 | label_H4q | label_Hcc | -0.0767 | 0.3590 |
| 22 | mod.fc.0 | 6 | label_H4q | label_Hcc | 0.0436 | 0.3590 |
| 23 | mod.fc.0 | 110 | label_H4q | label_Hcc | -0.0077 | 0.3590 |
| 24 | mod.fc.0 | 80 | label_H4q | label_Hcc | -0.0055 | 0.3590 |
| 25 | mod.fc.0 | 78 | label_H4q | label_Hcc | -2.817e-04 | 0.3590 |
| 26 | mod.fc.0 | 115 | label_H4q | label_Hcc | 2.358e-04 | 0.3590 |
| 27 | mod.fc.0 | 118 | label_H4q | label_Hcc | -3.512e-05 | 0.3590 |
| 28 | mod.fc.0 | 38 | label_H4q | label_Hcc | -2.008e-05 | 0.3590 |
| 29 | mod.fc.0 | 81 | label_H4q | label_Hcc | -1.657e-05 | 0.3590 |
| 30 | mod.fc.0 | 11 | label_H4q | label_Hcc | 1.657e-05 | 0.3590 |
| 31 | mod.fc.0 | 4 | label_H4q | label_Hcc | -1.645e-05 | 0.3590 |
| 32 | mod.fc.0 | 64 | label_H4q | label_Hcc | -1.102e-05 | 0.3590 |
| 33 | mod.fc.0 | 106 | label_H4q | label_Hcc | 1.032e-05 | 0.3590 |
| 34 | mod.fc.0 | 67 | label_H4q | label_Hcc | 9.675e-06 | 0.3590 |
| 35 | mod.fc.0 | 35 | label_H4q | label_Hcc | 9.399e-06 | 0.3590 |
| 36 | mod.fc.0 | 17 | label_H4q | label_Hcc | -9.398e-06 | 0.3590 |
| 37 | mod.fc.0 | 94 | label_H4q | label_Hcc | 9.134e-06 | 0.3590 |
| 38 | mod.fc.0 | 22 | label_H4q | label_Hcc | 8.362e-06 | 0.3590 |
| 39 | mod.fc.0 | 89 | label_H4q | label_Hcc | -8.192e-06 | 0.3590 |
| 40 | mod.fc.0 | 112 | label_H4q | label_Hcc | -7.646e-06 | 0.3590 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
