import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

with open("final_dataset_tqs.json", encoding="utf-8") as f:
    data = json.load(f)

N = len(data)  # 51

# ── palette ────────────────────────────────────────────────────────────────
BLUE   = "#2E6FBF"
LBLUE  = "#6AAED6"
GRAY   = "#9ABDD4"
LGRAY  = "#C8DCE8"
RED    = "#C0392B"
LRED   = "#E07B73"

fig, axes = plt.subplots(2, 3, figsize=(10, 5.2))
fig.subplots_adjust(hspace=0.52, wspace=0.38)

# ── helper ─────────────────────────────────────────────────────────────────
def hbar(ax, labels, values, colors, title, xlabel=False):
    y = np.arange(len(labels))
    bars = ax.barh(y, values, color=colors, height=0.55, edgecolor="white", linewidth=0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=7.5)
    ax.set_xlim(0, max(values) * 1.28)
    ax.tick_params(axis="x", labelsize=7)
    ax.set_title(title, fontsize=9, fontweight="bold", pad=4)
    ax.spines[["top", "right"]].set_visible(False)
    for bar, val in zip(bars, values):
        pct = val / N * 100
        ax.text(bar.get_width() + max(values) * 0.03,
                bar.get_y() + bar.get_height() / 2,
                f"{val} ({pct:.0f}%)", va="center", fontsize=6.8)
    if xlabel:
        ax.set_xlabel("Suites", fontsize=7)

# ── 1. Coverage ─────────────────────────────────────────────────────────────
ax = axes[0, 0]
labels = ["100%", "50–74%"]
vals   = [50, 1]
colors = [BLUE, LRED]
hbar(ax, labels, vals, colors, "(A2, A3) Coverage")

# ── 2. Mutation Score ────────────────────────────────────────────────────────
ax = axes[0, 1]
labels = ["100%", "75–99%", "50–74%", "1–49%", "0%"]
vals   = [21, 23, 1, 1, 5]
colors = [BLUE, LBLUE, GRAY, LGRAY, LRED]
hbar(ax, labels, vals, colors, "Mutation Score")

# ── 3. TQS ──────────────────────────────────────────────────────────────────
ax = axes[0, 2]
labels = ["6,0+", "5,0–5,5", "3,5–4,5", "2,5–3,0", "1,0–2,0"]
vals   = [4, 25, 12, 5, 5]
colors = [BLUE, BLUE, LBLUE, GRAY, LRED]
hbar(ax, labels, vals, colors, "TQS")

# ── 4. Edge Cases ────────────────────────────────────────────────────────────
ax = axes[1, 0]
labels = ["Detected", "No detected"]
vals   = [41, 10]
colors = [BLUE, LRED]
hbar(ax, labels, vals, colors, "(A1) Edge Cases")

# ── 5. Test Smells ──────────────────────────────────────────────────────────
ax = axes[1, 1]
labels = ["None", "magic_number", "redund. assert.", "assert. roulette"]
vals   = [17, 25, 11, 11]
colors = [BLUE, LRED, LRED, LRED]
hbar(ax, labels, vals, colors, "(A6) Test Smells")

# ── 6. Assert Types ─────────────────────────────────────────────────────────
ax = axes[1, 2]
labels = ["assertEqual", "assertFalse", "assertTrue",
          "assertRaises", "assertIsNone", "assertLess", "None"]
vals   = [35, 7, 7, 3, 2, 1, 9]
colors = [BLUE, BLUE, BLUE, LBLUE, LBLUE, GRAY, LRED]
hbar(ax, labels, vals, colors, "(A4) Assert Types")

# ── footnote ────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "* Test Smells and Assert Types are not mutually exclusive; a suite may contain multiple values.",
         ha="center", fontsize=6.5, color="#555555", style="italic")

plt.savefig("fig_corpus_distribution.pdf", bbox_inches="tight", dpi=300)
plt.savefig("fig_corpus_distribution.png", bbox_inches="tight", dpi=200)
print("Salvo: fig_corpus_distribution.pdf / .png")
