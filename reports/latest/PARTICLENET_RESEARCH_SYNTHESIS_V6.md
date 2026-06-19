# ParticleNet Research Synthesis v6

This report consolidates v3/v4/v5 outputs into a research board. It does not run the model; it reads latest CSV/JSON outputs and turns them into prioritized hypotheses.

## Baseline / validity

```json
{
  "n": 2560,
  "acc": 0.7574219107627869,
  "pred_counts": [
    241,
    243,
    220,
    280,
    274,
    255,
    251,
    270,
    273,
    253
  ],
  "true_counts": [
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256,
    256
  ]
}
```

## Hypothesis board
| id | priority | status | score | title | core evidence | risk | next test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H2 | P0 | CAUSAL_PATCHED | 78 | EdgeConv pseudo-head specialization | Strong internal pseudo-head groups: L1:ch16:32, L2:ch224:256, L0:ch40:48, L1:ch112:128, L0:ch24:32. | Equal channel slicing may hide or split real functional groups. | Add activation-cluster pseudo-heads and random channel-group controls. |
| H4 | P0 | CAUSAL_PATCHED | 72 | Leading-particle core hypothesis | top_pt ablation acc=0.4488 vs random=0.7250; gap=0.2762. | top_pt and top_energy highly overlap; need top-k sweep. | Run k sweep k=1,2,4,8,16 and per-class particle ablation. |
| H1 | P0 | CAUSAL_PATCHED | 34 | EdgeConv learned-neighborhood separator | Best EdgeConv pseudo-head 1:ch16:32 drops acc 0.7574->0.4934; full EdgeConv layers also previously dropped accuracy near random. | Channel-head groups are fixed slices, not learned clusters yet. | Cluster EdgeConv activations and patch learned clusters; run heldout stability. |
| H5 | P1 | CAUSAL_PATCHED | 74 | Explicit feature-channel class codes | label_H4q->part_pt_log, label_Hbb->part_logerel, label_Hcc->part_logerel, label_Hgg->part_deta, label_Hqql->part_pt_log, label_QCD->part_deta, label_Tbl->part_deta, label_Tbqq->part_deltaR | Zeroing feature channels may be out-of-distribution. | Permutation/noise controls and class contrast reports. |
| H6 | P1 | OBSERVED | 66 | Known-observable alignment | Tbqq-vs-Tbl: route ΔR gap L1=0.0539, sdmass gap=54.6329, nparticles gap=22.1602. | May be explained by known mass/multiplicity only. | Residual analysis after controlling for sdmass/nparticles/tau variables. |
| H3 | P1 | OBSERVED | 63 | Wqq compact route vs Tbqq wide route | Mean neighbor ΔR gap Tbqq-Wqq ≈ 0.1242 across route layers. | Route stats are descriptive; may be explained by mass/multiplicity. | Causal route-group patch: compact vs wide edges; regress against jet mass and nparticles. |
| H7 | P2 | TODO | 35 | Error-route hypothesis | Not tested yet: wrong predictions may share route/feature pattern with predicted class. | Needs confusion-pair analysis. | Build error atlas true->pred pairs with route stats and signed competing logits. |
| H8 | P2 | PAUSED | 20 | Transformer attention route hypothesis | ParT attention cannot be claimed until ParT accuracy is fixed. | Current ParT checkpoint invocation is invalid for claims. | Find/train valid ParT checkpoint, then extract attention heads / pair bias. |

## P0 immediate tests
- **H2 EdgeConv pseudo-head specialization**: Add activation-cluster pseudo-heads and random channel-group controls.
- **H4 Leading-particle core hypothesis**: Run k sweep k=1,2,4,8,16 and per-class particle ablation.
- **H1 EdgeConv learned-neighborhood separator**: Cluster EdgeConv activations and patch learned clusters; run heldout stability.

## P1 research tests
- **H5 Explicit feature-channel class codes**: Permutation/noise controls and class contrast reports.
- **H6 Known-observable alignment**: Residual analysis after controlling for sdmass/nparticles/tau variables.
- **H3 Wqq compact route vs Tbqq wide route**: Causal route-group patch: compact vs wide edges; regress against jet mass and nparticles.

## P2 backlog
- **H7 Error-route hypothesis**: Build error atlas true->pred pairs with route stats and signed competing logits.
- **H8 Transformer attention route hypothesis**: Find/train valid ParT checkpoint, then extract attention heads / pair bias.

## Current strongest facts
- Strongest EdgeConv pseudo-head: L1 ch16:32 drops acc to 0.4934.
- Top-pT particle ablation acc=0.4488; random control acc=0.7250.

## Known weaknesses to fix
- Edge pseudo-heads are currently equal channel slices; replace with activation clusters.
- Route stats are descriptive; add route-group causal patch.
- Need heldout stability across more ROOT files.
- Need error atlas for wrong predictions and competing logits.
- ParT attention is paused until valid accuracy is recovered.

## Output files

- `reports/latest/tables/research_hypothesis_board.csv`
- `manifests/latest/particlenet_research_synthesis_v6_summary.json`
