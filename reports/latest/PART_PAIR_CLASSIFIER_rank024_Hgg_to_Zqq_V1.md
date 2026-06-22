# PART_CLASSIFIER_LOGIT_DECODER_REAL_CONTRACT_V1

Classifier / CLS-logit decoder. Captures `mod.norm`, `mod.fc`, and final linear layers. Contribution is activation × gradient for `J`, plus exact final-linear target-source directions where available. This closes `CLS vector → class logits`.

- events: **64**
- rows: **320**
- summary_rows: **20**
- dim_rows: **252**
- src_label: `label_Hgg`
- tgt_label: `label_Zqq`

## Top classifier/norm module contributions
| rank | objective | module | type | tensor | group | mean_score | mean_abs | act_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | Linear | input | A_Hqql_correct | 1.4826 | 1.7873 | 3.8859 | 0.7026 |
| 2 | signed_hqql_tbl | mod.fc | Sequential | input | A_Hqql_correct | 1.4826 | 1.7873 | 3.8859 | 0.7026 |
| 3 | signed_hqql_tbl | mod.fc.0 | Linear | input | C_Tbl_correct | 1.3929 | 2.0325 | 4.2863 | 0.7026 |
| 4 | signed_hqql_tbl | mod.fc | Sequential | input | C_Tbl_correct | 1.3929 | 2.0325 | 4.2863 | 0.7026 |
| 5 | signed_hqql_tbl | mod.fc.0 | Linear | output | A_Hqql_correct | 1.4410 | 1.4916 | 12.3908 | 0.3536 |
| 6 | signed_hqql_tbl | mod.fc | Sequential | output | A_Hqql_correct | 1.4410 | 1.4916 | 12.3908 | 0.3536 |
| 7 | signed_hqql_tbl | mod.fc.0 | Linear | output | C_Tbl_correct | 1.4345 | 1.4915 | 12.2446 | 0.3536 |
| 8 | signed_hqql_tbl | mod.fc | Sequential | output | C_Tbl_correct | 1.4345 | 1.4915 | 12.2446 | 0.3536 |
| 9 | B_tbl_minus_hqql | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4661 | 1.4589 | 3.3986 | 0.7026 |
| 10 | B_tbl_minus_hqql | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4661 | 1.4589 | 3.3986 | 0.7026 |
| 11 | signed_hqql_tbl | mod.fc.0 | Linear | input | B_Hqql_to_Tbl | 0.4661 | 1.4589 | 3.3986 | 0.7026 |
| 12 | signed_hqql_tbl | mod.fc | Sequential | input | B_Hqql_to_Tbl | 0.4661 | 1.4589 | 3.3986 | 0.7026 |
| 13 | signed_hqql_tbl | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5076 | 0.9293 | 10.9267 | 0.3536 |
| 14 | signed_hqql_tbl | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5076 | 0.9293 | 10.9267 | 0.3536 |
| 15 | B_tbl_minus_hqql | mod.fc.0 | Linear | output | B_Hqql_to_Tbl | 0.5076 | 0.9293 | 10.9267 | 0.3536 |
| 16 | B_tbl_minus_hqql | mod.fc | Sequential | output | B_Hqql_to_Tbl | 0.5076 | 0.9293 | 10.9267 | 0.3536 |
| 17 | signed_hqql_tbl | mod.fc.0 | Linear | input | D_Tbl_to_Hqql | 0.3595 | 1.2974 | 3.0263 | 0.7026 |
| 18 | signed_hqql_tbl | mod.fc | Sequential | input | D_Tbl_to_Hqql | 0.3595 | 1.2974 | 3.0263 | 0.7026 |
| 19 | signed_hqql_tbl | mod.fc.0 | Linear | output | D_Tbl_to_Hqql | 0.3180 | 0.7765 | 11.2127 | 0.3536 |
| 20 | signed_hqql_tbl | mod.fc | Sequential | output | D_Tbl_to_Hqql | 0.3180 | 0.7765 | 11.2127 | 0.3536 |

## Top classifier dimensions
| rank | objective | module | tensor | group | dim | mean_contrib | mean_abs | act | grad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 2 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 3 | 1.0697 | 1.0697 | 4.2789 | 0.2500 |
| 3 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 4 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 6 | 0.9377 | 0.9377 | 3.7507 | 0.2500 |
| 5 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.6397 | 0.6397 | 2.5587 | 0.2500 |
| 6 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.6397 | 0.6397 | 2.5587 | 0.2500 |
| 7 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 6 | 0.6397 | 0.6397 | 2.5587 | 0.2500 |
| 8 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 6 | 0.6397 | 0.6397 | 2.5587 | 0.2500 |
| 9 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 103 | 0.6390 | 0.6390 | -2.2187 | -0.2880 |
| 10 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 103 | 0.6390 | 0.6390 | -2.2187 | -0.2880 |
| 11 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 3 | 0.5399 | 0.5399 | 2.1594 | 0.2500 |
| 12 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 3 | 0.5399 | 0.5399 | 2.1594 | 0.2500 |
| 13 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 79 | 0.5157 | 0.5157 | 2.3474 | 0.2197 |
| 14 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 79 | 0.5157 | 0.5157 | 2.3474 | 0.2197 |
| 15 | signed_hqql_tbl | mod.fc.0 | output | C_Tbl_correct | 3 | 0.4968 | 0.5538 | -1.9872 | -0.2500 |
| 16 | signed_hqql_tbl | mod.fc | output | C_Tbl_correct | 3 | 0.4968 | 0.5538 | -1.9872 | -0.2500 |
| 17 | signed_hqql_tbl | mod.fc.0 | output | A_Hqql_correct | 6 | 0.3713 | 0.4219 | -1.4852 | -0.2500 |
| 18 | signed_hqql_tbl | mod.fc | output | A_Hqql_correct | 6 | 0.3713 | 0.4219 | -1.4852 | -0.2500 |
| 19 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 103 | 0.3111 | 0.3287 | 1.0801 | 0.2880 |
| 20 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 103 | 0.3111 | 0.3287 | 1.0801 | 0.2880 |
| 21 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.2807 | 0.3673 | -0.9746 | -0.2880 |
| 22 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.2807 | 0.3673 | -0.9746 | -0.2880 |
| 23 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 103 | 0.2807 | 0.3673 | -0.9746 | -0.2880 |
| 24 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 103 | 0.2807 | 0.3673 | -0.9746 | -0.2880 |
| 25 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 121 | 0.2887 | 0.2887 | 1.0332 | 0.2794 |
| 26 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 121 | 0.2887 | 0.2887 | 1.0332 | 0.2794 |
| 27 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 79 | 0.2709 | 0.2798 | 1.2329 | 0.2197 |
| 28 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 79 | 0.2709 | 0.2798 | 1.2329 | 0.2197 |
| 29 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 57 | 0.2534 | 0.2534 | -1.0786 | -0.2350 |
| 30 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 57 | 0.2534 | 0.2534 | -1.0786 | -0.2350 |
| 31 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 57 | 0.2426 | 0.2426 | -1.0326 | -0.2350 |
| 32 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 57 | 0.2426 | 0.2426 | -1.0326 | -0.2350 |
| 33 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 8 | 0.2292 | 0.2434 | 1.6867 | 0.1359 |
| 34 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 8 | 0.2292 | 0.2434 | 1.6867 | 0.1359 |
| 35 | signed_hqql_tbl | mod.fc.0 | output | D_Tbl_to_Hqql | 6 | -0.2219 | 0.2367 | 0.8874 | -0.2500 |
| 36 | signed_hqql_tbl | mod.fc | output | D_Tbl_to_Hqql | 6 | -0.2219 | 0.2367 | 0.8874 | -0.2500 |
| 37 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 121 | 0.1732 | 0.2339 | -0.6199 | -0.2794 |
| 38 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 121 | 0.1732 | 0.2339 | -0.6199 | -0.2794 |
| 39 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.1744 | 0.1928 | 1.2833 | 0.1359 |
| 40 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.1744 | 0.1928 | 1.2833 | 0.1359 |
| 41 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 8 | 0.1744 | 0.1928 | 1.2833 | 0.1359 |
| 42 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 8 | 0.1744 | 0.1928 | 1.2833 | 0.1359 |
| 43 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 66 | 0.1770 | 0.1770 | -0.6128 | -0.2889 |
| 44 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 66 | 0.1770 | 0.1770 | -0.6128 | -0.2889 |
| 45 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1690 | 0.2010 | 0.7693 | -0.2197 |
| 46 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1690 | 0.2010 | 0.7693 | -0.2197 |
| 47 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 79 | -0.1690 | 0.2010 | 0.7693 | -0.2197 |
| 48 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 79 | -0.1690 | 0.2010 | 0.7693 | -0.2197 |
| 49 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 10 | 0.1674 | 0.1691 | 0.8464 | 0.1977 |
| 50 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 10 | 0.1674 | 0.1691 | 0.8464 | 0.1977 |
| 51 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.1637 | 0.1689 | -0.6966 | 0.2350 |
| 52 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.1637 | 0.1689 | -0.6966 | 0.2350 |
| 53 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 57 | -0.1637 | 0.1689 | -0.6966 | 0.2350 |
| 54 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 57 | -0.1637 | 0.1689 | -0.6966 | 0.2350 |
| 55 | B_tbl_minus_hqql | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.1320 | 0.2896 | 0.5282 | -0.2500 |
| 56 | B_tbl_minus_hqql | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.1320 | 0.2896 | 0.5282 | -0.2500 |
| 57 | signed_hqql_tbl | mod.fc.0 | output | B_Hqql_to_Tbl | 3 | -0.1320 | 0.2896 | 0.5282 | -0.2500 |
| 58 | signed_hqql_tbl | mod.fc | output | B_Hqql_to_Tbl | 3 | -0.1320 | 0.2896 | 0.5282 | -0.2500 |
| 59 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 121 | 0.1554 | 0.1614 | 0.5563 | 0.2794 |
| 60 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 121 | 0.1554 | 0.1614 | 0.5563 | 0.2794 |
| 61 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1268 | 0.1295 | 0.6414 | 0.1977 |
| 62 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1268 | 0.1295 | 0.6414 | 0.1977 |
| 63 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 10 | 0.1268 | 0.1295 | 0.6414 | 0.1977 |
| 64 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 10 | 0.1268 | 0.1295 | 0.6414 | 0.1977 |
| 65 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 10 | -0.1116 | 0.1116 | 0.5644 | -0.1977 |
| 66 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 10 | -0.1116 | 0.1116 | 0.5644 | -0.1977 |
| 67 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 103 | -0.0902 | 0.1635 | -0.3132 | 0.2880 |
| 68 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 103 | -0.0902 | 0.1635 | -0.3132 | 0.2880 |
| 69 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0947 | 0.0997 | -0.3279 | -0.2889 |
| 70 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0947 | 0.0997 | -0.3279 | -0.2889 |
| 71 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 66 | 0.0947 | 0.0997 | -0.3279 | -0.2889 |
| 72 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 66 | 0.0947 | 0.0997 | -0.3279 | -0.2889 |
| 73 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 8 | -0.0777 | 0.1106 | 0.5719 | -0.1359 |
| 74 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 8 | -0.0777 | 0.1106 | 0.5719 | -0.1359 |
| 75 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 66 | 0.0497 | 0.0763 | 0.1721 | 0.2889 |
| 76 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 66 | 0.0497 | 0.0763 | 0.1721 | 0.2889 |
| 77 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 66 | -0.0516 | 0.0631 | -0.1786 | 0.2889 |
| 78 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 66 | -0.0516 | 0.0631 | -0.1786 | 0.2889 |
| 79 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 57 | -0.0259 | 0.1892 | -0.1101 | 0.2350 |
| 80 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 57 | -0.0259 | 0.1892 | -0.1101 | 0.2350 |
| 81 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 79 | -0.0344 | 0.1288 | 0.1565 | -0.2197 |
| 82 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 79 | -0.0344 | 0.1288 | 0.1565 | -0.2197 |
| 83 | signed_hqql_tbl | mod.fc.0 | input | A_Hqql_correct | 82 | 0.0491 | 0.0491 | 0.2914 | 0.1687 |
| 84 | signed_hqql_tbl | mod.fc | input | A_Hqql_correct | 82 | 0.0491 | 0.0491 | 0.2914 | 0.1687 |
| 85 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0484 | 0.0484 | -0.5176 | -0.0934 |
| 86 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0484 | 0.0484 | -0.5176 | -0.0934 |
| 87 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 18 | 0.0484 | 0.0484 | -0.5176 | -0.0934 |
| 88 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 18 | 0.0484 | 0.0484 | -0.5176 | -0.0934 |
| 89 | B_tbl_minus_hqql | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0466 | 0.0466 | 0.3950 | 0.1181 |
| 90 | B_tbl_minus_hqql | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0466 | 0.0466 | 0.3950 | 0.1181 |
| 91 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 2 | 0.0466 | 0.0466 | 0.3950 | 0.1181 |
| 92 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 2 | 0.0466 | 0.0466 | 0.3950 | 0.1181 |
| 93 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 82 | 0.0439 | 0.0590 | -0.2601 | -0.1687 |
| 94 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 82 | 0.0439 | 0.0590 | -0.2601 | -0.1687 |
| 95 | signed_hqql_tbl | mod.fc.0 | input | D_Tbl_to_Hqql | 3 | 0.0440 | 0.0440 | -0.5060 | -0.0870 |
| 96 | signed_hqql_tbl | mod.fc | input | D_Tbl_to_Hqql | 3 | 0.0440 | 0.0440 | -0.5060 | -0.0870 |
| 97 | signed_hqql_tbl | mod.fc.0 | input | C_Tbl_correct | 2 | 0.0419 | 0.0486 | 0.3547 | 0.1181 |
| 98 | signed_hqql_tbl | mod.fc | input | C_Tbl_correct | 2 | 0.0419 | 0.0486 | 0.3547 | 0.1181 |
| 99 | signed_hqql_tbl | mod.fc.0 | input | B_Hqql_to_Tbl | 3 | -0.0406 | 0.0491 | -0.4669 | 0.0870 |
| 100 | signed_hqql_tbl | mod.fc | input | B_Hqql_to_Tbl | 3 | -0.0406 | 0.0491 | -0.4669 | 0.0870 |

## Exact final linear target-source direction
| rank | module | dim | src | tgt | W_tgt_minus_src | bias_tgt_minus_src |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.fc.0 | 66 | label_Hgg | label_Zqq | -1.1556 | 0.1661 |
| 2 | mod.fc.0 | 103 | label_Hgg | label_Zqq | -1.1520 | 0.1661 |
| 3 | mod.fc.0 | 121 | label_Hgg | label_Zqq | -1.1177 | 0.1661 |
| 4 | mod.fc.0 | 57 | label_Hgg | label_Zqq | 0.9398 | 0.1661 |
| 5 | mod.fc.0 | 79 | label_Hgg | label_Zqq | -0.8788 | 0.1661 |
| 6 | mod.fc.0 | 10 | label_Hgg | label_Zqq | 0.7910 | 0.1661 |
| 7 | mod.fc.0 | 82 | label_Hgg | label_Zqq | -0.6747 | 0.1661 |
| 8 | mod.fc.0 | 8 | label_Hgg | label_Zqq | 0.5436 | 0.1661 |
| 9 | mod.fc.0 | 76 | label_Hgg | label_Zqq | 0.4859 | 0.1661 |
| 10 | mod.fc.0 | 2 | label_Hgg | label_Zqq | 0.4724 | 0.1661 |
| 11 | mod.fc.0 | 18 | label_Hgg | label_Zqq | -0.3737 | 0.1661 |
| 12 | mod.fc.0 | 3 | label_Hgg | label_Zqq | 0.3478 | 0.1661 |
| 13 | mod.fc.0 | 91 | label_Hgg | label_Zqq | 0.2553 | 0.1661 |
| 14 | mod.fc.0 | 54 | label_Hgg | label_Zqq | -0.2073 | 0.1661 |
| 15 | mod.fc.0 | 58 | label_Hgg | label_Zqq | -0.2003 | 0.1661 |
| 16 | mod.fc.0 | 96 | label_Hgg | label_Zqq | 0.1988 | 0.1661 |
| 17 | mod.fc.0 | 23 | label_Hgg | label_Zqq | 0.1895 | 0.1661 |
| 18 | mod.fc.0 | 6 | label_Hgg | label_Zqq | 0.0604 | 0.1661 |
| 19 | mod.fc.0 | 124 | label_Hgg | label_Zqq | 0.0585 | 0.1661 |
| 20 | mod.fc.0 | 45 | label_Hgg | label_Zqq | 0.0502 | 0.1661 |
| 21 | mod.fc.0 | 80 | label_Hgg | label_Zqq | -0.0359 | 0.1661 |
| 22 | mod.fc.0 | 123 | label_Hgg | label_Zqq | -0.0333 | 0.1661 |
| 23 | mod.fc.0 | 110 | label_Hgg | label_Zqq | -0.0136 | 0.1661 |
| 24 | mod.fc.0 | 34 | label_Hgg | label_Zqq | 0.0011 | 0.1661 |
| 25 | mod.fc.0 | 78 | label_Hgg | label_Zqq | -7.180e-04 | 0.1661 |
| 26 | mod.fc.0 | 115 | label_Hgg | label_Zqq | -3.200e-04 | 0.1661 |
| 27 | mod.fc.0 | 20 | label_Hgg | label_Zqq | 2.886e-05 | 0.1661 |
| 28 | mod.fc.0 | 51 | label_Hgg | label_Zqq | -2.167e-05 | 0.1661 |
| 29 | mod.fc.0 | 4 | label_Hgg | label_Zqq | -1.150e-05 | 0.1661 |
| 30 | mod.fc.0 | 38 | label_Hgg | label_Zqq | 1.044e-05 | 0.1661 |
| 31 | mod.fc.0 | 40 | label_Hgg | label_Zqq | -9.960e-06 | 0.1661 |
| 32 | mod.fc.0 | 71 | label_Hgg | label_Zqq | 9.065e-06 | 0.1661 |
| 33 | mod.fc.0 | 98 | label_Hgg | label_Zqq | -8.915e-06 | 0.1661 |
| 34 | mod.fc.0 | 49 | label_Hgg | label_Zqq | 8.196e-06 | 0.1661 |
| 35 | mod.fc.0 | 87 | label_Hgg | label_Zqq | 7.659e-06 | 0.1661 |
| 36 | mod.fc.0 | 81 | label_Hgg | label_Zqq | 7.080e-06 | 0.1661 |
| 37 | mod.fc.0 | 11 | label_Hgg | label_Zqq | 7.052e-06 | 0.1661 |
| 38 | mod.fc.0 | 52 | label_Hgg | label_Zqq | 6.945e-06 | 0.1661 |
| 39 | mod.fc.0 | 31 | label_Hgg | label_Zqq | 6.825e-06 | 0.1661 |
| 40 | mod.fc.0 | 88 | label_Hgg | label_Zqq | 6.418e-06 | 0.1661 |

## Formula

```text
z = norm(cls_token)
logits = fc(z)
CLASSIFIER_PATH(dim) = z_dim * dJ/dz_dim
FINAL_LINEAR_DIR(dim) = W[tgt,dim] - W[src,dim]
positive supports J = target-source; negative resists it.
```
