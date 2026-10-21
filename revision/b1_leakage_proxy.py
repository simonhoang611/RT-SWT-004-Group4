"""
b1_leakage_proxy.py  (revision, Action Tracker B1; post-hoc analysis)

The user stories were reverse-engineered from the expert .feature files, so the
model input may carry wording of the ground truth (GT). This script measures
that overlap on the existing data and checks whether it goes with the score.
It is a proxy only: it does not replace an external backlog subset.

The reference files are stored with each line break as the two characters
backslash and n; these are turned into real line breaks before tokenising, as in
scripts/compute_metrics.py (corrected on 19 Oct 2026; the first version skipped
this step and produced tokens such as "nfeature").

Per file, on lowercased word tokens ([a-z0-9]+) of the full texts:
  story_gt_overlap   share of distinct GT word trigrams that also occur in the story
  gen_story_overlap  share of distinct generated trigrams that also occur in the story
  gen_gt_overlap     share of distinct generated trigrams that also occur in the GT
  gen_gt_not_story   share of distinct generated trigrams that occur in the GT but not in the story
Then Spearman correlations of these with skeleton_cosine, overall and per
project (exemplars 2, 102, 202 excluded).

Usage (from the repository root):  python revision/b1_leakage_proxy.py
"""
import os
import re

import pandas as pd
from scipy.stats import spearmanr

EXEMPLAR_IDS = [2, 102, 202]
TOK = re.compile(r"[a-z0-9]+")


def tri(text):
    w = TOK.findall(str(text).lower())
    return {tuple(w[i:i + 3]) for i in range(len(w) - 2)}


def share(a, b):
    return len(a & b) / len(a) if a else float("nan")


def main(outdir="revision/results"):
    os.makedirs(outdir, exist_ok=True)
    us = pd.read_csv("data/full_user_stories.csv")[["id", "project_name", "user_story"]]
    gt = pd.read_csv("data/full_ground_truth.csv")[["id", "gherkin_content"]]
    gen = pd.read_csv("results/full_gpt54mini_output.csv")[["id", "generated_gherkin"]]
    met = pd.read_csv("results/full_per_row_metrics.csv")[["id", "skeleton_cosine"]]
    df = us.merge(gt, on="id", validate="one_to_one").merge(gen, on="id", validate="one_to_one").merge(met, on="id", validate="one_to_one")
    rows = []
    for r in df.itertuples():
        s, g, o = tri(r.user_story), tri(str(r.gherkin_content).replace("\\n", "\n")), tri(r.generated_gherkin)
        rows.append({"id": r.id, "project": r.project_name, "skeleton_cosine": r.skeleton_cosine,
                     "story_gt_overlap": share(g, s), "gen_story_overlap": share(o, s),
                     "gen_gt_overlap": share(o, g), "gen_gt_not_story": share(o, g - s)})
    per = pd.DataFrame(rows)
    per.to_csv(os.path.join(outdir, "b1_overlap_per_file.csv"), index=False)
    d = per[~per.id.isin(EXEMPLAR_IDS)]
    cols = ["story_gt_overlap", "gen_story_overlap", "gen_gt_overlap", "gen_gt_not_story"]
    rep = ["Median overlap by project (exemplars excluded):",
           d.groupby("project")[cols].median().round(3).to_string(), "",
           "Spearman rho with skeleton_cosine (p):"]
    out = []
    for name, g in [("All", d)] + list(d.groupby("project")):
        for c in cols:
            rho, p = spearmanr(g[c], g.skeleton_cosine, nan_policy="omit")
            out.append({"group": name, "N": len(g), "measure": c, "rho": rho, "p": p})
    o = pd.DataFrame(out)
    o.to_csv(os.path.join(outdir, "b1_spearman.csv"), index=False)
    rep.append(o.round(4).to_string(index=False))
    open(os.path.join(outdir, "b1_report.txt"), "w", encoding="utf-8").write("\n".join(rep))
    print("\n".join(rep))


if __name__ == "__main__":
    main()
