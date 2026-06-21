# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.7199 | 0.0000 | 0.0101 | 0.6230 | 0.0228 | 0.0228 | 0 | 0.5616 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.6279 | 0.0000 | 0.0172 | 0.4333 | 0.0201 | 0.0201 | 0 | 0.5153 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.6431 | 0.0000 | 0.1260 | 0.7188 | -0.1879 | -0.1879 | 0 | 0.4319 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.4370 | 0.0000 | 0.2885 | 0.1895 | 0.0228 | 0.0228 | 0 | 0.3175 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.4671 | 0.0000 | 0.4834 | 0.2287 | 0.0201 | 0.0201 | 0 | 0.2891 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.4240 | 0.0000 | 0.4219 | 0.1725 | -0.1879 | -0.1879 | 0 | 0.2754 |
| 7 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1020 | 0.0000 | 2.012e-07 | 2.608e-08 | 0.0613 | 0.0613 | 0 | 0.1020 |
| 8 | mod.cls_blocks.0.attn.h0 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1158 | 0.0000 | 2.012e-07 | 0.4219 | 0.0348 | 0.0348 | 0 | 0.0104 |
| 9 | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0101 | 0.0000 | 2.012e-07 | 2.608e-08 | 0.0613 | 0.0613 | 0 | 0.0101 |
| 10 | mod.cls_blocks.0.attn.h0 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0108 | 0.0000 | 2.012e-07 | 0.0194 | 0.0348 | 0.0348 | 0 | 0.0060 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.7573 | -0.7573 | 0 | 2.114e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.7030 | -0.7030 | 0 | 2.114e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.6487 | -0.6487 | 0 | 2.114e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.7573 | -0.7573 | 0 | -5.681e-08 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.7030 | -0.7030 | 0 | -5.681e-08 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -2.682e-07 | 0.0000 | 2.012e-07 | 2.608e-08 | -0.6487 | -0.6487 | 0 | -5.681e-08 |
