# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2160**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 18, 'B_Tbl_push_read_write': 6, 'weak_or_distributed': 2136}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank003_Hcc_to_Hbb_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank003_Hcc_to_Hbb_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.3351 | -0.1675 | -0.1675 | 0.1675 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.1675, value/write=-0.1675 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.2754 | -0.1377 | -0.1377 | 0.1377 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.1377, value/write=-0.1377 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2274 | -0.1137 | -0.1137 | 0.1137 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1137, value/write=-0.1137 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.2003 | -0.1002 | -0.1002 | 0.1002 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1002, value/write=-0.1002 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1882 | -0.0941 | -0.0941 | 0.0941 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.0941, value/write=-0.0941 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1868 | -0.0934 | -0.0934 | 0.0934 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=-0.0934, value/write=-0.0934 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1721 | -0.0861 | -0.0861 | 0.0861 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0861, value/write=-0.0861 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1666 | -0.0833 | -0.0833 | 0.0833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0833, value/write=-0.0833 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1489 | 0.0745 | 0.0745 | 0.0745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0745, value/write=0.0745 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1489 | 0.0745 | 0.0745 | 0.0745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-muon; natural A×grad=0.0745, value/write=0.0745 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1416 | -0.0708 | -0.0708 | 0.0708 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=-0.0708, value/write=-0.0708 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1242 | -0.0621 | -0.0621 | 0.0621 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0621, value/write=-0.0621 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.0984 | 0.0492 | 0.0492 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h3 uses electron<-muon; natural A×grad=0.0492, value/write=0.0492 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0984 | 0.0492 | 0.0492 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h3 uses CLS<-muon; natural A×grad=0.0492, value/write=0.0492 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0957 | 0.0435 | 0.0435 | 0.0522 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses electron<-muon; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0957 | 0.0435 | 0.0435 | 0.0522 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0923 | -0.0462 | -0.0462 | 0.0462 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0462, value/write=-0.0462 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0838 | -0.0401 | -0.0401 | 0.0437 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0401, value/write=-0.0401 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0823 | -0.0411 | -0.0411 | 0.0411 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0411, value/write=-0.0411 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0731 | -0.0366 | -0.0366 | 0.0366 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0366, value/write=-0.0366 so it resists Tbl / protective. Routes:  |
| 21 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0714 | -0.0357 | -0.0357 | 0.0357 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=-0.0357, value/write=-0.0357 so it resists Tbl / protective. Routes:  |
| 22 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0550 | -0.0275 | -0.0275 | 0.0275 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-electron; natural A×grad=-0.0275, value/write=-0.0275 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0525 | -0.0242 | -0.0242 | 0.0283 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0242, value/write=-0.0242 so it resists Tbl / protective. Routes:  |
| 24 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0470 | -0.0221 | -0.0221 | 0.0250 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0429 | -0.0199 | -0.0199 | 0.0230 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0199, value/write=-0.0199 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-neutral_hadron | 0.0358 | 0.0175 | 0.0175 | 0.0183 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-neutral_hadron; natural A×grad=0.0175, value/write=0.0175 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.blocks.3.attn.h7 | electron<-muon | 0.0356 | -0.0177 | -0.0177 | 0.0179 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h7 uses electron<-muon; natural A×grad=-0.0177, value/write=-0.0177 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.blocks.4.attn.h3 | electron<-muon | 0.0341 | -0.0170 | -0.0170 | 0.0170 | n/a | 0 | n/a | n/a | mod.blocks.4.attn.h3 uses electron<-muon; natural A×grad=-0.0170, value/write=-0.0170 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.blocks.3.attn.h2 | electron<-muon | 0.0335 | 0.0167 | 0.0167 | 0.0167 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h2 uses electron<-muon; natural A×grad=0.0167, value/write=0.0167 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-muon | 0.0325 | 0.0163 | 0.0163 | 0.0163 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-muon; natural A×grad=0.0163, value/write=0.0163 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.1489 | 0.0745 | 0.0745 | 0.0745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0745, value/write=0.0745 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-muon | 0.1489 | 0.0745 | 0.0745 | 0.0745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-muon; natural A×grad=0.0745, value/write=0.0745 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h3 | electron<-muon | 0.0984 | 0.0492 | 0.0492 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h3 uses electron<-muon; natural A×grad=0.0492, value/write=0.0492 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.1.attn.h3 | CLS<-muon | 0.0984 | 0.0492 | 0.0492 | 0.0492 | n/a | 0 | n/a | n/a | mod.cls_blocks.1.attn.h3 uses CLS<-muon; natural A×grad=0.0492, value/write=0.0492 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | electron<-muon | 0.0957 | 0.0435 | 0.0435 | 0.0522 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses electron<-muon; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0957 | 0.0435 | 0.0435 | 0.0522 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=0.0435, value/write=0.0435 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.3351 | -0.1675 | -0.1675 | 0.1675 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.1675, value/write=-0.1675 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.2754 | -0.1377 | -0.1377 | 0.1377 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.1377, value/write=-0.1377 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2274 | -0.1137 | -0.1137 | 0.1137 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.1137, value/write=-0.1137 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.2003 | -0.1002 | -0.1002 | 0.1002 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1002, value/write=-0.1002 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1882 | -0.0941 | -0.0941 | 0.0941 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.0941, value/write=-0.0941 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1868 | -0.0934 | -0.0934 | 0.0934 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=-0.0934, value/write=-0.0934 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.1721 | -0.0861 | -0.0861 | 0.0861 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.0861, value/write=-0.0861 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1666 | -0.0833 | -0.0833 | 0.0833 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0833, value/write=-0.0833 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1416 | -0.0708 | -0.0708 | 0.0708 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=-0.0708, value/write=-0.0708 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1242 | -0.0621 | -0.0621 | 0.0621 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.0621, value/write=-0.0621 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0923 | -0.0462 | -0.0462 | 0.0462 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0462, value/write=-0.0462 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0838 | -0.0401 | -0.0401 | 0.0437 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0401, value/write=-0.0401 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0823 | -0.0411 | -0.0411 | 0.0411 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0411, value/write=-0.0411 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0731 | -0.0366 | -0.0366 | 0.0366 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0366, value/write=-0.0366 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0714 | -0.0357 | -0.0357 | 0.0357 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=-0.0357, value/write=-0.0357 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0550 | -0.0275 | -0.0275 | 0.0275 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-electron; natural A×grad=-0.0275, value/write=-0.0275 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0525 | -0.0242 | -0.0242 | 0.0283 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0242, value/write=-0.0242 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0470 | -0.0221 | -0.0221 | 0.0250 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
