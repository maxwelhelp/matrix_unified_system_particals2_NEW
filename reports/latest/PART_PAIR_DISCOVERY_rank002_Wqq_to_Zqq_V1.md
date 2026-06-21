# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2048**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 18, 'B_Tbl_push_read_write': 4, 'weak_or_distributed': 2026}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank002_Wqq_to_Zqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank002_Wqq_to_Zqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.5147 | -0.7573 | -0.7573 | 0.7573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.7573, value/write=-0.7573 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.4060 | -0.7030 | -0.7030 | 0.7030 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.7030, value/write=-0.7030 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.2974 | -0.6487 | -0.6487 | 0.6487 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.6487, value/write=-0.6487 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4062 | -0.1879 | -0.1879 | 0.2182 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1879, value/write=-0.1879 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3811 | -0.1906 | -0.1906 | 0.1906 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1906, value/write=-0.1906 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3178 | -0.1589 | -0.1589 | 0.1589 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1589, value/write=-0.1589 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.2546 | -0.1273 | -0.1273 | 0.1273 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1273, value/write=-0.1273 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.1876 | -0.0838 | -0.0838 | 0.1038 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0838, value/write=-0.0838 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.1226 | 0.0613 | 0.0613 | 0.0613 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-muon; natural A×grad=0.0613, value/write=0.0613 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0913 | -0.0430 | -0.0430 | 0.0483 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0430, value/write=-0.0430 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0877 | -0.0438 | -0.0438 | 0.0438 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0438, value/write=-0.0438 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0810 | -0.0241 | -0.0241 | 0.0570 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0241, value/write=-0.0241 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0740 | -0.0370 | -0.0370 | 0.0370 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0370, value/write=-0.0370 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0720 | -0.0360 | -0.0360 | 0.0360 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0360, value/write=-0.0360 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0697 | -0.0348 | -0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0348, value/write=-0.0348 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0695 | 0.0348 | 0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0348, value/write=0.0348 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0653 | -0.0326 | -0.0326 | 0.0326 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0326, value/write=-0.0326 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0562 | -0.0281 | -0.0281 | 0.0281 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0281, value/write=-0.0281 so it resists Tbl / protective. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0551 | 0.0228 | 0.0228 | 0.0323 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0228, value/write=0.0228 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0532 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-muon; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0506 | -0.0056 | -0.0056 | 0.0450 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0056, value/write=-0.0056 so it resists Tbl / protective. Routes:  |
| 22 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0494 | -0.0225 | -0.0225 | 0.0269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0225, value/write=-0.0225 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0462 | 0.0201 | 0.0201 | 0.0262 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=0.0201, value/write=0.0201 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0422 | -0.0184 | -0.0184 | 0.0238 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=-0.0184, value/write=-0.0184 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0386 | 0.0151 | 0.0151 | 0.0235 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0151, value/write=0.0151 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0381 | 0.0169 | 0.0169 | 0.0212 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=0.0169, value/write=0.0169 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-muon | 0.0371 | 0.0185 | 0.0185 | 0.0185 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-muon; natural A×grad=0.0185, value/write=0.0185 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0337 | -0.0168 | -0.0168 | 0.0168 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.0168, value/write=-0.0168 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-muon | 0.0297 | -0.0149 | -0.0149 | 0.0149 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-muon; natural A×grad=-0.0149, value/write=-0.0149 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0265 | -0.0132 | -0.0132 | 0.0132 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=-0.0132, value/write=-0.0132 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-muon | 0.1226 | 0.0613 | 0.0613 | 0.0613 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-muon; natural A×grad=0.0613, value/write=0.0613 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0695 | 0.0348 | 0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0348, value/write=0.0348 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0551 | 0.0228 | 0.0228 | 0.0323 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=0.0228, value/write=0.0228 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0462 | 0.0201 | 0.0201 | 0.0262 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=0.0201, value/write=0.0201 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.5147 | -0.7573 | -0.7573 | 0.7573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=-0.7573, value/write=-0.7573 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.4060 | -0.7030 | -0.7030 | 0.7030 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.7030, value/write=-0.7030 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 1.2974 | -0.6487 | -0.6487 | 0.6487 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.6487, value/write=-0.6487 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4062 | -0.1879 | -0.1879 | 0.2182 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.1879, value/write=-0.1879 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.3811 | -0.1906 | -0.1906 | 0.1906 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=-0.1906, value/write=-0.1906 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3178 | -0.1589 | -0.1589 | 0.1589 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.1589, value/write=-0.1589 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.2546 | -0.1273 | -0.1273 | 0.1273 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=-0.1273, value/write=-0.1273 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.1876 | -0.0838 | -0.0838 | 0.1038 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0838, value/write=-0.0838 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0913 | -0.0430 | -0.0430 | 0.0483 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0430, value/write=-0.0430 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0877 | -0.0438 | -0.0438 | 0.0438 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=-0.0438, value/write=-0.0438 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0810 | -0.0241 | -0.0241 | 0.0570 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=-0.0241, value/write=-0.0241 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0740 | -0.0370 | -0.0370 | 0.0370 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=-0.0370, value/write=-0.0370 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0720 | -0.0360 | -0.0360 | 0.0360 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0360, value/write=-0.0360 so it resists Tbl / protective. Routes:  |
| 14 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0697 | -0.0348 | -0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=-0.0348, value/write=-0.0348 so it resists Tbl / protective. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0653 | -0.0326 | -0.0326 | 0.0326 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=-0.0326, value/write=-0.0326 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0562 | -0.0281 | -0.0281 | 0.0281 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=-0.0281, value/write=-0.0281 so it resists Tbl / protective. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-muon | 0.0532 | -0.0266 | -0.0266 | 0.0266 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-muon; natural A×grad=-0.0266, value/write=-0.0266 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0494 | -0.0225 | -0.0225 | 0.0269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=-0.0225, value/write=-0.0225 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
