# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1604 | 0.1604 | 0 | 3.502e-07 |
| 2 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1573 | 0.1573 | 0 | 3.502e-07 |
| 3 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1492 | 0.1492 | 0 | 3.502e-07 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1208 | 0.1208 | 0 | 3.502e-07 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1176 | 0.1176 | 0 | 3.502e-07 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1129 | 0.1129 | 0 | 3.502e-07 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.0495 | 0.0495 | 0 | 3.502e-07 |
| 8 | mod.cls_blocks.0.attn.h0 | photon<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.0372 | 0.0372 | 0 | 3.502e-07 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1604 | 0.1604 | 0 | -1.043e-07 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1573 | 0.1573 | 0 | -1.043e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1492 | 0.1492 | 0 | -1.043e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1208 | 0.1208 | 0 | -1.043e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1176 | 0.1176 | 0 | -1.043e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.1129 | 0.1129 | 0 | -1.043e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.0495 | 0.0495 | 0 | -1.043e-07 |
| 16 | mod.cls_blocks.0.attn.h0 | photon<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -4.545e-07 | 0.0000 | 1.043e-07 | 3.129e-07 | 0.0372 | 0.0372 | 0 | -1.043e-07 |
