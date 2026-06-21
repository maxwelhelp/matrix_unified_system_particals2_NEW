# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2064**
- diagnosis_counts: `{'B_Tbl_push_read_write': 21, 'B_Tbl_resist_or_protective_read_write': 1, 'weak_or_distributed': 2042}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank001_Zqq_to_Wqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank001_Zqq_to_Wqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.6794 | 0.8397 | 0.8397 | 0.8397 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.8397, value/write=0.8397 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.3832 | 0.6916 | 0.6916 | 0.6916 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.6916, value/write=0.6916 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 1.2845 | 0.6422 | 0.6422 | 0.6422 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.6422, value/write=0.6422 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4857 | 0.2304 | 0.2304 | 0.2553 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.2304, value/write=0.2304 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2974 | 0.1487 | 0.1487 | 0.1487 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1487, value/write=0.1487 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2539 | 0.1269 | 0.1269 | 0.1269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1269, value/write=0.1269 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2394 | 0.1197 | 0.1197 | 0.1197 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1197, value/write=0.1197 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1080 | 0.0523 | 0.0523 | 0.0557 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0523, value/write=0.0523 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.1079 | 0.0539 | 0.0539 | 0.0539 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0539, value/write=0.0539 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.1030 | 0.0515 | 0.0515 | 0.0515 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0515, value/write=0.0515 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0954 | 0.0239 | 0.0239 | 0.0715 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0239, value/write=0.0239 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0845 | 0.0423 | 0.0423 | 0.0423 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0423, value/write=0.0423 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h3 | charged_hadron<-CLS | 0.0836 | 0.0418 | 0.0418 | 0.0418 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses charged_hadron<-CLS; natural A×grad=0.0418, value/write=0.0418 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0830 | 0.0260 | 0.0260 | 0.0570 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0260, value/write=0.0260 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0812 | 0.0308 | 0.0308 | 0.0504 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0308, value/write=0.0308 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0777 | 0.0388 | 0.0388 | 0.0388 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0388, value/write=0.0388 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0774 | -0.0346 | -0.0346 | 0.0428 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0346, value/write=-0.0346 so it resists Tbl / protective. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0767 | 0.0384 | 0.0384 | 0.0384 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0384, value/write=0.0384 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0692 | 0.0346 | 0.0346 | 0.0346 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0346, value/write=0.0346 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h3 | CLS<-CLS | 0.0506 | 0.0253 | 0.0253 | 0.0253 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses CLS<-CLS; natural A×grad=0.0253, value/write=0.0253 so it pushes B toward Tbl. Routes:  |
| 21 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0506 | 0.0221 | 0.0221 | 0.0285 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0221, value/write=0.0221 so it pushes B toward Tbl. Routes:  |
| 22 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0452 | 0.0226 | 0.0226 | 0.0226 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=0.0226, value/write=0.0226 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0427 | -0.0193 | -0.0193 | 0.0234 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-charged_hadron; natural A×grad=-0.0193, value/write=-0.0193 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0412 | 0.0054 | 0.0054 | 0.0358 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=0.0054, value/write=0.0054 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h3 | photon<-CLS | 0.0396 | 0.0198 | 0.0198 | 0.0198 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses photon<-CLS; natural A×grad=0.0198, value/write=0.0198 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0351 | -0.0130 | -0.0130 | 0.0221 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0130, value/write=-0.0130 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0287 | -0.0103 | -0.0103 | 0.0183 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=-0.0103, value/write=-0.0103 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-electron | 0.0282 | 0.0141 | 0.0141 | 0.0141 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-electron; natural A×grad=0.0141, value/write=0.0141 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0280 | 0.0032 | 0.0032 | 0.0247 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0032, value/write=0.0032 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0268 | 0.0134 | 0.0134 | 0.0134 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=0.0134, value/write=0.0134 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 1.6794 | 0.8397 | 0.8397 | 0.8397 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.8397, value/write=0.8397 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 1.3832 | 0.6916 | 0.6916 | 0.6916 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.6916, value/write=0.6916 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 1.2845 | 0.6422 | 0.6422 | 0.6422 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.6422, value/write=0.6422 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.4857 | 0.2304 | 0.2304 | 0.2553 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.2304, value/write=0.2304 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.2974 | 0.1487 | 0.1487 | 0.1487 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.1487, value/write=0.1487 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2539 | 0.1269 | 0.1269 | 0.1269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1269, value/write=0.1269 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2394 | 0.1197 | 0.1197 | 0.1197 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1197, value/write=0.1197 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1080 | 0.0523 | 0.0523 | 0.0557 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0523, value/write=0.0523 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.1079 | 0.0539 | 0.0539 | 0.0539 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0539, value/write=0.0539 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.1030 | 0.0515 | 0.0515 | 0.0515 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0515, value/write=0.0515 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0954 | 0.0239 | 0.0239 | 0.0715 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=0.0239, value/write=0.0239 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0845 | 0.0423 | 0.0423 | 0.0423 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0423, value/write=0.0423 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h3 | charged_hadron<-CLS | 0.0836 | 0.0418 | 0.0418 | 0.0418 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses charged_hadron<-CLS; natural A×grad=0.0418, value/write=0.0418 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0830 | 0.0260 | 0.0260 | 0.0570 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0260, value/write=0.0260 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0812 | 0.0308 | 0.0308 | 0.0504 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0308, value/write=0.0308 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0777 | 0.0388 | 0.0388 | 0.0388 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0388, value/write=0.0388 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0767 | 0.0384 | 0.0384 | 0.0384 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0384, value/write=0.0384 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0692 | 0.0346 | 0.0346 | 0.0346 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0346, value/write=0.0346 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h3 | CLS<-CLS | 0.0506 | 0.0253 | 0.0253 | 0.0253 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h3 uses CLS<-CLS; natural A×grad=0.0253, value/write=0.0253 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0506 | 0.0221 | 0.0221 | 0.0285 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0221, value/write=0.0221 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0774 | -0.0346 | -0.0346 | 0.0428 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0346, value/write=-0.0346 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
