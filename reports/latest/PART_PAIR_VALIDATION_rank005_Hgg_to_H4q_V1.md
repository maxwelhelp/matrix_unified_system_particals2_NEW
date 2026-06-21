# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | weak_or_distributed | down | 1 | 40.0000 | -0.1146 | 0.0000 | 0.1959 | 0.1497 | 0.0161 | 0.0161 | 0 | 0.0282 |
| 2 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.1364 | 0.1364 | 0 | 2.887e-07 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.1111 | 0.1111 | 0 | 2.887e-07 |
| 4 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0859 | 0.0859 | 0 | 2.887e-07 |
| 5 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0692 | 0.0692 | 0 | 2.887e-07 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0496 | 0.0496 | 0 | 2.887e-07 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0300 | 0.0300 | 0 | 2.887e-07 |
| 8 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | weak_or_distributed | up | 1 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0128 | 0.0128 | 0 | 2.887e-07 |
| 9 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.1364 | 0.1364 | 0 | -9.872e-08 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.1111 | 0.1111 | 0 | -9.872e-08 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0859 | 0.0859 | 0 | -9.872e-08 |
| 12 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0692 | 0.0692 | 0 | -9.872e-08 |
| 13 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0496 | 0.0496 | 0 | -9.872e-08 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0300 | 0.0300 | 0 | -9.872e-08 |
| 15 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | weak_or_distributed | down | 0 | 40.0000 | 3.874e-07 | 0.0000 | 1.416e-07 | 2.533e-07 | 0.0128 | 0.0128 | 0 | -9.872e-08 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | weak_or_distributed | up | 0 | 40.0000 | -0.1933 | 0.0000 | 0.3265 | 0.2144 | 0.0161 | 0.0161 | 0 | -0.1352 |
