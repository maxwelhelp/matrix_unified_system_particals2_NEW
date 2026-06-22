# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.5397 | 0.0000 | 0.3796 | 0.2444 | 0.0225 | 0.0225 | 0 | 0.3837 |
| 2 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.6068 | 0.0000 | 0.7522 | 0.2195 | 0.0351 | 0.0351 | 0 | 0.3639 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.4713 | 0.0000 | 0.1295 | 0.4948 | 0.0365 | 0.0365 | 0 | 0.3152 |
| 4 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2124 | 0.0000 | 0.0892 | 0.0133 | 0.0249 | 0.0249 | 0 | 0.1867 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.4614 | 0.0000 | 1.0372 | 0.1351 | 0.0365 | 0.0365 | 0 | 0.1683 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1807 | 0.0000 | 0.0102 | 0.0869 | 0.0225 | 0.0225 | 0 | 0.1564 |
| 7 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1731 | 0.0000 | 0.0496 | 0.0510 | 0.0423 | 0.0423 | 0 | 0.1479 |
| 8 | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1440 | 0.0000 | 0.0054 | 0.0281 | 0.0351 | 0.0351 | 0 | 0.1357 |
| 9 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0202 | 0.0000 | 0.0020 | 2.817e-04 | 0.0249 | 0.0249 | 0 | 0.0196 |
| 10 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0171 | 0.0000 | 0.0096 | 0.0011 | 0.0306 | 0.0306 | 0 | 0.0145 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0122 | 0.0000 | 6.922e-04 | 6.692e-04 | 0.0423 | 0.0423 | 0 | 0.0119 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -2.906e-07 | 0.0000 | 3.241e-07 | 2.831e-07 | 0.4448 | 0.4448 | 0 | 1.388e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | down | 1 | 40.0000 | -2.906e-07 | 0.0000 | 3.241e-07 | 2.831e-07 | 0.1455 | 0.1455 | 0 | 1.388e-07 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -2.906e-07 | 0.0000 | 3.241e-07 | 2.831e-07 | 0.4448 | 0.4448 | 0 | -1.518e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_push_read_write | up | 0 | 40.0000 | -2.906e-07 | 0.0000 | 3.241e-07 | 2.831e-07 | 0.1455 | 0.1455 | 0 | -1.518e-07 |
| 16 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | B_Tbl_push_read_write | up | 0 | 40.0000 | -0.0324 | 0.0000 | 0.0990 | 0.0246 | 0.0306 | 0.0306 | 0 | -0.0309 |
