# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0517 | 0.0000 | 0.0536 | 0.1039 | 0.0207 | 0.0207 | 0 | 0.0123 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | 0.2539 | 0.2539 | 0 | -5.960e-08 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | 0.0909 | 0.0909 | 0 | -5.960e-08 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.1378 | -0.1378 | 0 | -5.960e-08 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.1002 | -0.1002 | 0 | -5.960e-08 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0992 | -0.0992 | 0 | -5.960e-08 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0506 | -0.0506 | 0 | -5.960e-08 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0439 | -0.0439 | 0 | -5.960e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | 0.2539 | 0.2539 | 0 | -1.714e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | 0.0909 | 0.0909 | 0 | -1.714e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.1378 | -0.1378 | 0 | -1.714e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.1002 | -0.1002 | 0 | -1.714e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0992 | -0.0992 | 0 | -1.714e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0506 | -0.0506 | 0 | -1.714e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 1.118e-07 | 0.0000 | 6.557e-07 | 2.980e-08 | -0.0439 | -0.0439 | 0 | -1.714e-07 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.3167 | 0.0000 | 0.0625 | 0.5836 | 0.0207 | 0.0207 | 0 | -0.1615 |
