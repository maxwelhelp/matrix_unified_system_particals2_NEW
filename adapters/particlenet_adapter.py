class ParticleNetAdapter:
    """Small helper around Weaver ParticleNet for patch/atlas experiments."""
    def __init__(self, model):
        self.model = model
    def describe(self):
        return {
            'has_edge_convs': hasattr(self.model, 'edge_convs'),
            'n_edge_convs': len(getattr(self.model, 'edge_convs', [])),
            'has_fc': hasattr(self.model, 'fc'),
            'n_fc': len(getattr(self.model, 'fc', [])) if hasattr(self.model, 'fc') else 0,
            'has_bn_fts': hasattr(self.model, 'bn_fts'),
            'use_counts': bool(getattr(self.model, 'use_counts', False)),
            'use_fusion': bool(getattr(self.model, 'use_fusion', False)),
        }
    def edge_convs(self):
        return list(getattr(self.model, 'edge_convs', []))
    def fc_layers(self):
        return list(getattr(self.model, 'fc', [])) if hasattr(self.model, 'fc') else []
