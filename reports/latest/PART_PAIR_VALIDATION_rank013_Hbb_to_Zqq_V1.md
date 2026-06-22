# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -2.5652 | 0.0000 | 0.0813 | 1.2303 | 0.2288 | 0.2288 | 0 | 2.2373 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -2.4556 | 0.0000 | 0.1325 | 1.2162 | 0.1340 | 0.1340 | 0 | 2.1185 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.5487 | 0.0000 | 1.1005 | 0.3298 | 0.2288 | 0.2288 | 0 | 0.1911 |
| 4 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1982 | 0.0000 | 0.3131 | 2.682e-07 | 0.2892 | 0.2892 | 0 | 0.1199 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.5395 | 0.5395 | 0 | -7.078e-08 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.4769 | 0.4769 | 0 | -7.078e-08 |
| 7 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.2892 | 0.2892 | 0 | -7.078e-08 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.2061 | 0.2061 | 0 | -7.078e-08 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.1701 | 0.1701 | 0 | -7.078e-08 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.5395 | 0.5395 | 0 | -1.751e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.4769 | 0.4769 | 0 | -1.751e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.2892 | 0.2892 | 0 | -1.751e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.2061 | 0.2061 | 0 | -1.751e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -1.043e-07 | 0.0000 | 4.321e-07 | 2.682e-07 | 0.1701 | 0.1701 | 0 | -1.751e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0360 | 0.0000 | 0.4377 | 2.682e-07 | 0.2892 | 0.2892 | 0 | -0.0734 |
| 16 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.6618 | 0.0000 | 1.3919 | 1.4367 | 0.1340 | 0.1340 | 0 | -0.7072 |
