# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **64**
- candidates_tested: **8**
- rows: **16**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | CLS<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.8186 | -0.3125 | 0.6804 | 0.5612 | 0.3179 | 0.3179 | 0 | 1.1331 |
| 2 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.8177 | -0.3125 | 0.8239 | 0.5503 | 0.3699 | 0.3699 | 0 | 1.0992 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.9261 | -0.1875 | 0.5774 | 1.8199 | 0.1808 | 0.1808 | 0 | 0.7018 |
| 4 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.9290 | -0.1875 | 0.6598 | 1.8168 | 0.2365 | 0.2365 | 0 | 0.6848 |
| 5 | mod.cls_blocks.0.attn.h4 | muon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.3070 | 0.3070 | 0 | -5.960e-08 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2573 | 0.2573 | 0 | -5.960e-08 |
| 7 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2407 | 0.2407 | 0 | -5.960e-08 |
| 8 | mod.cls_blocks.0.attn.h6 | muon<-CLS | B_Tbl_push_read_write | up | 1 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2181 | 0.2181 | 0 | -5.960e-08 |
| 9 | mod.cls_blocks.0.attn.h4 | muon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.3070 | 0.3070 | 0 | -1.490e-07 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2573 | 0.2573 | 0 | -1.490e-07 |
| 11 | mod.cls_blocks.0.attn.h4 | electron<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2407 | 0.2407 | 0 | -1.490e-07 |
| 12 | mod.cls_blocks.0.attn.h6 | muon<-CLS | B_Tbl_push_read_write | down | 0 | 40.0000 | 8.941e-08 | 0.0000 | 5.662e-07 | 2.980e-08 | 0.2181 | 0.2181 | 0 | -1.490e-07 |
| 13 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.5042 | 0.0000 | 2.1269 | 1.2259 | 0.2365 | 0.2365 | 0 | -0.3340 |
| 14 | mod.cls_blocks.0.attn.h4 | CLS<-electron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0236 | -0.1250 | 2.0108 | 1.2808 | 0.1808 | 0.1808 | 0 | -0.5493 |
| 15 | mod.cls_blocks.0.attn.h4 | CLS<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.3601 | 0.0000 | 4.4037 | 0.0692 | 0.3179 | 0.3179 | 0 | -0.7582 |
| 16 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.3378 | 0.0000 | 4.2766 | 0.2273 | 0.3699 | 0.3699 | 0 | -0.7881 |
