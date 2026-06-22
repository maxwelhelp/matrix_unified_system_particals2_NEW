# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.7533 | 0.0000 | 0.1015 | 0.1596 | 0.0610 | 0.0610 | 0 | 0.6880 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.7186 | 0.0000 | 1.4800 | 0.2234 | 0.0511 | 0.0511 | 0 | 0.2928 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.3000 | 0.0000 | 0.0290 | 0.1610 | 0.0435 | 0.0435 | 0 | 0.2525 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1982 | 0.0000 | 0.0073 | 0.1801 | 0.0610 | 0.0610 | 0 | 0.1513 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.4441 | 0.0000 | 0.3246 | 0.9930 | 0.0511 | 0.0511 | 0 | 0.1147 |
| 6 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0274 | 0.0000 | 0.0062 | 0.0236 | 0.0204 | 0.0204 | 0 | 0.0200 |
| 7 | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0923 | 0.0000 | 0.2517 | 0.0663 | 0.0204 | 0.0204 | 0 | 0.0128 |
| 8 | mod.cls_blocks.1.attn.h2 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | 0.0239 | 0.0239 | 0 | -2.421e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -1.2670 | -1.2670 | 0 | -2.421e-08 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -0.7504 | -0.7504 | 0 | -2.421e-08 |
| 11 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -0.6762 | -0.6762 | 0 | -2.421e-08 |
| 12 | mod.cls_blocks.1.attn.h2 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | 0.0239 | 0.0239 | 0 | -1.024e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -1.2670 | -1.2670 | 0 | -1.024e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -0.7504 | -0.7504 | 0 | -1.024e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.823e-08 | 0.0000 | 3.427e-07 | 6.706e-08 | -0.6762 | -0.6762 | 0 | -1.024e-07 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1293 | 0.0000 | 0.9205 | 0.2300 | 0.0435 | 0.0435 | 0 | -0.1584 |
