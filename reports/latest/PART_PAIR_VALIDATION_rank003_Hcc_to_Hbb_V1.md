# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.4486 | 0.0000 | 8.196e-08 | 0.6314 | -0.1675 | -0.1675 | 0 | 0.2908 |
| 2 | mod.cls_blocks.0.attn.h1 | electron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1132 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0435 | 0.0435 | 0 | 0.1132 |
| 3 | mod.cls_blocks.0.attn.h0 | electron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0533 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0745 | 0.0745 | 0 | 0.0533 |
| 4 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.0601 | 0.0000 | 8.196e-08 | 0.1088 | -0.1675 | -0.1675 | 0 | 0.0329 |
| 5 | mod.cls_blocks.0.attn.h1 | electron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0215 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0435 | 0.0435 | 0 | 0.0215 |
| 6 | mod.cls_blocks.0.attn.h1 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0215 | 0.0000 | 0.0022 | 0.0093 | 0.0435 | 0.0435 | 0 | 0.0187 |
| 7 | mod.cls_blocks.1.attn.h3 | electron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0174 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0492 | 0.0492 | 0 | 0.0174 |
| 8 | mod.cls_blocks.1.attn.h3 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0174 | 0.0000 | 1.258e-04 | 4.418e-05 | 0.0492 | 0.0492 | 0 | 0.0173 |
| 9 | mod.cls_blocks.0.attn.h0 | electron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0167 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0745 | 0.0745 | 0 | 0.0167 |
| 10 | mod.cls_blocks.0.attn.h0 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0167 | 0.0000 | 1.628e-04 | 0.0281 | 0.0745 | 0.0745 | 0 | 0.0096 |
| 11 | mod.cls_blocks.1.attn.h3 | electron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 9.989e-05 | 0.0000 | 8.196e-08 | 2.459e-07 | 0.0492 | 0.0492 | 0 | 9.981e-05 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 3.204e-07 | 0.0000 | 8.196e-08 | 2.459e-07 | -0.1377 | -0.1377 | 0 | 2.384e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 3.204e-07 | 0.0000 | 8.196e-08 | 2.459e-07 | -0.1377 | -0.1377 | 0 | -8.196e-08 |
| 14 | mod.cls_blocks.1.attn.h3 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 9.989e-05 | 0.0000 | 0.0013 | 0.0685 | 0.0492 | 0.0492 | 0 | -0.0174 |
| 15 | mod.cls_blocks.0.attn.h1 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1132 | 0.0000 | 0.1802 | 0.3477 | 0.0435 | 0.0435 | 0 | -0.0187 |
| 16 | mod.cls_blocks.0.attn.h0 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0533 | 0.0000 | 0.0834 | 0.8788 | 0.0745 | 0.0745 | 0 | -0.1872 |
