# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.8494 | 0.0000 | 0.5507 | 0.9342 | -0.0386 | -0.0386 | 0 | 0.4782 |
| 2 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.0866 | 0.0000 | 0.0756 | 0.1149 | -0.0293 | -0.0293 | 0 | 0.0390 |
| 3 | mod.cls_blocks.0.attn.h2 | charged_hadron<-muon | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.0042 | 0.0000 | 0.0016 | 0.0017 | -0.0293 | -0.0293 | 0 | 0.0034 |
| 4 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0016 | 0.0000 | 0.0013 | 0.0011 | 0.0208 | 0.0208 | 0 | 0.0011 |
| 5 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | 0.0296 | 0.0296 | 0 | 1.490e-08 |
| 6 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | 0.0252 | 0.0252 | 0 | 1.490e-08 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0619 | -0.0619 | 0 | 1.490e-08 |
| 8 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0459 | -0.0459 | 0 | 1.490e-08 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0232 | -0.0232 | 0 | 1.490e-08 |
| 10 | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | 0.0296 | 0.0296 | 0 | -2.682e-07 |
| 11 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | 0.0252 | 0.0252 | 0 | -2.682e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0619 | -0.0619 | 0 | -2.682e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0459 | -0.0459 | 0 | -2.682e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 2.831e-07 | 0.0000 | 1.013e-06 | 5.960e-08 | -0.0232 | -0.0232 | 0 | -2.682e-07 |
| 15 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0467 | 0.0000 | 0.0879 | 0.3030 | 0.0208 | 0.0208 | 0 | -0.0510 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -0.0531 | 0.0000 | 0.4481 | 0.0808 | -0.0386 | -0.0386 | 0 | -0.1322 |
