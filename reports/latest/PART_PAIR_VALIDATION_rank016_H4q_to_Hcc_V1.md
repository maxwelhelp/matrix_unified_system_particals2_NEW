# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.3384 | 0.0000 | 0.1039 | 0.0536 | -0.0347 | -0.0347 | 0 | 0.2991 |
| 2 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0573 | 0.0000 | 0.0831 | 3.576e-07 | 0.0234 | 0.0234 | 0 | 0.0365 |
| 3 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0063 | 0.0000 | 2.199e-04 | 3.576e-07 | 0.0234 | 0.0234 | 0 | 0.0063 |
| 4 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.1123 | 0.1123 | 0 | -9.499e-08 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0809 | 0.0809 | 0 | -9.499e-08 |
| 6 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0704 | 0.0704 | 0 | -9.499e-08 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0586 | 0.0586 | 0 | -9.499e-08 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | -0.0432 | -0.0432 | 0 | -9.499e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | weak_or_distributed | down | 1 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | -0.0177 | -0.0177 | 0 | -9.499e-08 |
| 10 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.1123 | 0.1123 | 0 | -1.248e-07 |
| 11 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0809 | 0.0809 | 0 | -1.248e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | photon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0704 | 0.0704 | 0 | -1.248e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | 0.0586 | 0.0586 | 0 | -1.248e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | -0.0432 | -0.0432 | 0 | -1.248e-07 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | weak_or_distributed | up | 0 | 40.0000 | 2.980e-08 | 0.0000 | 1.416e-07 | 3.576e-07 | -0.0177 | -0.0177 | 0 | -1.248e-07 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.4596 | 0.0000 | 0.5836 | 0.0625 | -0.0347 | -0.0347 | 0 | -0.1615 |
