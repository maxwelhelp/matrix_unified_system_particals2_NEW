# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h6 | muon<-muon | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -1.4327 | 0.0000 | 0.2148 | 0.6266 | -0.2745 | -0.2745 | 0 | 1.2224 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -0.7682 | 0.0000 | 0.0235 | 0.5621 | -0.7200 | -0.7200 | 0 | 0.6218 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.5805 | 0.0000 | 0.2213 | 0.0264 | -0.7200 | -0.7200 | 0 | 0.5186 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.5550 | 0.0000 | 0.1977 | 0.0374 | 0.0230 | 0.0230 | 0 | 0.4962 |
| 5 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.2730 | 0.0000 | 5.066e-07 | 0.0710 | 0.0288 | 0.0288 | 0 | 0.2552 |
| 6 | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.2945 | 0.0000 | 0.0315 | 0.1383 | 0.0230 | 0.0230 | 0 | 0.2520 |
| 7 | mod.cls_blocks.0.attn.h6 | muon<-muon | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.2376 | 0.0000 | 0.0744 | 0.0146 | -0.2745 | -0.2745 | 0 | 0.2153 |
| 8 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1528 | 0.0000 | 0.0422 | 0.0349 | 0.0235 | 0.0235 | 0 | 0.1335 |
| 9 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0439 | 0.0000 | 5.066e-07 | 4.470e-08 | 0.0205 | 0.0205 | 0 | 0.0439 |
| 10 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0354 | 0.0000 | 5.066e-07 | 4.470e-08 | 0.0312 | 0.0312 | 0 | 0.0354 |
| 11 | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0374 | 0.0000 | 0.0080 | 0.0050 | 0.0235 | 0.0235 | 0 | 0.0341 |
| 12 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0174 | 0.0000 | 5.066e-07 | 4.470e-08 | 0.0312 | 0.0312 | 0 | 0.0174 |
| 13 | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0106 | 0.0000 | 5.066e-07 | 4.470e-08 | 0.0205 | 0.0205 | 0 | 0.0106 |
| 14 | mod.blocks.6.attn.h1 | muon<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0066 | 0.0000 | 5.066e-07 | 2.084e-04 | 0.0210 | 0.0210 | 0 | 0.0065 |
| 15 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0069 | 0.0000 | 5.066e-07 | 0.0016 | 0.0288 | 0.0288 | 0 | 0.0065 |
| 16 | mod.blocks.6.attn.h1 | muon<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0043 | 0.0000 | 5.066e-07 | 5.466e-04 | 0.0210 | 0.0210 | 0 | 0.0041 |
