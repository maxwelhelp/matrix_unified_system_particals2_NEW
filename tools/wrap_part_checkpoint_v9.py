#!/usr/bin/env python3
import argparse
from pathlib import Path
import torch

def unwrap(o):
    if isinstance(o, dict):
        for k in ["state_dict", "model_state_dict", "model", "net", "module"]:
            if k in o and isinstance(o[k], dict):
                return o[k]
    return o

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    raw = torch.load(args.input, map_location="cpu")
    sd = unwrap(raw)

    if not isinstance(sd, dict):
        raise TypeError(f"Expected state_dict dict, got {type(sd)}")

    tensor_keys = [k for k, v in sd.items() if torch.is_tensor(v)]
    if not tensor_keys:
        raise RuntimeError("No tensor keys found in checkpoint")

    n_mod = sum(k.startswith("mod.") for k in tensor_keys)
    n_plain = len(tensor_keys) - n_mod

    wrapped = {}
    for k, v in sd.items():
        if not torch.is_tensor(v):
            wrapped[k] = v
            continue

        nk = k
        for pref in ["module.", "model.", "part."]:
            if nk.startswith(pref):
                nk = nk[len(pref):]

        if not nk.startswith("mod."):
            nk = "mod." + nk

        wrapped[nk] = v

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    torch.save(wrapped, out)

    print({
        "input": args.input,
        "output": str(out),
        "tensor_keys": len(tensor_keys),
        "already_mod_keys": n_mod,
        "plain_keys": n_plain,
        "saved": True,
        "first_keys": list(wrapped.keys())[:10],
    })

if __name__ == "__main__":
    main()
