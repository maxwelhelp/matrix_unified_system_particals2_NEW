# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2160**
- diagnosis_counts: `{'B_Tbl_push_read_write': 8, 'B_Tbl_resist_or_protective_read_write': 4, 'weak_or_distributed': 2148}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank004_Hbb_to_Hcc_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank004_Hbb_to_Hcc_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3297 | 0.1649 | 0.1649 | 0.1649 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1649, value/write=0.1649 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1999 | -0.1000 | -0.1000 | 0.1000 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1000, value/write=-0.1000 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1609 | 0.0804 | 0.0804 | 0.0804 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0804, value/write=0.0804 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1236 | 0.0618 | 0.0618 | 0.0618 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0618, value/write=0.0618 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.1017 | 0.0509 | 0.0509 | 0.0509 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0509, value/write=0.0509 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.1013 | 0.0506 | 0.0506 | 0.0506 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0506, value/write=0.0506 so it pushes B toward Tbl. Routes:  |
| 7 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.0904 | -6.446e-04 | -6.446e-04 | 0.0897 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-6.446e-04, value/write=-6.446e-04 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0815 | -0.0407 | -0.0407 | 0.0407 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-muon; natural A×grad=-0.0407, value/write=-0.0407 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0808 | 0.0404 | 0.0404 | 0.0404 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0404, value/write=0.0404 so it pushes B toward Tbl. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0807 | -0.0337 | -0.0337 | 0.0470 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.0337, value/write=-0.0337 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0777 | 0.0389 | 0.0389 | 0.0389 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0389, value/write=0.0389 so it pushes B toward Tbl. Routes:  |
| 12 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0730 | 0.0365 | 0.0365 | 0.0365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0365, value/write=0.0365 so it pushes B toward Tbl. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0466 | -0.0233 | -0.0233 | 0.0233 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses neutral_hadron<-muon; natural A×grad=-0.0233, value/write=-0.0233 so it resists Tbl / protective. Routes:  |
| 14 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-CLS | 0.0335 | 0.0168 | 0.0168 | 0.0168 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-CLS; natural A×grad=0.0168, value/write=0.0168 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | photon<-CLS | 0.0314 | 0.0157 | 0.0157 | 0.0157 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses photon<-CLS; natural A×grad=0.0157, value/write=0.0157 so it pushes B toward Tbl. Routes:  |
| 16 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-electron | 0.0273 | -0.0136 | -0.0136 | 0.0136 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-electron; natural A×grad=-0.0136, value/write=-0.0136 so it resists Tbl / protective. Routes:  |
| 17 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-muon | 0.0272 | -0.0111 | -0.0111 | 0.0160 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-muon; natural A×grad=-0.0111, value/write=-0.0111 so it resists Tbl / protective. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0270 | 0.0135 | 0.0135 | 0.0135 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-CLS; natural A×grad=0.0135, value/write=0.0135 so it pushes B toward Tbl. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0269 | 0.0135 | 0.0135 | 0.0135 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-CLS; natural A×grad=0.0135, value/write=0.0135 so it pushes B toward Tbl. Routes:  |
| 20 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0263 | 0.0124 | 0.0124 | 0.0139 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0124, value/write=0.0124 so it pushes B toward Tbl. Routes:  |
| 21 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | charged_hadron<-CLS | 0.0251 | 0.0125 | 0.0125 | 0.0125 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses charged_hadron<-CLS; natural A×grad=0.0125, value/write=0.0125 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0243 | 0.0094 | 0.0094 | 0.0150 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0094, value/write=0.0094 so it pushes B toward Tbl. Routes:  |
| 23 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | CLS<-CLS | 0.0237 | 0.0118 | 0.0118 | 0.0118 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses CLS<-CLS; natural A×grad=0.0118, value/write=0.0118 so it pushes B toward Tbl. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0231 | 0.0040 | 0.0040 | 0.0191 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0040, value/write=0.0040 so it pushes B toward Tbl. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0205 | 0.0102 | 0.0102 | 0.0103 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses neutral_hadron<-neutral_hadron; natural A×grad=0.0102, value/write=0.0102 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-CLS | 0.0202 | 0.0101 | 0.0101 | 0.0101 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-CLS; natural A×grad=0.0101, value/write=0.0101 so it pushes B toward Tbl. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | CLS<-neutral_hadron | 0.0193 | 0.0072 | 0.0072 | 0.0121 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses CLS<-neutral_hadron; natural A×grad=0.0072, value/write=0.0072 so it pushes B toward Tbl. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | charged_hadron<-neutral_hadron | 0.0192 | 0.0065 | 0.0065 | 0.0126 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses charged_hadron<-neutral_hadron; natural A×grad=0.0065, value/write=0.0065 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | neutral_hadron<-CLS | 0.0191 | 0.0095 | 0.0095 | 0.0095 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses neutral_hadron<-CLS; natural A×grad=0.0095, value/write=0.0095 so it pushes B toward Tbl. Routes:  |
| 30 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | photon<-neutral_hadron | 0.0186 | 0.0062 | 0.0062 | 0.0124 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses photon<-neutral_hadron; natural A×grad=0.0062, value/write=0.0062 so it pushes B toward Tbl. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.3297 | 0.1649 | 0.1649 | 0.1649 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses charged_hadron<-CLS; natural A×grad=0.1649, value/write=0.1649 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.1609 | 0.0804 | 0.0804 | 0.0804 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses charged_hadron<-CLS; natural A×grad=0.0804, value/write=0.0804 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.1236 | 0.0618 | 0.0618 | 0.0618 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=0.0618, value/write=0.0618 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.1017 | 0.0509 | 0.0509 | 0.0509 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=0.0509, value/write=0.0509 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.1013 | 0.0506 | 0.0506 | 0.0506 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-CLS; natural A×grad=0.0506, value/write=0.0506 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h0 | charged_hadron<-CLS | 0.0808 | 0.0404 | 0.0404 | 0.0404 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses charged_hadron<-CLS; natural A×grad=0.0404, value/write=0.0404 so it pushes B toward Tbl. Routes:  |
| 7 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.0777 | 0.0389 | 0.0389 | 0.0389 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=0.0389, value/write=0.0389 so it pushes B toward Tbl. Routes:  |
| 8 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0730 | 0.0365 | 0.0365 | 0.0365 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-CLS; natural A×grad=0.0365, value/write=0.0365 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.1999 | -0.1000 | -0.1000 | 0.1000 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.1000, value/write=-0.1000 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | neutral_hadron<-muon | 0.0815 | -0.0407 | -0.0407 | 0.0407 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses neutral_hadron<-muon; natural A×grad=-0.0407, value/write=-0.0407 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.0807 | -0.0337 | -0.0337 | 0.0470 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-CLS; natural A×grad=-0.0337, value/write=-0.0337 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h2 | neutral_hadron<-muon | 0.0466 | -0.0233 | -0.0233 | 0.0233 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h2 uses neutral_hadron<-muon; natural A×grad=-0.0233, value/write=-0.0233 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
