# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2144**
- diagnosis_counts: `{'B_Tbl_push_read_write': 20, 'B_Tbl_resist_or_protective_read_write': 3, 'weak_or_distributed': 2121}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank013_Hbb_to_Zqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank013_Hbb_to_Zqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.0790 | 0.5395 | 0.5395 | 0.5395 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.5395, value/write=0.5395 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.9538 | 0.4769 | 0.4769 | 0.4769 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.4769, value/write=0.4769 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.5784 | 0.2892 | 0.2892 | 0.2892 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.2892, value/write=0.2892 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.5784 | 0.2892 | 0.2892 | 0.2892 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.2892, value/write=0.2892 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4873 | 0.2288 | 0.2288 | 0.2586 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.2288, value/write=0.2288 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4122 | 0.2061 | 0.2061 | 0.2061 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.2061, value/write=0.2061 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3403 | 0.1701 | 0.1701 | 0.1701 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1701, value/write=0.1701 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.3026 | 0.1340 | 0.1340 | 0.1686 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.1340, value/write=0.1340 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1626 | 0.0782 | 0.0782 | 0.0845 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0782, value/write=0.0782 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.1388 | 0.0694 | 0.0694 | 0.0694 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0694, value/write=0.0694 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1247 | 0.0623 | 0.0623 | 0.0623 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.0623, value/write=0.0623 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1247 | 0.0623 | 0.0623 | 0.0623 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.0623, value/write=0.0623 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.1070 | 0.0535 | 0.0535 | 0.0535 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0535, value/write=0.0535 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.1043 | 0.0411 | 0.0411 | 0.0633 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0411, value/write=0.0411 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.1007 | 0.0469 | 0.0469 | 0.0538 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0469, value/write=0.0469 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0897 | 0.0350 | 0.0350 | 0.0547 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0350, value/write=0.0350 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0707 | -0.0353 | -0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-muon; natural A×grad=-0.0353, value/write=-0.0353 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0704 | 0.0352 | 0.0352 | 0.0352 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0352, value/write=0.0352 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0609 | 0.0290 | 0.0290 | 0.0319 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0290, value/write=0.0290 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0600 | 0.0300 | 0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0300, value/write=0.0300 so it pushes B toward Tbl. Routes:  |
| 21 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0576 | -0.0254 | -0.0254 | 0.0322 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0254, value/write=-0.0254 so it resists Tbl / protective. Routes:  |
| 22 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0533 | -0.0257 | -0.0257 | 0.0276 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0257, value/write=-0.0257 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0474 | 0.0204 | 0.0204 | 0.0270 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0204, value/write=0.0204 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0460 | -0.0153 | -0.0153 | 0.0308 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0153, value/write=-0.0153 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0408 | -0.0193 | -0.0193 | 0.0216 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=-0.0193, value/write=-0.0193 so it resists Tbl / protective. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0398 | 0.0199 | 0.0199 | 0.0199 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0199, value/write=0.0199 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0391 | -0.0186 | -0.0186 | 0.0205 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0186, value/write=-0.0186 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0390 | -0.0195 | -0.0195 | 0.0195 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-electron; natural A×grad=-0.0195, value/write=-0.0195 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0349 | -0.0092 | -0.0092 | 0.0256 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=-0.0092, value/write=-0.0092 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0336 | 0.0131 | 0.0131 | 0.0205 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-charged_hadron; natural A×grad=0.0131, value/write=0.0131 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.0790 | 0.5395 | 0.5395 | 0.5395 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.5395, value/write=0.5395 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.9538 | 0.4769 | 0.4769 | 0.4769 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.4769, value/write=0.4769 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.5784 | 0.2892 | 0.2892 | 0.2892 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.2892, value/write=0.2892 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.5784 | 0.2892 | 0.2892 | 0.2892 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.2892, value/write=0.2892 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4873 | 0.2288 | 0.2288 | 0.2586 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.2288, value/write=0.2288 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4122 | 0.2061 | 0.2061 | 0.2061 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.2061, value/write=0.2061 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3403 | 0.1701 | 0.1701 | 0.1701 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1701, value/write=0.1701 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.3026 | 0.1340 | 0.1340 | 0.1686 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.1340, value/write=0.1340 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1626 | 0.0782 | 0.0782 | 0.0845 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0782, value/write=0.0782 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.1388 | 0.0694 | 0.0694 | 0.0694 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0694, value/write=0.0694 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1247 | 0.0623 | 0.0623 | 0.0623 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.0623, value/write=0.0623 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1247 | 0.0623 | 0.0623 | 0.0623 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.0623, value/write=0.0623 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.1070 | 0.0535 | 0.0535 | 0.0535 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0535, value/write=0.0535 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.1043 | 0.0411 | 0.0411 | 0.0633 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0411, value/write=0.0411 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.1007 | 0.0469 | 0.0469 | 0.0538 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0469, value/write=0.0469 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0897 | 0.0350 | 0.0350 | 0.0547 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0350, value/write=0.0350 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0704 | 0.0352 | 0.0352 | 0.0352 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0352, value/write=0.0352 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0609 | 0.0290 | 0.0290 | 0.0319 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0290, value/write=0.0290 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0600 | 0.0300 | 0.0300 | 0.0300 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0300, value/write=0.0300 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0474 | 0.0204 | 0.0204 | 0.0270 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0204, value/write=0.0204 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0707 | -0.0353 | -0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-muon; natural A×grad=-0.0353, value/write=-0.0353 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0576 | -0.0254 | -0.0254 | 0.0322 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0254, value/write=-0.0254 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0533 | -0.0257 | -0.0257 | 0.0276 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0257, value/write=-0.0257 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
