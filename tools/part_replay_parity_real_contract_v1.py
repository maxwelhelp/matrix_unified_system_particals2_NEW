#!/usr/bin/env python3
import json, csv, sys, gc
from pathlib import Path
from collections import defaultdict, Counter
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.part_attention_supertrace_real_contract_v1 import (
    LABELS, load_groups, load_model, build_batch, wcsv, wjson
)

def select_events(rows, n=64):
    by = defaultdict(list)
    for r in rows:
        by[r["analysis_group"]].append(r)
    out = []
    for g in ["A_Hqql_correct", "B_Hqql_to_Tbl", "C_Tbl_correct", "D_Tbl_to_Hqql"]:
        out += by[g][:n]
    return out

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    groups, counts = load_groups(
        "reports/latest/tables/part_hqql_tbl_groups_real_contract_v1.csv",
        "reports/latest/part_weaver_predict_smoke_v3_*.root",
        "manifests/latest/part_weaver_predict_smoke_v3_args.txt",
        64, 64, 64, 64,
    )
    rows = select_events(groups, 64)

    model, dc = load_model(
        "external/particle_transformer/networks/example_ParticleTransformer.py",
        "external/particle_transformer/models/ParT_kinpid.pt",
        "external/particle_transformer/data/JetClass/JetClass_kinpid.yaml",
        device,
    )

    out = []
    mb = 8
    for s in range(0, len(rows), mb):
        sub = rows[s:s+mb]
        pts, fts, vec, msk, meta = build_batch(sub, device, dc)
        with torch.no_grad():
            logits = model(pts, fts, vec, msk).detach().cpu()
            probs = torch.softmax(logits.float(), dim=1)
        pred = logits.argmax(dim=1).tolist()
        for i, r in enumerate(sub):
            direct_pred = LABELS[pred[i]]
            root_pred = r.get("pred_label", "")
            true_label = r.get("true_label", "")
            out.append({
                "analysis_group": r["analysis_group"],
                "source_group": r["source_group"],
                "entry_idx": r["entry_idx"],
                "true_label_root": true_label,
                "pred_label_root": root_pred,
                "pred_label_direct": direct_pred,
                "match_root_pred": int(root_pred == direct_pred),
                "direct_score_Hqql": float(logits[i, LABELS.index("label_Hqql")]),
                "direct_score_Tbl": float(logits[i, LABELS.index("label_Tbl")]),
                "direct_tbl_minus_hqql": float(logits[i, LABELS.index("label_Tbl")] - logits[i, LABELS.index("label_Hqql")]),
                "root_score_Hqql": r.get("score_Hqql", ""),
                "root_score_Tbl": r.get("score_Tbl", ""),
            })
        del pts, fts, vec, msk, logits, probs
        if device.type == "cuda":
            torch.cuda.empty_cache()
        gc.collect()

    by = defaultdict(list)
    for r in out:
        by[r["analysis_group"]].append(r)

    summary = []
    for g, xs in by.items():
        n = len(xs)
        match = sum(x["match_root_pred"] for x in xs)
        root_pred_counts = Counter(x["pred_label_root"] for x in xs)
        direct_pred_counts = Counter(x["pred_label_direct"] for x in xs)
        summary.append({
            "group": g,
            "n": n,
            "root_direct_pred_match_rate": match / max(1, n),
            "root_pred_counts": dict(root_pred_counts),
            "direct_pred_counts": dict(direct_pred_counts),
            "mean_direct_tbl_minus_hqql": sum(x["direct_tbl_minus_hqql"] for x in xs) / max(1, n),
        })

    Path("reports/latest/tables").mkdir(parents=True, exist_ok=True)
    Path("manifests/latest").mkdir(parents=True, exist_ok=True)
    wcsv("reports/latest/tables/part_replay_parity_real_contract_v1_rows.csv", out)
    wcsv("reports/latest/tables/part_replay_parity_real_contract_v1_summary.csv", summary)
    wjson("manifests/latest/part_replay_parity_real_contract_v1.json", {"ok": True, "rows": len(out), "summary": summary})

    lines = []
    lines.append("# PART_REPLAY_PARITY_REAL_CONTRACT_V1\n")
    lines.append("Checks whether direct reconstructed ParT forward reproduces prediction ROOT labels for the same selected events.\n")
    lines.append("## Summary\n")
    lines.append("| group | n | root/direct pred match | root pred counts | direct pred counts | mean direct Tbl-Hqql |")
    lines.append("| --- | ---: | ---: | --- | --- | ---: |")
    for s in summary:
        lines.append(f"| {s['group']} | {s['n']} | {s['root_direct_pred_match_rate']:.4f} | `{s['root_pred_counts']}` | `{s['direct_pred_counts']}` | {s['mean_direct_tbl_minus_hqql']:.6f} |")
    lines.append("\n## Decision\n")
    worst = min(s["root_direct_pred_match_rate"] for s in summary) if summary else 0
    if worst < 0.90:
        lines.append("`REPLAY_PARITY_FAIL`: exact route patch is only a margin-sensitivity probe until reconstruction/prediction parity is fixed.\n")
    else:
        lines.append("`REPLAY_PARITY_OK`: exact route patch can be interpreted as causal evidence on the same prediction regime.\n")
    Path("reports/latest/PART_REPLAY_PARITY_REAL_CONTRACT_V1.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
