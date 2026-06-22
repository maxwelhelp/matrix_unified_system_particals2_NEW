# PART_RESIDUAL_PATH_TRACE_REAL_CONTRACT_V2

Residual path composition trace with correct CLS-block residual capture. Particle blocks use residual `x`; CLS blocks use residual `x_cls`. Contribution is `dot(block_out - residual_in, dJ/dblock_out)`.

- events: **64**
- rows: **800**
- summary_rows: **50**
- kind_rows: `{'particle': 640, 'cls': 160}`
- missed_rows: **0**

## Top residual block contributions
| rank | objective | module | kind | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | -0.3708 | 0.3708 | 153.6730 | 0.0374 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | -0.3356 | 0.3356 | 149.6900 | 0.0380 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | 0.3071 | 0.3071 | 49.7953 | 0.0740 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | 0.2856 | 0.2856 | 47.8338 | 0.0803 |
| 5 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | 0.1128 | 0.8393 | 128.3794 | 0.0019 |
| 6 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0982 | 0.7538 | 121.5717 | 0.0014 |
| 7 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | -0.0982 | 0.7538 | 127.5561 | 0.0017 |
| 8 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | -0.0728 | 0.7995 | 108.9801 | 8.606e-04 |
| 9 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | -0.1054 | 0.5380 | 121.5100 | 0.0014 |
| 10 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | 0.1454 | 0.2875 | 293.0705 | 2.665e-04 |
| 11 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1293 | 0.2947 | 304.6158 | 2.890e-04 |
| 12 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | 0.1293 | 0.2947 | 296.9902 | 2.499e-04 |
| 13 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | 0.1214 | 0.3001 | 262.8722 | 1.173e-04 |
| 14 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | -0.0828 | 0.4238 | 109.8403 | 7.145e-04 |
| 15 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1192 | 0.1239 | 166.0184 | 0.0350 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | -0.1192 | 0.1239 | 166.0184 | 0.0350 |
| 17 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | -0.0804 | 0.2706 | 296.9868 | 3.145e-04 |
| 18 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0551 | 0.3665 | 124.1075 | 0.0012 |
| 19 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | -0.0551 | 0.3665 | 129.8858 | 0.0014 |
| 20 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0744 | 0.2739 | 103.7667 | 0.0011 |
| 21 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | -0.0744 | 0.2739 | 108.9364 | 0.0013 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1047 | 0.1134 | 52.5395 | 0.0674 |
| 23 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | 0.1047 | 0.1134 | 52.5395 | 0.0674 |
| 24 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | -0.0522 | 0.3027 | 123.0651 | 0.0012 |
| 25 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | -0.0609 | 0.2470 | 103.7558 | 0.0011 |
| 26 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | -0.0715 | 0.1997 | 150.3879 | 6.407e-04 |
| 27 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | 0.0439 | 0.2852 | 108.8183 | 0.0013 |
| 28 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | -0.0666 | 0.1882 | 194.0508 | 4.534e-04 |
| 29 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | -0.0452 | 0.2739 | 91.8748 | 6.196e-04 |
| 30 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | -0.0880 | 0.0880 | 170.9541 | 0.0341 |
| 31 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | -0.0531 | 0.2254 | 119.3704 | 8.606e-04 |
| 32 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | -0.0496 | 0.2197 | 96.8020 | 9.829e-04 |
| 33 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0576 | 0.1792 | 196.9291 | 4.561e-04 |
| 34 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | 0.0576 | 0.1792 | 187.9527 | 3.943e-04 |
| 35 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0501 | 0.1964 | 119.3347 | 8.477e-04 |
| 36 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | 0.0501 | 0.1964 | 114.3436 | 7.307e-04 |
| 37 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | 3.344e-04 | 0.3937 | 129.6335 | 0.0015 |
| 38 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | -0.0320 | 0.2631 | 88.6964 | 5.234e-04 |
| 39 | signed_hqql_tbl | mod.blocks.3 | particle | D_Tbl_to_Hqql | -0.0300 | 0.2544 | 99.8777 | 0.0011 |
| 40 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0449 | 0.1822 | 150.3372 | 6.502e-04 |
| 41 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | 0.0449 | 0.1822 | 142.8963 | 5.620e-04 |
| 42 | signed_hqql_tbl | mod.blocks.4 | particle | A_Hqql_correct | -0.0365 | 0.2146 | 101.7508 | 4.110e-04 |
| 43 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0234 | 0.2487 | 97.8638 | 9.049e-04 |
| 44 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | -0.0234 | 0.2487 | 100.5677 | 0.0011 |
| 45 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | 0.0582 | 0.0715 | 52.7583 | 0.0699 |
| 46 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | 0.0387 | 0.1383 | 189.0753 | 4.654e-04 |
| 47 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | 0.0243 | 0.1830 | 113.4507 | 8.328e-04 |
| 48 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | 0.0275 | 0.1579 | 161.8836 | 2.023e-04 |
| 49 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | 0.0186 | 0.1571 | 144.6992 | 6.650e-04 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | A_Hqql_correct | 0.0039 | 0.1751 | 122.9819 | 3.033e-04 |

## CLS residual contributions
| rank | objective | module | group | mean_score | mean_abs | delta_norm | grad_norm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | A_Hqql_correct | -0.3708 | 0.3708 | 153.6730 | 0.0374 |
| 2 | signed_hqql_tbl | mod.cls_blocks.1 | C_Tbl_correct | -0.3356 | 0.3356 | 149.6900 | 0.0380 |
| 3 | signed_hqql_tbl | mod.cls_blocks.0 | C_Tbl_correct | 0.3071 | 0.3071 | 49.7953 | 0.0740 |
| 4 | signed_hqql_tbl | mod.cls_blocks.0 | A_Hqql_correct | 0.2856 | 0.2856 | 47.8338 | 0.0803 |
| 5 | B_tbl_minus_hqql | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1192 | 0.1239 | 166.0184 | 0.0350 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | B_Hqql_to_Tbl | -0.1192 | 0.1239 | 166.0184 | 0.0350 |
| 7 | signed_hqql_tbl | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1047 | 0.1134 | 52.5395 | 0.0674 |
| 8 | B_tbl_minus_hqql | mod.cls_blocks.0 | B_Hqql_to_Tbl | 0.1047 | 0.1134 | 52.5395 | 0.0674 |
| 9 | signed_hqql_tbl | mod.cls_blocks.1 | D_Tbl_to_Hqql | -0.0880 | 0.0880 | 170.9541 | 0.0341 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | D_Tbl_to_Hqql | 0.0582 | 0.0715 | 52.7583 | 0.0699 |

## Top role-level residual contributions
| rank | objective | module | kind | group | role | mean_score | mean_abs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | neutral_hadron | -0.4095 | 0.4095 |
| 2 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | charged_hadron | 0.3934 | 0.3934 |
| 3 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | muon | -0.3900 | 0.3900 |
| 4 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | charged_hadron | -0.3889 | 0.3889 |
| 5 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | photon | -0.3828 | 0.3828 |
| 6 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | CLS | -0.3708 | 0.3708 |
| 7 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | charged_hadron | -0.3606 | 0.3606 |
| 8 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | CLS | -0.3356 | 0.3356 |
| 9 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | photon | 0.3305 | 0.3305 |
| 10 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | neutral_hadron | 0.3175 | 0.3175 |
| 11 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | CLS | 0.3071 | 0.3071 |
| 12 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | charged_hadron | 0.3065 | 0.3065 |
| 13 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | muon | 0.2916 | 0.2916 |
| 14 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | CLS | 0.2856 | 0.2856 |
| 15 | signed_hqql_tbl | mod.cls_blocks.1 | cls | C_Tbl_correct | neutral_hadron | -0.2480 | 0.2480 |
| 16 | signed_hqql_tbl | mod.cls_blocks.1 | cls | A_Hqql_correct | photon | -0.2134 | 0.2134 |
| 17 | signed_hqql_tbl | mod.cls_blocks.0 | cls | C_Tbl_correct | neutral_hadron | 0.2131 | 0.2131 |
| 18 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1831 | 0.1831 |
| 19 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | neutral_hadron | -0.1831 | 0.1831 |
| 20 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1514 | 0.1514 |
| 21 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | neutral_hadron | 0.1514 | 0.1514 |
| 22 | signed_hqql_tbl | mod.cls_blocks.0 | cls | A_Hqql_correct | photon | 0.1228 | 0.1228 |
| 23 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1192 | 0.1239 |
| 24 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | CLS | -0.1192 | 0.1239 |
| 25 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1047 | 0.1134 |
| 26 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | CLS | 0.1047 | 0.1134 |
| 27 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0981 | 0.1045 |
| 28 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | charged_hadron | -0.0981 | 0.1045 |
| 29 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | charged_hadron | -0.0993 | 0.0993 |
| 30 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0855 | 0.1085 |
| 31 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | charged_hadron | 0.0855 | 0.1085 |
| 32 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | CLS | -0.0880 | 0.0880 |
| 33 | signed_hqql_tbl | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0807 | 0.0879 |
| 34 | B_tbl_minus_hqql | mod.cls_blocks.1 | cls | B_Hqql_to_Tbl | photon | -0.0807 | 0.0879 |
| 35 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | neutral_hadron | -0.0818 | 0.0818 |
| 36 | signed_hqql_tbl | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0812 | 0.0814 |
| 37 | B_tbl_minus_hqql | mod.cls_blocks.0 | cls | B_Hqql_to_Tbl | photon | 0.0812 | 0.0814 |
| 38 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | muon | -0.0804 | 0.0804 |
| 39 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | charged_hadron | 0.0767 | 0.0880 |
| 40 | signed_hqql_tbl | mod.cls_blocks.1 | cls | D_Tbl_to_Hqql | photon | -0.0701 | 0.0701 |
| 41 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | CLS | 0.0582 | 0.0715 |
| 42 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | photon | 0.0510 | 0.0510 |
| 43 | signed_hqql_tbl | mod.cls_blocks.0 | cls | D_Tbl_to_Hqql | neutral_hadron | 0.0416 | 0.0608 |
| 44 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | muon | -0.0413 | 0.0413 |
| 45 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | electron | 0.0346 | 0.0346 |
| 46 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | muon | 0.0343 | 0.0343 |
| 47 | signed_hqql_tbl | mod.blocks.0 | particle | A_Hqql_correct | electron | 0.0292 | 0.0292 |
| 48 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0252 | 0.0252 |
| 49 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | electron | 0.0252 | 0.0252 |
| 50 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | muon | -0.0249 | 0.0249 |
| 51 | signed_hqql_tbl | mod.blocks.5 | particle | C_Tbl_correct | electron | -0.0228 | 0.0238 |
| 52 | signed_hqql_tbl | mod.blocks.0 | particle | D_Tbl_to_Hqql | electron | 0.0213 | 0.0214 |
| 53 | signed_hqql_tbl | mod.blocks.2 | particle | D_Tbl_to_Hqql | electron | 0.0192 | 0.0192 |
| 54 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | muon | -0.0186 | 0.0186 |
| 55 | signed_hqql_tbl | mod.blocks.3 | particle | C_Tbl_correct | electron | -0.0177 | 0.0177 |
| 56 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | electron | -0.0161 | 0.0161 |
| 57 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | electron | -0.0153 | 0.0189 |
| 58 | signed_hqql_tbl | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0157 | 0.0157 |
| 59 | B_tbl_minus_hqql | mod.blocks.5 | particle | B_Hqql_to_Tbl | electron | -0.0157 | 0.0157 |
| 60 | B_tbl_minus_hqql | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0145 | 0.0197 |
| 61 | signed_hqql_tbl | mod.blocks.4 | particle | B_Hqql_to_Tbl | electron | -0.0145 | 0.0197 |
| 62 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | electron | -0.0111 | 0.0305 |
| 63 | signed_hqql_tbl | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0134 | 0.0134 |
| 64 | B_tbl_minus_hqql | mod.blocks.6 | particle | B_Hqql_to_Tbl | electron | 0.0134 | 0.0134 |
| 65 | signed_hqql_tbl | mod.blocks.1 | particle | C_Tbl_correct | electron | -0.0122 | 0.0146 |
| 66 | signed_hqql_tbl | mod.blocks.2 | particle | C_Tbl_correct | muon | -0.0126 | 0.0126 |
| 67 | signed_hqql_tbl | mod.blocks.1 | particle | A_Hqql_correct | electron | 0.0123 | 0.0123 |
| 68 | signed_hqql_tbl | mod.blocks.4 | particle | C_Tbl_correct | muon | -0.0112 | 0.0131 |
| 69 | signed_hqql_tbl | mod.blocks.7 | particle | A_Hqql_correct | electron | -0.0113 | 0.0113 |
| 70 | signed_hqql_tbl | mod.blocks.5 | particle | D_Tbl_to_Hqql | electron | 0.0110 | 0.0110 |
| 71 | signed_hqql_tbl | mod.blocks.7 | particle | D_Tbl_to_Hqql | electron | -0.0103 | 0.0118 |
| 72 | signed_hqql_tbl | mod.blocks.6 | particle | D_Tbl_to_Hqql | electron | 0.0095 | 0.0095 |
| 73 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | electron | -0.0086 | 0.0120 |
| 74 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0039 | 0.0245 |
| 75 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | electron | -0.0039 | 0.0245 |
| 76 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0074 | 0.0094 |
| 77 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | electron | -0.0074 | 0.0094 |
| 78 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | neutral_hadron | 0.0061 | 0.0139 |
| 79 | signed_hqql_tbl | mod.blocks.6 | particle | A_Hqql_correct | electron | 0.0075 | 0.0075 |
| 80 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | electron | -0.0062 | 0.0128 |
| 81 | signed_hqql_tbl | mod.blocks.6 | particle | C_Tbl_correct | muon | 0.0063 | 0.0085 |
| 82 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | charged_hadron | 0.0058 | 0.0077 |
| 83 | signed_hqql_tbl | mod.blocks.0 | particle | C_Tbl_correct | charged_hadron | -0.0055 | 0.0078 |
| 84 | signed_hqql_tbl | mod.blocks.3 | particle | A_Hqql_correct | electron | 0.0059 | 0.0059 |
| 85 | B_tbl_minus_hqql | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0050 | 0.0078 |
| 86 | signed_hqql_tbl | mod.blocks.0 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0050 | 0.0078 |
| 87 | signed_hqql_tbl | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0051 | 0.0054 |
| 88 | B_tbl_minus_hqql | mod.blocks.1 | particle | B_Hqql_to_Tbl | electron | -0.0051 | 0.0054 |
| 89 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0043 | 0.0079 |
| 90 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | neutral_hadron | 0.0043 | 0.0079 |
| 91 | signed_hqql_tbl | mod.blocks.4 | particle | D_Tbl_to_Hqql | electron | -0.0019 | 0.0171 |
| 92 | B_tbl_minus_hqql | mod.blocks.7 | particle | B_Hqql_to_Tbl | charged_hadron | 0.0046 | 0.0060 |
| 93 | signed_hqql_tbl | mod.blocks.7 | particle | B_Hqql_to_Tbl | charged_hadron | 0.0046 | 0.0060 |
| 94 | signed_hqql_tbl | mod.blocks.7 | particle | C_Tbl_correct | photon | 0.0043 | 0.0059 |
| 95 | B_tbl_minus_hqql | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0034 | 0.0095 |
| 96 | signed_hqql_tbl | mod.blocks.3 | particle | B_Hqql_to_Tbl | electron | -0.0034 | 0.0095 |
| 97 | signed_hqql_tbl | mod.blocks.2 | particle | A_Hqql_correct | electron | 0.0046 | 0.0046 |
| 98 | signed_hqql_tbl | mod.blocks.1 | particle | D_Tbl_to_Hqql | neutral_hadron | 0.0043 | 0.0049 |
| 99 | signed_hqql_tbl | mod.blocks.2 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0042 | 0.0050 |
| 100 | B_tbl_minus_hqql | mod.blocks.2 | particle | B_Hqql_to_Tbl | charged_hadron | -0.0042 | 0.0050 |

## Formula

```text
particle block: R_l = block_l(x) - x
CLS block:      R_l = block_l(x, x_cls) - x_cls
PATH(l, role) = mean dot(R_l[token], dJ/d block_l_out[token])
positive = residual update supports objective J
negative = residual update resists objective J
```
