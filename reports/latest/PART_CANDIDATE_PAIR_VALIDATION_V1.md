# PART_CANDIDATE_PAIR_VALIDATION_V1

Exact head+role-pair validation over discovery candidates. It applies down/up attention-logit interventions to the exact candidate pair and checks whether B_Hqql_to_Tbl margin moves in the expected direction.

- events: **256**
- candidates_tested: **24**
- rows: **144**

## Top validated pair candidates
| rank | head | pair | diag | action | ok | best_s | B_delta | B_flip | A_dmg | C_dmg | B_write | Agrad | rules | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | mod.blocks.7.attn.h3 | charged_hadron<-muon | causal_candidate | up | 3 | 20.0000 | -0.1163 | -0.0312 | 0.0385 | 0.1657 | -5.225e-04 | -5.225e-04 | 2 | 0.1278 |
| 2 | mod.blocks.7.attn.h3 | charged_hadron<-electron | causal_candidate | up | 3 | 40.0000 | -0.0682 | -0.0312 | 0.0503 | 0.1253 | -6.774e-04 | -6.774e-04 | 2 | 0.0868 |
| 3 | mod.blocks.7.attn.h3 | photon<-muon | causal_candidate | up | 3 | 20.0000 | -0.0853 | -0.0156 | 0.0256 | 0.1315 | -3.182e-04 | -3.182e-04 | 2 | 0.0773 |
| 4 | mod.blocks.7.attn.h3 | charged_hadron<-neutral_hadron | causal_candidate | down | 3 | 40.0000 | -0.0072 | -0.0312 | 0.0039 | 0.0012 | 1.220e-05 | 1.220e-05 | 2 | 0.0684 |
| 5 | mod.blocks.7.attn.h3 | photon<-electron | causal_candidate | up | 3 | 80.0000 | -0.0579 | -0.0156 | 0.0340 | 0.0941 | -3.540e-04 | -3.540e-04 | 2 | 0.0571 |
| 6 | mod.blocks.7.attn.h3 | charged_hadron<-charged_hadron | causal_candidate | down | 3 | 40.0000 | -0.0425 | -0.0156 | 0.0338 | 0.0617 | 4.247e-05 | 4.247e-05 | 2 | 0.0499 |
| 7 | mod.blocks.7.attn.h3 | charged_hadron<-photon | causal_candidate | up | 3 | 20.0000 | 0.0593 | -0.0156 | 0.1208 | 0.0437 | 1.948e-05 | 1.948e-05 | 2 | 0.0494 |
| 8 | mod.blocks.7.attn.h3 | photon<-charged_hadron | causal_candidate | down | 3 | 40.0000 | -0.0260 | -0.0156 | 0.0184 | 0.0310 | 2.927e-05 | 2.927e-05 | 2 | 0.0449 |
| 9 | mod.blocks.7.attn.h3 | neutral_hadron<-muon | causal_candidate | up | 3 | 80.0000 | -0.0161 | -0.0156 | 0.0025 | 0.0233 | -3.625e-04 | -3.625e-04 | 2 | 0.0409 |
| 10 | mod.blocks.7.attn.h3 | neutral_hadron<-electron | causal_candidate | up | 3 | 80.0000 | -0.0132 | -0.0156 | 0.0044 | 0.0190 | -3.257e-04 | -3.257e-04 | 2 | 0.0386 |
| 11 | mod.blocks.7.attn.h3 | neutral_hadron<-neutral_hadron | causal_candidate | down | 3 | 20.0000 | -0.0043 | -0.0156 | 2.816e-04 | 6.771e-05 | 1.292e-05 | 1.292e-05 | 2 | 0.0354 |
| 12 | mod.blocks.7.attn.h3 | neutral_hadron<-photon | causal_candidate | up | 3 | 40.0000 | 0.0079 | -0.0156 | 0.0113 | 0.0069 | 1.535e-05 | 1.535e-05 | 2 | 0.0346 |
| 13 | mod.blocks.7.attn.h3 | electron<-neutral_hadron | causal_candidate | down | 3 | 20.0000 | -8.941e-04 | -0.0156 | 1.044e-04 | 6.202e-04 | 3.658e-05 | 3.658e-05 | 2 | 0.0320 |
| 14 | mod.blocks.7.attn.h3 | charged_hadron<-charged_hadron | causal_candidate | up | 3 | 40.0000 | 0.0677 | 0.0000 | 0.1503 | 0.0610 | 4.247e-05 | 4.247e-05 | 2 | 0.0148 |
| 15 | mod.blocks.7.attn.h3 | photon<-neutral_hadron | causal_candidate | up | 3 | 80.0000 | 0.0066 | -0.0156 | 0.0896 | 0.0032 | 2.140e-05 | 2.140e-05 | 2 | 0.0147 |
| 16 | mod.blocks.7.attn.h3 | charged_hadron<-muon | causal_candidate | down | 3 | 20.0000 | 0.0332 | 0.0000 | 0.0617 | 0.0279 | -5.225e-04 | -5.225e-04 | 2 | 0.0108 |
| 17 | mod.blocks.7.attn.h3 | neutral_hadron<-charged_hadron | causal_candidate | up | 3 | 40.0000 | 0.0123 | 0.0000 | 0.0111 | 0.0056 | 2.727e-05 | 2.727e-05 | 2 | 0.0081 |
| 18 | mod.blocks.7.attn.h3 | photon<-photon | causal_candidate | down | 3 | 20.0000 | -0.0106 | 0.0000 | 0.0094 | 0.0092 | 1.989e-05 | 1.989e-05 | 2 | 0.0059 |
| 19 | mod.blocks.7.attn.h3 | charged_hadron<-electron | causal_candidate | down | 3 | 20.0000 | 0.0305 | 0.0000 | 0.0745 | 0.0248 | -6.774e-04 | -6.774e-04 | 2 | 0.0057 |
| 20 | mod.blocks.7.attn.h3 | neutral_hadron<-neutral_hadron | causal_candidate | up | 3 | 20.0000 | 0.0091 | 0.0000 | 0.0142 | 0.0020 | 1.292e-05 | 1.292e-05 | 2 | 0.0051 |
| 21 | mod.blocks.7.attn.h3 | neutral_hadron<-electron | causal_candidate | down | 3 | 20.0000 | 0.0062 | 0.0000 | 0.0045 | 0.0028 | -3.257e-04 | -3.257e-04 | 2 | 0.0044 |
| 22 | mod.blocks.7.attn.h3 | photon<-muon | causal_candidate | down | 3 | 40.0000 | 0.0144 | 0.0000 | 0.0317 | 0.0126 | -3.182e-04 | -3.182e-04 | 2 | 0.0033 |
| 23 | mod.blocks.7.attn.h3 | charged_hadron<-photon | causal_candidate | down | 3 | 20.0000 | -0.0070 | 0.0000 | 0.0033 | 0.0114 | 1.948e-05 | 1.948e-05 | 2 | 0.0033 |
| 24 | mod.blocks.7.attn.h3 | photon<-neutral_hadron | causal_candidate | down | 3 | 40.0000 | -0.0039 | 0.0000 | 0.0023 | 8.118e-04 | 2.140e-05 | 2.140e-05 | 2 | 0.0032 |
| 25 | mod.blocks.7.attn.h3 | neutral_hadron<-muon | causal_candidate | down | 3 | 20.0000 | 0.0053 | 0.0000 | 0.0066 | 0.0028 | -3.625e-04 | -3.625e-04 | 2 | 0.0030 |
| 26 | mod.blocks.7.attn.h3 | neutral_hadron<-charged_hadron | causal_candidate | down | 3 | 40.0000 | -0.0048 | 0.0000 | 0.0015 | 0.0065 | 2.727e-05 | 2.727e-05 | 2 | 0.0027 |
| 27 | mod.blocks.7.attn.h3 | electron<-photon | causal_candidate | up | 3 | 40.0000 | 0.0062 | 0.0000 | 0.0143 | 0.0039 | 2.304e-05 | 2.304e-05 | 2 | 0.0017 |
| 28 | mod.blocks.7.attn.h3 | muon<-electron | causal_candidate | down | 3 | 20.0000 | 0.0029 | 0.0000 | 7.026e-06 | 0.0049 | -0.0019 | -0.0019 | 2 | 0.0016 |
| 29 | mod.blocks.7.attn.h3 | neutral_hadron<-photon | causal_candidate | down | 3 | 40.0000 | -0.0021 | 0.0000 | 8.617e-04 | 0.0026 | 1.535e-05 | 1.535e-05 | 2 | 0.0012 |
| 30 | mod.blocks.7.attn.h3 | muon<-charged_hadron | causal_candidate | up | 3 | 20.0000 | 0.0027 | 0.0000 | 8.169e-04 | 0.0064 | 2.199e-04 | 2.199e-04 | 2 | 8.867e-04 |
| 31 | mod.blocks.7.attn.h3 | photon<-photon | causal_candidate | up | 3 | 40.0000 | 0.0245 | 0.0000 | 0.0757 | 0.0207 | 1.989e-05 | 1.989e-05 | 2 | 4.578e-04 |
| 32 | mod.blocks.7.attn.h3 | muon<-photon | causal_candidate | down | 3 | 20.0000 | -2.337e-04 | 0.0000 | 6.714e-05 | 6.452e-04 | 2.464e-05 | 2.464e-05 | 2 | 5.557e-05 |
| 33 | mod.blocks.7.attn.h3 | electron<-photon | causal_candidate | down | 3 | 20.0000 | -1.830e-04 | 0.0000 | 3.453e-04 | 1.829e-04 | 2.304e-05 | 2.304e-05 | 2 | 5.093e-05 |
| 34 | mod.blocks.7.attn.h3 | muon<-neutral_hadron | causal_candidate | down | 0 | 40.0000 | 1.935e-04 | 0.0000 | 1.006e-06 | 2.931e-04 | 3.053e-05 | 3.053e-05 | 2 | -7.353e-05 |
| 35 | mod.blocks.7.attn.h3 | electron<-muon | causal_candidate | down | 3 | 20.0000 | 4.386e-04 | 0.0000 | 2.712e-05 | 0.0023 | -5.469e-04 | -5.469e-04 | 2 | -1.442e-04 |
| 36 | mod.blocks.7.attn.h3 | photon<-charged_hadron | causal_candidate | up | 3 | 20.0000 | 0.0318 | 0.0000 | 0.0934 | 0.0347 | 2.927e-05 | 2.927e-05 | 2 | -2.433e-04 |
| 37 | mod.blocks.7.attn.h3 | muon<-photon | causal_candidate | up | 3 | 20.0000 | 0.0051 | 0.0000 | 0.0131 | 0.0083 | 2.464e-05 | 2.464e-05 | 2 | -2.464e-04 |
| 38 | mod.blocks.7.attn.h3 | electron<-muon | causal_candidate | up | 3 | 40.0000 | -0.0034 | 0.0000 | 5.069e-04 | 0.0140 | -5.469e-04 | -5.469e-04 | 2 | -2.487e-04 |
| 39 | mod.blocks.7.attn.h3 | photon<-electron | causal_candidate | down | 3 | 20.0000 | 0.0155 | 0.0000 | 0.0506 | 0.0148 | -3.540e-04 | -3.540e-04 | 2 | -8.572e-04 |
| 40 | mod.blocks.7.attn.h3 | electron<-electron | causal_candidate | down | 0 | 20.0000 | 4.622e-05 | 0.0000 | 0.0036 | 0.0011 | 2.234e-06 | 2.234e-06 | 2 | -0.0012 |
| 41 | mod.blocks.7.attn.h3 | electron<-charged_hadron | causal_candidate | up | 3 | 40.0000 | 5.816e-04 | 0.0000 | 0.0030 | 0.0044 | 6.600e-05 | 6.600e-05 | 2 | -0.0013 |
| 42 | mod.blocks.7.attn.h3 | electron<-neutral_hadron | causal_candidate | up | 3 | 20.0000 | 0.0040 | 0.0000 | 0.0181 | 0.0045 | 3.658e-05 | 3.658e-05 | 2 | -0.0017 |
| 43 | mod.blocks.7.attn.h3 | muon<-electron | causal_candidate | up | 3 | 40.0000 | -7.334e-04 | 0.0000 | 7.772e-05 | 0.0100 | -0.0019 | -0.0019 | 2 | -0.0018 |
| 44 | mod.blocks.7.attn.h3 | charged_hadron<-neutral_hadron | causal_candidate | up | 3 | 80.0000 | 0.0326 | 0.0000 | 0.1339 | 0.0057 | 1.220e-05 | 1.220e-05 | 2 | -0.0023 |
| 45 | mod.blocks.7.attn.h3 | muon<-neutral_hadron | causal_candidate | up | 3 | 80.0000 | 0.0025 | 0.0000 | 0.0162 | 0.0034 | 3.053e-05 | 3.053e-05 | 2 | -0.0024 |
| 46 | mod.blocks.7.attn.h3 | muon<-charged_hadron | causal_candidate | down | 0 | 40.0000 | 9.548e-04 | 0.0000 | 0.0110 | 0.0038 | 2.199e-04 | 2.199e-04 | 2 | -0.0037 |
| 47 | mod.blocks.7.attn.h3 | electron<-charged_hadron | causal_candidate | down | 0 | 20.0000 | 0.0035 | 0.0000 | 0.0108 | 0.0075 | 6.600e-05 | 6.600e-05 | 2 | -0.0046 |
| 48 | mod.blocks.7.attn.h3 | electron<-electron | causal_candidate | up | 0 | 20.0000 | -0.0068 | -0.0156 | 0.0033 | 0.0336 | 2.234e-06 | 2.234e-06 | 2 | -0.0092 |
