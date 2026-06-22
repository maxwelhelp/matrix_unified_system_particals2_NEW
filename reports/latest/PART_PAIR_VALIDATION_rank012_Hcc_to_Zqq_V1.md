# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.6378 | 0.0000 | 0.2553 | 1.1188 | 0.1759 | 0.1759 | 0 | 0.2943 |
| 2 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.2140 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1210 | 0.1210 | 0 | 0.2140 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.4700 | 0.4700 | 0 | 9.313e-09 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.3984 | 0.3984 | 0 | 9.313e-09 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.3558 | 0.3558 | 0 | 9.313e-09 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.2980 | 0.2980 | 0 | 9.313e-09 |
| 7 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1477 | 0.1477 | 0 | 9.313e-09 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1218 | 0.1218 | 0 | 9.313e-09 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.4700 | 0.4700 | 0 | -1.024e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.3984 | 0.3984 | 0 | -1.024e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.3558 | 0.3558 | 0 | -1.024e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.2980 | 0.2980 | 0 | -1.024e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1477 | 0.1477 | 0 | -1.024e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1218 | 0.1218 | 0 | -1.024e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.0345 | 0.0000 | 3.725e-08 | 3.725e-07 | 0.1210 | 0.1210 | 0 | -1.024e-07 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.1198 | 0.0000 | 0.1790 | 0.5488 | 0.1759 | 0.1759 | 0 | -0.1819 |
