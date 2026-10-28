"""Draw Fig. 2 and Fig. 3 of the paper (Appendix A) from the stored C0 results.

Run from the repository root:  python paper_revised/figures/make_figures.py

Both figures are drawn at their printed size (0.85 of the LNCS text width, 12.2 cm)
in Computer Modern at 9 pt, the font and size of the appendix tables and captions,
so that they are not scaled when included.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXEMPLARS = [2, 102, 202]  # prompt exemplars of C0, excluded from the primary analysis

WIDTH = 0.85 * 12.2 / 2.54  # inches
HEIGHT = WIDTH * 3.7 / 6.3

meta = pd.read_csv(ROOT / "data/full_user_stories.csv")[["id", "domain"]]
df = pd.read_csv(ROOT / "results/full_per_row_metrics.csv").merge(meta, on="id", validate="one_to_one")
df = df[~df.id.isin(EXEMPLARS)]
assert len(df) == 258

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["cmr10"],
    "mathtext.fontset": "cm",
    "axes.formatter.use_mathtext": True,
    "axes.unicode_minus": False,
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
})


def save(fig, name):
    fig.savefig(OUT / (name + ".png"), dpi=300, facecolor="white")
    plt.close(fig)


fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT), layout="constrained")
ax.hist(df.skeleton_cosine, bins=np.arange(.55, 1.025, .025), color="#286F8C", edgecolor="white", linewidth=0.5)
ax.axvline(.85, color="#B23B31", linestyle="--", linewidth=1.0, label="Reference point 0.85")
median = df.skeleton_cosine.median()
ax.axvline(median, color="#173A3D", linestyle=":", linewidth=1.1, label=f"Median {median:.4f}")
ax.set(xlabel="Skeleton cosine similarity", ylabel="Feature-file pairs",
       title="Distribution after excluding prompt exemplars (N=258)", xlim=(.55, 1.01))
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
save(fig, "fig1_skeleton_distribution_258")

fig, ax = plt.subplots(figsize=(WIDTH, HEIGHT), layout="constrained")
domains = ["E-commerce", "Finance/Banking", "Social Network"]
values = [df[df.domain == d].skeleton_cosine for d in domains]
bp = ax.boxplot(values, patch_artist=True, widths=.55,
                tick_labels=["E-commerce\nSylius (n=99)", "Finance/Banking\nFineract (n=99)",
                             "Social Network\nDiaspora (n=60)"],
                boxprops={"linewidth": 0.6}, whiskerprops={"linewidth": 0.6}, capprops={"linewidth": 0.6},
                medianprops={"color": "#162C31", "linewidth": 1.0},
                flierprops={"marker": "o", "markersize": 2, "markerfacecolor": "white",
                            "markeredgecolor": "#475963", "markeredgewidth": 0.5})
for patch, col in zip(bp["boxes"], ["#7DA9C8", "#74B69B", "#DCC069"]):
    patch.set_facecolor(col)
ax.axhline(.85, color="#B23B31", linestyle="--", linewidth=0.9, label="Reference point 0.85")
ax.set(ylabel="Skeleton cosine similarity",
       title="Domain distributions after exemplar exclusion (N=258)", ylim=(.55, 1.035))
for i, v in enumerate(values, 1):
    ax.text(i, 1.01, f"Median {v.median():.3f}", ha="center")
ax.legend(frameon=False, loc="lower right")
ax.spines[["top", "right"]].set_visible(False)
save(fig, "fig2_domain_distributions_258")
