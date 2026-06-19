# ALL HEAD QUESTIONS AND ANALYSIS

This is the explicit file for all current ParticleNet pseudo-head questions and analysis. It is generated from `reports/latest/tables/head_projection_question_map.csv`.

## What this file contains

- every current EdgeConv pseudo-head group;
- its causal effect;
- the natural-language question it appears to ask;
- semantic hint from weight projections and class effects;
- composite projection lens to test next;
- next validation test.

## Strongest current head

**Head:** `L1_ch16:32`

**Effect:** accuracy `0.7574 -> 0.4934`, acc_drop `0.2641`, delta_logit `9.1146`.

**Role:** middle learned-neighborhood / route-composition head

**Question:** Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer?

**Semantic hint:** kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq

**Composite lens:** `Patch lens: zero EdgeConv L1 ch16:32 | Weight lens: source/input blocks -> output ch16:32 | Route lens: compact/wide KNN route stats -> this pseudo-head | Class lens: strongest affected classes = label_Hbb, label_Hcc, label_Zqq`

**Weight evidence:** WL3 output pseudo-head projection: Output group 16:32 carries 0.3578 of module weight energy. || WL2 input/source projection: Input slice 16:32 carries 0.3557 of module weight energy. || WL3 output pseudo-head projection: Output group 16:32 carries 0.3524 of module weight energy. || WL3 output pseudo-head projection: Output group 16:32 carries 0.3488 of module weight energy.

**Class effects:** label_Hbb: drop=14.3446, acc=0.2578 || label_Hcc: drop=12.5046, acc=0.1875 || label_Zqq: drop=11.1146, acc=0.0898 || label_Wqq: drop=10.5074, acc=0.0430 || label_H4q: drop=10.0451, acc=0.5273

**Next test:** Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch16:32 -> class contrast.

## L1 middle learned-neighborhood / route-composition heads

| head | acc_drop | role | question | semantic_hint | confidence | next_test |
| --- | --- | --- | --- | --- | --- | --- |
| L1_ch16:32 | 0.2641 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Zqq | HIGH causal, MEDIUM semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch16:32 -> class contrast. |
| L1_ch112:128 | 0.1156 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hbb, label_H4q, label_Hgg | MEDIUM causal, LOW/MEDIUM semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch112:128 -> class contrast. |
| L1_ch96:112 | 0.0734 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hqql | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch96:112 -> class contrast. |
| L1_ch32:48 | 0.0484 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_Tbqq | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch32:48 -> class contrast. |
| L1_ch0:16 | 0.0234 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch0:16 -> class contrast. |
| L1_ch48:64 | 0.0215 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_H4q | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch48:64 -> class contrast. |
| L1_ch64:80 | 0.0195 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Hcc | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch64:80 -> class contrast. |
| L1_ch80:96 | 0.0156 | middle learned-neighborhood / route-composition head | Does this pseudo-head combine previous learned features into a class-separating particle-neighborhood answer? | kinematic/energy, class-specific: label_Tbl, label_Hqql, label_H4q | LOW causal, exploratory semantic | Test route-width/leading-particle composite: compact/wide/top-pT routes -> L1 ch80:96 -> class contrast. |

## L0 early raw feature / geometry / PID readers

| head | acc_drop | role | question | semantic_hint | confidence | next_test |
| --- | --- | --- | --- | --- | --- | --- |
| L0_ch24:32 | 0.1996 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hbb, label_Hcc, label_Hgg | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch0:8 | 0.1602 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_Hbb | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch40:48 | 0.1371 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_Zqq, label_Wqq | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch48:56 | 0.1359 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_H4q, label_Hcc, label_Hbb | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch8:16 | 0.1348 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Hbb | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch16:24 | 0.1277 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Tbqq, label_Hgg, label_Zqq | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch56:64 | 0.0852 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Hqql, label_H4q, label_Hgg | MEDIUM causal, LOW/MEDIUM semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L0_ch32:40 | 0.0422 | early feature/geometry/PID reader | Does this pseudo-head convert raw particle features and local geometry into first-stage message evidence? | kinematic/energy, class-specific: label_Wqq, label_Hcc, label_Zqq | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |

## L2 late aggregation / class-evidence heads

| head | acc_drop | role | question | semantic_hint | confidence | next_test |
| --- | --- | --- | --- | --- | --- | --- |
| L2_ch0:32 | 0.0797 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_H4q, label_Hgg, label_Tbl | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch224:256 | 0.0629 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hbb, label_Wqq, label_Zqq | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch32:64 | 0.0160 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Tbl, label_Hcc, label_H4q | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch64:96 | 0.0156 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_QCD, label_Hbb, label_Hcc | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch128:160 | 0.0121 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Tbqq | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch192:224 | 0.0086 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Tbqq, label_Wqq, label_Zqq | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch160:192 | 0.0066 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_Hqql, label_Tbl, label_Hcc | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |
| L2_ch96:128 | -0.0012 | late aggregation / class-evidence head | Does this pseudo-head aggregate higher-level particle-neighborhood evidence before the classifier? | kinematic/energy, class-specific: label_QCD, label_H4q, label_Hgg | LOW causal, exploratory semantic | Activation-cluster this head and compare against random channel groups; then project its activation into class contrast directions. |

## Full JSON

Machine-readable full version: `manifests/latest/all_head_questions_and_analysis.json`.
