# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **96**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | weak_or_distributed | down | 1 | 40.0000 | -1.3754 | 0.0000 | 0.2133 | 1.6331 | 0.0190 | 0.0190 | 0 | 0.9138 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | weak_or_distributed | down | 1 | 40.0000 | -1.3155 | 0.0000 | 1.1089 | 1.6334 | 0.0059 | 0.0059 | 0 | 0.6299 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-photon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.6371 | 0.0000 | 0.6317 | 0.4325 | 0.0267 | 0.0267 | 0 | 0.3711 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.4505 | 0.0000 | 0.5567 | 0.1988 | -0.0263 | -0.0263 | 0 | 0.2616 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.3192 | 0.0000 | 0.1246 | 0.3151 | 0.0989 | 0.0989 | 0 | 0.2093 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | weak_or_distributed | down | 1 | 40.0000 | -0.2110 | 0.0000 | 0.0235 | 0.2274 | 0.0079 | 0.0079 | 0 | 0.1483 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0963 | 0.0000 | 0.1447 | 0.0178 | 0.0259 | 0.0259 | 0 | 0.0556 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.0642 | 0.0000 | 0.0464 | 0.0470 | -0.0263 | -0.0263 | 0 | 0.0408 |
| 9 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | weak_or_distributed | down | 1 | 40.0000 | -0.0365 | 0.0000 | 0.0035 | 0.0108 | 0.0151 | 0.0151 | 0 | 0.0329 |
| 10 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | weak_or_distributed | up | 1 | 40.0000 | 0.1211 | 0.0000 | 0.7082 | 0.0323 | 0.0151 | 0.0151 | 0 | -0.0640 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-photon | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.0488 | 0.0000 | 0.5631 | 0.0070 | 0.0267 | 0.0267 | 0 | -0.1425 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | weak_or_distributed | up | 0 | 40.0000 | -0.0308 | 0.0000 | 0.5536 | 0.1142 | 0.0190 | 0.0190 | 0 | -0.1670 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.0184 | 0.0000 | 0.7128 | 0.0334 | 0.0259 | 0.0259 | 0 | -0.1866 |
| 14 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.1668 | 0.0000 | 0.7163 | 0.1098 | 0.0989 | 0.0989 | 0 | -0.2065 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | weak_or_distributed | up | 0 | 40.0000 | -1.0059 | 0.0000 | 0.3954 | 0.7622 | 0.0059 | 0.0059 | 0 | -0.2894 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | weak_or_distributed | up | 0 | 40.0000 | -1.9841 | 0.0000 | 0.2490 | 1.4137 | 0.0079 | 0.0079 | 0 | -0.4157 |
