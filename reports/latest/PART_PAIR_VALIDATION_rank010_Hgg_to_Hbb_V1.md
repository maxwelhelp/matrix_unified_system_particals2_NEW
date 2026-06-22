# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | weak_or_distributed | up | 1 | 40.0000 | 0.3615 | 0.0000 | 0.6232 | 0.0360 | 0.0105 | 0.0105 | 0 | 0.1967 |
| 2 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | weak_or_distributed | down | 1 | 40.0000 | -0.1576 | 0.0000 | 0.1226 | 0.0190 | 0.0105 | 0.0105 | 0 | 0.1222 |
| 3 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1712 | 0.1712 | 0 | -4.843e-08 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1668 | 0.1668 | 0 | -4.843e-08 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1517 | 0.1517 | 0 | -4.843e-08 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1404 | 0.1404 | 0 | -4.843e-08 |
| 7 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1338 | 0.1338 | 0 | -4.843e-08 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1105 | 0.1105 | 0 | -4.843e-08 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.0304 | 0.0304 | 0 | -4.843e-08 |
| 10 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1712 | 0.1712 | 0 | -9.313e-08 |
| 11 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1668 | 0.1668 | 0 | -9.313e-08 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1517 | 0.1517 | 0 | -9.313e-08 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1404 | 0.1404 | 0 | -9.313e-08 |
| 14 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1338 | 0.1338 | 0 | -9.313e-08 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.1105 | 0.1105 | 0 | -9.313e-08 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 4.470e-08 | 0.0000 | 1.192e-07 | 2.533e-07 | 0.0304 | 0.0304 | 0 | -9.313e-08 |
