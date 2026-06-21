# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **268**
- src_label: `label_Hcc`
- tgt_label: `label_Hbb`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 0.5644 | 0.7296 | 14.5730 | 0.1768 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 0.5644 | 0.7296 | 14.5730 | 0.1768 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 0.5464 | 0.7580 | 5.5365 | 0.2343 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 0.5464 | 0.7580 | 5.5365 | 0.2343 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 0.5061 | 0.7921 | 5.3393 | 0.2343 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 0.5061 | 0.7921 | 5.3393 | 0.2343 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 0.4881 | 0.8662 | 12.6692 | 0.1768 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 0.4881 | 0.8662 | 12.6692 | 0.1768 |
| 9 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.1906 | 0.6120 | 12.7288 | 0.1768 |
| 10 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.1906 | 0.6120 | 12.7288 | 0.1768 |
| 11 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1609 | 0.7359 | 12.8175 | 0.1768 |
| 12 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1609 | 0.7359 | 12.8175 | 0.1768 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.1609 | 0.7359 | 12.8175 | 0.1768 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.1609 | 0.7359 | 12.8175 | 0.1768 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1789 | 0.4704 | 4.4973 | 0.2343 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1789 | 0.4704 | 4.4973 | 0.2343 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.1789 | 0.4704 | 4.4973 | 0.2343 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.1789 | 0.4704 | 4.4973 | 0.2343 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.1726 | 0.4742 | 4.1971 | 0.2343 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.1726 | 0.4742 | 4.1971 | 0.2343 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 1 | 0.6657 | 0.6657 | 5.3259 | 0.1250 |
| 2 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 1 | 0.6657 | 0.6657 | 5.3259 | 0.1250 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 2 | 0.5667 | 0.5667 | 4.5335 | 0.1250 |
| 4 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 2 | 0.5667 | 0.5667 | 4.5335 | 0.1250 |
| 5 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.4388 | 0.4388 | 3.5101 | 0.1250 |
| 6 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.4388 | 0.4388 | 3.5101 | 0.1250 |
| 7 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 1 | 0.4388 | 0.4388 | 3.5101 | 0.1250 |
| 8 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 1 | 0.4388 | 0.4388 | 3.5101 | 0.1250 |
| 9 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 2 | 0.4009 | 0.4009 | 3.2069 | 0.1250 |
| 10 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 2 | 0.4009 | 0.4009 | 3.2069 | 0.1250 |
| 11 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.3554 | 0.3624 | -2.5646 | -0.1386 |
| 12 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.3554 | 0.3624 | -2.5646 | -0.1386 |
| 13 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.2779 | 0.2971 | 2.2232 | -0.1250 |
| 14 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.2779 | 0.2971 | 2.2232 | -0.1250 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 2 | -0.2779 | 0.2971 | 2.2232 | -0.1250 |
| 16 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 2 | -0.2779 | 0.2971 | 2.2232 | -0.1250 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 1 | -0.2102 | 0.2111 | 1.6819 | -0.1250 |
| 18 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 1 | -0.2102 | 0.2111 | 1.6819 | -0.1250 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.1901 | 0.2401 | 1.3720 | 0.1386 |
| 20 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.1901 | 0.2401 | 1.3720 | 0.1386 |
| 21 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 2 | -0.1777 | 0.2005 | 1.4213 | -0.1250 |
| 22 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 2 | -0.1777 | 0.2005 | 1.4213 | -0.1250 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.1635 | 0.1835 | 1.4828 | 0.1102 |
| 24 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.1635 | 0.1835 | 1.4828 | 0.1102 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | 0.1335 | 0.1385 | -0.9634 | -0.1386 |
| 26 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | 0.1335 | 0.1385 | -0.9634 | -0.1386 |
| 27 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.1045 | 0.1163 | 0.9480 | 0.1102 |
| 28 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.1045 | 0.1163 | 0.9480 | 0.1102 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.1045 | 0.1163 | 0.9480 | 0.1102 |
| 30 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.1045 | 0.1163 | 0.9480 | 0.1102 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.1051 | 0.1078 | -1.2485 | -0.0842 |
| 32 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.1051 | 0.1078 | -1.2485 | -0.0842 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 76 | 0.0743 | 0.0743 | 1.1582 | 0.0642 |
| 34 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 76 | 0.0743 | 0.0743 | 1.1582 | 0.0642 |
| 35 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0586 | 0.1190 | 0.4230 | 0.1386 |
| 36 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0586 | 0.1190 | 0.4230 | 0.1386 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.0586 | 0.1190 | 0.4230 | 0.1386 |
| 38 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.0586 | 0.1190 | 0.4230 | 0.1386 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | 0.0659 | 0.0659 | 1.4786 | 0.0446 |
| 40 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | 0.0659 | 0.0659 | 1.4786 | 0.0446 |
| 41 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.0597 | 0.0597 | 3.7199 | 0.0160 |
| 42 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.0597 | 0.0597 | 3.7199 | 0.0160 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 8 | 0.0493 | 0.0987 | -0.4474 | -0.1102 |
| 44 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 8 | 0.0493 | 0.0987 | -0.4474 | -0.1102 |
| 45 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.0518 | 0.0518 | 3.2308 | -0.0160 |
| 46 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.0518 | 0.0518 | 3.2308 | -0.0160 |
| 47 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.0518 | 0.0518 | 3.2308 | -0.0160 |
| 48 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.0518 | 0.0518 | 3.2308 | -0.0160 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | -0.0515 | 0.0515 | 3.2114 | -0.0160 |
| 50 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | -0.0515 | 0.0515 | 3.2114 | -0.0160 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | 0.0353 | 0.1011 | -0.3205 | -0.1102 |
| 52 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | 0.0353 | 0.1011 | -0.3205 | -0.1102 |
| 53 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 76 | 0.0462 | 0.0462 | 0.7197 | 0.0642 |
| 54 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 76 | 0.0462 | 0.0462 | 0.7197 | 0.0642 |
| 55 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.0457 | 0.0457 | 2.8464 | 0.0160 |
| 56 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.0457 | 0.0457 | 2.8464 | 0.0160 |
| 57 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0375 | 0.0375 | 1.9475 | 0.0193 |
| 58 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0375 | 0.0375 | 1.9475 | 0.0193 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 34 | 0.0375 | 0.0375 | 1.9475 | 0.0193 |
| 60 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 34 | 0.0375 | 0.0375 | 1.9475 | 0.0193 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 34 | -0.0334 | 0.0334 | 1.7332 | -0.0193 |
| 62 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 34 | -0.0334 | 0.0334 | 1.7332 | -0.0193 |
| 63 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | -0.0322 | 0.0390 | 0.7232 | -0.0446 |
| 64 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | -0.0322 | 0.0390 | 0.7232 | -0.0446 |
| 65 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0328 | 0.0328 | 0.7352 | 0.0446 |
| 66 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0328 | 0.0328 | 0.7352 | 0.0446 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | 0.0328 | 0.0328 | 0.7352 | 0.0446 |
| 68 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | 0.0328 | 0.0328 | 0.7352 | 0.0446 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | -0.0321 | 0.0321 | 0.7198 | -0.0446 |
| 70 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | -0.0321 | 0.0321 | 0.7198 | -0.0446 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0288 | 0.0415 | 0.4496 | -0.0642 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0288 | 0.0415 | 0.4496 | -0.0642 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 76 | -0.0288 | 0.0415 | 0.4496 | -0.0642 |
| 74 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 76 | -0.0288 | 0.0415 | 0.4496 | -0.0642 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 34 | 0.0292 | 0.0331 | 1.5164 | 0.0193 |
| 76 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 34 | 0.0292 | 0.0331 | 1.5164 | 0.0193 |
| 77 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 1 | -0.0023 | 0.1629 | 0.0180 | -0.1250 |
| 78 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 1 | -0.0023 | 0.1629 | 0.0180 | -0.1250 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 34 | -0.0278 | 0.0289 | 1.4426 | -0.0193 |
| 80 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 34 | -0.0278 | 0.0289 | 1.4426 | -0.0193 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.0221 | 0.0399 | 0.2626 | 0.0842 |
| 82 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.0221 | 0.0399 | 0.2626 | 0.0842 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | -0.0184 | 0.0369 | -0.2188 | 0.0842 |
| 84 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | -0.0184 | 0.0369 | -0.2188 | 0.0842 |
| 85 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0161 | 0.0353 | -0.1917 | -0.0842 |
| 86 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0161 | 0.0353 | -0.1917 | -0.0842 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 121 | 0.0161 | 0.0353 | -0.1917 | -0.0842 |
| 88 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 121 | 0.0161 | 0.0353 | -0.1917 | -0.0842 |
| 89 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 45 | 0.0174 | 0.0218 | -0.2581 | -0.0674 |
| 90 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 45 | 0.0174 | 0.0218 | -0.2581 | -0.0674 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 3 | 0.0120 | 0.0169 | 0.4460 | 0.0270 |
| 92 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 3 | 0.0120 | 0.0169 | 0.4460 | 0.0270 |
| 93 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 45 | 0.0109 | 0.0126 | -0.1625 | -0.0674 |
| 94 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 45 | 0.0109 | 0.0126 | -0.1625 | -0.0674 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 45 | 0.0109 | 0.0126 | -0.1625 | -0.0674 |
| 96 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 45 | 0.0109 | 0.0126 | -0.1625 | -0.0674 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 10 | 0.0111 | 0.0111 | -0.8666 | -0.0128 |
| 98 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 10 | 0.0111 | 0.0111 | -0.8666 | -0.0128 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 18 | -0.0095 | 0.0142 | -0.3849 | 0.0248 |
| 100 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 18 | -0.0095 | 0.0142 | -0.3849 | 0.0248 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 103 | label_Hcc | label_Hbb | 1.1085 | -0.1443 |
| 2 | mod.fc.0 | 8 | label_Hcc | label_Hbb | 0.8819 | -0.1443 |
| 3 | mod.fc.0 | 121 | label_Hcc | label_Hbb | -0.6736 | -0.1443 |
| 4 | mod.fc.0 | 45 | label_Hcc | label_Hbb | -0.5391 | -0.1443 |
| 5 | mod.fc.0 | 76 | label_Hcc | label_Hbb | -0.5133 | -0.1443 |
| 6 | mod.fc.0 | 57 | label_Hcc | label_Hbb | 0.3565 | -0.1443 |
| 7 | mod.fc.0 | 58 | label_Hcc | label_Hbb | -0.3124 | -0.1443 |
| 8 | mod.fc.0 | 23 | label_Hcc | label_Hbb | -0.2249 | -0.1443 |
| 9 | mod.fc.0 | 3 | label_Hcc | label_Hbb | 0.2157 | -0.1443 |
| 10 | mod.fc.0 | 18 | label_Hcc | label_Hbb | 0.1982 | -0.1443 |
| 11 | mod.fc.0 | 54 | label_Hcc | label_Hbb | 0.1572 | -0.1443 |
| 12 | mod.fc.0 | 34 | label_Hcc | label_Hbb | 0.1541 | -0.1443 |
| 13 | mod.fc.0 | 82 | label_Hcc | label_Hbb | 0.1485 | -0.1443 |
| 14 | mod.fc.0 | 79 | label_Hcc | label_Hbb | -0.1283 | -0.1443 |
| 15 | mod.fc.0 | 124 | label_Hcc | label_Hbb | -0.1225 | -0.1443 |
| 16 | mod.fc.0 | 123 | label_Hcc | label_Hbb | 0.1092 | -0.1443 |
| 17 | mod.fc.0 | 10 | label_Hcc | label_Hbb | 0.1028 | -0.1443 |
| 18 | mod.fc.0 | 66 | label_Hcc | label_Hbb | 0.0750 | -0.1443 |
| 19 | mod.fc.0 | 2 | label_Hcc | label_Hbb | 0.0708 | -0.1443 |
| 20 | mod.fc.0 | 96 | label_Hcc | label_Hbb | -0.0467 | -0.1443 |
| 21 | mod.fc.0 | 91 | label_Hcc | label_Hbb | 0.0307 | -0.1443 |
| 22 | mod.fc.0 | 80 | label_Hcc | label_Hbb | -0.0096 | -0.1443 |
| 23 | mod.fc.0 | 110 | label_Hcc | label_Hbb | 0.0076 | -0.1443 |
| 24 | mod.fc.0 | 6 | label_Hcc | label_Hbb | -0.0016 | -0.1443 |
| 25 | mod.fc.0 | 115 | label_Hcc | label_Hbb | -5.403e-04 | -0.1443 |
| 26 | mod.fc.0 | 78 | label_Hcc | label_Hbb | -6.303e-05 | -0.1443 |
| 27 | mod.fc.0 | 38 | label_Hcc | label_Hbb | 5.013e-05 | -0.1443 |
| 28 | mod.fc.0 | 49 | label_Hcc | label_Hbb | 2.782e-05 | -0.1443 |
| 29 | mod.fc.0 | 81 | label_Hcc | label_Hbb | 2.077e-05 | -0.1443 |
| 30 | mod.fc.0 | 118 | label_Hcc | label_Hbb | 1.910e-05 | -0.1443 |
| 31 | mod.fc.0 | 19 | label_Hcc | label_Hbb | 1.899e-05 | -0.1443 |
| 32 | mod.fc.0 | 20 | label_Hcc | label_Hbb | -1.606e-05 | -0.1443 |
| 33 | mod.fc.0 | 64 | label_Hcc | label_Hbb | 1.547e-05 | -0.1443 |
| 34 | mod.fc.0 | 112 | label_Hcc | label_Hbb | 1.504e-05 | -0.1443 |
| 35 | mod.fc.0 | 89 | label_Hcc | label_Hbb | 1.455e-05 | -0.1443 |
| 36 | mod.fc.0 | 119 | label_Hcc | label_Hbb | -1.406e-05 | -0.1443 |
| 37 | mod.fc.0 | 113 | label_Hcc | label_Hbb | -1.395e-05 | -0.1443 |
| 38 | mod.fc.0 | 46 | label_Hcc | label_Hbb | 1.262e-05 | -0.1443 |
| 39 | mod.fc.0 | 92 | label_Hcc | label_Hbb | -1.224e-05 | -0.1443 |
| 40 | mod.fc.0 | 67 | label_Hcc | label_Hbb | -1.198e-05 | -0.1443 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
