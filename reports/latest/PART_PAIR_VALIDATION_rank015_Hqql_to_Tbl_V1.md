# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -1.4079 | -0.3750 | 0.2273 | 4.2766 | -0.4600 | -0.4600 | 0 | 1.0320 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.2846 | 0.0000 | 0.5503 | 0.8239 | -0.4600 | -0.4600 | 0 | 0.9410 |
| 3 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1714 | -0.0625 | 0.0228 | 0.1865 | 0.0453 | 0.0453 | 0 | 0.2441 |
| 4 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2564 | 0.0000 | 0.0242 | 0.0705 | 0.0255 | 0.0255 | 0 | 0.2327 |
| 5 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2380 | 0.0000 | 0.0555 | 0.0124 | 0.0453 | 0.0453 | 0 | 0.2210 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0520 | 0.0000 | 0.0017 | 0.0064 | 0.0255 | 0.0255 | 0 | 0.0500 |
| 7 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5568 | -0.5568 | 0 | -1.118e-07 |
| 8 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5568 | -0.5568 | 0 | -1.118e-07 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5465 | -0.5465 | 0 | -1.118e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5465 | -0.5465 | 0 | -1.118e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | muon<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5361 | -0.5361 | 0 | -1.118e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | muon<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.5361 | -0.5361 | 0 | -1.118e-07 |
| 13 | mod.cls_blocks.0.attn.h6 | electron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.2968 | -0.2968 | 0 | -1.118e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | electron<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.2968 | -0.2968 | 0 | -1.118e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.2700 | -0.2700 | 0 | -1.118e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 0 | 40.0000 | 0.0000 | 0.0000 | 8.941e-08 | 3.576e-07 | -0.2700 | -0.2700 | 0 | -1.118e-07 |
