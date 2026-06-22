# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | photon<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1522 | 0.0000 | 0.0477 | 2.086e-07 | 0.0321 | 0.0321 | 0 | 0.1403 |
| 2 | mod.cls_blocks.0.attn.h4 | photon<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0093 | 0.0000 | 0.0038 | 2.086e-07 | 0.0321 | 0.0321 | 0 | 0.0084 |
| 3 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.9473 | -0.9473 | 0 | -2.347e-07 |
| 4 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.6079 | -0.6079 | 0 | -2.347e-07 |
| 5 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.5028 | -0.5028 | 0 | -2.347e-07 |
| 6 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.4789 | -0.4789 | 0 | -2.347e-07 |
| 7 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2534 | -0.2534 | 0 | -2.347e-07 |
| 8 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2187 | -0.2187 | 0 | -2.347e-07 |
| 9 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2186 | -0.2186 | 0 | -2.347e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.9473 | -0.9473 | 0 | -2.421e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.6079 | -0.6079 | 0 | -2.421e-07 |
| 12 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.5028 | -0.5028 | 0 | -2.421e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | photon<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.4789 | -0.4789 | 0 | -2.421e-07 |
| 14 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2534 | -0.2534 | 0 | -2.421e-07 |
| 15 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2187 | -0.2187 | 0 | -2.421e-07 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | B_Tbl_resist_or_protective_read_write | down | 0 | 40.0000 | -7.451e-09 | 0.0000 | 7.600e-07 | 2.086e-07 | -0.2186 | -0.2186 | 0 | -2.421e-07 |
