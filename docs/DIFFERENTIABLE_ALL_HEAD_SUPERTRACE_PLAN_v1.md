# Differentiable All-Head Supertrace Plan v1

This document records the idea:

> Instead of looking at one pseudo-head at a time, look at all heads simultaneously as one differentiable super-head.

## Analogy to text tokens

For text:

```text
all attention heads -> token importance / next-token logit
```

For ParticleNet:

```text
all EdgeConv pseudo-heads -> particle importance / class logit
```

The natural token analogue is:

```text
text token -> particle inside a jet
```

## What the all-head supertrace should answer

For one batch of jets:

1. Which pseudo-head groups support the predicted class logit?
2. Which particles are important when all heads are considered together?
3. Is the all-head answer mostly:
   - top-pT/core particles;
   - wide-angle/boundary particles;
   - charged/PID particles;
   - a mixture of boundary + core context?
4. Which classes use which head mixture?
5. Which individual head is important only alone, and which only works in combination?

## Differentiable gate method

Add one differentiable scalar gate per pseudo-head group:

```text
EdgeConv L0 group 0..7
EdgeConv L1 group 0..7
EdgeConv L2 group 0..7
```

During forward:

```text
output[:, group_channels, :] *= gate[layer, group]
```

Then compute objective:

```text
objective = mean(logit[predicted_class])
```

Backprop:

```text
d objective / d gate[layer, group]
```

Interpretation:

- positive gradient: increasing this head would support current prediction;
- negative gradient: this head may suppress or compete with current prediction;
- high absolute gradient: prediction is sensitive to this head.

## Super-head particle score

For each head group:

```text
head_particle_energy[event, particle] = ||head_output_channels||
```

Then combine all heads with gradient weights:

```text
super_particle_score = sum_heads relu(grad_head) * normalized_head_particle_energy
```

This produces a particle-level token trace for the whole network.

## What we expect to see

If the previous single-head result is real, then all-head supertrace may reveal:

```text
boundary/wide particles + core high-pT particles
```

instead of only top-pT particles.

If the model is mostly using a simple known shortcut, we expect:

```text
super_particle_score dominated by top-pT/top-energy particles
```

If the model uses richer particle interactions, we expect:

```text
some heads select wide/boundary fragments,
others select core/high-pT particles,
and the joint score combines both.
```

## Why this matters

One head can be misleading. A single pseudo-head may select boundary particles, but the model’s final decision may use it together with core heads.

The all-head supertrace asks:

```text
What does the whole head system look at when it answers?
```

This is closer to the real network computation.

## Next reports

`PARTICLENET_ALL_HEAD_SUPERTRACE_V1.md` should include:

- top differentiable head gates;
- class-wise head gate summaries;
- top events by super-head score;
- top particles by all-head score;
- comparison against single-head trace;
- next tests: route-neighbor trace and class-contrast supertrace.
