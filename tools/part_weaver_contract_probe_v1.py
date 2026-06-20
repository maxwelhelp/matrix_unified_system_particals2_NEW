#!/usr/bin/env python3
import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("NUMBA_DISABLE_CACHE", "1")

import numba
import numpy as np
import torch
import awkward as ak
import uproot

_numba_njit = numba.njit


def _njit_no_cache(*args, **kwargs):
    kwargs.pop("cache", None)
    return _numba_njit(*args, **kwargs)


numba.njit = _njit_no_cache

from weaver.utils.data.config import DataConfig


LABEL_GROUPS = [
    ("HToBB", "HToBB_*.root"),
    ("HToCC", "HToCC_*.root"),
    ("HToGG", "HToGG_*.root"),
    ("HToWW2Q1L", "HToWW2Q1L_*.root"),
    ("HToWW4Q", "HToWW4Q_*.root"),
    ("TTBar", "TTBar_[0-9]*.root"),
    ("TTBarLep", "TTBarLep_*.root"),
    ("WToQQ", "WToQQ_*.root"),
    ("ZToQQ", "ZToQQ_*.root"),
    ("ZJetsToNuNu", "ZJetsToNuNu_*.root"),
]


def import_module(path):
    spec = importlib.util.spec_from_file_location("_part_network", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def first_file(split_dir, pattern):
    hits = sorted(Path(split_dir).glob(pattern))
    if not hits:
        raise FileNotFoundError(f"no files matching {pattern} in {split_dir}")
    return str(hits[0])


def tensor_stats(x):
    arr = x.detach().cpu().float()
    return {
        "shape": list(arr.shape),
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def pad_1d(values, length, mode, pad_value=0):
    values = np.asarray(values, dtype=np.float32)
    if len(values) >= length:
        return values[:length]
    if mode == "wrap" and len(values) > 0:
        reps = int(np.ceil(length / len(values)))
        return np.tile(values, reps)[:length].astype(np.float32)
    out = np.full(length, pad_value, dtype=np.float32)
    out[: len(values)] = values
    return out


def delta_phi(a, b):
    return (a - b + np.pi) % (2 * np.pi) - np.pi


def read_direct_batch(filepath, data_config, batch_size):
    raw_branches = {
        "part_px",
        "part_py",
        "part_pz",
        "part_energy",
        "part_deta",
        "part_dphi",
        "part_d0val",
        "part_d0err",
        "part_dzval",
        "part_dzerr",
        "part_charge",
        "part_isChargedHadron",
        "part_isNeutralHadron",
        "part_isPhoton",
        "part_isElectron",
        "part_isMuon",
        "jet_pt",
        "jet_eta",
        "jet_phi",
        "jet_energy",
        "jet_nparticles",
        "jet_sdmass",
        "jet_tau1",
        "jet_tau2",
        "jet_tau3",
        "jet_tau4",
        *data_config.label_value,
    }
    with uproot.open(filepath) as root_file:
        tree_name = next(k for k, v in root_file.items() if getattr(v, "classname", "") == "TTree")
        table = root_file[tree_name].arrays(sorted(raw_branches), entry_start=0, entry_stop=batch_size)

    n = len(table["jet_pt"])
    particle_vars = {}
    particle_vars["part_px"] = table["part_px"]
    particle_vars["part_py"] = table["part_py"]
    particle_vars["part_pz"] = table["part_pz"]
    particle_vars["part_energy"] = table["part_energy"]
    particle_vars["part_deta"] = table["part_deta"]
    particle_vars["part_dphi"] = table["part_dphi"]
    particle_vars["part_d0val"] = table["part_d0val"]
    particle_vars["part_d0err"] = table["part_d0err"]
    particle_vars["part_dzval"] = table["part_dzval"]
    particle_vars["part_dzerr"] = table["part_dzerr"]
    particle_vars["part_charge"] = table["part_charge"]
    particle_vars["part_isChargedHadron"] = table["part_isChargedHadron"]
    particle_vars["part_isNeutralHadron"] = table["part_isNeutralHadron"]
    particle_vars["part_isPhoton"] = table["part_isPhoton"]
    particle_vars["part_isElectron"] = table["part_isElectron"]
    particle_vars["part_isMuon"] = table["part_isMuon"]

    # Jagged particle arrays: compute pt per event, not as one rectangular numpy array.
    px_list = ak.to_list(table["part_px"])
    py_list = ak.to_list(table["part_py"])
    part_pt = [
        np.hypot(np.asarray(px, dtype=np.float32), np.asarray(py, dtype=np.float32))
        for px, py in zip(px_list, py_list)
    ]
    particle_vars["part_pt"] = ak.Array(part_pt)
    particle_vars["part_pt_log"] = ak.Array([np.log(np.asarray(x, dtype=np.float32)) for x in part_pt])
    particle_vars["part_e_log"] = ak.Array([np.log(np.asarray(x, dtype=np.float32)) for x in ak.to_list(table["part_energy"])])
    particle_vars["part_logptrel"] = ak.Array(
        [np.log(np.asarray(part_pt[i], dtype=np.float32) / float(table["jet_pt"][i])) for i in range(n)]
    )
    particle_vars["part_logerel"] = ak.Array(
        [
            np.log(np.asarray(table["part_energy"][i], dtype=np.float32) / float(table["jet_energy"][i]))
            for i in range(n)
        ]
    )
    particle_vars["part_deltaR"] = ak.Array(
        [
            np.hypot(np.asarray(table["part_deta"][i], dtype=np.float32), np.asarray(table["part_dphi"][i], dtype=np.float32))
            for i in range(n)
        ]
    )
    particle_vars["part_d0"] = ak.Array([np.tanh(np.asarray(x, dtype=np.float32)) for x in ak.to_list(table["part_d0val"])])
    particle_vars["part_dz"] = ak.Array([np.tanh(np.asarray(x, dtype=np.float32)) for x in ak.to_list(table["part_dzval"])])
    particle_vars["part_mask"] = ak.Array([np.ones(len(x), dtype=np.float32) for x in ak.to_list(table["part_energy"])])

    X = {}
    for input_name, var_names in data_config.input_dicts.items():
        rows = []
        for i in range(n):
            channels = []
            for var_name in var_names:
                params = data_config.preprocess_params[var_name]
                values = np.asarray(particle_vars[var_name][i], dtype=np.float32)
                if params["center"] is not None:
                    values = np.clip((values - params["center"]) * params["scale"], params["min"], params["max"])
                channels.append(
                    pad_1d(
                        values,
                        params["length"],
                        params["pad_mode"],
                        params.get("pad_value", 0),
                    )
                )
            rows.append(np.stack(channels, axis=0))
        X[input_name] = torch.tensor(np.stack(rows, axis=0), dtype=torch.float32)

    label_matrix = np.stack([np.asarray(table[name], dtype=np.int64) for name in data_config.label_value], axis=1)
    labels = torch.tensor(label_matrix.argmax(axis=1), dtype=torch.long)
    Z = {
        k: torch.tensor(np.asarray(table[k]), dtype=torch.float32)
        for k in data_config.observer_names
        if k in table.fields
    }
    return X, labels, Z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part-repo", default="external/particle_transformer")
    ap.add_argument("--mode", default="full", choices=["kin", "kinpid", "full"])
    ap.add_argument("--checkpoint", default=None)
    ap.add_argument("--network-config", default=None)
    ap.add_argument("--split-dir", default=os.path.expanduser("~/Рабочий стол/JetClassOfficial/val_5M"))
    ap.add_argument("--class-name", default="HToBB")
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--load-fraction", type=float, default=0.001)
    ap.add_argument("--skip-batch", action="store_true", help="Only check model/checkpoint contract with dummy inputs.")
    ap.add_argument("--out-json", default="manifests/latest/part_weaver_contract_probe_v1.json")
    args = ap.parse_args()

    part_repo = Path(args.part_repo)
    data_config_path = part_repo / "data" / "JetClass" / f"JetClass_{args.mode}.yaml"
    network_path = Path(args.network_config or part_repo / "networks" / "example_ParticleTransformer_legacy.py")
    checkpoint = Path(args.checkpoint or part_repo / "models" / f"ParT_{args.mode}.pt")

    print("probe: loading data config", file=sys.stderr, flush=True)
    data_config = DataConfig.load(str(data_config_path), load_observers=False, load_reweight_info=False)
    print("probe: importing network", file=sys.stderr, flush=True)
    network = import_module(str(network_path))
    print("probe: building models", file=sys.stderr, flush=True)
    model_random, model_info = network.get_model(data_config)
    model_loaded, _ = network.get_model(data_config)

    print("probe: loading checkpoint strict", file=sys.stderr, flush=True)
    state = torch.load(checkpoint, map_location="cpu")
    load_result = model_loaded.load_state_dict(state, strict=True)
    model_random.eval()
    model_loaded.eval()

    param_count = sum(p.numel() for p in model_loaded.parameters())
    sd_items = list(state.items())

    base_out = {
        "mode": args.mode,
        "checkpoint": str(checkpoint),
        "data_config": str(data_config_path),
        "network": str(network_path),
        "weaver_input_names": list(data_config.input_names),
        "weaver_input_shapes": {k: list(v) for k, v in data_config.input_shapes.items()},
        "label_order": list(data_config.label_value),
        "model_info": model_info,
        "strict_load_missing": list(load_result.missing_keys),
        "strict_load_unexpected": list(load_result.unexpected_keys),
        "parameter_count": int(param_count),
        "state_keys_n": len(state),
        "state_first_shapes": [[k, list(v.shape)] for k, v in sd_items[:8]],
        "state_last_shapes": [[k, list(v.shape)] for k, v in sd_items[-8:]],
    }

    if args.skip_batch:
        length = data_config.input_shapes["pf_features"][2]
        x = torch.randn(1, len(data_config.input_dicts["pf_features"]), length)
        v = torch.randn(1, 4, length)
        v[:, 3, :] = v[:, :3, :].pow(2).sum(1).sqrt() + 0.1
        mask = torch.ones(1, 1, length)
        with torch.no_grad():
            logits_random = model_random(None, x, v, mask).float()
            logits_loaded = model_loaded(None, x, v, mask).float()
        out = {
            **base_out,
            "dummy_forward": True,
            "logit_delta_norm_loaded_minus_random": float(torch.linalg.vector_norm(logits_loaded - logits_random)),
            "logits_random": tensor_stats(logits_random),
            "logits_loaded": tensor_stats(logits_loaded),
            "loaded_argmax": int(logits_loaded.argmax(dim=1)[0]),
        }
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out_json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    class_patterns = dict(LABEL_GROUPS)
    if args.class_name not in class_patterns:
        raise ValueError(f"unknown class {args.class_name}; expected one of {sorted(class_patterns)}")

    selected_file = first_file(args.split_dir, class_patterns[args.class_name])
    print(f"probe: selected file {selected_file}", file=sys.stderr, flush=True)
    print("probe: reading one direct batch", file=sys.stderr, flush=True)
    X, labels, Z = read_direct_batch(selected_file, data_config, args.batch_size)
    inputs = [X[k].float() for k in data_config.input_names]

    print("probe: running random forward", file=sys.stderr, flush=True)
    with torch.no_grad():
        logits_random = model_random(*inputs).float()
        print("probe: running loaded forward", file=sys.stderr, flush=True)
        logits_loaded = model_loaded(*inputs).float()
        probs_loaded = torch.softmax(logits_loaded, dim=1)

    pred = probs_loaded.argmax(dim=1)
    out = {
        **base_out,
        "selected_file": selected_file,
        "batch_labels": labels.tolist(),
        "batch_label_counts": {str(int(k)): int(v) for k, v in zip(*np.unique(labels.numpy(), return_counts=True))},
        "batch_pred_counts": {str(int(k)): int(v) for k, v in zip(*np.unique(pred.numpy(), return_counts=True))},
        "accuracy_on_batch": float((pred == labels).float().mean()),
        "logit_delta_norm_loaded_minus_random": float(torch.linalg.vector_norm(logits_loaded - logits_random)),
        "logits_random": tensor_stats(logits_random),
        "logits_loaded": tensor_stats(logits_loaded),
        "probs_loaded": tensor_stats(probs_loaded),
        "top_prob_mean": float(probs_loaded.max(dim=1).values.mean()),
        "inputs": {k: tensor_stats(X[k].float()) for k in data_config.input_names},
        "mask_real_particle_counts": X["pf_mask"].float().sum(dim=(1, 2)).tolist() if "pf_mask" in X else None,
        "observers": {k: tensor_stats(v.float()) for k, v in Z.items()},
    }

    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
