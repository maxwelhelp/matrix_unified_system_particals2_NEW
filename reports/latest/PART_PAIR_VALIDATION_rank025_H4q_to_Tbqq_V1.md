# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.5120 | 0.0000 | 0.1044 | 0.2088 | 0.0219 | 0.0219 | 0 | 0.4337 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0913 | 0.0000 | 0.0099 | 0.0062 | 0.0219 | 0.0219 | 0 | 0.0873 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | 0.0578 | 0.0578 | 0 | -1.006e-07 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | 0.0343 | 0.0343 | 0 | -1.006e-07 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.6735 | -0.6735 | 0 | -1.006e-07 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.3573 | -0.3573 | 0 | -1.006e-07 |
| 7 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.3326 | -0.3326 | 0 | -1.006e-07 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.1868 | -0.1868 | 0 | -1.006e-07 |
| 9 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.1072 | -0.1072 | 0 | -1.006e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | 0.0578 | 0.0578 | 0 | -1.080e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | 0.0343 | 0.0343 | 0 | -1.080e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.6735 | -0.6735 | 0 | -1.080e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.3573 | -0.3573 | 0 | -1.080e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.3326 | -0.3326 | 0 | -1.080e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.1868 | -0.1868 | 0 | -1.080e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 8.941e-08 | 3.427e-07 | -0.1072 | -0.1072 | 0 | -1.080e-07 |
