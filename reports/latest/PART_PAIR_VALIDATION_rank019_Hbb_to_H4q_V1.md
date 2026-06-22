# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.5688 | 0.0000 | 0.2134 | 0.1151 | 0.0450 | 0.0450 | 0 | 0.4867 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.7067 | 0.7067 | 0 | -3.725e-08 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.4105 | 0.4105 | 0 | -3.725e-08 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.1692 | 0.1692 | 0 | -3.725e-08 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.1143 | 0.1143 | 0 | -3.725e-08 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0768 | 0.0768 | 0 | -3.725e-08 |
| 7 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0477 | 0.0477 | 0 | -3.725e-08 |
| 8 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0405 | 0.0405 | 0 | -3.725e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.7067 | 0.7067 | 0 | -2.235e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.4105 | 0.4105 | 0 | -2.235e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.1692 | 0.1692 | 0 | -2.235e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.1143 | 0.1143 | 0 | -2.235e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0768 | 0.0768 | 0 | -2.235e-07 |
| 14 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0477 | 0.0477 | 0 | -2.235e-07 |
| 15 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.863e-07 | 0.0000 | 6.706e-07 | 2.235e-07 | 0.0405 | 0.0405 | 0 | -2.235e-07 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.3303 | 0.0000 | 0.8761 | 0.5393 | 0.0450 | 0.0450 | 0 | -0.3539 |
