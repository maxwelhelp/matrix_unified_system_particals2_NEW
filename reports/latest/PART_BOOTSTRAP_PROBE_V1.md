# PART_BOOTSTRAP_PROBE_V1

Bootstrap probe for Particle Transformer / ParT integration. This does not train or run inference yet.

- repo_dir: `external/particle_transformer`
- exists: **True**
- model files found: **2**
- config/json files found: **7**
- checkpoint files found: **6**

## Import checks
| module | ok | file/error |
| --- | --- | --- |
| weaver | True | /home/maxwelhelp/main/lib/python3.12/site-packages/weaver/__init__.py |
| weaver.nn | True | /home/maxwelhelp/main/lib/python3.12/site-packages/weaver/nn/__init__.py |
| weaver.nn.model | True | /home/maxwelhelp/main/lib/python3.12/site-packages/weaver/nn/model/__init__.py |
| weaver.nn.model.ParticleTransformer | True | /home/maxwelhelp/main/lib/python3.12/site-packages/weaver/nn/model/ParticleTransformer.py |
| weaver.nn.model.ParticleTransformer2023 | False | ModuleNotFoundError("No module named 'weaver.nn.model.ParticleTransformer2023'") |

## Candidate model files
| path |
| --- |
| networks/example_ParticleTransformer.py |
| networks/example_ParticleTransformer_finetune.py |

## Candidate config files
| path |
| --- |
| data/JetClass/JetClass_full.yaml |
| data/JetClass/JetClass_kin.yaml |
| data/JetClass/JetClass_kinpid.yaml |
| data/QuarkGluon/qg_kin.yaml |
| data/QuarkGluon/qg_kinpid.yaml |
| data/QuarkGluon/qg_kinpidplus.yaml |
| data/TopLandscape/top_kin.yaml |

## Candidate checkpoints inside repo
| path |
| --- |
| models/ParT_full.pt |
| models/ParT_kin.pt |
| models/ParT_kinpid.pt |
| models/ParticleNet_full.pt |
| models/ParticleNet_kin.pt |
| models/ParticleNet_kinpid.pt |

## Next

If the ParticleTransformer module imports, write `PART_INFERENCE_V1`. If import fails, install requirements and rerun this probe.
