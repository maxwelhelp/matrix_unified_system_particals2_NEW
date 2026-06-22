# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.6067 | 0.0000 | 0.1757 | 0.2979 | 0.0970 | 0.0970 | 0 | 0.4883 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2088 | 0.0000 | 0.0106 | 0.0150 | 0.0850 | 0.0850 | 0 | 0.2024 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2630 | 0.0000 | 0.3968 | 0.0150 | 0.0514 | 0.0514 | 0 | 0.1600 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0246 | 0.0000 | 0.0039 | 0.0013 | 0.0850 | 0.0850 | 0 | 0.0233 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.9810 | 0.9810 | 0 | -5.960e-08 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.5133 | 0.5133 | 0 | -5.960e-08 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.2472 | 0.2472 | 0 | -5.960e-08 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.1771 | 0.1771 | 0 | -5.960e-08 |
| 9 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.1201 | 0.1201 | 0 | -5.960e-08 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.9810 | 0.9810 | 0 | -1.192e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.5133 | 0.5133 | 0 | -1.192e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.2472 | 0.2472 | 0 | -1.192e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.1771 | 0.1771 | 0 | -1.192e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -5.960e-08 | 0.0000 | 1.937e-07 | 2.831e-07 | 0.1201 | 0.1201 | 0 | -1.192e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0290 | 0.0000 | 0.1354 | 0.0013 | 0.0514 | 0.0514 | 0 | -0.0052 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1735 | 0.0000 | 1.2304 | 0.4538 | 0.0970 | 0.0970 | 0 | -0.2476 |
