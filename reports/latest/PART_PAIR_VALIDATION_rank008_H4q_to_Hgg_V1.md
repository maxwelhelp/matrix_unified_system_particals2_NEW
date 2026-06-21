# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | weak_or_distributed | up | 1 | 40.0000 | -0.3685 | 0.0000 | 0.2144 | 0.3265 | -0.0134 | -0.0134 | 0 | 0.2332 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | weak_or_distributed | down | 1 | 40.0000 | 0.1846 | 0.0000 | 0.1497 | 0.1959 | -0.0134 | -0.0134 | 0 | 0.0982 |
| 3 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0525 | 0.0000 | 0.0084 | 1.490e-08 | 0.0352 | 0.0352 | 0 | 0.0504 |
| 4 | mod.cls_blocks.0.attn.h7 | neutral_hadron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0049 | 0.0000 | 2.221e-04 | 1.490e-08 | 0.0352 | 0.0352 | 0 | 0.0049 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.1752 | -0.1752 | 0 | -2.794e-08 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.1365 | -0.1365 | 0 | -2.794e-08 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0637 | -0.0637 | 0 | -2.794e-08 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0528 | -0.0528 | 0 | -2.794e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0204 | -0.0204 | 0 | -2.794e-08 |
| 10 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0202 | -0.0202 | 0 | -2.794e-08 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.1752 | -0.1752 | 0 | -5.774e-08 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.1365 | -0.1365 | 0 | -5.774e-08 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0637 | -0.0637 | 0 | -5.774e-08 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0528 | -0.0528 | 0 | -5.774e-08 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0204 | -0.0204 | 0 | -5.774e-08 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.980e-08 | 0.0000 | 2.161e-07 | 1.490e-08 | -0.0202 | -0.0202 | 0 | -5.774e-08 |
