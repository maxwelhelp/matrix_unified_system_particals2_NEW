# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2112**
- diagnosis_counts: `{'B_Tbl_push_read_write': 7, 'weak_or_distributed': 2105}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank010_Hgg_to_Hbb_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank010_Hgg_to_Hbb_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3425 | 0.1712 | 0.1712 | 0.1712 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1712, value/write=0.1712 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3336 | 0.1668 | 0.1668 | 0.1668 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.1668, value/write=0.1668 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.3033 | 0.1517 | 0.1517 | 0.1517 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.1517, value/write=0.1517 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.2808 | 0.1404 | 0.1404 | 0.1404 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.1404, value/write=0.1404 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2676 | 0.1338 | 0.1338 | 0.1338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1338, value/write=0.1338 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2210 | 0.1105 | 0.1105 | 0.1105 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1105, value/write=0.1105 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0608 | 0.0304 | 0.0304 | 0.0304 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0304, value/write=0.0304 so it pushes B toward Tbl. Routes:  |
| 8 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0377 | 0.0105 | 0.0105 | 0.0272 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0105, value/write=0.0105 so it pushes B toward Tbl. Routes:  |
| 9 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0296 | 0.0091 | 0.0091 | 0.0205 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0091, value/write=0.0091 so it pushes B toward Tbl. Routes:  |
| 10 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0230 | 0.0047 | 0.0047 | 0.0184 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0047, value/write=0.0047 so it pushes B toward Tbl. Routes:  |
| 11 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0223 | -0.0112 | -0.0112 | 0.0112 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0112, value/write=-0.0112 so it resists Tbl / protective. Routes:  |
| 12 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-neutral_hadron | 0.0207 | -0.0038 | -0.0038 | 0.0169 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-neutral_hadron; natural A×grad=-0.0038, value/write=-0.0038 so it resists Tbl / protective. Routes:  |
| 13 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0198 | -0.0099 | -0.0099 | 0.0099 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0099, value/write=-0.0099 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0190 | 0.0095 | 0.0095 | 0.0095 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.0095, value/write=0.0095 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-photon | 0.0189 | -0.0072 | -0.0072 | 0.0117 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-photon; natural A×grad=-0.0072, value/write=-0.0072 so it resists Tbl / protective. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0180 | -0.0090 | -0.0090 | 0.0090 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=-0.0090, value/write=-0.0090 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0177 | -0.0089 | -0.0089 | 0.0089 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0089, value/write=-0.0089 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0163 | 9.349e-04 | 9.349e-04 | 0.0153 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-photon; natural A×grad=9.349e-04, value/write=9.349e-04 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0158 | -0.0079 | -0.0079 | 0.0079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0079, value/write=-0.0079 so it resists Tbl / protective. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0158 | -0.0079 | -0.0079 | 0.0079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0079, value/write=-0.0079 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0157 | 0.0069 | 0.0069 | 0.0088 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=0.0069, value/write=0.0069 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-photon | 0.0150 | -0.0045 | -0.0045 | 0.0104 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-photon; natural A×grad=-0.0045, value/write=-0.0045 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0140 | 0.0022 | 0.0022 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0022, value/write=0.0022 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | photon<-charged_hadron | 0.0140 | -0.0036 | -0.0036 | 0.0104 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-charged_hadron; natural A×grad=-0.0036, value/write=-0.0036 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0133 | -0.0066 | -0.0066 | 0.0066 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0066, value/write=-0.0066 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-neutral_hadron | 0.0132 | 0.0049 | 0.0049 | 0.0083 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-neutral_hadron; natural A×grad=0.0049, value/write=0.0049 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-photon | 0.0131 | -0.0049 | -0.0049 | 0.0082 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-photon; natural A×grad=-0.0049, value/write=-0.0049 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0123 | -0.0061 | -0.0061 | 0.0061 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-CLS; natural A×grad=-0.0061, value/write=-0.0061 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0121 | 0.0015 | 0.0015 | 0.0106 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-charged_hadron; natural A×grad=0.0015, value/write=0.0015 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-charged_hadron | 0.0117 | -0.0022 | -0.0022 | 0.0095 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0022, value/write=-0.0022 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.3425 | 0.1712 | 0.1712 | 0.1712 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1712, value/write=0.1712 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.3336 | 0.1668 | 0.1668 | 0.1668 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.1668, value/write=0.1668 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.3033 | 0.1517 | 0.1517 | 0.1517 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.1517, value/write=0.1517 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.2808 | 0.1404 | 0.1404 | 0.1404 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.1404, value/write=0.1404 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2676 | 0.1338 | 0.1338 | 0.1338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1338, value/write=0.1338 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2210 | 0.1105 | 0.1105 | 0.1105 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.1105, value/write=0.1105 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0608 | 0.0304 | 0.0304 | 0.0304 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0304, value/write=0.0304 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
_No rows._

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
