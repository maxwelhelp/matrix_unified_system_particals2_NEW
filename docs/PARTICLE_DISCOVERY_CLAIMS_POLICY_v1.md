# Particle Discovery Claims Policy v1

This project should not claim that a neural network has proven new physics just because a patch changes logits.

Correct claim levels:

## Level 1 — Mechanistic observation

Example:

> In this trained ParticleNet, zeroing EdgeConv layer 1 drops balanced JetClass accuracy from ~0.76 to ~0.10.

This is allowed when baseline accuracy is valid and the patch is causal.

## Level 2 — Candidate hypothesis

Example:

> The model appears to separate several jet classes mainly through learned dynamic particle-neighbor message passing rather than only through final classifier weights.

This requires:

- valid baseline accuracy;
- causal patch effect;
- stable effect across samples;
- per-class table;
- control patch.

## Level 3 — Physics hypothesis

Example:

> The model may be using a latent particle-neighborhood signature related to jet substructure that is not captured by a single jet-level observable.

This requires:

- Level 2 evidence;
- KNN/Edge route statistics;
- particle-subset controls;
- comparison to known physical observables such as pt, mass, tau variables, particle multiplicity, core/wide-angle structure;
- validation on a heldout split.

## Level 4 — Discovery claim

Do not claim this yet.

A discovery-level claim needs external validation, domain expert review, heldout datasets, and comparison to known physics baselines.

## What we can sell or present now

We can present the system as:

> A causal model-inspection and hypothesis-generation tool for trained particle classifiers. It turns trained model behavior into candidate physical/mechanistic hypotheses, with patch controls and per-class evidence.

Not as:

> It discovers new particles automatically.

## Current validated direction

Validated model:

- ParticleNet_kinpid on balanced JetClass tiny subset.

Invalid/paused:

- ParT attention claims, because current ParT checkpoint invocation gives ~random accuracy.

## Next evidence needed

- Discovery Atlas v4 with KNN route probe.
- Heldout validation on more ROOT files.
- Known-observable comparison.
- Stable candidate hypotheses across sample size.
