# PART_VALUE_WRITE_GRAD_REAL_CONTRACT_V1

Value/write contribution trace using manual legacy MHA forward. It computes real `A`, projected `V`, and `context=A@V`; after backward it aggregates `A[q,k] * dot(V[k], grad_context[q])` by physical role-pairs. This answers not only where attention looks, but what value/write signal the looked-at particle contributes to the objective.

- events: **64**
- events_per_group: **16**
- micro_batch: **4**
- roles: `['CLS', 'electron', 'muon', 'charged_hadron', 'neutral_hadron', 'photon']`
- role_pairs: **36**
- objectives: `['signed_hqql_tbl', 'B_tbl_minus_hqql']`
- rows: **10032**

## Top value/write role-links: `signed_hqql_tbl`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-CLS | 0.1099 | 0.5395 | 0.5395 | 1.0377 | 0.5395 | 152.1469 | 0.0421 | 1.1932 |
| 2 | mod.cls_blocks.0.attn.h4 | CLS<-CLS | 0.1160 | 0.4769 | 0.4769 | 0.8721 | 0.4769 | 152.1469 | 0.0369 | 1.0322 |
| 3 | mod.cls_blocks.0.attn.h4 | electron<-CLS | 0.1342 | 0.2892 | 0.2892 | 1.0797 | 0.2892 | 152.1469 | 0.0214 | 0.9013 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-CLS | 0.0939 | 0.2061 | 0.2061 | 0.3434 | 0.2061 | 102.3998 | 0.0274 | 0.4293 |
| 5 | mod.cls_blocks.0.attn.h6 | CLS<-CLS | 0.1006 | 0.1701 | 0.1701 | 0.2916 | 0.1701 | 102.3998 | 0.0233 | 0.3585 |
| 6 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0473 | 0.1866 | 0.2173 | 0.1853 | 0.0949 | 14.7687 | 0.0181 | 0.3336 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.4475 | 0.0000 | 0.0000 | 0.0000 | 0.2238 |
| 8 | mod.cls_blocks.0.attn.h6 | electron<-CLS | 0.1207 | 0.0623 | 0.0623 | 0.2450 | 0.0623 | 102.3998 | 0.0111 | 0.2004 |
| 9 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0420 | 0.1083 | 0.1431 | 0.1088 | 0.0693 | 11.9455 | 0.0149 | 0.1985 |
| 10 | mod.cls_blocks.0.attn.h4 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.3266 | 0.0000 | 0.0000 | 0.0000 | 0.1633 |
| 11 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-CLS | 0.0600 | 0.0694 | 0.0694 | 0.0866 | 0.0694 | 64.1643 | 0.0316 | 0.1300 |
| 12 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0404 | 0.0621 | 0.0684 | 0.0617 | 0.0268 | 10.7365 | 0.0099 | 0.1101 |
| 13 | mod.cls_blocks.0.attn.h0 | CLS<-CLS | 0.0565 | 0.0535 | 0.0535 | 0.0703 | 0.0535 | 64.1643 | 0.0292 | 0.1021 |
| 14 | mod.cls_blocks.0.attn.h6 | charged_hadron<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1803 | 0.0000 | 0.0000 | 0.0000 | 0.0901 |
| 15 | mod.cls_blocks.0.attn.h4 | photon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.1607 | 0.0000 | 0.0000 | 0.0000 | 0.0804 |
| 16 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0643 | -0.0353 | 0.0353 | -0.0605 | -0.0353 | 20.2855 | 0.0821 | 0.0744 |
| 17 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.2349 | 0.0357 | 0.0357 | 0.0588 | 0.0357 | 50.0922 | 0.0142 | 0.0740 |
| 18 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-muon | 0.1109 | 0.0370 | 0.0370 | 0.0476 | 0.0363 | 36.5028 | 0.0354 | 0.0700 |
| 19 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0453 | 0.0411 | 0.0633 | 0.0245 | 0.0343 | 3.2044 | 0.0033 | 0.0691 |
| 20 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-CLS | 0.0299 | 0.0352 | 0.0352 | 0.0496 | 0.0352 | 66.5560 | 0.0394 | 0.0689 |
| 21 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0364 | 0.0370 | 0.0438 | 0.0375 | 0.0228 | 9.0731 | 0.0082 | 0.0667 |
| 22 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0350 | 0.0547 | 0.0303 | 0.0191 | 2.8714 | 0.0036 | 0.0638 |
| 23 | mod.cls_blocks.0.attn.h1 | CLS<-CLS | 0.0305 | 0.0300 | 0.0300 | 0.0424 | 0.0300 | 66.5560 | 0.0331 | 0.0587 |
| 24 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0293 | -0.0268 | 0.0324 | -0.0429 | -0.0153 | 1.6391 | 0.0045 | 0.0563 |
| 25 | mod.cls_blocks.0.attn.h6 | muon<-CLS | 0.0000 | 0.0000 | 0.0000 | 0.0988 | 0.0000 | 0.0000 | 0.0000 | 0.0494 |
| 26 | mod.cls_blocks.0.attn.h1 | CLS<-muon | 0.0975 | 0.0218 | 0.0275 | 0.0326 | 0.0030 | 30.7758 | 0.0359 | 0.0449 |
| 27 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0345 | -0.0257 | 0.0276 | -0.0245 | -0.0257 | 6.7118 | 0.0092 | 0.0449 |
| 28 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0373 | -0.0152 | 0.0185 | -0.0467 | -0.4142 | 16.1238 | 0.0661 | 0.0432 |
| 29 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0450 | -0.0195 | 0.0195 | -0.0305 | -0.0195 | 26.4818 | 0.0308 | 0.0397 |
| 30 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0314 | -0.0193 | 0.0216 | -0.0285 | -0.0123 | 2.8223 | 0.0038 | 0.0389 |

## Top value/write role-links: `B_tbl_minus_hqql`
| rank | head | pair | B_A | B_write | B_abs_write | B-A | B-C | V_norm | grad_norm | support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.cls_blocks.0.attn.h4 | electron<-electron | 0.1342 | 0.2892 | 0.2892 | 0.2892 | 0.2892 | 152.1468 | 0.0214 | 0.5061 |
| 2 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-neutral_hadron | 0.0518 | 0.2288 | 0.2586 | 0.2288 | 0.2288 | 17.6911 | 0.0181 | 0.4078 |
| 3 | mod.cls_blocks.0.attn.h4 | CLS<-neutral_hadron | 0.0450 | 0.1340 | 0.1686 | 0.1340 | 0.1340 | 13.8688 | 0.0149 | 0.2432 |
| 4 | mod.cls_blocks.0.attn.h6 | neutral_hadron<-neutral_hadron | 0.0464 | 0.0782 | 0.0845 | 0.0782 | 0.0782 | 12.9731 | 0.0099 | 0.1384 |
| 5 | mod.cls_blocks.0.attn.h6 | electron<-electron | 0.1207 | 0.0623 | 0.0623 | 0.0623 | 0.0623 | 102.3998 | 0.0111 | 0.1091 |
| 6 | mod.cls_blocks.0.attn.h6 | CLS<-neutral_hadron | 0.0402 | 0.0469 | 0.0538 | 0.0469 | 0.0469 | 10.5248 | 0.0082 | 0.0838 |
| 7 | mod.cls_blocks.0.attn.h4 | charged_hadron<-charged_hadron | 0.0453 | 0.0411 | 0.0633 | 0.0411 | 0.0411 | 3.2044 | 0.0033 | 0.0774 |
| 8 | mod.cls_blocks.0.attn.h4 | photon<-photon | 0.0310 | 0.0350 | 0.0547 | 0.0350 | 0.0350 | 2.8714 | 0.0036 | 0.0661 |
| 9 | mod.cls_blocks.0.attn.h4 | photon<-muon | 0.0643 | -0.0353 | 0.0353 | -0.0353 | -0.0353 | 20.2855 | 0.0821 | 0.0618 |
| 10 | mod.cls_blocks.0.attn.h4 | CLS<-electron | 0.0373 | 0.0290 | 0.0319 | 0.0290 | 0.0290 | 30.7756 | 0.0312 | 0.0515 |
| 11 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-charged_hadron | 0.0288 | -0.0254 | 0.0322 | -0.0254 | -0.0254 | 1.5988 | 0.0045 | 0.0461 |
| 12 | mod.cls_blocks.0.attn.h4 | photon<-neutral_hadron | 0.0345 | -0.0257 | 0.0276 | -0.0257 | -0.0257 | 6.7118 | 0.0092 | 0.0455 |
| 13 | mod.cls_blocks.0.attn.h0 | neutral_hadron<-neutral_hadron | 0.0400 | 0.0204 | 0.0270 | 0.0204 | 0.0204 | 8.8665 | 0.0099 | 0.0373 |
| 14 | mod.cls_blocks.0.attn.h4 | charged_hadron<-photon | 0.0314 | -0.0193 | 0.0216 | -0.0193 | -0.0193 | 2.8223 | 0.0038 | 0.0343 |
| 15 | mod.cls_blocks.0.attn.h0 | charged_hadron<-electron | 0.0450 | -0.0195 | 0.0195 | -0.0195 | -0.0195 | 26.4818 | 0.0308 | 0.0342 |
| 16 | mod.cls_blocks.0.attn.h4 | neutral_hadron<-photon | 0.0225 | -0.0186 | 0.0205 | -0.0186 | -0.0186 | 1.4793 | 0.0043 | 0.0330 |
| 17 | mod.cls_blocks.0.attn.h4 | CLS<-charged_hadron | 0.0316 | -0.0153 | 0.0308 | -0.0153 | -0.0153 | 1.8048 | 0.0040 | 0.0306 |
| 18 | mod.cls_blocks.0.attn.h5 | charged_hadron<-electron | 0.0756 | -0.0153 | 0.0153 | -0.0153 | -0.0153 | 24.3095 | 0.0249 | 0.0268 |
| 19 | mod.cls_blocks.0.attn.h0 | photon<-muon | 0.0468 | -0.0147 | 0.0147 | -0.0147 | -0.0147 | 30.5716 | 0.0346 | 0.0257 |
| 20 | mod.cls_blocks.0.attn.h1 | neutral_hadron<-neutral_hadron | 0.0324 | 0.0141 | 0.0182 | 0.0141 | 0.0141 | 9.9930 | 0.0117 | 0.0257 |
| 21 | mod.cls_blocks.0.attn.h1 | electron<-electron | 0.0321 | 0.0143 | 0.0143 | 0.0143 | 0.0143 | 66.5561 | 0.0142 | 0.0250 |
| 22 | mod.cls_blocks.0.attn.h6 | charged_hadron<-charged_hadron | 0.0449 | 0.0131 | 0.0205 | 0.0131 | 0.0131 | 2.7663 | 0.0019 | 0.0248 |
| 23 | mod.cls_blocks.0.attn.h4 | electron<-charged_hadron | 0.0429 | -0.0129 | 0.0186 | -0.0129 | -0.0129 | 2.4433 | 0.0018 | 0.0240 |
| 24 | mod.cls_blocks.0.attn.h4 | electron<-neutral_hadron | 0.0349 | -0.0132 | 0.0132 | -0.0132 | -0.0132 | 32.5168 | 0.0214 | 0.0230 |
| 25 | mod.cls_blocks.0.attn.h0 | CLS<-neutral_hadron | 0.0361 | 0.0120 | 0.0186 | 0.0120 | 0.0120 | 7.5238 | 0.0087 | 0.0227 |
| 26 | mod.cls_blocks.0.attn.h6 | photon<-photon | 0.0346 | 0.0114 | 0.0192 | 0.0114 | 0.0114 | 2.6164 | 0.0021 | 0.0219 |
| 27 | mod.cls_blocks.0.attn.h4 | CLS<-photon | 0.0250 | -0.0092 | 0.0256 | -0.0092 | -0.0092 | 1.8787 | 0.0040 | 0.0203 |
| 28 | mod.blocks.3.attn.h5 | electron<-muon | 0.2032 | -0.0102 | 0.0102 | -0.0102 | -0.0102 | 6.1546 | 0.0047 | 0.0178 |
| 29 | mod.cls_blocks.0.attn.h4 | CLS<-muon | 0.0339 | -0.0093 | 0.0142 | -0.0093 | -0.0093 | 16.9426 | 0.0661 | 0.0176 |
| 30 | mod.cls_blocks.0.attn.h4 | photon<-charged_hadron | 0.0311 | -0.0096 | 0.0116 | -0.0096 | -0.0096 | 1.6105 | 0.0031 | 0.0174 |

## Interpretation

- `B_write`: signed value/write contribution for B_Hqql_to_Tbl. Positive means the value written through this role-link increases the objective; negative resists it.
- `B_abs_write`: magnitude regardless of sign; high values mean the role-link writes a strong signal even if mixed.
- `V_norm` and `grad_norm` separate whether the link is strong because the value vector is large or because the downstream objective is sensitive.
- This is the missing write-side evidence to connect natural attention routes to matrix-program effects.
