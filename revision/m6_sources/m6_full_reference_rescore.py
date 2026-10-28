"""
m6_full_reference_rescore.py  (revision, Action Tracker M6)

The scored reference is the text stored in data/full_ground_truth.csv. For 23
Fineract files of the first collection batch that text stops at 30,038 CSV
characters, and for 53 Sylius and Diaspora files of that batch the Feature
description lines are missing (revision/m6_sources/results/provenance_per_file.csv).
This sensitivity analysis rescores every C0 output against the full file
committed in data/raw/ instead, with to_skeleton() and the ONNX encoder of
revision/h2/h2_cosine_onnx.py, and repeats the RQ1 tests on the 258
non-exemplar files (exact sign test and Wilcoxon signed-rank test, one-sided,
reference point 0.85). It also parses both versions of every reference with the
behave parser.

Usage (from the repository root, after m6_provenance_check.py):
  python revision/m6_sources/m6_full_reference_rescore.py --onnx-dir <folder with model.onnx and tokenizer.json>
"""
import argparse
import os
import subprocess
import sys

import numpy as np
import pandas as pd
from behave.parser import parse_feature
from scipy.stats import binomtest, wilcoxon

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "h2"))
from h2_cosine_onnx import Encoder, to_skeleton  # noqa: E402

T = 0.85
C0_EXEMPLARS = [2, 102, 202]


def parses(text):
    try:
        parse_feature(text)
        return True
    except Exception:  # behave raises several parser error types
        return False


def rq1(x):
    above, below = int((x > T).sum()), int((x < T).sum())
    return {"N": len(x), "median": np.median(x), "above": above, "below": below,
            "sign_p_greater": binomtest(above, above + below, 0.5, alternative="greater").pvalue,
            "wilcoxon_p_greater": wilcoxon(x - T, alternative="greater").pvalue}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--onnx-dir", required=True)
    ap.add_argument("--outdir", default=os.path.join("revision", "m6_sources", "results"))
    a = ap.parse_args()
    prov = pd.read_csv(os.path.join(a.outdir, "provenance_per_file.csv"))
    cut = prov[prov.csv_field_chars == 30038].id.tolist()
    prov = prov[["id", "project", "raw_path", "stored_vs_raw"]]
    gt = pd.read_csv("data/full_ground_truth.csv")[["id", "gherkin_content"]]
    gen = pd.read_csv("results/full_gpt54mini_output.csv")[["id", "generated_gherkin"]]
    orig = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    df = prov.merge(gt, on="id", validate="one_to_one").merge(gen, on="id", validate="one_to_one").merge(
        orig, on="id", validate="one_to_one")

    enc = Encoder(a.onnx_dir)
    stored, full, p_stored, p_full = [], [], [], []
    for r in df.itertuples():
        raw = subprocess.run(["git", "show", f"2b09c3a:{r.raw_path}"], capture_output=True, check=True).stdout.decode("utf-8")
        g = enc.encode(to_skeleton(str(r.generated_gherkin)))
        stored.append(float(g @ enc.encode(to_skeleton(str(r.gherkin_content)))))
        full.append(float(g @ enc.encode(to_skeleton(raw.replace("\r\n", "\n")))))
        p_stored.append(parses(str(r.gherkin_content).replace("\\n", "\n")))
        p_full.append(parses(raw.replace("\r\n", "\n")))
    df["cos_stored_recomputed"] = stored
    df["cos_full_reference"] = full
    df["change"] = df.cos_full_reference - df.cos_stored_recomputed
    df["parses_stored"] = p_stored
    df["parses_full"] = p_full
    repro = (df.cos_stored_recomputed - df.skeleton_cosine).abs().max()
    df.drop(columns=["gherkin_content", "generated_gherkin"]).to_csv(
        os.path.join(a.outdir, "full_reference_rescore_per_file.csv"), index=False, lineterminator="\n")

    prim = df[~df.id.isin(C0_EXEMPLARS)]
    res = pd.DataFrame([dict(reference="stored (paper)", **rq1(prim.skeleton_cosine.to_numpy(float))),
                        dict(reference="full file in data/raw", **rq1(prim.cos_full_reference.to_numpy(float)))])
    changed = df[df.change.abs() > 1e-6][["id", "project", "stored_vs_raw", "cos_stored_recomputed", "cos_full_reference", "change"]]
    rep = [f"max |recomputed - results/full_per_row_metrics.csv| = {repro:.2e}", "",
           "files whose score changes:", changed.round(4).to_string(index=False), "",
           "RQ1 on the 258 non-exemplar files:", res.round(4).to_string(index=False), "",
           "references that fail to parse (all 261):",
           f"  stored text: {sorted(df[~df.parses_stored].id)}",
           f"  full file:   {sorted(df[~df.parses_full].id)}",
           f"  stored text cut at 30,038 CSV characters: {sorted(set(df[~df.parses_stored].id) & set(df[df.id.isin(cut)].id))}"]
    res.to_csv(os.path.join(a.outdir, "full_reference_rescore_rq1.csv"), index=False, lineterminator="\n")
    open(os.path.join(a.outdir, "full_reference_rescore_report.txt"), "w", encoding="utf-8", newline="\n").write("\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
