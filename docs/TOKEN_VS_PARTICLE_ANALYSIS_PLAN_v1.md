# Token vs Particle Analysis Plan v1

This document fixes an important methodological point.

In the Qwen/text experiments, the natural unit was:

```text
token / word
```

So analysis could ask:

```text
For the word Python, JavaScript, etc., which head changed the logit and why?
```

For particle physics / jets, the analogous natural unit is:

```text
particle inside a jet
```

A jet is like a sentence, and particles are like tokens:

```text
text model:
    sentence -> tokens -> attention heads -> next-token logit

ParticleNet:
    jet -> particles -> KNN/EdgeConv pseudo-heads -> class logit
```

## What was missing

Previous reports mostly asked:

```text
Which pseudo-head is important globally?
What question might it ask?
```

But the text-style equivalent should also ask:

```text
For this concrete jet, which particles did this head focus on?
What particle features were high?
What class logit did this support?
Which neighbor/route pattern was used?
```

## Correct particle-level analysis

For a selected pseudo-head, for example:

```text
EdgeConv L1 ch16:32
```

we need:

1. capture head activation per particle;
2. rank particles by head energy;
3. show particle features:
   - pt / energy;
   - deta / dphi / deltaR;
   - charge/PID;
   - mask / real particle count;
4. compare to predicted/true class;
5. later add neighbor list / KNN route for top particles;
6. later project head activation into class-contrast directions.

## Why short tests were used before

Short runs were sanity checks:

- validate checkpoint loading;
- validate labels;
- validate ROOT preprocessing;
- validate direct loader vs official Weaver;
- avoid pushing huge logs.

That was correct for debugging, but not enough for discovery-level claims.

## What long tests should do

For discovery/hypothesis testing, use larger sweeps:

```text
SAMPLES_PER_FILE=256, 512, 1024
more ROOT files
heldout tar parts
separate reports per run
```

and compare stability of:

- head ranks;
- head questions;
- route width stats;
- top-particle ablation;
- class contrasts;
- feature-channel maps.

## Next required tools

1. `particlenet_single_head_particle_trace_v1.py`
   - token-style particle analysis for one head.

2. `particlenet_long_context_stability_v1.py`
   - run same dashboard on larger sample sizes / heldout files.

3. route-neighbor trace:
   - top particles -> their KNN neighbors -> head output.

4. head-to-class contrast:
   - selected head activation -> class contrast direction.

## Current interpretation rule

Do not say:

```text
This head discovered a new particle.
```

Say:

```text
This head currently appears to answer a particle-level question. We have a causal effect and need particle-level traces + heldout stability before a physics hypothesis.
```
