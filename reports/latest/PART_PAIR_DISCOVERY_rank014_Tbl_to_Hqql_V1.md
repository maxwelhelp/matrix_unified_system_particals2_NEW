# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2176**
- diagnosis_counts: `{'B_Tbl_push_read_write': 20, 'weak_or_distributed': 2156}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank014_Tbl_to_Hqql_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank014_Tbl_to_Hqql_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.7399 | 0.3699 | 0.3699 | 0.3699 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=0.3699, value/write=0.3699 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.6358 | 0.3179 | 0.3179 | 0.3179 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=0.3179, value/write=0.3179 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.6140 | 0.3070 | 0.3070 | 0.3070 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-CLS; natural A×grad=0.3070, value/write=0.3070 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.5146 | 0.2573 | 0.2573 | 0.2573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.2573, value/write=0.2573 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.4815 | 0.2407 | 0.2407 | 0.2407 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.2407, value/write=0.2407 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.4734 | 0.2365 | 0.2365 | 0.2369 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.2365, value/write=0.2365 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.4363 | 0.2181 | 0.2181 | 0.2181 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-CLS; natural A×grad=0.2181, value/write=0.2181 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.3644 | 0.1808 | 0.1808 | 0.1835 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.1808, value/write=0.1808 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.3620 | 0.1810 | 0.1810 | 0.1810 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=0.1810, value/write=0.1810 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3107 | 0.1553 | 0.1553 | 0.1553 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1553, value/write=0.1553 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.3103 | 0.1548 | 0.1548 | 0.1555 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=0.1548, value/write=0.1548 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.2688 | 0.1344 | 0.1344 | 0.1344 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.1344, value/write=0.1344 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.2613 | 0.1305 | 0.1305 | 0.1308 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.1305, value/write=0.1305 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.2012 | 0.0994 | 0.0994 | 0.1017 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0994, value/write=0.0994 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0602 | 0.0143 | 0.0143 | 0.0459 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0143, value/write=0.0143 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0568 | 0.0284 | 0.0284 | 0.0284 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=0.0284, value/write=0.0284 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0535 | 0.0268 | 0.0268 | 0.0268 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0268, value/write=0.0268 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0503 | 0.0252 | 0.0252 | 0.0252 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-muon; natural A×grad=0.0252, value/write=0.0252 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0474 | 0.0235 | 0.0235 | 0.0239 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-electron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0438 | 0.0219 | 0.0219 | 0.0219 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-CLS; natural A×grad=0.0219, value/write=0.0219 so it pushes B toward Tbl. Routes:  |
| 21 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0432 | 0.0213 | 0.0213 | 0.0219 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0213, value/write=0.0213 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0397 | -0.0198 | -0.0198 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0198, value/write=-0.0198 so it resists Tbl / protective. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | muon<-muon | 0.0396 | 0.0198 | 0.0198 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses muon<-muon; natural A×grad=0.0198, value/write=0.0198 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0387 | -0.0186 | -0.0186 | 0.0201 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-neutral_hadron; natural A×grad=-0.0186, value/write=-0.0186 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-electron | 0.0368 | 0.0180 | 0.0180 | 0.0188 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-electron; natural A×grad=0.0180, value/write=0.0180 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | electron<-CLS | 0.0360 | 0.0180 | 0.0180 | 0.0180 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses electron<-CLS; natural A×grad=0.0180, value/write=0.0180 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | muon<-CLS | 0.0357 | 0.0178 | 0.0178 | 0.0178 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses muon<-CLS; natural A×grad=0.0178, value/write=0.0178 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0353 | 0.0176 | 0.0176 | 0.0176 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=0.0176, value/write=0.0176 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0340 | 0.0169 | 0.0169 | 0.0170 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-muon; natural A×grad=0.0169, value/write=0.0169 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | muon<-CLS | 0.0332 | 0.0166 | 0.0166 | 0.0166 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses muon<-CLS; natural A×grad=0.0166, value/write=0.0166 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 0.7399 | 0.3699 | 0.3699 | 0.3699 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=0.3699, value/write=0.3699 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.6358 | 0.3179 | 0.3179 | 0.3179 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=0.3179, value/write=0.3179 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.6140 | 0.3070 | 0.3070 | 0.3070 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-CLS; natural A×grad=0.3070, value/write=0.3070 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.5146 | 0.2573 | 0.2573 | 0.2573 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.2573, value/write=0.2573 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.4815 | 0.2407 | 0.2407 | 0.2407 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.2407, value/write=0.2407 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.4734 | 0.2365 | 0.2365 | 0.2369 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.2365, value/write=0.2365 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.4363 | 0.2181 | 0.2181 | 0.2181 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-CLS; natural A×grad=0.2181, value/write=0.2181 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.3644 | 0.1808 | 0.1808 | 0.1835 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.1808, value/write=0.1808 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.3620 | 0.1810 | 0.1810 | 0.1810 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=0.1810, value/write=0.1810 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.3107 | 0.1553 | 0.1553 | 0.1553 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1553, value/write=0.1553 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.3103 | 0.1548 | 0.1548 | 0.1555 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=0.1548, value/write=0.1548 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.2688 | 0.1344 | 0.1344 | 0.1344 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.1344, value/write=0.1344 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.2613 | 0.1305 | 0.1305 | 0.1308 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.1305, value/write=0.1305 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.2012 | 0.0994 | 0.0994 | 0.1017 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0994, value/write=0.0994 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-CLS | 0.0568 | 0.0284 | 0.0284 | 0.0284 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-CLS; natural A×grad=0.0284, value/write=0.0284 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0535 | 0.0268 | 0.0268 | 0.0268 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0268, value/write=0.0268 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0503 | 0.0252 | 0.0252 | 0.0252 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-muon; natural A×grad=0.0252, value/write=0.0252 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0474 | 0.0235 | 0.0235 | 0.0239 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-electron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | muon<-CLS | 0.0438 | 0.0219 | 0.0219 | 0.0219 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-CLS; natural A×grad=0.0219, value/write=0.0219 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0432 | 0.0213 | 0.0213 | 0.0219 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=0.0213, value/write=0.0213 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
_No rows._

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
