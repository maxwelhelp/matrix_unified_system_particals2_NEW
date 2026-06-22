# PART_DISCOVERY_CANDIDATES_REAL_CONTRACT_V1

End-to-end discovery candidates for ParT Hqql/Tbl. This report joins natural attention `A×grad`, value/write contribution, all-head gate gradients, compiled pseudocode routes, and bundle/zero-head causal evidence into one ranked mechanism table.

- candidates: **2128**
- diagnosis_counts: `{'B_Tbl_resist_or_protective_read_write': 13, 'B_Tbl_push_read_write': 6, 'weak_or_distributed': 2109}`
- natural_attention: `reports/latest/tables/part_pair_natural_attention_rank022_Hcc_to_Tbqq_summary_v1.csv`
- value_write: `reports/latest/tables/part_pair_value_write_rank022_Hcc_to_Tbqq_summary_v1.csv`
- all_head_grad: `reports/latest/tables/__missing_pair_head_grad.csv`
- rules: `reports/latest/tables/__missing_pair_rules.csv`
- bundle: `reports/latest/tables/__missing_pair_bundle.csv`

## Top candidates overall
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 1.4401 | -0.7200 | -0.7200 | 0.7200 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=-0.7200, value/write=-0.7200 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.5489 | -0.2745 | -0.2745 | 0.2745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=-0.2745, value/write=-0.2745 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.5407 | -0.2645 | -0.2645 | 0.2762 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.2645, value/write=-0.2645 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2252 | -0.0949 | -0.0949 | 0.1303 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.0949, value/write=-0.0949 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2252 | -0.0949 | -0.0949 | 0.1303 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.0949, value/write=-0.0949 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.2059 | -0.1010 | -0.1010 | 0.1048 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=-0.1010, value/write=-0.1010 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.1931 | -0.0966 | -0.0966 | 0.0966 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.0966, value/write=-0.0966 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1827 | -0.0914 | -0.0914 | 0.0914 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.0914, value/write=-0.0914 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1367 | -0.0684 | -0.0684 | 0.0684 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0684, value/write=-0.0684 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1367 | -0.0684 | -0.0684 | 0.0684 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.0684, value/write=-0.0684 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1189 | -0.0464 | -0.0464 | 0.0725 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0464, value/write=-0.0464 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0834 | -0.0417 | -0.0417 | 0.0417 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-muon; natural A×grad=-0.0417, value/write=-0.0417 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0624 | 0.0312 | 0.0312 | 0.0312 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-electron; natural A×grad=0.0312, value/write=0.0312 so it pushes B toward Tbl. Routes:  |
| 14 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0576 | 0.0288 | 0.0288 | 0.0288 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-muon; natural A×grad=0.0288, value/write=0.0288 so it pushes B toward Tbl. Routes:  |
| 15 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0558 | -0.0123 | -0.0123 | 0.0435 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-electron; natural A×grad=-0.0123, value/write=-0.0123 so it resists Tbl / protective. Routes:  |
| 16 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0551 | 0.0230 | 0.0230 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-charged_hadron; natural A×grad=0.0230, value/write=0.0230 so it pushes B toward Tbl. Routes:  |
| 17 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0492 | 0.0235 | 0.0235 | 0.0257 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses muon<-neutral_hadron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 18 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | CLS<-electron | 0.0457 | -0.0188 | -0.0188 | 0.0269 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-electron; natural A×grad=-0.0188, value/write=-0.0188 so it resists Tbl / protective. Routes:  |
| 19 | weak_or_distributed | mod.cls_blocks.0.attn.h4 | muon<-neutral_hadron | 0.0439 | 0.0199 | 0.0199 | 0.0240 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-neutral_hadron; natural A×grad=0.0199, value/write=0.0199 so it pushes B toward Tbl. Routes:  |
| 20 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0428 | 0.0205 | 0.0205 | 0.0223 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses electron<-neutral_hadron; natural A×grad=0.0205, value/write=0.0205 so it pushes B toward Tbl. Routes:  |
| 21 | B_Tbl_push_read_write | mod.blocks.6.attn.h1 | muon<-electron | 0.0419 | 0.0210 | 0.0210 | 0.0210 | n/a | 0 | n/a | n/a | mod.blocks.6.attn.h1 uses muon<-electron; natural A×grad=0.0210, value/write=0.0210 so it pushes B toward Tbl. Routes:  |
| 22 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0411 | -0.0176 | -0.0176 | 0.0236 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0176, value/write=-0.0176 so it resists Tbl / protective. Routes:  |
| 23 | B_Tbl_resist_or_protective_read_write | mod.blocks.3.attn.h0 | muon<-electron | 0.0405 | -0.0203 | -0.0203 | 0.0203 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h0 uses muon<-electron; natural A×grad=-0.0203, value/write=-0.0203 so it resists Tbl / protective. Routes:  |
| 24 | weak_or_distributed | mod.cls_blocks.0.attn.h1 | muon<-neutral_hadron | 0.0390 | -0.0186 | -0.0186 | 0.0204 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h1 uses muon<-neutral_hadron; natural A×grad=-0.0186, value/write=-0.0186 so it resists Tbl / protective. Routes:  |
| 25 | weak_or_distributed | mod.cls_blocks.0.attn.h7 | electron<-charged_hadron | 0.0372 | 0.0177 | 0.0177 | 0.0194 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses electron<-charged_hadron; natural A×grad=0.0177, value/write=0.0177 so it pushes B toward Tbl. Routes:  |
| 26 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0369 | -0.0184 | -0.0184 | 0.0184 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses CLS<-CLS; natural A×grad=-0.0184, value/write=-0.0184 so it resists Tbl / protective. Routes:  |
| 27 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | photon<-CLS | 0.0369 | -0.0184 | -0.0184 | 0.0184 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses photon<-CLS; natural A×grad=-0.0184, value/write=-0.0184 so it resists Tbl / protective. Routes:  |
| 28 | weak_or_distributed | mod.cls_blocks.0.attn.h6 | muon<-neutral_hadron | 0.0367 | 0.0184 | 0.0184 | 0.0184 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-neutral_hadron; natural A×grad=0.0184, value/write=0.0184 so it pushes B toward Tbl. Routes:  |
| 29 | weak_or_distributed | mod.cls_blocks.0.attn.h0 | electron<-electron | 0.0358 | -0.0179 | -0.0179 | 0.0179 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses electron<-electron; natural A×grad=-0.0179, value/write=-0.0179 so it resists Tbl / protective. Routes:  |
| 30 | weak_or_distributed | mod.blocks.4.attn.h7 | electron<-muon | 0.0338 | -0.0169 | -0.0169 | 0.0169 | n/a | 0 | n/a | n/a | mod.blocks.4.attn.h7 uses electron<-muon; natural A×grad=-0.0169, value/write=-0.0169 so it resists Tbl / protective. Routes:  |

## Causal candidates
_No rows._

## B→Tbl push candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-electron | 0.0624 | 0.0312 | 0.0312 | 0.0312 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-electron; natural A×grad=0.0312, value/write=0.0312 so it pushes B toward Tbl. Routes:  |
| 2 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-muon | 0.0576 | 0.0288 | 0.0288 | 0.0288 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-muon; natural A×grad=0.0288, value/write=0.0288 so it pushes B toward Tbl. Routes:  |
| 3 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h4 | muon<-charged_hadron | 0.0551 | 0.0230 | 0.0230 | 0.0321 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-charged_hadron; natural A×grad=0.0230, value/write=0.0230 so it pushes B toward Tbl. Routes:  |
| 4 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | muon<-neutral_hadron | 0.0492 | 0.0235 | 0.0235 | 0.0257 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses muon<-neutral_hadron; natural A×grad=0.0235, value/write=0.0235 so it pushes B toward Tbl. Routes:  |
| 5 | B_Tbl_push_read_write | mod.cls_blocks.0.attn.h7 | electron<-neutral_hadron | 0.0428 | 0.0205 | 0.0205 | 0.0223 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h7 uses electron<-neutral_hadron; natural A×grad=0.0205, value/write=0.0205 so it pushes B toward Tbl. Routes:  |
| 6 | B_Tbl_push_read_write | mod.blocks.6.attn.h1 | muon<-electron | 0.0419 | 0.0210 | 0.0210 | 0.0210 | n/a | 0 | n/a | n/a | mod.blocks.6.attn.h1 uses muon<-electron; natural A×grad=0.0210, value/write=0.0210 so it pushes B toward Tbl. Routes:  |

## B→Tbl resist/protect candidates
| rank | diagnosis | head | pair | score | B_AxGrad | B_write | abs_write | grad_signed | rules | bundle_dm | bundle_flip | summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | muon<-muon | 1.4401 | -0.7200 | -0.7200 | 0.7200 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses muon<-muon; natural A×grad=-0.7200, value/write=-0.7200 so it resists Tbl / protective. Routes:  |
| 2 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | muon<-muon | 0.5489 | -0.2745 | -0.2745 | 0.2745 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses muon<-muon; natural A×grad=-0.2745, value/write=-0.2745 so it resists Tbl / protective. Routes:  |
| 3 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.5407 | -0.2645 | -0.2645 | 0.2762 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-muon; natural A×grad=-0.2645, value/write=-0.2645 so it resists Tbl / protective. Routes:  |
| 4 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.2252 | -0.0949 | -0.0949 | 0.1303 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses CLS<-CLS; natural A×grad=-0.0949, value/write=-0.0949 so it resists Tbl / protective. Routes:  |
| 5 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.2252 | -0.0949 | -0.0949 | 0.1303 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses photon<-CLS; natural A×grad=-0.0949, value/write=-0.0949 so it resists Tbl / protective. Routes:  |
| 6 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-muon | 0.2059 | -0.1010 | -0.1010 | 0.1048 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-muon; natural A×grad=-0.1010, value/write=-0.1010 so it resists Tbl / protective. Routes:  |
| 7 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.1931 | -0.0966 | -0.0966 | 0.0966 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses electron<-electron; natural A×grad=-0.0966, value/write=-0.0966 so it resists Tbl / protective. Routes:  |
| 8 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1827 | -0.0914 | -0.0914 | 0.0914 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses electron<-electron; natural A×grad=-0.0914, value/write=-0.0914 so it resists Tbl / protective. Routes:  |
| 9 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1367 | -0.0684 | -0.0684 | 0.0684 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses CLS<-CLS; natural A×grad=-0.0684, value/write=-0.0684 so it resists Tbl / protective. Routes:  |
| 10 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h6 | photon<-CLS | 0.1367 | -0.0684 | -0.0684 | 0.0684 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h6 uses photon<-CLS; natural A×grad=-0.0684, value/write=-0.0684 so it resists Tbl / protective. Routes:  |
| 11 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.1189 | -0.0464 | -0.0464 | 0.0725 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h4 uses neutral_hadron<-neutral_hadron; natural A×grad=-0.0464, value/write=-0.0464 so it resists Tbl / protective. Routes:  |
| 12 | B_Tbl_resist_or_protective_read_write | mod.cls_blocks.0.attn.h0 | muon<-muon | 0.0834 | -0.0417 | -0.0417 | 0.0417 | n/a | 0 | n/a | n/a | mod.cls_blocks.0.attn.h0 uses muon<-muon; natural A×grad=-0.0417, value/write=-0.0417 so it resists Tbl / protective. Routes:  |
| 13 | B_Tbl_resist_or_protective_read_write | mod.blocks.3.attn.h0 | muon<-electron | 0.0405 | -0.0203 | -0.0203 | 0.0203 | n/a | 0 | n/a | n/a | mod.blocks.3.attn.h0 uses muon<-electron; natural A×grad=-0.0203, value/write=-0.0203 so it resists Tbl / protective. Routes:  |

## Reading

- `B_AxGrad`: real natural attention mass times gradient. This is read-side importance.
- `B_write`: `A[q,k] * dot(V[k], grad_context[q])`. This is write-side contribution.
- `rules`: compiled pseudocode/route evidence attached to the same head.
- `bundle_dm` / `bundle_flip`: causal intervention evidence when available.
- Strong mechanism = same head/pair has read-side evidence, write-side evidence, head gradient, route/pseudocode support, and causal/bundle effect.
