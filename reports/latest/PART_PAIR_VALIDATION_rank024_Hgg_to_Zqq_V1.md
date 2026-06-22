# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 1.4209 | 1.4209 | 0 | 1.071e-07 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 1.0000 | 1.0000 | 0 | 1.071e-07 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.7485 | 0.7485 | 0 | 1.071e-07 |
| 4 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.4621 | 0.4621 | 0 | 1.071e-07 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.4098 | 0.4098 | 0 | 1.071e-07 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.3567 | 0.3567 | 0 | 1.071e-07 |
| 7 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.2723 | 0.2723 | 0 | 1.071e-07 |
| 8 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.2305 | 0.2305 | 0 | 1.071e-07 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 1.4209 | 1.4209 | 0 | -1.760e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 1.0000 | 1.0000 | 0 | -1.760e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.7485 | 0.7485 | 0 | -1.760e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.4621 | 0.4621 | 0 | -1.760e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.4098 | 0.4098 | 0 | -1.760e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.3567 | 0.3567 | 0 | -1.760e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.2723 | 0.2723 | 0 | -1.760e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 3.055e-07 | 3.986e-07 | 0.2305 | 0.2305 | 0 | -1.760e-07 |
