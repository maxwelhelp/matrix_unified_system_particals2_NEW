# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.9907 | 0.0000 | 0.1402 | 0.8644 | -0.0251 | -0.0251 | 0 | 0.7396 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.6870 | 0.0000 | 0.0147 | 0.6340 | -0.0240 | -0.0240 | 0 | 0.5249 |
| 3 | mod.cls_blocks.0.attn.h6 | CLS<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2883 | 0.0000 | 0.2061 | 0.0144 | 0.0226 | 0.0226 | 0 | 0.2331 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1823 | 0.0000 | 0.2061 | 1.490e-08 | 0.0350 | 0.0350 | 0 | 0.1308 |
| 5 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.1535 | 0.0000 | 0.0688 | 0.1750 | -0.0251 | -0.0251 | 0 | 0.0925 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.1003 | 0.0000 | 0.0124 | 0.0553 | -0.0240 | -0.0240 | 0 | 0.0834 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0190 | 0.0000 | 0.0129 | 6.858e-05 | 0.0226 | 0.0226 | 0 | 0.0158 |
| 8 | mod.cls_blocks.0.attn.h6 | charged_hadron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0150 | 0.0000 | 0.0129 | 1.490e-08 | 0.0350 | 0.0350 | 0 | 0.0118 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1833 | -0.1833 | 0 | 1.192e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1833 | -0.1833 | 0 | 1.192e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1496 | -0.1496 | 0 | 1.192e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1496 | -0.1496 | 0 | 1.192e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1833 | -0.1833 | 0 | -8.941e-08 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1833 | -0.1833 | 0 | -8.941e-08 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1496 | -0.1496 | 0 | -8.941e-08 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.086e-07 | 0.0000 | 3.427e-07 | 1.490e-08 | -0.1496 | -0.1496 | 0 | -8.941e-08 |
