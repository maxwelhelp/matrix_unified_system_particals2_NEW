# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **128**
- candidates_tested: **12**
- rows: **24**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -1.1925 | -0.3750 | 0.9901 | 1.9078 | -0.4598 | -0.4598 | 0 | 1.2180 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-electron | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -1.0486 | -0.4062 | 1.3805 | 1.6979 | -0.3289 | -0.3289 | 0 | 1.0916 |
| 3 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | up | 1 | 40.0000 | -1.1249 | -0.3438 | 0.6201 | 3.3142 | -0.4664 | -0.4664 | 0 | 0.8288 |
| 4 | mod.cls_blocks.0.attn.h4 | muon<-muon | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 1.0003 | 0.0000 | 0.8061 | 0.8141 | -0.4664 | -0.4664 | 0 | 0.5953 |
| 5 | mod.cls_blocks.0.attn.h4 | electron<-electron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.9589 | 0.0000 | 1.3631 | 0.7772 | -0.4598 | -0.4598 | 0 | 0.4238 |
| 6 | mod.cls_blocks.0.attn.h4 | CLS<-electron | B_Tbl_resist_or_protective_read_write | down | 1 | 40.0000 | 0.9461 | 0.0000 | 1.3714 | 0.7233 | -0.3289 | -0.3289 | 0 | 0.4224 |
| 7 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.3823 | 0.0000 | 0.0277 | 0.0460 | 0.0261 | 0.0261 | 0 | 0.3639 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | high_gradient_write_node | up | 1 | 40.0000 | 0.2301 | 0.0000 | 0.0121 | 0.0523 | 0.0173 | 0.0173 | 0 | 0.2140 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.1109 | -0.0625 | 0.0114 | 0.1530 | 0.0261 | 0.0261 | 0 | 0.1948 |
| 10 | mod.cls_blocks.0.attn.h4 | electron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.1421 | 0.0000 | 5.960e-08 | 0.2789 | 0.0209 | 0.0209 | 0 | 0.0724 |
| 11 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | high_gradient_write_node | down | 1 | 40.0000 | -0.0366 | 0.0000 | 8.497e-04 | 0.0095 | 0.0173 | 0.0173 | 0 | 0.0340 |
| 12 | mod.blocks.7.attn.h3 | charged_hadron<-electron | causal_candidate | up | 1 | 40.0000 | -0.0682 | 0.0000 | 0.0546 | 0.1019 | -6.774e-04 | -6.774e-04 | 2 | 0.0291 |
| 13 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | B_Tbl_push_read_write | up | 1 | 40.0000 | 0.0257 | 0.0000 | 0.0282 | 0.0164 | 0.0396 | 0.0396 | 0 | 0.0145 |
| 14 | mod.blocks.7.attn.h3 | charged_hadron<-electron | causal_candidate | down | 1 | 40.0000 | 0.0402 | 0.0000 | 0.0831 | 0.0254 | -6.774e-04 | -6.774e-04 | 2 | 0.0131 |
| 15 | mod.cls_blocks.0.attn.h1 | charged_hadron<-photon | high_gradient_write_node | up | 1 | 40.0000 | 0.0554 | 0.0000 | 0.1543 | 0.0178 | 0.0167 | 0.0167 | 0 | 0.0124 |
| 16 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | high_gradient_write_node | up | 1 | 40.0000 | -0.0391 | 0.0000 | 0.0445 | 0.0702 | -0.0089 | -0.0089 | 0 | 0.0104 |
| 17 | mod.cls_blocks.0.attn.h1 | charged_hadron<-photon | high_gradient_write_node | down | 1 | 40.0000 | -0.0126 | 0.0000 | 0.0061 | 0.0122 | 0.0167 | 0.0167 | 0 | 0.0080 |
| 18 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | high_gradient_write_node | down | 1 | 40.0000 | 0.0564 | 0.0000 | 0.1094 | 0.0906 | -0.0089 | -0.0089 | 0 | 0.0064 |
| 19 | mod.blocks.7.attn.h3 | muon<-electron | causal_candidate | down | 1 | 40.0000 | 0.0036 | 0.0000 | 1.396e-05 | 5.192e-04 | -0.0019 | -0.0019 | 2 | 0.0034 |
| 20 | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0027 | 0.0000 | 8.086e-04 | 0.0016 | 0.0396 | 0.0396 | 0 | 0.0021 |
| 21 | mod.blocks.7.attn.h3 | electron<-muon | causal_candidate | down | 1 | 40.0000 | 6.216e-04 | 0.0000 | 5.415e-05 | 4.884e-04 | -5.469e-04 | -5.469e-04 | 2 | 4.860e-04 |
| 22 | mod.blocks.7.attn.h3 | muon<-electron | causal_candidate | up | 1 | 40.0000 | -0.0017 | 0.0000 | 1.555e-04 | 0.0080 | -0.0019 | -0.0019 | 2 | -3.521e-04 |
| 23 | mod.blocks.7.attn.h3 | electron<-muon | causal_candidate | up | 1 | 40.0000 | -0.0033 | 0.0000 | 0.0010 | 0.0145 | -5.469e-04 | -5.469e-04 | 2 | -5.942e-04 |
| 24 | mod.cls_blocks.0.attn.h4 | electron<-muon | B_Tbl_push_read_write | down | 1 | 40.0000 | -0.0059 | 0.0000 | 5.960e-08 | 0.0780 | 0.0209 | 0.0209 | 0 | -0.0136 |
