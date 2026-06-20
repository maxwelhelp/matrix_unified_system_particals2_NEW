import importlib.util
import os
from pathlib import Path

import torch
from weaver.utils.logger import _logger

_impl_path = Path(__file__).with_name("ParticleTransformer_legacy.py")
_spec = importlib.util.spec_from_file_location("_part_legacy_impl", _impl_path)
_impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_impl)
ParticleTransformer = _impl.ParticleTransformer

LABELS = ['label_QCD','label_Hbb','label_Hcc','label_Hgg','label_H4q','label_Hqql','label_Zqq','label_Wqq','label_Tbqq','label_Tbl']
HQQL = LABELS.index('label_Hqql')
TBL = LABELS.index('label_Tbl')


class ParticleTransformerPairAdapter(torch.nn.Module):
    """Same parameter names as legacy wrapper, but remaps pair logits.

    Existing Hqql/Tbl interpretation tools are hardcoded to read logits at
    label_Hqql and label_Tbl. For all-class atlas we can reuse those tools by
    projecting arbitrary source/target logits into those two slots:

      output[:, label_Hqql] = raw[:, PART_PAIR_SRC_LABEL]
      output[:, label_Tbl]  = raw[:, PART_PAIR_TGT_LABEL]

    State dict names remain `mod.*`, so the official checkpoint still loads
    strictly into this wrapper.
    """
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.mod = ParticleTransformer(**kwargs)
        self.src_label = os.environ.get('PART_PAIR_SRC_LABEL', 'label_Hqql')
        self.tgt_label = os.environ.get('PART_PAIR_TGT_LABEL', 'label_Tbl')
        if self.src_label not in LABELS or self.tgt_label not in LABELS:
            raise RuntimeError(f'bad PART_PAIR labels: {self.src_label}, {self.tgt_label}')
        self.src_idx = LABELS.index(self.src_label)
        self.tgt_idx = LABELS.index(self.tgt_label)

    @torch.jit.ignore
    def no_weight_decay(self):
        return {"mod.cls_token"}

    def forward(self, points, features, lorentz_vectors, mask):
        raw = self.mod(features, v=lorentz_vectors, mask=mask)
        out = raw.clone()
        out[:, HQQL] = raw[:, self.src_idx]
        out[:, TBL] = raw[:, self.tgt_idx]
        return out


def get_model(data_config, **kwargs):
    cfg = dict(
        input_dim=len(data_config.input_dicts["pf_features"]),
        num_classes=len(data_config.label_value),
        pair_input_dim=4,
        use_pre_activation_pair=False,
        embed_dims=[128, 512, 128],
        pair_embed_dims=[64, 64, 64],
        num_heads=8,
        num_layers=8,
        num_cls_layers=2,
        block_params=None,
        cls_block_params={"dropout": 0, "attn_dropout": 0, "activation_dropout": 0},
        fc_params=[],
        activation="gelu",
        trim=True,
        for_inference=False,
    )
    cfg.update(**kwargs)
    _logger.info("Legacy pair-adapter config: %s" % str(cfg))
    model = ParticleTransformerPairAdapter(**cfg)
    model_info = {
        "input_names": list(data_config.input_names),
        "input_shapes": {k: ((1,) + s[1:]) for k, s in data_config.input_shapes.items()},
        "output_names": ["softmax"],
        "dynamic_axes": {
            **{k: {0: "N", 2: "n_" + k.split("_")[0]} for k, s in data_config.input_shapes.items()},
            **{"softmax": {0: "N"}},
        },
    }
    return model, model_info


def get_loss(data_config, **kwargs):
    return torch.nn.CrossEntropyLoss()
