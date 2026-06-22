# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2128**
- diagnosis_counts: `{'B_Tbl_push_read_write': 19, 'B_Tbl_resist_or_protective_read_write': 3, 'weak_or_distributed': 2106}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank012_Hcc_to_Zqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank012_Hcc_to_Zqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.9399 | 0.4700 | 0.4700 | 0.4700 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.4700, value/write=0.4700 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.7968 | 0.3984 | 0.3984 | 0.3984 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.3984, value/write=0.3984 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.7115 | 0.3558 | 0.3558 | 0.3558 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.3558, value/write=0.3558 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.5959 | 0.2980 | 0.2980 | 0.2980 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.2980, value/write=0.2980 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.3522 | 0.1759 | 0.1759 | 0.1763 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.1759, value/write=0.1759 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2953 | 0.1477 | 0.1477 | 0.1477 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1477, value/write=0.1477 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2436 | 0.1218 | 0.1218 | 0.1218 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1218, value/write=0.1218 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.2420 | 0.1210 | 0.1210 | 0.1210 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.1210, value/write=0.1210 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1956 | 0.0978 | 0.0978 | 0.0978 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0978, value/write=0.0978 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1882 | 0.0941 | 0.0941 | 0.0941 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.0941, value/write=0.0941 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.1249 | 0.0624 | 0.0624 | 0.0624 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0624, value/write=0.0624 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1085 | 0.0540 | 0.0540 | 0.0546 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0540, value/write=0.0540 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.1055 | 0.0396 | 0.0396 | 0.0659 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0396, value/write=0.0396 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0830 | 0.0235 | 0.0235 | 0.0595 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0680 | -0.0294 | -0.0294 | 0.0386 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0294, value/write=-0.0294 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0675 | 0.0338 | 0.0338 | 0.0338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0338, value/write=0.0338 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0644 | 0.0322 | 0.0322 | 0.0322 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.0322, value/write=0.0322 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0617 | 0.0158 | 0.0158 | 0.0459 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-photon; natural A×grad=0.0158, value/write=0.0158 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0516 | -0.0229 | -0.0229 | 0.0287 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=-0.0229, value/write=-0.0229 so it resists Tbl / protective. Routes:  |
| 20 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0471 | -0.0222 | -0.0222 | 0.0250 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0222, value/write=-0.0222 so it resists Tbl / protective. Routes:  |
| 21 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0461 | 0.0203 | 0.0203 | 0.0258 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0203, value/write=0.0203 so it pushes B toward Tbl. Routes:  |
| 22 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0453 | 0.0226 | 0.0226 | 0.0226 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0226, value/write=0.0226 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0437 | -0.0026 | -0.0026 | 0.0411 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-neutral_hadron; natural A×grad=-0.0026, value/write=-0.0026 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0431 | -0.0194 | -0.0194 | 0.0237 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-neutral_hadron; natural A×grad=-0.0194, value/write=-0.0194 so it resists Tbl / protective. Routes:  |
| 25 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0418 | 0.0209 | 0.0209 | 0.0209 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0209, value/write=0.0209 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0390 | -0.0029 | -0.0029 | 0.0362 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-charged_hadron; natural A×grad=-0.0029, value/write=-0.0029 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0335 | 0.0145 | 0.0145 | 0.0190 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0145, value/write=0.0145 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h5 | electron<-neutral_hadron | 0.0331 | -0.0155 | -0.0155 | 0.0176 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h5 uses electron<-neutral_hadron; natural A×grad=-0.0155, value/write=-0.0155 so it resists Tbl / protective. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0328 | 0.0163 | 0.0163 | 0.0165 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=0.0163, value/write=0.0163 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0328 | -0.0147 | -0.0147 | 0.0181 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-photon; natural A×grad=-0.0147, value/write=-0.0147 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.9399 | 0.4700 | 0.4700 | 0.4700 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=0.4700, value/write=0.4700 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.7968 | 0.3984 | 0.3984 | 0.3984 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=0.3984, value/write=0.3984 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.7115 | 0.3558 | 0.3558 | 0.3558 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-CLS; natural A×grad=0.3558, value/write=0.3558 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.5959 | 0.2980 | 0.2980 | 0.2980 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=0.2980, value/write=0.2980 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.3522 | 0.1759 | 0.1759 | 0.1763 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.1759, value/write=0.1759 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.2953 | 0.1477 | 0.1477 | 0.1477 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=0.1477, value/write=0.1477 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.2436 | 0.1218 | 0.1218 | 0.1218 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.1218, value/write=0.1218 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.2420 | 0.1210 | 0.1210 | 0.1210 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=0.1210, value/write=0.1210 so it pushes B toward Tbl. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.1956 | 0.0978 | 0.0978 | 0.0978 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0978, value/write=0.0978 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1882 | 0.0941 | 0.0941 | 0.0941 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-CLS; natural A×grad=0.0941, value/write=0.0941 so it pushes B toward Tbl. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.1249 | 0.0624 | 0.0624 | 0.0624 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=0.0624, value/write=0.0624 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.1085 | 0.0540 | 0.0540 | 0.0546 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0540, value/write=0.0540 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.1055 | 0.0396 | 0.0396 | 0.0659 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-photon; natural A×grad=0.0396, value/write=0.0396 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0830 | 0.0235 | 0.0235 | 0.0595 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-charged_hadron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 15 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0675 | 0.0338 | 0.0338 | 0.0338 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0338, value/write=0.0338 so it pushes B toward Tbl. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.0644 | 0.0322 | 0.0322 | 0.0322 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=0.0322, value/write=0.0322 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0461 | 0.0203 | 0.0203 | 0.0258 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0203, value/write=0.0203 so it pushes B toward Tbl. Routes:  |
| 18 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0453 | 0.0226 | 0.0226 | 0.0226 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0226, value/write=0.0226 so it pushes B toward Tbl. Routes:  |
| 19 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0418 | 0.0209 | 0.0209 | 0.0209 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0209, value/write=0.0209 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-neutral_hadron | 0.0680 | -0.0294 | -0.0294 | 0.0386 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-neutral_hadron; natural A×grad=-0.0294, value/write=-0.0294 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0516 | -0.0229 | -0.0229 | 0.0287 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-charged_hadron; natural A×grad=-0.0229, value/write=-0.0229 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0471 | -0.0222 | -0.0222 | 0.0250 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-photon; natural A×grad=-0.0222, value/write=-0.0222 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
