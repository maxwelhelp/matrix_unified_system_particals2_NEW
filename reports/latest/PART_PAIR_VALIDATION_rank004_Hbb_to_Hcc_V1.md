# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.1649 | 0.1649 | 0 | -4.098e-08 |
| 2 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0804 | 0.0804 | 0 | -4.098e-08 |
| 3 | mod.cls_blocks.0.attn.h0 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0618 | 0.0618 | 0 | -4.098e-08 |
| 4 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0509 | 0.0509 | 0 | -4.098e-08 |
| 5 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0506 | 0.0506 | 0 | -4.098e-08 |
| 6 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0404 | 0.0404 | 0 | -4.098e-08 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0389 | 0.0389 | 0 | -4.098e-08 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0365 | 0.0365 | 0 | -4.098e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.1649 | 0.1649 | 0 | -1.155e-07 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0804 | 0.0804 | 0 | -1.155e-07 |
| 11 | mod.cls_blocks.0.attn.h0 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0618 | 0.0618 | 0 | -1.155e-07 |
| 12 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0509 | 0.0509 | 0 | -1.155e-07 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0506 | 0.0506 | 0 | -1.155e-07 |
| 14 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0404 | 0.0404 | 0 | -1.155e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0389 | 0.0389 | 0 | -1.155e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 7.451e-08 | 0.0000 | 3.353e-07 | 1.267e-07 | 0.0365 | 0.0365 | 0 | -1.155e-07 |
