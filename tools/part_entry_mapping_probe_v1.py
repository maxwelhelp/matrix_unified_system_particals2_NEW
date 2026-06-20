#!/usr/bin/env python3
import sys, json, csv, gc
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np
import torch
import uproot

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import LABELS, load_groups, load_model, build_batch, wcsv, wjson

def pred_root_file_for_group(g):
    m = {
        "HToWW2Q1L": "reports/latest/part_weaver_predict_smoke_v3_HToWW2Q1L.root",
        "TTBarLep": "reports/latest/part_weaver_predict_smoke_v3_TTBarLep.root",
    }
    return m[g]

def tree(path):
    f = uproot.open(path)
    for k, v in f.items():
        if hasattr(v, "arrays"):
            return v
    raise RuntimeError("no tree " + str(path))

def score_branches(keys):
    out = []
    for lab in LABELS:
        for pref in ["score_", "scores_", "prob_", "output_"]:
            c = pref + lab
            if c in keys:
                out.append(c)
                break
        else:
            raise RuntimeError("missing score for " + lab)
    return out

def softmax_np(x):
    x = x - x.max(axis=1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=1, keepdims=True)

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    groups, _ = load_groups(
        "reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv",
        "reports/latest/part_weaver_predict_smoke_v3_*.root",
        "manifests/latest/part_weaver_predict_smoke_v3_args.txt",
        128,128,128,128,
    )

    # берем только Hqql/Tbl source groups
    chosen = [r for r in groups if r["analysis_group"] in ("A_Hqql_correct","B_Hqql_to_Tbl","C_Tbl_correct","D_Tbl_to_Hqql")]
    by_src = defaultdict(list)
    for r in chosen:
        by_src[(r["source_group"], r["source_root"])].append(r)

    model, dc = load_model(
        "external/particle_transformer/networks/example_ParticleTransformer_legacy.py",
        "external/particle_transformer/models/ParT_kinpid.pt",
        "external/particle_transformer/data/JetClass/JetClass_kinpid.yaml",
        device,
    )

    rows = []
    mb = 8
    for (sg, src), rs in by_src.items():
        pred_path = pred_root_file_for_group(sg)
        tr = tree(pred_path)
        keys = list(tr.keys())
        scores = score_branches(keys)

        # читаем score ROOT по тем entry_idx, которые выбраны группами
        idxs = [int(r["entry_idx"]) for r in rs]
        maxidx = max(idxs)
        arr = tr.arrays(scores, entry_start=0, entry_stop=maxidx+1, library="np")
        root_scores = np.stack([arr[s] for s in scores], axis=1)

        for s in range(0, len(rs), mb):
            sub = rs[s:s+mb]
            pts, fts, vec, msk, metas = build_batch(sub, device, dc)
            with torch.no_grad():
                logits = model(pts, fts, vec, msk).detach().cpu().numpy()
            probs = softmax_np(logits)
            for i, r in enumerate(sub):
                ei = int(r["entry_idx"])
                root_vec = root_scores[ei]
                root_pred = LABELS[int(root_vec.argmax())]
                direct_pred = LABELS[int(probs[i].argmax())]
                l2 = float(np.linalg.norm(root_vec - probs[i]))
                # local neighborhood: does direct current event match exact root vector badly?
                rows.append({
                    "analysis_group": r["analysis_group"],
                    "source_group": sg,
                    "entry_idx": ei,
                    "root_pred": root_pred,
                    "direct_pred": direct_pred,
                    "same_pred": int(root_pred == direct_pred),
                    "root_Hqql": float(root_vec[LABELS.index("label_Hqql")]),
                    "root_Tbl": float(root_vec[LABELS.index("label_Tbl")]),
                    "direct_Hqql": float(probs[i, LABELS.index("label_Hqql")]),
                    "direct_Tbl": float(probs[i, LABELS.index("label_Tbl")]),
                    "score_l2_root_vs_direct": l2,
                })
            del pts,fts,vec,msk,logits
            if device.type == "cuda":
                torch.cuda.empty_cache()
            gc.collect()

    summary = []
    for g in sorted(set(r["analysis_group"] for r in rows)):
        xs = [r for r in rows if r["analysis_group"] == g]
        summary.append({
            "group": g,
            "n": len(xs),
            "same_pred_rate": sum(r["same_pred"] for r in xs)/max(1,len(xs)),
            "mean_score_l2": sum(r["score_l2_root_vs_direct"] for r in xs)/max(1,len(xs)),
            "root_pred_counts": dict(Counter(r["root_pred"] for r in xs)),
            "direct_pred_counts": dict(Counter(r["direct_pred"] for r in xs)),
        })

    Path("reports/latest/tables").mkdir(parents=True, exist_ok=True)
    Path("manifests/latest").mkdir(parents=True, exist_ok=True)
    wcsv("reports/latest/tables/part_entry_mapping_probe_v1_rows.csv", rows)
    wcsv("reports/latest/tables/part_entry_mapping_probe_v1_summary.csv", summary)
    wjson("manifests/latest/part_entry_mapping_probe_v1.json", {"ok": True, "summary": summary})

    lines = ["# PART_ENTRY_MAPPING_PROBE_V1", "", "Compares prediction ROOT scores at the selected entry_idx with direct legacy-wrapper replay probabilities for the same source entry.", "", "| group | n | same pred rate | mean score L2 | root pred counts | direct pred counts |", "| --- | ---: | ---: | ---: | --- | --- |"]
    for s in summary:
        lines.append(f"| {s['group']} | {s['n']} | {s['same_pred_rate']:.4f} | {s['mean_score_l2']:.6f} | `{s['root_pred_counts']}` | `{s['direct_pred_counts']}` |")
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    worst = min(s["same_pred_rate"] for s in summary) if summary else 0
    l2max = max(s["mean_score_l2"] for s in summary) if summary else 999
    if worst < 0.80 or l2max > 0.15:
        lines.append("`ENTRY_MAPPING_OR_SCORE_PARITY_FAIL`: prediction ROOT selected rows are not reliably the same replayed source events/scores. Do not use error groups for causal claims yet.")
    else:
        lines.append("`ENTRY_MAPPING_OK`: prediction ROOT rows match direct replay scores well enough for causal route patch.")
    Path("reports/latest/PART_ENTRY_MAPPING_PROBE_V1.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
