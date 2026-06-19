# FULL HEAD QUESTION CATALOG

This is the huge explicit list the project needs: every current pseudo-head multiplied by every question/lens we should ask.

## Counts

- Heads: **24**
- Questions per head: **14**
- Total question rows: **336**
- Status counts: `{"ANSWERED_PARTIAL": 96, "TODO_P0": 120, "TODO_P1": 96, "TODO_P2": 24}`

## Question types

| question_id | status | priority | question | next lens |
| --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | head_projection_composer_v2 + activation-cluster pseudo-head lens |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | weight projection WL4 block interaction + activation source clustering |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | feature-channel lens + permutation/noise controls |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | compact/wide route causal lens |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | leading-particle top-k sweep lens |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | per-class head patch + signed logit attribution |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | class contrast projection lens WL6 + component activation projection |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | activation-cluster pseudo-head lens |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | random channel-group control |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | weight-vs-activation-vs-patch consistency lens |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | heldout stability lens |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | error-route lens |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | KNN neighbor-to-head route lens |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | multi-head composition lens |

## Heads overview

| head | layer | group | acc_drop | role | current best question | semantic hint |
| --- | --- | --- | --- | --- | --- | --- |
| L1_ch16:32 | 1 | ch16:32 | 0.2641 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq |
| L0_ch24:32 | 0 | ch24:32 | 0.1996 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Hgg |
| L0_ch0:8 | 0 | ch0:8 | 0.1602 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_Hbb |
| L0_ch40:48 | 0 | ch40:48 | 0.1371 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq |
| L0_ch48:56 | 0 | ch48:56 | 0.1359 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_H4q, label_Hcc, label_Hbb |
| L0_ch8:16 | 0 | ch8:16 | 0.1348 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Hbb |
| L0_ch16:24 | 0 | ch16:24 | 0.1277 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_Zqq |
| L1_ch112:128 | 1 | ch112:128 | 0.1156 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_H4q, label_Hgg |
| L0_ch56:64 | 0 | ch56:64 | 0.0852 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_H4q, label_Hgg |
| L2_ch0:32 | 2 | ch0:32 | 0.0797 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Tbl |
| L1_ch96:112 | 1 | ch96:112 | 0.0734 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hqql |
| L2_ch224:256 | 2 | ch224:256 | 0.0629 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hbb, label_Wqq, label_Zqq |
| L1_ch32:48 | 1 | ch32:48 | 0.0484 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_Tbqq |
| L0_ch32:40 | 0 | ch32:40 | 0.0422 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Zqq |
| L1_ch0:16 | 1 | ch0:16 | 0.0234 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq |
| L1_ch48:64 | 1 | ch48:64 | 0.0215 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_H4q |
| L1_ch64:80 | 1 | ch64:80 | 0.0195 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hcc |
| L2_ch32:64 | 2 | ch32:64 | 0.0160 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_H4q |
| L2_ch64:96 | 2 | ch64:96 | 0.0156 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_QCD, label_Hbb, label_Hcc |
| L1_ch80:96 | 1 | ch80:96 | 0.0156 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_H4q |
| L2_ch128:160 | 2 | ch128:160 | 0.0121 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Tbqq |
| L2_ch192:224 | 2 | ch192:224 | 0.0086 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Tbqq, label_Wqq, label_Zqq |
| L2_ch160:192 | 2 | ch160:192 | 0.0066 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Hcc |
| L2_ch96:128 | 2 | ch96:128 | -0.0012 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_QCD, label_H4q, label_Hgg |

## L1_ch16:32 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.2641`, patch_acc `0.4934`, delta_logit `9.1146`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L1 ch16:32 | Weight lens: source/input blocks -> output ch16:32 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Hbb, label_Hcc, label_Zqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 16:32 carries 0.3578 of module weight energy. || WL2 input/source projection: Input slice 16:32 carries 0.3557 of module weight energy. || WL3 output pseudo-head projection: Output group 16:32 carries 0.3524 of module weight energy. || WL3 output pseudo-head projection: Output group 16:32 carries 0.3488 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hbb: drop=14.3446, acc=0.2578 || label_Hcc: drop=12.5046, acc=0.1875 || label_Zqq: drop=11.1146, acc=0.0898 || label_Wqq: drop=10.5074, acc=0.0430 || label_H4q: drop=10.0451, acc=0.5273 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch24:32 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1996`, patch_acc `0.5578`, delta_logit `2.3407`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Hgg

**Composite lens:** `Patch lens: zero EdgeConv L0 ch24:32 | Weight lens: source/input blocks -> output ch24:32 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Hbb, label_Hcc, label_Hgg`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 24:32 carries 0.3864 of module weight energy. || WL3 output pseudo-head projection: Output group 24:32 carries 0.3478 of module weight energy. || WL2 input/source projection: Input slice 24:32 carries 0.3271 of module weight energy. || WL2 input/source projection: Input slice 24:32 carries 0.3261 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Hgg | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hbb: drop=3.6554, acc=0.5039 || label_Hcc: drop=3.5842, acc=0.2383 || label_Hgg: drop=3.3949, acc=0.4922 || label_Zqq: drop=3.3818, acc=0.1836 || label_H4q: drop=3.3739, acc=0.5859 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch0:8 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1602`, patch_acc `0.5973`, delta_logit `0.8533`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Tbl, label_Hcc, label_Hbb

**Composite lens:** `Patch lens: zero EdgeConv L0 ch0:8 | Weight lens: source/input blocks -> output ch0:8 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Tbl, label_Hcc, label_Hbb`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 0:8 carries 0.4766 of module weight energy. || WL4 block interaction projection: Block 9:11->0:8 carries 0.3740 of module weight energy. || WL3 output pseudo-head projection: Output group 0:8 carries 0.3644 of module weight energy. || WL3 output pseudo-head projection: Output group 0:8 carries 0.3553 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_Hbb | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbl: drop=1.9491, acc=0.7734 || label_Hcc: drop=1.5474, acc=0.4453 || label_Hbb: drop=1.2686, acc=0.3984 || label_Zqq: drop=1.2602, acc=0.3477 || label_Wqq: drop=0.9157, acc=0.3438 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch40:48 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1371`, patch_acc `0.6203`, delta_logit `3.8152`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq

**Composite lens:** `Patch lens: zero EdgeConv L0 ch40:48 | Weight lens: source/input blocks -> output ch40:48 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Hqql, label_Zqq, label_Wqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 40:48 carries 0.3866 of module weight energy. || WL2 input/source projection: Input slice 40:48 carries 0.3768 of module weight energy. || WL3 output pseudo-head projection: Output group 40:48 carries 0.3423 of module weight energy. || WL3 output pseudo-head projection: Output group 40:48 carries 0.3396 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hqql: drop=5.6707, acc=0.7539 || label_Zqq: drop=5.1546, acc=0.0781 || label_Wqq: drop=5.0696, acc=0.3984 || label_Hcc: drop=3.8231, acc=0.2930 || label_H4q: drop=3.7930, acc=0.6797 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch48:56 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1359`, patch_acc `0.6215`, delta_logit `1.3935`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_H4q, label_Hcc, label_Hbb

**Composite lens:** `Patch lens: zero EdgeConv L0 ch48:56 | Weight lens: source/input blocks -> output ch48:56 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_H4q, label_Hcc, label_Hbb`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 48:56 carries 0.3956 of module weight energy. || WL3 output pseudo-head projection: Output group 48:56 carries 0.3568 of module weight energy. || WL3 output pseudo-head projection: Output group 48:56 carries 0.3555 of module weight energy. || WL2 input/source projection: Input slice 48:56 carries 0.3549 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_H4q, label_Hcc, label_Hbb | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_H4q: drop=2.0118, acc=0.4414 || label_Hcc: drop=1.7808, acc=0.3438 || label_Hbb: drop=1.6748, acc=0.3828 || label_Hgg: drop=1.5961, acc=0.8047 || label_Tbqq: drop=1.5847, acc=0.6914 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch8:16 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1348`, patch_acc `0.6227`, delta_logit `1.6804`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Hbb

**Composite lens:** `Patch lens: zero EdgeConv L0 ch8:16 | Weight lens: source/input blocks -> output ch8:16 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Wqq, label_Hcc, label_Hbb`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 8:16 carries 0.4536 of module weight energy. || WL3 output pseudo-head projection: Output group 8:16 carries 0.4241 of module weight energy. || WL3 output pseudo-head projection: Output group 8:16 carries 0.3584 of module weight energy. || WL2 input/source projection: Input slice 8:16 carries 0.3273 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Hbb | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Wqq: drop=2.3991, acc=0.6211 || label_Hcc: drop=2.3409, acc=0.1602 || label_Hbb: drop=2.0909, acc=0.7188 || label_Zqq: drop=1.9289, acc=0.4258 || label_Hqql: drop=1.9026, acc=0.8945 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch16:24 — early feature/geometry/PID reader

**Effect:** acc_drop `0.1277`, patch_acc `0.6297`, delta_logit `1.0691`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L0 ch16:24 | Weight lens: source/input blocks -> output ch16:24 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Tbqq, label_Hgg, label_Zqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 16:24 carries 0.4144 of module weight energy. || WL2 input/source projection: Input slice 16:24 carries 0.3697 of module weight energy. || WL4 block interaction projection: Block 22:26->16:24 carries 0.3275 of module weight energy. || WL2 input/source projection: Input slice 16:24 carries 0.3249 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_Zqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbqq: drop=1.8746, acc=0.7383 || label_Hgg: drop=1.8032, acc=0.2422 || label_Zqq: drop=1.3137, acc=0.3867 || label_Wqq: drop=1.3008, acc=0.7344 || label_Hcc: drop=1.2524, acc=0.3398 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch112:128 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.1156`, patch_acc `0.6418`, delta_logit `3.2633`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Hbb, label_H4q, label_Hgg

**Composite lens:** `Patch lens: zero EdgeConv L1 ch112:128 | Weight lens: source/input blocks -> output ch112:128 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Hbb, label_H4q, label_Hgg`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 112:128 carries 0.3978 of module weight energy. || WL2 input/source projection: Input slice 112:128 carries 0.3728 of module weight energy. || WL3 output pseudo-head projection: Output group 112:128 carries 0.3662 of module weight energy. || WL3 output pseudo-head projection: Output group 112:128 carries 0.3647 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hbb, label_H4q, label_Hgg | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hbb: drop=4.7396, acc=0.6328 || label_H4q: drop=4.6334, acc=0.6172 || label_Hgg: drop=4.5187, acc=0.6172 || label_Hcc: drop=4.3861, acc=0.3242 || label_Tbqq: drop=3.0648, acc=0.9336 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch56:64 — early feature/geometry/PID reader

**Effect:** acc_drop `0.0852`, patch_acc `0.6723`, delta_logit `0.6102`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Hqql, label_H4q, label_Hgg

**Composite lens:** `Patch lens: zero EdgeConv L0 ch56:64 | Weight lens: source/input blocks -> output ch56:64 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Hqql, label_H4q, label_Hgg`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 56:64 carries 0.3879 of module weight energy. || WL3 output pseudo-head projection: Output group 56:64 carries 0.3826 of module weight energy. || WL3 output pseudo-head projection: Output group 56:64 carries 0.3679 of module weight energy. || WL2 input/source projection: Input slice 56:64 carries 0.3398 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hqql, label_H4q, label_Hgg | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hqql: drop=1.0867, acc=0.8633 || label_H4q: drop=1.0004, acc=0.4219 || label_Hgg: drop=0.8431, acc=0.6562 || label_Wqq: drop=0.6603, acc=0.4570 || label_Zqq: drop=0.6129, acc=0.5977 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch0:32 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0797`, patch_acc `0.6777`, delta_logit `0.8878`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_H4q, label_Hgg, label_Tbl

**Composite lens:** `Patch lens: zero EdgeConv L2 ch0:32 | Weight lens: source/input blocks -> output ch0:32 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_H4q, label_Hgg, label_Tbl`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 0:32 carries 0.3803 of module weight energy. || WL2 input/source projection: Input slice 0:32 carries 0.3585 of module weight energy. || WL3 output pseudo-head projection: Output group 0:32 carries 0.3517 of module weight energy. || WL2 input/source projection: Input slice 0:32 carries 0.3464 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Tbl | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_H4q: drop=2.4325, acc=0.1680 || label_Hgg: drop=1.6845, acc=0.3906 || label_Tbl: drop=1.3911, acc=0.9766 || label_Hqql: drop=0.9546, acc=0.9375 || label_Hbb: drop=0.6631, acc=0.6250 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch96:112 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0734`, patch_acc `0.6840`, delta_logit `0.8114`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hqql

**Composite lens:** `Patch lens: zero EdgeConv L1 ch96:112 | Weight lens: source/input blocks -> output ch96:112 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_H4q, label_Hgg, label_Hqql`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 96:112 carries 0.3922 of module weight energy. || WL3 output pseudo-head projection: Output group 96:112 carries 0.3704 of module weight energy. || WL3 output pseudo-head projection: Output group 96:112 carries 0.3555 of module weight energy. || WL3 output pseudo-head projection: Output group 96:112 carries 0.3498 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hqql | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_H4q: drop=1.5645, acc=0.7852 || label_Hgg: drop=1.3860, acc=0.5391 || label_Hqql: drop=1.1903, acc=0.8906 || label_Hcc: drop=1.1874, acc=0.2539 || label_Hbb: drop=0.8001, acc=0.8164 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch224:256 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0629`, patch_acc `0.6945`, delta_logit `4.7637`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_Hbb, label_Wqq, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L2 ch224:256 | Weight lens: source/input blocks -> output ch224:256 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_Hbb, label_Wqq, label_Zqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 224:256 carries 0.3697 of module weight energy. || WL2 input/source projection: Input slice 224:256 carries 0.3569 of module weight energy. || WL3 output pseudo-head projection: Output group 224:256 carries 0.3563 of module weight energy. || WL3 output pseudo-head projection: Output group 224:256 carries 0.3554 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hbb, label_Wqq, label_Zqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hbb: drop=6.4418, acc=0.5938 || label_Wqq: drop=6.3631, acc=0.3633 || label_Zqq: drop=5.9527, acc=0.3516 || label_Hcc: drop=5.7249, acc=0.5195 || label_Tbl: drop=4.4718, acc=0.9805 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch32:48 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0484`, patch_acc `0.7090`, delta_logit `0.4806`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Tbl, label_Hqql, label_Tbqq

**Composite lens:** `Patch lens: zero EdgeConv L1 ch32:48 | Weight lens: source/input blocks -> output ch32:48 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Tbl, label_Hqql, label_Tbqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 32:48 carries 0.3585 of module weight energy. || WL2 input/source projection: Input slice 32:48 carries 0.3578 of module weight energy. || WL3 output pseudo-head projection: Output group 32:48 carries 0.3521 of module weight energy. || WL2 input/source projection: Input slice 32:48 carries 0.3487 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_Tbqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbl: drop=1.7141, acc=0.9375 || label_Hqql: drop=0.6421, acc=0.9609 || label_Tbqq: drop=0.5872, acc=0.8867 || label_QCD: drop=0.5776, acc=0.5820 || label_Hgg: drop=0.4599, acc=0.3594 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L0_ch32:40 — early feature/geometry/PID reader

**Effect:** acc_drop `0.0422`, patch_acc `0.7152`, delta_logit `0.4912`.

**Current best question:** Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence?

**Semantic hint:** kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L0 ch32:40 | Weight lens: source/input blocks -> output ch32:40 | Physical feature lens: raw kin/PID/geometry -> this pseudo-head | Class lens: strongest affected classes = label_Wqq, label_Hcc, label_Zqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 32:40 carries 0.4167 of module weight energy. || WL3 output pseudo-head projection: Output group 32:40 carries 0.3844 of module weight energy. || WL3 output pseudo-head projection: Output group 32:40 carries 0.3673 of module weight energy. || WL2 input/source projection: Input slice 32:40 carries 0.3491 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Zqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Wqq: drop=0.8320, acc=0.8047 || label_Hcc: drop=0.7634, acc=0.4375 || label_Zqq: drop=0.7254, acc=0.4375 || label_QCD: drop=0.7075, acc=0.6758 || label_Hbb: drop=0.6087, acc=0.5820 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch0:16 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0234`, patch_acc `0.7340`, delta_logit `0.2483`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq

**Composite lens:** `Patch lens: zero EdgeConv L1 ch0:16 | Weight lens: source/input blocks -> output ch0:16 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Hqql, label_Zqq, label_Wqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 0:16 carries 0.3656 of module weight energy. || WL2 input/source projection: Input slice 0:16 carries 0.3631 of module weight energy. || WL3 output pseudo-head projection: Output group 0:16 carries 0.3600 of module weight energy. || WL3 output pseudo-head projection: Output group 0:16 carries 0.3538 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hqql: drop=0.4776, acc=0.9492 || label_Zqq: drop=0.4502, acc=0.4297 || label_Wqq: drop=0.3744, acc=0.7578 || label_Tbqq: drop=0.3626, acc=0.8867 || label_Hcc: drop=0.3560, acc=0.4492 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch48:64 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0215`, patch_acc `0.7359`, delta_logit `0.4032`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_H4q

**Composite lens:** `Patch lens: zero EdgeConv L1 ch48:64 | Weight lens: source/input blocks -> output ch48:64 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Tbqq, label_Hgg, label_H4q`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 48:64 carries 0.3774 of module weight energy. || WL2 input/source projection: Input slice 48:64 carries 0.3609 of module weight energy. || WL3 output pseudo-head projection: Output group 48:64 carries 0.3523 of module weight energy. || WL2 input/source projection: Input slice 48:64 carries 0.3507 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_H4q | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbqq: drop=0.9448, acc=0.8828 || label_Hgg: drop=0.5995, acc=0.6016 || label_H4q: drop=0.5841, acc=0.8047 || label_Hcc: drop=0.5099, acc=0.5078 || label_Hqql: drop=0.4488, acc=0.9453 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch64:80 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0195`, patch_acc `0.7379`, delta_logit `0.1514`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hcc

**Composite lens:** `Patch lens: zero EdgeConv L1 ch64:80 | Weight lens: source/input blocks -> output ch64:80 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_H4q, label_Hgg, label_Hcc`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 64:80 carries 0.3885 of module weight energy. || WL3 output pseudo-head projection: Output group 64:80 carries 0.3771 of module weight energy. || WL2 input/source projection: Input slice 64:80 carries 0.3738 of module weight energy. || WL3 output pseudo-head projection: Output group 64:80 carries 0.3643 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hcc | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_H4q: drop=0.9435, acc=0.6523 || label_Hgg: drop=0.5232, acc=0.7031 || label_Hcc: drop=0.4102, acc=0.5898 || label_Tbqq: drop=0.3964, acc=0.9219 || label_QCD: drop=-0.3856, acc=0.6680 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch32:64 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0160`, patch_acc `0.7414`, delta_logit `0.1883`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_Tbl, label_Hcc, label_H4q

**Composite lens:** `Patch lens: zero EdgeConv L2 ch32:64 | Weight lens: source/input blocks -> output ch32:64 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_Tbl, label_Hcc, label_H4q`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 32:64 carries 0.3899 of module weight energy. || WL2 input/source projection: Input slice 32:64 carries 0.3774 of module weight energy. || WL3 output pseudo-head projection: Output group 32:64 carries 0.3654 of module weight energy. || WL3 output pseudo-head projection: Output group 32:64 carries 0.3635 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_H4q | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbl: drop=1.0875, acc=0.9570 || label_Hcc: drop=0.5021, acc=0.3008 || label_H4q: drop=0.2375, acc=0.7227 || label_Hbb: drop=-0.0904, acc=0.6523 || label_Hqql: drop=0.0697, acc=0.9648 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch64:96 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0156`, patch_acc `0.7418`, delta_logit `1.5940`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_QCD, label_Hbb, label_Hcc

**Composite lens:** `Patch lens: zero EdgeConv L2 ch64:96 | Weight lens: source/input blocks -> output ch64:96 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_QCD, label_Hbb, label_Hcc`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 64:96 carries 0.3719 of module weight energy. || WL3 output pseudo-head projection: Output group 64:96 carries 0.3622 of module weight energy. || WL2 input/source projection: Input slice 64:96 carries 0.3532 of module weight energy. || WL3 output pseudo-head projection: Output group 64:96 carries 0.3485 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_QCD, label_Hbb, label_Hcc | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_QCD: drop=2.9694, acc=0.6523 || label_Hbb: drop=2.0622, acc=0.6445 || label_Hcc: drop=2.0188, acc=0.5703 || label_Zqq: drop=1.5663, acc=0.4922 || label_Tbl: drop=1.5453, acc=0.9727 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L1_ch80:96 — middle learned-neighborhood / route-composition head

**Effect:** acc_drop `0.0156`, patch_acc `0.7418`, delta_logit `0.3713`.

**Current best question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Tbl, label_Hqql, label_H4q

**Composite lens:** `Patch lens: zero EdgeConv L1 ch80:96 | Weight lens: source/input blocks -> output ch80:96 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Tbl, label_Hqql, label_H4q`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 80:96 carries 0.4088 of module weight energy. || WL2 input/source projection: Input slice 80:96 carries 0.3599 of module weight energy. || WL3 output pseudo-head projection: Output group 80:96 carries 0.3543 of module weight energy. || WL3 output pseudo-head projection: Output group 80:96 carries 0.3507 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_H4q | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbl: drop=2.4967, acc=0.8750 || label_Hqql: drop=2.1697, acc=0.9258 || label_H4q: drop=-0.2636, acc=0.8633 || label_QCD: drop=-0.2316, acc=0.6719 || label_Hbb: drop=-0.2046, acc=0.5625 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch128:160 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0121`, patch_acc `0.7453`, delta_logit `0.7800`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Tbqq

**Composite lens:** `Patch lens: zero EdgeConv L2 ch128:160 | Weight lens: source/input blocks -> output ch128:160 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_Hqql, label_Tbl, label_Tbqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 128:160 carries 0.3887 of module weight energy. || WL2 input/source projection: Input slice 128:160 carries 0.3615 of module weight energy. || WL2 input/source projection: Input slice 128:160 carries 0.3601 of module weight energy. || WL2 input/source projection: Input slice 128:160 carries 0.3575 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Tbqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hqql: drop=2.2104, acc=0.9414 || label_Tbl: drop=2.1597, acc=0.9531 || label_Tbqq: drop=0.8848, acc=0.8516 || label_Hbb: drop=0.5976, acc=0.5898 || label_Hcc: drop=0.5470, acc=0.5039 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch192:224 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0086`, patch_acc `0.7488`, delta_logit `0.3158`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_Tbqq, label_Wqq, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L2 ch192:224 | Weight lens: source/input blocks -> output ch192:224 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_Tbqq, label_Wqq, label_Zqq`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 192:224 carries 0.3753 of module weight energy. || WL2 input/source projection: Input slice 192:224 carries 0.3697 of module weight energy. || WL3 output pseudo-head projection: Output group 192:224 carries 0.3612 of module weight energy. || WL3 output pseudo-head projection: Output group 192:224 carries 0.3600 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Tbqq, label_Wqq, label_Zqq | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Tbqq: drop=1.0973, acc=0.8398 || label_Wqq: drop=0.9475, acc=0.6484 || label_Zqq: drop=0.4254, acc=0.6367 || label_Hqql: drop=0.2216, acc=0.9453 || label_QCD: drop=0.2163, acc=0.7422 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch160:192 — late aggregation / class-evidence head

**Effect:** acc_drop `0.0066`, patch_acc `0.7508`, delta_logit `0.4214`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Hcc

**Composite lens:** `Patch lens: zero EdgeConv L2 ch160:192 | Weight lens: source/input blocks -> output ch160:192 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_Hqql, label_Tbl, label_Hcc`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL3 output pseudo-head projection: Output group 160:192 carries 0.3712 of module weight energy. || WL2 input/source projection: Input slice 160:192 carries 0.3581 of module weight energy. || WL3 output pseudo-head projection: Output group 160:192 carries 0.3564 of module weight energy. || WL2 input/source projection: Input slice 160:192 carries 0.3518 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Hcc | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_Hqql: drop=0.7531, acc=0.9492 || label_Tbl: drop=0.7166, acc=0.9453 || label_Hcc: drop=0.6458, acc=0.5547 || label_Tbqq: drop=0.6165, acc=0.8398 || label_Hgg: drop=0.5743, acc=0.6992 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## L2_ch96:128 — late aggregation / class-evidence head

**Effect:** acc_drop `-0.0012`, patch_acc `0.7586`, delta_logit `0.1720`.

**Current best question:** Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier?

**Semantic hint:** kinematic/energy, class-specific: label_QCD, label_H4q, label_Hgg

**Composite lens:** `Patch lens: zero EdgeConv L2 ch96:128 | Weight lens: source/input blocks -> output ch96:128 | Class direction lens: this pseudo-head -> classifier class/contrast direction | Class lens: strongest affected classes = label_QCD, label_H4q, label_Hgg`

| qid | status | priority | question | current answer | what to compute next |
| --- | --- | --- | --- | --- | --- |
| CORE_CURRENT_QUESTION | ANSWERED_PARTIAL | P0 | What is the current best natural-language question this pseudo-head appears to ask? | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | Refine the label with activation clustering and more specific projection lenses. |
| WEIGHT_SOURCE_TO_HEAD | ANSWERED_PARTIAL | P0 | Which weight/source blocks feed this pseudo-head output group? | WL2 input/source projection: Input slice 96:128 carries 0.3573 of module weight energy. || WL3 output pseudo-head projection: Output group 96:128 carries 0.3570 of module weight energy. || WL3 output pseudo-head projection: Output group 96:128 carries 0.3564 of module weight energy. || WL2 input/source projection: Input slice 96:128 carries 0.3495 of module weight energy. | Map strongest source blocks to activation clusters and physical/route evidence. |
| PHYSICAL_FEATURE_TO_HEAD | ANSWERED_PARTIAL | P0 | Does this head read physical feature evidence such as kinematics, PID/charge, or geometry? | kinematic/energy, class-specific: label_QCD, label_H4q, label_Hgg | Use feature-channel patch/noise/permutation controls and check per-class effects. |
| ROUTE_WIDTH_TO_HEAD | TODO_P0 | P0 | Does this head encode compact-vs-wide learned particle-neighbor routing? | Not computed yet for this specific head. | Patch compact/wide route groups and measure this head activation/logit drop. |
| LEADING_PARTICLE_TO_HEAD | TODO_P0 | P0 | Does this head depend on leading top-pT/top-energy particles? | Not computed yet for this specific head. | Run top-k particle sweep and measure head activation/logit effect for k=1,2,4,8,16. |
| HEAD_TO_CLASS_EFFECT | ANSWERED_PARTIAL | P0 | Which classes lose logit/accuracy when this head is patched? | label_QCD: drop=0.3546, acc=0.6992 || label_H4q: drop=0.3103, acc=0.7695 || label_Hgg: drop=0.2312, acc=0.7266 || label_Hcc: drop=0.2186, acc=0.6602 || label_Wqq: drop=0.1978, acc=0.7695 | Make per-class and per-example signed logit attribution for this head. |
| HEAD_TO_CLASS_CONTRAST | TODO_P0 | P0 | Which class contrast direction does this head support, e.g. Wqq-vs-Zqq, Tbqq-vs-Tbl, Hbb-vs-Hcc? | Not computed yet for this specific head. | Project head activations into classifier contrast directions and patch the head. |
| ACTIVATION_CLUSTER_HEAD | TODO_P0 | P0 | Is this equal channel-slice actually a learned activation cluster, or should it be split/merged? | Not computed yet for this specific head. | Cluster EdgeConv activations by covariance/class response; patch learned clusters. |
| RANDOM_CHANNEL_CONTROL | TODO_P0 | P0 | Is this head stronger than random channel groups of the same size? | Not computed yet for this specific head. | Patch random channel groups with same size and compare effect distribution. |
| WEIGHT_PATCH_CONSISTENCY | TODO_P1 | P1 | Do weight-projection questions agree with causal patch evidence for this head? | Not computed yet for this specific head. | Compare projection score, activation strength, patch effect, and class drops for the same head. |
| HELDOUT_STABILITY | TODO_P1 | P1 | Does this head ask the same question on more files / heldout samples? | Not computed yet for this specific head. | Run the same head map on more ROOT files and compare effect sizes/ranks. |
| ERROR_ROUTE_HEAD | TODO_P2 | P2 | When the model is wrong, does this head answer like the predicted class instead of the true class? | Not computed yet for this specific head. | Build true->pred error atlas and compare head activation/question answers on errors. |
| KNN_NEIGHBOR_TO_HEAD | TODO_P1 | P1 | Which KNN neighbor patterns feed this head: compact core, wide-angle, high-pT neighbors, or random neighbors? | Not computed yet for this specific head. | Measure head activation under compact/wide/top-pT/random neighbor route interventions. |
| MULTI_HEAD_COMBINATION | TODO_P1 | P1 | Does this head work together with another head to answer a larger composite question? | Not computed yet for this specific head. | Patch head pairs/groups and compare to additive single-head effects. |

## Files

- CSV: `reports/latest/tables/full_head_question_catalog.csv`
- JSON: `manifests/latest/full_head_question_catalog.json`
