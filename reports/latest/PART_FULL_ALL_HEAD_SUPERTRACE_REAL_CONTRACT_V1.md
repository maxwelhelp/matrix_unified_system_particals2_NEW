# PART_FULL_ALL_HEAD_SUPERTRACE_REAL_CONTRACT_V1

ParT port of the old ParticleNet all-head differentiable supertrace. It gates every attention head output slice simultaneously, backpropagates objectives through all gates, then builds an all-head particle super-score from natural head-output energies weighted by gate gradients.

- events: **256**
- events_per_group: **64**
- micro_batch: **8**
- objectives: `['pred_logit', 'signed_hqql_tbl']`
- weight_note: `positive pred_logit gate gradient`
- head_grad_rows: **160**
- groups_csv: `reports/latest/tables/part_hqql_tbl_groups_direct_replay_v1.csv`

## Top differentiable head gates: `pred_logit`
| rank | head | grad | abs_grad | channels |
| --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h3 | -3.5946 | 3.5946 | ch48:64 |
| 2 | mod.cls_blocks.0.attn.h2 | 1.6602 | 1.6602 | ch32:48 |
| 3 | mod.cls_blocks.1.attn.h3 | -1.3604 | 1.3604 | ch48:64 |
| 4 | mod.cls_blocks.1.attn.h2 | 0.8643 | 0.8643 | ch32:48 |
| 5 | mod.cls_blocks.0.attn.h7 | 0.6266 | 0.6266 | ch112:128 |
| 6 | mod.cls_blocks.0.attn.h4 | 0.3923 | 0.3923 | ch64:80 |
| 7 | mod.cls_blocks.0.attn.h1 | 0.3670 | 0.3670 | ch16:32 |
| 8 | mod.cls_blocks.0.attn.h0 | 0.3192 | 0.3192 | ch0:16 |
| 9 | mod.cls_blocks.1.attn.h7 | 0.1954 | 0.1954 | ch112:128 |
| 10 | mod.cls_blocks.1.attn.h0 | 0.1385 | 0.1385 | ch0:16 |
| 11 | mod.cls_blocks.0.attn.h6 | 0.1315 | 0.1315 | ch96:112 |
| 12 | mod.cls_blocks.1.attn.h1 | 0.1192 | 0.1192 | ch16:32 |
| 13 | mod.cls_blocks.1.attn.h5 | -0.1160 | 0.1160 | ch80:96 |
| 14 | mod.cls_blocks.1.attn.h6 | 0.1086 | 0.1086 | ch96:112 |
| 15 | mod.cls_blocks.0.attn.h5 | 0.0978 | 0.0978 | ch80:96 |
| 16 | mod.blocks.2.attn.h4 | -0.0809 | 0.0809 | ch64:80 |
| 17 | mod.blocks.2.attn.h0 | 0.0785 | 0.0785 | ch0:16 |
| 18 | mod.blocks.4.attn.h0 | 0.0684 | 0.0684 | ch0:16 |
| 19 | mod.blocks.5.attn.h0 | 0.0675 | 0.0675 | ch0:16 |
| 20 | mod.blocks.1.attn.h0 | 0.0636 | 0.0636 | ch0:16 |
| 21 | mod.blocks.6.attn.h0 | 0.0591 | 0.0591 | ch0:16 |
| 22 | mod.blocks.7.attn.h1 | -0.0572 | 0.0572 | ch16:32 |
| 23 | mod.blocks.1.attn.h5 | -0.0541 | 0.0541 | ch80:96 |
| 24 | mod.cls_blocks.1.attn.h4 | 0.0503 | 0.0503 | ch64:80 |
| 25 | mod.blocks.1.attn.h7 | 0.0481 | 0.0481 | ch112:128 |
| 26 | mod.blocks.3.attn.h5 | -0.0479 | 0.0479 | ch80:96 |
| 27 | mod.blocks.0.attn.h5 | -0.0474 | 0.0474 | ch80:96 |
| 28 | mod.blocks.1.attn.h2 | 0.0452 | 0.0452 | ch32:48 |
| 29 | mod.blocks.3.attn.h7 | 0.0448 | 0.0448 | ch112:128 |
| 30 | mod.blocks.5.attn.h4 | -0.0443 | 0.0443 | ch64:80 |

## Top differentiable head gates: `signed_hqql_tbl`
| rank | head | grad | abs_grad | channels |
| --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h3 | -1.6206 | 1.6206 | ch48:64 |
| 2 | mod.cls_blocks.0.attn.h7 | 0.6910 | 0.6910 | ch112:128 |
| 3 | mod.cls_blocks.0.attn.h4 | 0.5459 | 0.5459 | ch64:80 |
| 4 | mod.cls_blocks.1.attn.h3 | -0.3158 | 0.3158 | ch48:64 |
| 5 | mod.cls_blocks.1.attn.h6 | 0.2679 | 0.2679 | ch96:112 |
| 6 | mod.cls_blocks.0.attn.h1 | 0.1384 | 0.1384 | ch16:32 |
| 7 | mod.cls_blocks.0.attn.h6 | 0.1324 | 0.1324 | ch96:112 |
| 8 | mod.cls_blocks.0.attn.h2 | 0.0771 | 0.0771 | ch32:48 |
| 9 | mod.cls_blocks.0.attn.h5 | 0.0765 | 0.0765 | ch80:96 |
| 10 | mod.cls_blocks.1.attn.h2 | -0.0646 | 0.0646 | ch32:48 |
| 11 | mod.cls_blocks.1.attn.h4 | 0.0552 | 0.0552 | ch64:80 |
| 12 | mod.blocks.7.attn.h4 | 0.0503 | 0.0503 | ch64:80 |
| 13 | mod.blocks.4.attn.h7 | -0.0474 | 0.0474 | ch112:128 |
| 14 | mod.blocks.5.attn.h6 | 0.0474 | 0.0474 | ch96:112 |
| 15 | mod.blocks.7.attn.h7 | 0.0428 | 0.0428 | ch112:128 |
| 16 | mod.blocks.5.attn.h1 | -0.0424 | 0.0424 | ch16:32 |
| 17 | mod.blocks.3.attn.h1 | -0.0409 | 0.0409 | ch16:32 |
| 18 | mod.cls_blocks.0.attn.h0 | -0.0407 | 0.0407 | ch0:16 |
| 19 | mod.blocks.0.attn.h1 | -0.0386 | 0.0386 | ch16:32 |
| 20 | mod.blocks.6.attn.h4 | 0.0375 | 0.0375 | ch64:80 |
| 21 | mod.blocks.1.attn.h1 | -0.0364 | 0.0364 | ch16:32 |
| 22 | mod.blocks.2.attn.h6 | 0.0363 | 0.0363 | ch96:112 |
| 23 | mod.cls_blocks.1.attn.h5 | 0.0358 | 0.0358 | ch80:96 |
| 24 | mod.blocks.6.attn.h1 | -0.0357 | 0.0357 | ch16:32 |
| 25 | mod.blocks.6.attn.h0 | 0.0344 | 0.0344 | ch0:16 |
| 26 | mod.blocks.5.attn.h4 | 0.0337 | 0.0337 | ch64:80 |
| 27 | mod.blocks.5.attn.h0 | 0.0318 | 0.0318 | ch0:16 |
| 28 | mod.blocks.4.attn.h6 | 0.0299 | 0.0299 | ch96:112 |
| 29 | mod.blocks.1.attn.h0 | 0.0295 | 0.0295 | ch0:16 |
| 30 | mod.blocks.4.attn.h4 | 0.0293 | 0.0293 | ch64:80 |

## Class summary by predicted class
| pred_label | n_pred | super_mean | super_p90 | acc_within_pred |
| --- | --- | --- | --- | --- |
| label_Hqql | 128 | 5.6934 | 5.7908 | 0.5000 |
| label_Tbl | 128 | 5.7292 | 5.8079 | 0.5000 |

## Top events by all-head super-score
| event | group | true | pred | conf | super_max | real_particles | top_particle_indices |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.5811 | 5.8963 | 30 | [0, 19, 22, 29, 26, 21, 17, 16] |
| 17 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9871 | 5.8932 | 44 | [0, 37, 11, 9, 5, 18, 19, 30] |
| 251 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.8700 | 5.8800 | 36 | [0, 16, 22, 8, 3, 27, 26, 21] |
| 183 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.8766 | 29 | [0, 2, 3, 1, 25, 9, 20, 4] |
| 90 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9444 | 5.8671 | 44 | [0, 1, 36, 2, 8, 34, 4, 19] |
| 127 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8638 | 5.8623 | 57 | [0, 31, 7, 29, 11, 19, 36, 21] |
| 60 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9730 | 5.8531 | 14 | [0, 2, 1, 3, 11, 9, 4, 5] |
| 148 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9337 | 5.8510 | 36 | [0, 30, 11, 2, 1, 27, 28, 24] |
| 206 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.8318 | 5.8508 | 67 | [0, 12, 6, 19, 13, 23, 42, 7] |
| 192 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.9551 | 5.8494 | 51 | [0, 1, 22, 3, 9, 8, 6, 49] |
| 254 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.9855 | 5.8305 | 36 | [0, 22, 6, 5, 8, 27, 10, 1] |
| 122 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.5029 | 5.8288 | 10 | [0, 9, 8, 3, 1, 7, 5, 6] |
| 36 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9794 | 5.8268 | 33 | [0, 8, 32, 9, 14, 21, 4, 25] |
| 81 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.6506 | 5.8253 | 32 | [0, 17, 4, 2, 3, 1, 26, 7] |
| 112 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8849 | 5.8217 | 14 | [0, 10, 2, 7, 3, 5, 1, 8] |
| 197 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.8434 | 5.8191 | 11 | [0, 9, 10, 8, 6, 1, 7, 2] |
| 65 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9342 | 5.8187 | 34 | [0, 17, 33, 1, 32, 7, 2, 15] |
| 110 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8950 | 5.8156 | 52 | [0, 13, 2, 12, 8, 4, 22, 17] |
| 114 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.7183 | 5.8121 | 52 | [0, 36, 3, 39, 21, 7, 6, 11] |
| 64 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8083 | 5.8085 | 15 | [0, 13, 2, 6, 5, 11, 12, 10] |
| 160 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9992 | 5.8079 | 44 | [0, 17, 13, 23, 25, 20, 24, 12] |
| 158 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9992 | 5.8079 | 17 | [0, 2, 10, 6, 16, 5, 9, 7] |
| 87 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.7029 | 5.8067 | 20 | [0, 14, 10, 15, 13, 7, 2, 19] |
| 187 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.8028 | 16 | [0, 9, 8, 4, 1, 5, 11, 10] |
| 86 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.5983 | 5.8025 | 39 | [0, 14, 2, 1, 4, 28, 13, 12] |
| 241 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.7358 | 5.8023 | 34 | [0, 14, 7, 2, 13, 17, 6, 11] |
| 188 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9793 | 5.8023 | 38 | [0, 35, 16, 13, 7, 37, 9, 12] |
| 212 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.6211 | 5.8017 | 24 | [0, 11, 1, 3, 23, 13, 5, 2] |
| 104 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.7311 | 5.8009 | 19 | [0, 15, 18, 13, 17, 1, 12, 16] |
| 180 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.8006 | 18 | [0, 16, 6, 4, 5, 2, 7, 3] |
| 239 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.7370 | 5.8001 | 27 | [0, 21, 23, 26, 2, 1, 24, 19] |
| 96 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.5307 | 5.7995 | 23 | [0, 22, 20, 4, 8, 19, 6, 3] |
| 73 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8044 | 5.7987 | 87 | [0, 13, 20, 9, 11, 2, 15, 36] |
| 181 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7980 | 28 | [0, 7, 1, 11, 20, 16, 25, 3] |
| 252 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.6120 | 5.7956 | 17 | [0, 6, 10, 8, 15, 14, 2, 3] |
| 176 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7937 | 14 | [0, 8, 10, 13, 5, 9, 12, 1] |
| 171 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9999 | 5.7914 | 10 | [0, 8, 2, 3, 7, 9, 6, 5] |
| 178 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7912 | 29 | [0, 14, 1, 23, 15, 9, 2, 20] |
| 28 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9901 | 5.7910 | 26 | [0, 18, 9, 7, 1, 11, 16, 6] |
| 25 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9935 | 5.7908 | 9 | [0, 8, 1, 7, 4, 6, 3, 5] |
| 88 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.5553 | 5.7891 | 15 | [0, 3, 1, 2, 7, 8, 6, 4] |
| 37 | A_Hqql_correct | label_Hqql | label_Hqql | 0.5001 | 5.7877 | 31 | [0, 1, 2, 9, 25, 7, 18, 26] |
| 222 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.7214 | 5.7875 | 59 | [0, 2, 4, 1, 8, 30, 6, 24] |
| 223 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.5341 | 5.7873 | 27 | [0, 1, 13, 4, 19, 5, 26, 8] |
| 151 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9999 | 5.7872 | 16 | [0, 3, 10, 5, 4, 12, 9, 2] |
| 67 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8684 | 5.7856 | 42 | [0, 9, 3, 6, 30, 16, 8, 22] |
| 224 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.9393 | 5.7850 | 35 | [0, 3, 2, 25, 1, 9, 28, 8] |
| 6 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9999 | 5.7849 | 14 | [0, 12, 1, 13, 6, 5, 4, 2] |
| 106 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8289 | 5.7846 | 20 | [0, 18, 1, 14, 8, 10, 5, 17] |
| 1 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9997 | 5.7842 | 25 | [0, 22, 24, 21, 6, 13, 7, 4] |
| 105 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9745 | 5.7837 | 37 | [0, 30, 29, 2, 35, 25, 19, 4] |
| 225 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.5046 | 5.7832 | 64 | [0, 21, 13, 14, 4, 12, 23, 19] |
| 128 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7825 | 12 | [0, 5, 2, 1, 9, 7, 8, 11] |
| 141 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9944 | 5.7810 | 10 | [0, 2, 8, 1, 6, 3, 5, 7] |
| 116 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8374 | 5.7797 | 22 | [0, 16, 13, 9, 18, 11, 19, 8] |
| 7 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9872 | 5.7796 | 36 | [0, 11, 15, 9, 16, 25, 1, 2] |
| 177 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9946 | 5.7787 | 24 | [0, 2, 1, 6, 12, 5, 14, 11] |
| 52 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9914 | 5.7774 | 46 | [0, 6, 27, 17, 3, 2, 8, 1] |
| 191 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9656 | 5.7773 | 26 | [0, 14, 25, 9, 16, 17, 3, 1] |
| 240 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.8176 | 5.7763 | 42 | [0, 3, 2, 26, 39, 1, 28, 36] |
| 66 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9442 | 5.7759 | 14 | [0, 2, 13, 1, 3, 5, 4, 6] |
| 146 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9999 | 5.7756 | 29 | [0, 22, 2, 11, 4, 6, 14, 15] |
| 98 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8902 | 5.7741 | 16 | [0, 6, 3, 2, 1, 13, 10, 8] |
| 84 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.8391 | 5.7704 | 24 | [0, 21, 23, 7, 6, 4, 13, 3] |
| 113 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.7153 | 5.7698 | 28 | [0, 25, 27, 19, 3, 11, 21, 4] |
| 237 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.7511 | 5.7672 | 19 | [0, 13, 7, 8, 15, 9, 4, 1] |
| 143 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9487 | 5.7670 | 41 | [0, 18, 15, 11, 2, 10, 25, 1] |
| 82 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.6556 | 5.7663 | 20 | [0, 16, 12, 10, 8, 14, 1, 17] |
| 26 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9986 | 5.7657 | 36 | [0, 1, 4, 17, 12, 30, 13, 3] |
| 103 | B_Hqql_to_Tbl | label_Hqql | label_Tbl | 0.9180 | 5.7650 | 12 | [0, 7, 6, 3, 1, 4, 5, 2] |
| 190 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9929 | 5.7649 | 16 | [0, 2, 3, 4, 1, 11, 6, 8] |
| 243 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.9209 | 5.7645 | 34 | [0, 8, 5, 9, 4, 14, 1, 13] |
| 130 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7635 | 15 | [0, 1, 3, 4, 13, 10, 7, 8] |
| 245 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.5028 | 5.7613 | 25 | [0, 24, 12, 9, 15, 20, 17, 10] |
| 27 | A_Hqql_correct | label_Hqql | label_Hqql | 0.9999 | 5.7589 | 16 | [0, 1, 3, 9, 2, 4, 8, 5] |
| 250 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.9907 | 5.7584 | 34 | [0, 1, 11, 15, 2, 6, 13, 20] |
| 182 | C_Tbl_correct | label_Tbl | label_Tbl | 0.9994 | 5.7577 | 32 | [0, 2, 5, 4, 8, 6, 1, 3] |
| 231 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.7357 | 5.7575 | 18 | [0, 1, 5, 6, 8, 2, 13, 4] |
| 234 | D_Tbl_to_Hqql | label_Tbl | label_Hqql | 0.5167 | 5.7572 | 26 | [0, 2, 3, 1, 12, 9, 5, 21] |
| 168 | C_Tbl_correct | label_Tbl | label_Tbl | 1.0000 | 5.7569 | 32 | [0, 31, 29, 30, 16, 5, 3, 18] |

## Top particles inside top events
| event | rank | particle | role | super_score | group | pred |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0 | electron | 5.7842 | A_Hqql_correct | label_Hqql |
| 1 | 2 | 22 | neutral_hadron | 0.6680 | A_Hqql_correct | label_Hqql |
| 1 | 3 | 24 | charged_hadron | 0.6187 | A_Hqql_correct | label_Hqql |
| 1 | 4 | 21 | photon | 0.5926 | A_Hqql_correct | label_Hqql |
| 1 | 5 | 6 | charged_hadron | 0.5786 | A_Hqql_correct | label_Hqql |
| 1 | 6 | 13 | photon | 0.5727 | A_Hqql_correct | label_Hqql |
| 1 | 7 | 7 | charged_hadron | 0.5712 | A_Hqql_correct | label_Hqql |
| 1 | 8 | 4 | charged_hadron | 0.5695 | A_Hqql_correct | label_Hqql |
| 6 | 1 | 0 | electron | 5.7849 | A_Hqql_correct | label_Hqql |
| 6 | 2 | 12 | charged_hadron | 0.6140 | A_Hqql_correct | label_Hqql |
| 6 | 3 | 1 | charged_hadron | 0.5808 | A_Hqql_correct | label_Hqql |
| 6 | 4 | 13 | neutral_hadron | 0.5370 | A_Hqql_correct | label_Hqql |
| 6 | 5 | 6 | neutral_hadron | 0.5216 | A_Hqql_correct | label_Hqql |
| 6 | 6 | 5 | photon | 0.5157 | A_Hqql_correct | label_Hqql |
| 6 | 7 | 4 | charged_hadron | 0.5109 | A_Hqql_correct | label_Hqql |
| 6 | 8 | 2 | photon | 0.5068 | A_Hqql_correct | label_Hqql |
| 7 | 1 | 0 | muon | 5.7796 | A_Hqql_correct | label_Hqql |
| 7 | 2 | 11 | charged_hadron | 0.7303 | A_Hqql_correct | label_Hqql |
| 7 | 3 | 15 | charged_hadron | 0.7201 | A_Hqql_correct | label_Hqql |
| 7 | 4 | 9 | neutral_hadron | 0.6768 | A_Hqql_correct | label_Hqql |
| 7 | 5 | 16 | charged_hadron | 0.6714 | A_Hqql_correct | label_Hqql |
| 7 | 6 | 25 | charged_hadron | 0.6582 | A_Hqql_correct | label_Hqql |
| 7 | 7 | 1 | charged_hadron | 0.6356 | A_Hqql_correct | label_Hqql |
| 7 | 8 | 2 | charged_hadron | 0.6282 | A_Hqql_correct | label_Hqql |
| 17 | 1 | 0 | muon | 5.8932 | A_Hqql_correct | label_Hqql |
| 17 | 2 | 37 | charged_hadron | 0.7510 | A_Hqql_correct | label_Hqql |
| 17 | 3 | 11 | charged_hadron | 0.6768 | A_Hqql_correct | label_Hqql |
| 17 | 4 | 9 | charged_hadron | 0.6608 | A_Hqql_correct | label_Hqql |
| 17 | 5 | 5 | charged_hadron | 0.6587 | A_Hqql_correct | label_Hqql |
| 17 | 6 | 18 | neutral_hadron | 0.6573 | A_Hqql_correct | label_Hqql |
| 17 | 7 | 19 | photon | 0.6527 | A_Hqql_correct | label_Hqql |
| 17 | 8 | 30 | charged_hadron | 0.6493 | A_Hqql_correct | label_Hqql |
| 25 | 1 | 0 | muon | 5.7908 | A_Hqql_correct | label_Hqql |
| 25 | 2 | 8 | photon | 0.7007 | A_Hqql_correct | label_Hqql |
| 25 | 3 | 1 | charged_hadron | 0.6913 | A_Hqql_correct | label_Hqql |
| 25 | 4 | 7 | photon | 0.6855 | A_Hqql_correct | label_Hqql |
| 25 | 5 | 4 | charged_hadron | 0.6779 | A_Hqql_correct | label_Hqql |
| 25 | 6 | 6 | charged_hadron | 0.6629 | A_Hqql_correct | label_Hqql |
| 25 | 7 | 3 | charged_hadron | 0.6558 | A_Hqql_correct | label_Hqql |
| 25 | 8 | 5 | photon | 0.6356 | A_Hqql_correct | label_Hqql |
| 26 | 1 | 0 | neutral_hadron | 5.7657 | A_Hqql_correct | label_Hqql |
| 26 | 2 | 1 | electron | 0.7709 | A_Hqql_correct | label_Hqql |
| 26 | 3 | 4 | electron | 0.7604 | A_Hqql_correct | label_Hqql |
| 26 | 4 | 17 | neutral_hadron | 0.7530 | A_Hqql_correct | label_Hqql |
| 26 | 5 | 12 | photon | 0.6976 | A_Hqql_correct | label_Hqql |
| 26 | 6 | 30 | charged_hadron | 0.6918 | A_Hqql_correct | label_Hqql |
| 26 | 7 | 13 | charged_hadron | 0.6824 | A_Hqql_correct | label_Hqql |
| 26 | 8 | 3 | charged_hadron | 0.6737 | A_Hqql_correct | label_Hqql |
| 27 | 1 | 0 | muon | 5.7589 | A_Hqql_correct | label_Hqql |
| 27 | 2 | 1 | charged_hadron | 0.6634 | A_Hqql_correct | label_Hqql |
| 27 | 3 | 3 | charged_hadron | 0.5651 | A_Hqql_correct | label_Hqql |
| 27 | 4 | 9 | charged_hadron | 0.5557 | A_Hqql_correct | label_Hqql |
| 27 | 5 | 2 | charged_hadron | 0.5487 | A_Hqql_correct | label_Hqql |
| 27 | 6 | 4 | charged_hadron | 0.5453 | A_Hqql_correct | label_Hqql |
| 27 | 7 | 8 | charged_hadron | 0.5384 | A_Hqql_correct | label_Hqql |
| 27 | 8 | 5 | neutral_hadron | 0.5381 | A_Hqql_correct | label_Hqql |
| 28 | 1 | 0 | electron | 5.7910 | A_Hqql_correct | label_Hqql |
| 28 | 2 | 18 | charged_hadron | 0.6506 | A_Hqql_correct | label_Hqql |
| 28 | 3 | 9 | charged_hadron | 0.5585 | A_Hqql_correct | label_Hqql |
| 28 | 4 | 7 | charged_hadron | 0.5563 | A_Hqql_correct | label_Hqql |
| 28 | 5 | 1 | charged_hadron | 0.5440 | A_Hqql_correct | label_Hqql |
| 28 | 6 | 11 | charged_hadron | 0.5332 | A_Hqql_correct | label_Hqql |
| 28 | 7 | 16 | neutral_hadron | 0.5276 | A_Hqql_correct | label_Hqql |
| 28 | 8 | 6 | photon | 0.5257 | A_Hqql_correct | label_Hqql |
| 36 | 1 | 0 | electron | 5.8268 | A_Hqql_correct | label_Hqql |
| 36 | 2 | 8 | neutral_hadron | 0.7440 | A_Hqql_correct | label_Hqql |
| 36 | 3 | 32 | charged_hadron | 0.7342 | A_Hqql_correct | label_Hqql |
| 36 | 4 | 9 | photon | 0.7057 | A_Hqql_correct | label_Hqql |
| 36 | 5 | 14 | neutral_hadron | 0.7045 | A_Hqql_correct | label_Hqql |
| 36 | 6 | 21 | charged_hadron | 0.7028 | A_Hqql_correct | label_Hqql |
| 36 | 7 | 4 | neutral_hadron | 0.7002 | A_Hqql_correct | label_Hqql |
| 36 | 8 | 25 | photon | 0.6710 | A_Hqql_correct | label_Hqql |
| 37 | 1 | 0 | muon | 5.7877 | A_Hqql_correct | label_Hqql |
| 37 | 2 | 1 | neutral_hadron | 0.6406 | A_Hqql_correct | label_Hqql |
| 37 | 3 | 2 | charged_hadron | 0.5818 | A_Hqql_correct | label_Hqql |
| 37 | 4 | 9 | charged_hadron | 0.5808 | A_Hqql_correct | label_Hqql |
| 37 | 5 | 25 | photon | 0.5656 | A_Hqql_correct | label_Hqql |
| 37 | 6 | 7 | charged_hadron | 0.5632 | A_Hqql_correct | label_Hqql |
| 37 | 7 | 18 | charged_hadron | 0.5610 | A_Hqql_correct | label_Hqql |
| 37 | 8 | 26 | charged_hadron | 0.5532 | A_Hqql_correct | label_Hqql |
| 52 | 1 | 0 | electron | 5.7774 | A_Hqql_correct | label_Hqql |
| 52 | 2 | 6 | neutral_hadron | 0.6951 | A_Hqql_correct | label_Hqql |
| 52 | 3 | 27 | charged_hadron | 0.6948 | A_Hqql_correct | label_Hqql |
| 52 | 4 | 17 | neutral_hadron | 0.6922 | A_Hqql_correct | label_Hqql |
| 52 | 5 | 3 | charged_hadron | 0.6744 | A_Hqql_correct | label_Hqql |
| 52 | 6 | 2 | charged_hadron | 0.6730 | A_Hqql_correct | label_Hqql |
| 52 | 7 | 8 | charged_hadron | 0.6708 | A_Hqql_correct | label_Hqql |
| 52 | 8 | 1 | photon | 0.6650 | A_Hqql_correct | label_Hqql |
| 60 | 1 | 0 | muon | 5.8531 | A_Hqql_correct | label_Hqql |
| 60 | 2 | 2 | neutral_hadron | 0.5164 | A_Hqql_correct | label_Hqql |
| 60 | 3 | 1 | neutral_hadron | 0.5140 | A_Hqql_correct | label_Hqql |
| 60 | 4 | 3 | charged_hadron | 0.5077 | A_Hqql_correct | label_Hqql |
| 60 | 5 | 11 | photon | 0.5042 | A_Hqql_correct | label_Hqql |
| 60 | 6 | 9 | charged_hadron | 0.4914 | A_Hqql_correct | label_Hqql |
| 60 | 7 | 4 | charged_hadron | 0.4855 | A_Hqql_correct | label_Hqql |
| 60 | 8 | 5 | charged_hadron | 0.4810 | A_Hqql_correct | label_Hqql |
| 64 | 1 | 0 | electron | 5.8085 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 2 | 13 | charged_hadron | 0.7148 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 3 | 2 | neutral_hadron | 0.6118 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 4 | 6 | charged_hadron | 0.6111 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 5 | 5 | charged_hadron | 0.5988 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 6 | 11 | charged_hadron | 0.5781 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 7 | 12 | photon | 0.5678 | B_Hqql_to_Tbl | label_Tbl |
| 64 | 8 | 10 | photon | 0.5633 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 1 | 0 | electron | 5.8187 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 2 | 17 | neutral_hadron | 0.6492 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 3 | 33 | photon | 0.5447 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 4 | 1 | neutral_hadron | 0.5069 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 5 | 32 | charged_hadron | 0.5052 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 6 | 7 | charged_hadron | 0.4980 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 7 | 2 | charged_hadron | 0.4922 | B_Hqql_to_Tbl | label_Tbl |
| 65 | 8 | 15 | charged_hadron | 0.4916 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 1 | 0 | muon | 5.7759 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 2 | 2 | charged_hadron | 0.5959 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 3 | 13 | photon | 0.5848 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 4 | 1 | photon | 0.5816 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 5 | 3 | photon | 0.5727 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 6 | 5 | charged_hadron | 0.5638 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 7 | 4 | charged_hadron | 0.5494 | B_Hqql_to_Tbl | label_Tbl |
| 66 | 8 | 6 | charged_hadron | 0.5387 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 1 | 0 | muon | 5.7856 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 2 | 9 | charged_hadron | 0.7422 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 3 | 3 | charged_hadron | 0.7195 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 4 | 6 | charged_hadron | 0.7024 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 5 | 30 | neutral_hadron | 0.7019 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 6 | 16 | charged_hadron | 0.6992 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 7 | 8 | charged_hadron | 0.6877 | B_Hqql_to_Tbl | label_Tbl |
| 67 | 8 | 22 | neutral_hadron | 0.6723 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 1 | 0 | electron | 5.7987 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 2 | 13 | photon | 0.8574 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 3 | 20 | neutral_hadron | 0.6550 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 4 | 9 | charged_hadron | 0.6513 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 5 | 11 | charged_hadron | 0.6481 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 6 | 2 | charged_hadron | 0.6436 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 7 | 15 | charged_hadron | 0.6408 | B_Hqql_to_Tbl | label_Tbl |
| 73 | 8 | 36 | neutral_hadron | 0.6365 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 1 | 0 | electron | 5.8253 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 2 | 17 | charged_hadron | 0.5837 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 3 | 4 | charged_hadron | 0.5830 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 4 | 2 | charged_hadron | 0.5561 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 5 | 3 | charged_hadron | 0.5561 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 6 | 1 | photon | 0.5418 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 7 | 26 | charged_hadron | 0.5346 | B_Hqql_to_Tbl | label_Tbl |
| 81 | 8 | 7 | charged_hadron | 0.5301 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 1 | 0 | electron | 5.7663 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 2 | 16 | photon | 0.5467 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 3 | 12 | photon | 0.5316 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 4 | 10 | charged_hadron | 0.5313 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 5 | 8 | charged_hadron | 0.5247 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 6 | 14 | charged_hadron | 0.5246 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 7 | 1 | charged_hadron | 0.5210 | B_Hqql_to_Tbl | label_Tbl |
| 82 | 8 | 17 | charged_hadron | 0.5200 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 1 | 0 | electron | 5.7704 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 2 | 21 | photon | 0.7006 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 3 | 23 | charged_hadron | 0.6051 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 4 | 7 | charged_hadron | 0.5410 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 5 | 6 | charged_hadron | 0.5394 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 6 | 4 | neutral_hadron | 0.5371 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 7 | 13 | photon | 0.5360 | B_Hqql_to_Tbl | label_Tbl |
| 84 | 8 | 3 | charged_hadron | 0.5262 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 1 | 0 | muon | 5.8025 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 2 | 14 | photon | 0.8049 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 3 | 2 | charged_hadron | 0.6747 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 4 | 1 | neutral_hadron | 0.6687 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 5 | 4 | neutral_hadron | 0.6573 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 6 | 28 | charged_hadron | 0.6402 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 7 | 13 | charged_hadron | 0.6336 | B_Hqql_to_Tbl | label_Tbl |
| 86 | 8 | 12 | charged_hadron | 0.6293 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 1 | 0 | electron | 5.8067 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 2 | 14 | neutral_hadron | 0.6078 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 3 | 10 | charged_hadron | 0.5700 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 4 | 15 | charged_hadron | 0.5656 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 5 | 13 | neutral_hadron | 0.5646 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 6 | 7 | neutral_hadron | 0.5332 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 7 | 2 | neutral_hadron | 0.5122 | B_Hqql_to_Tbl | label_Tbl |
| 87 | 8 | 19 | photon | 0.5091 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 1 | 0 | muon | 5.7891 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 2 | 3 | neutral_hadron | 0.6407 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 3 | 1 | photon | 0.5030 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 4 | 2 | neutral_hadron | 0.5001 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 5 | 7 | charged_hadron | 0.4989 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 6 | 8 | charged_hadron | 0.4948 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 7 | 6 | photon | 0.4851 | B_Hqql_to_Tbl | label_Tbl |
| 88 | 8 | 4 | charged_hadron | 0.4746 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 1 | 0 | electron | 5.8671 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 2 | 1 | photon | 0.8217 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 3 | 36 | neutral_hadron | 0.6840 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 4 | 2 | neutral_hadron | 0.5782 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 5 | 8 | charged_hadron | 0.5453 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 6 | 34 | photon | 0.5296 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 7 | 4 | charged_hadron | 0.5293 | B_Hqql_to_Tbl | label_Tbl |
| 90 | 8 | 19 | charged_hadron | 0.5271 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 1 | 0 | muon | 5.7995 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 2 | 22 | photon | 0.6174 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 3 | 20 | photon | 0.6000 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 4 | 4 | charged_hadron | 0.5911 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 5 | 8 | charged_hadron | 0.5776 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 6 | 19 | photon | 0.5664 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 7 | 6 | charged_hadron | 0.5660 | B_Hqql_to_Tbl | label_Tbl |
| 96 | 8 | 3 | charged_hadron | 0.5593 | B_Hqql_to_Tbl | label_Tbl |

## Interpretation

This is the full all-head map for current ParT replay groups. Read it like the old supertrace: all heads are active together, gradients rank which head slices support the objective, and particle super-score shows where the weighted multi-head computation concentrates. Use this before single-route/bundle probes.
