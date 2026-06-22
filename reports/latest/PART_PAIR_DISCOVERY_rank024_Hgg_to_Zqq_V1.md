# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2016**
- diagnosis_counts: `{'B_Tbl_push_read_write': 19, 'B_Tbl_resist_or_protective_read_write': 5, 'weak_or_distributed': 1992}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank024_Hgg_to_Zqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank024_Hgg_to_Zqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 2.8417 | 1.4209 | 1.4209 | 1.4209 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=1.4209, value/write=1.4209 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 2.0000 | 1.0000 | 1.0000 | 1.0000 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=1.0000, value/write=1.0000 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.4969 | 0.7485 | 0.7485 | 0.7485 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.7485, value/write=0.7485 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.9241 | 0.4621 | 0.4621 | 0.4621 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.4621, value/write=0.4621 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.8195 | 0.4098 | 0.4098 | 0.4098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.4098, value/write=0.4098 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.7135 | 0.3567 | 0.3567 | 0.3567 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.3567, value/write=0.3567 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.5445 | 0.2723 | 0.2723 | 0.2723 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.2723, value/write=0.2723 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4611 | 0.2305 | 0.2305 | 0.2305 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.2305, value/write=0.2305 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.3915 | 0.1836 | 0.1836 | 0.2079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.1836, value/write=0.1836 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1808 | 0.0830 | 0.0830 | 0.0978 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0830, value/write=0.0830 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.1573 | -0.0787 | -0.0787 | 0.0787 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-electron; natural A×grad=-0.0787, value/write=-0.0787 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1250 | 0.0625 | 0.0625 | 0.0625 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0625, value/write=0.0625 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.1194 | 0.0597 | 0.0597 | 0.0597 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0597, value/write=0.0597 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.1158 | 0.0386 | 0.0386 | 0.0772 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0386, value/write=0.0386 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0969 | 0.0292 | 0.0292 | 0.0676 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0292, value/write=0.0292 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0781 | 0.0390 | 0.0390 | 0.0390 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0390, value/write=0.0390 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0780 | 0.0390 | 0.0390 | 0.0390 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0390, value/write=0.0390 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0729 | -0.0365 | -0.0365 | 0.0365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-electron; natural A×grad=-0.0365, value/write=-0.0365 so it resists Tbl / protective. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0718 | 0.0175 | 0.0175 | 0.0544 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0175, value/write=0.0175 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0707 | 0.0353 | 0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-electron; natural A×grad=0.0353, value/write=0.0353 so it pushes B toward Tbl. Routes:  |
| 21 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0697 | 0.0348 | 0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h5 uses photon<-electron; natural A×grad=0.0348, value/write=0.0348 so it pushes B toward Tbl. Routes:  |
| 22 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0646 | 0.0323 | 0.0323 | 0.0323 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0323, value/write=0.0323 so it pushes B toward Tbl. Routes:  |
| 23 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0604 | -0.0302 | -0.0302 | 0.0302 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0302, value/write=-0.0302 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0569 | 0.0185 | 0.0185 | 0.0384 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-neutral_hadron; natural A×grad=0.0185, value/write=0.0185 so it pushes B toward Tbl. Routes:  |
| 25 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0494 | -0.0209 | -0.0209 | 0.0285 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0209, value/write=-0.0209 so it resists Tbl / protective. Routes:  |
| 26 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0461 | -0.0221 | -0.0221 | 0.0240 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0435 | -0.0185 | -0.0185 | 0.0250 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=-0.0185, value/write=-0.0185 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0405 | 0.0024 | 0.0024 | 0.0380 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0024, value/write=0.0024 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0394 | 0.0197 | 0.0197 | 0.0197 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-CLS; natural A×grad=0.0197, value/write=0.0197 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0391 | -0.0027 | -0.0027 | 0.0364 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0027, value/write=-0.0027 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 2.8417 | 1.4209 | 1.4209 | 1.4209 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=1.4209, value/write=1.4209 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 2.0000 | 1.0000 | 1.0000 | 1.0000 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=1.0000, value/write=1.0000 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.4969 | 0.7485 | 0.7485 | 0.7485 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.7485, value/write=0.7485 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.9241 | 0.4621 | 0.4621 | 0.4621 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.4621, value/write=0.4621 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.8195 | 0.4098 | 0.4098 | 0.4098 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.4098, value/write=0.4098 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.7135 | 0.3567 | 0.3567 | 0.3567 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.3567, value/write=0.3567 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.5445 | 0.2723 | 0.2723 | 0.2723 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.2723, value/write=0.2723 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.4611 | 0.2305 | 0.2305 | 0.2305 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.2305, value/write=0.2305 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.3915 | 0.1836 | 0.1836 | 0.2079 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.1836, value/write=0.1836 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1808 | 0.0830 | 0.0830 | 0.0978 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0830, value/write=0.0830 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1250 | 0.0625 | 0.0625 | 0.0625 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0625, value/write=0.0625 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.1194 | 0.0597 | 0.0597 | 0.0597 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0597, value/write=0.0597 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.1158 | 0.0386 | 0.0386 | 0.0772 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0386, value/write=0.0386 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0969 | 0.0292 | 0.0292 | 0.0676 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0292, value/write=0.0292 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0781 | 0.0390 | 0.0390 | 0.0390 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0390, value/write=0.0390 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0780 | 0.0390 | 0.0390 | 0.0390 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0390, value/write=0.0390 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-electron | 0.0707 | 0.0353 | 0.0353 | 0.0353 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-electron; natural A×grad=0.0353, value/write=0.0353 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h5 | photon<-electron | 0.0697 | 0.0348 | 0.0348 | 0.0348 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h5 uses photon<-electron; natural A×grad=0.0348, value/write=0.0348 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0646 | 0.0323 | 0.0323 | 0.0323 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0323, value/write=0.0323 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-electron | 0.1573 | -0.0787 | -0.0787 | 0.0787 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-electron; natural A×grad=-0.0787, value/write=-0.0787 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h7 | photon<-electron | 0.0729 | -0.0365 | -0.0365 | 0.0365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-electron; natural A×grad=-0.0365, value/write=-0.0365 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0604 | -0.0302 | -0.0302 | 0.0302 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0302, value/write=-0.0302 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0494 | -0.0209 | -0.0209 | 0.0285 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0209, value/write=-0.0209 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0461 | -0.0221 | -0.0221 | 0.0240 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0221, value/write=-0.0221 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
