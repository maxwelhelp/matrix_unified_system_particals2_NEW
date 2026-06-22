# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2112**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 20, 'B_Tbl_push_read_write': 5, 'weak_or_distributed': 2087}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank018_Zqq_to_Hcc_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank018_Zqq_to_Hcc_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 2.5339 | -1.2670 | -1.2670 | 1.2670 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-1.2670, value/write=-1.2670 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.5007 | -0.7504 | -0.7504 | 0.7504 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.7504, value/write=-0.7504 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.3523 | -0.6762 | -0.6762 | 0.6762 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.6762, value/write=-0.6762 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.7875 | -0.3938 | -0.3938 | 0.3938 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.3938, value/write=-0.3938 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.7643 | -0.3821 | -0.3821 | 0.3821 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.3821, value/write=-0.3821 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.4888 | -0.2444 | -0.2444 | 0.2444 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2444, value/write=-0.2444 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4440 | -0.1886 | -0.1886 | 0.2555 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1886, value/write=-0.1886 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.4155 | -0.2077 | -0.2077 | 0.2077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.2077, value/write=-0.2077 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3365 | -0.1682 | -0.1682 | 0.1682 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1682, value/write=-0.1682 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.3073 | -0.0970 | -0.0970 | 0.2103 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0970, value/write=-0.0970 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1455 | -0.0644 | -0.0644 | 0.0812 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0644, value/write=-0.0644 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.1311 | 0.0610 | 0.0610 | 0.0701 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0610, value/write=0.0610 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1218 | -0.0609 | -0.0609 | 0.0609 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0609, value/write=-0.0609 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.1214 | 0.0511 | 0.0511 | 0.0703 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0511, value/write=0.0511 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.1001 | -0.0501 | -0.0501 | 0.0501 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0501, value/write=-0.0501 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0969 | -0.0223 | -0.0223 | 0.0747 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0223, value/write=-0.0223 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0933 | -0.0352 | -0.0352 | 0.0581 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=-0.0352, value/write=-0.0352 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0903 | 0.0435 | 0.0435 | 0.0468 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0748 | -0.0037 | -0.0037 | 0.0711 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0037, value/write=-0.0037 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0706 | -0.0353 | -0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0353, value/write=-0.0353 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0670 | -0.0037 | -0.0037 | 0.0633 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0037, value/write=-0.0037 so it resists Tbl / protective. Routes:  |
| 22 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0659 | -0.0330 | -0.0330 | 0.0330 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0330, value/write=-0.0330 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0630 | -0.0315 | -0.0315 | 0.0315 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0315, value/write=-0.0315 so it resists Tbl / protective. Routes:  |
| 24 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0510 | -0.0255 | -0.0255 | 0.0255 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0255, value/write=-0.0255 so it resists Tbl / protective. Routes:  |
| 25 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0496 | -0.0248 | -0.0248 | 0.0248 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0248, value/write=-0.0248 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0478 | 8.248e-05 | 8.248e-05 | 0.0477 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=8.248e-05, value/write=8.248e-05 so it pushes B toward Tbl. Routes:  |
| 27 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h2 | charged_hadron<-CLS | 0.0478 | 0.0239 | 0.0239 | 0.0239 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h2 uses charged_hadron<-CLS; natural A×grad=0.0239, value/write=0.0239 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0433 | 0.0196 | 0.0196 | 0.0237 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=0.0196, value/write=0.0196 so it pushes B toward Tbl. Routes:  |
| 29 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0428 | 0.0204 | 0.0204 | 0.0224 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=0.0204, value/write=0.0204 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0383 | 0.0126 | 0.0126 | 0.0257 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=0.0126, value/write=0.0126 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.1311 | 0.0610 | 0.0610 | 0.0701 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=0.0610, value/write=0.0610 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.1214 | 0.0511 | 0.0511 | 0.0703 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=0.0511, value/write=0.0511 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0903 | 0.0435 | 0.0435 | 0.0468 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h2 | charged_hadron<-CLS | 0.0478 | 0.0239 | 0.0239 | 0.0239 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h2 uses charged_hadron<-CLS; natural A×grad=0.0239, value/write=0.0239 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0428 | 0.0204 | 0.0204 | 0.0224 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=0.0204, value/write=0.0204 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 2.5339 | -1.2670 | -1.2670 | 1.2670 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-1.2670, value/write=-1.2670 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.5007 | -0.7504 | -0.7504 | 0.7504 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.7504, value/write=-0.7504 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.3523 | -0.6762 | -0.6762 | 0.6762 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.6762, value/write=-0.6762 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.7875 | -0.3938 | -0.3938 | 0.3938 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.3938, value/write=-0.3938 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.7643 | -0.3821 | -0.3821 | 0.3821 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.3821, value/write=-0.3821 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.4888 | -0.2444 | -0.2444 | 0.2444 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.2444, value/write=-0.2444 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4440 | -0.1886 | -0.1886 | 0.2555 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1886, value/write=-0.1886 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.4155 | -0.2077 | -0.2077 | 0.2077 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.2077, value/write=-0.2077 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3365 | -0.1682 | -0.1682 | 0.1682 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1682, value/write=-0.1682 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.3073 | -0.0970 | -0.0970 | 0.2103 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0970, value/write=-0.0970 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1455 | -0.0644 | -0.0644 | 0.0812 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0644, value/write=-0.0644 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1218 | -0.0609 | -0.0609 | 0.0609 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0609, value/write=-0.0609 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.1001 | -0.0501 | -0.0501 | 0.0501 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0501, value/write=-0.0501 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0969 | -0.0223 | -0.0223 | 0.0747 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0223, value/write=-0.0223 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0933 | -0.0352 | -0.0352 | 0.0581 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=-0.0352, value/write=-0.0352 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0706 | -0.0353 | -0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0353, value/write=-0.0353 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0659 | -0.0330 | -0.0330 | 0.0330 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0330, value/write=-0.0330 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0630 | -0.0315 | -0.0315 | 0.0315 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0315, value/write=-0.0315 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0510 | -0.0255 | -0.0255 | 0.0255 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0255, value/write=-0.0255 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0496 | -0.0248 | -0.0248 | 0.0248 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0248, value/write=-0.0248 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
