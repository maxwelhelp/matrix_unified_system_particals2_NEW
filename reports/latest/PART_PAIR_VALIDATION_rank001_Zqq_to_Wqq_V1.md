# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1500 | 0.0000 | 0.1773 | 0.0305 | 0.0523 | 0.0523 | 0 | 0.0980 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.2074 | 0.0000 | 0.1725 | 0.4219 | 0.2304 | 0.2304 | 0 | 0.0588 |
| 3 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.8397 | 0.8397 | 0 | 1.676e-07 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.6916 | 0.6916 | 0 | 1.676e-07 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.6422 | 0.6422 | 0 | 1.676e-07 |
| 6 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1487 | 0.1487 | 0 | 1.676e-07 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1269 | 0.1269 | 0 | 1.676e-07 |
| 8 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1197 | 0.1197 | 0 | 1.676e-07 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.8397 | 0.8397 | 0 | -1.527e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.6916 | 0.6916 | 0 | -1.527e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.6422 | 0.6422 | 0 | -1.527e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1487 | 0.1487 | 0 | -1.527e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1269 | 0.1269 | 0 | -1.527e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -3.204e-07 | 0.0000 | 4.992e-07 | 1.118e-07 | 0.1197 | 0.1197 | 0 | -1.527e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1270 | 0.0000 | 0.6860 | 0.0359 | 0.0523 | 0.0523 | 0 | -0.0535 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.0110 | 0.0000 | 0.7188 | 0.1260 | 0.2304 | 0.2304 | 0 | -0.2112 |
