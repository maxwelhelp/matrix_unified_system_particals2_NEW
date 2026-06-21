# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.4548 | -0.4548 | 0 | -9.686e-08 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.3269 | -0.3269 | 0 | -9.686e-08 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.2648 | -0.2648 | 0 | -9.686e-08 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.2078 | -0.2078 | 0 | -9.686e-08 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1541 | -0.1541 | 0 | -9.686e-08 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1471 | -0.1471 | 0 | -9.686e-08 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1388 | -0.1388 | 0 | -9.686e-08 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1133 | -0.1133 | 0 | -9.686e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.4548 | -0.4548 | 0 | -1.416e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.3269 | -0.3269 | 0 | -1.416e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.2648 | -0.2648 | 0 | -1.416e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.2078 | -0.2078 | 0 | -1.416e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1541 | -0.1541 | 0 | -1.416e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1471 | -0.1471 | 0 | -1.416e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1388 | -0.1388 | 0 | -1.416e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 4.470e-08 | 0.0000 | 4.321e-07 | 1.341e-07 | -0.1133 | -0.1133 | 0 | -1.416e-07 |
