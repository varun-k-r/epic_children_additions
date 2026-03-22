"""
analyze.py — Summary statistics and plots for the epic_children dataset.

Usage:
    python analyze.py                        # reads epic_children.csv in current dir
    python analyze.py path/to/file.csv       # reads specified file

Produces:
    1. Sex ratio by tradition (table + plot)
    2. Sex ratio by historicity (table)
    3. Row type distribution
    4. Partner multiplicity (wives per husband, husbands per wife)
    5. Children-per-couple distribution
    6. Cross-tradition parallels
    7. The Vanishing Daughters (plot)
"""

import csv
import sys
import re
from collections import defaultdict, Counter
from pathlib import Path

# ── Load ──────────────────────────────────────────────────────────────────────

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("epic_children.csv")
if not path.exists():
    for alt in ["epic_children_v13.csv", "epic_children_v12.csv"]:
        if Path(alt).exists():
            path = Path(alt); break
with open(path) as f:
    rows = list(csv.DictReader(f))
print(f"Loaded {len(rows)} rows from {path}\n")

# ── Helpers ───────────────────────────────────────────────────────────────────

TRADITION = {
    'mahabharat': 'Hindu', 'ramayan': 'Hindu', 'bhagavata_purana': 'Hindu',
    'shiva_purana': 'Hindu', 'markandeya_purana': 'Hindu', 'panchatantra': 'Hindu',
    'silappadikaram': 'Hindu (Tamil)',
    'hebrew_bible': 'Jewish', 'christian_nt': 'Christian', 'arthurian': 'Arthurian',
    'quran': 'Islamic', 'islam': 'Islamic',
    'greek': 'Greco-Roman', 'roman': 'Greco-Roman', 'trojan_cycle': 'Greco-Roman',
    'norse': 'Norse', 'celtic': 'Celtic', 'shahnameh': 'Persian',
    'dede_korkut': 'Turkic', 'koroghlu': 'Turkic', 'manas': 'Turkic',
    'kojiki': 'Japanese', 'fengshen_yanyi': 'Chinese', 'kalevala': 'Finnish',
    'popol_vuh': 'Maya', 'sundiata': 'W. African', 'egyptian': 'Egyptian',
    'mesopotamian': 'Mesopotamian', 'king_gesar': 'Tibetan', 'sassoun': 'Armenian',
    'buddhist': 'Buddhist', 'jain': 'Jain',
}

CAP = 200

def sons(r):
    return float(r['n_sons']) if r['n_sons'].strip() else 0

def daughters(r):
    return float(r['n_daughters']) if r['n_daughters'].strip() else 0

def sons_adj(r):
    return min(sons(r), CAP)

def total(r):
    return sons(r) + daughters(r)

def pct_male(s, d):
    return 100 * s / (s + d) if (s + d) > 0 else float('nan')

def ratio_str(s, d):
    return f"{s/d:.1f}:1" if d > 0 else "∞"

def print_table(header, rows_data, col_widths=None):
    if col_widths is None:
        col_widths = [max(len(str(r[i])) for r in [header] + rows_data) + 2
                      for i in range(len(header))]
    hline = "  ".join(str(h).ljust(w) for h, w in zip(header, col_widths))
    print(hline)
    print("  ".join("─" * w for w in col_widths))
    for row in rows_data:
        print("  ".join(str(v).ljust(w) for v, w in zip(row, col_widths)))
    print()


# ── 1. Sex Ratio by Tradition ────────────────────────────────────────────────

print("=" * 70)
print("  1. SEX RATIO BY TRADITION (sons capped at 200/parent)")
print("=" * 70)

trad = defaultdict(lambda: {"s": 0, "d": 0, "n": 0})
for r in rows:
    g = TRADITION.get(r['epic'].strip(), r['epic'].strip())
    trad[g]["s"] += sons_adj(r)
    trad[g]["d"] += daughters(r)
    trad[g]["n"] += 1

table = []
gs = gd = 0
for g, s in sorted(trad.items(), key=lambda x: -(x[1]['s'] + x[1]['d'])):
    t = s['s'] + s['d']
    if t == 0:
        continue
    table.append([g, s['n'], f"{s['s']:.0f}", f"{s['d']:.0f}", f"{t:.0f}",
                  ratio_str(s['s'], s['d']), f"{pct_male(s['s'], s['d']):.0f}%"])
    gs += s['s']; gd += s['d']
table.append(["TOTAL", len(rows), f"{gs:.0f}", f"{gd:.0f}", f"{gs+gd:.0f}",
              ratio_str(gs, gd), f"{pct_male(gs, gd):.0f}%"])

print_table(
    ["Tradition", "N", "Sons", "Daughters", "Total", "M:F", "% Male"],
    table, [22, 5, 7, 10, 7, 8, 7]
)


# ── 2. Sex Ratio by Historicity ──────────────────────────────────────────────

print("=" * 70)
print("  2. SEX RATIO BY HISTORICITY")
print("=" * 70)

hist = defaultdict(lambda: {"s": 0, "d": 0, "n": 0})
for r in rows:
    h = r.get('historicity', 'legendary').strip()
    hist[h]["s"] += sons_adj(r)
    hist[h]["d"] += daughters(r)
    hist[h]["n"] += 1

table = []
for h in ['legendary', 'mythological', 'historical']:
    s = hist[h]
    t = s['s'] + s['d']
    if t == 0:
        continue
    table.append([h, s['n'], f"{s['s']:.0f}", f"{s['d']:.0f}", f"{t:.0f}",
                  ratio_str(s['s'], s['d']), f"{pct_male(s['s'], s['d']):.0f}%"])
table.append(["TOTAL", len(rows), f"{gs:.0f}", f"{gd:.0f}", f"{gs+gd:.0f}",
              ratio_str(gs, gd), f"{pct_male(gs, gd):.0f}%"])

print_table(
    ["Historicity", "N", "Sons", "Daughters", "Total", "M:F", "% Male"],
    table, [16, 5, 7, 10, 7, 8, 7]
)


# ── 3. Row Type Distribution ─────────────────────────────────────────────────

print("=" * 70)
print("  3. ROW TYPE DISTRIBUTION")
print("=" * 70)

type_counts = Counter(r['row_type'].strip() for r in rows)
table = [[t, c] for t, c in type_counts.most_common()]
print_table(["Row Type", "N"], table, [22, 5])


# ── 4. Partner Multiplicity ──────────────────────────────────────────────────

print("=" * 70)
print("  4. PARTNER MULTIPLICITY")
print("=" * 70)

# Use husband_id / wife_id if available, else parse parents
has_ids = 'husband_id' in rows[0]

if has_ids:
    h_counts = Counter(r['husband_id'] for r in rows if r.get('husband_id', '').strip())
    w_counts = Counter(r['wife_id'] for r in rows if r.get('wife_id', '').strip())

    print(f"\n  Unique husbands (with ID): {len(h_counts)}")
    print(f"  Unique wives (with ID):    {len(w_counts)}")
    print(f"  Husbands with 1 wife:  {sum(1 for v in h_counts.values() if v==1)} ({100*sum(1 for v in h_counts.values() if v==1)/len(h_counts):.0f}%)")
    print(f"  Wives with 1 husband:  {sum(1 for v in w_counts.values() if v==1)} ({100*sum(1 for v in w_counts.values() if v==1)/len(w_counts):.0f}%)")
    print()

    print("Most wives per husband:\n")
    table = []
    for hid, n in h_counts.most_common(12):
        name = next((r.get('husband', '') for r in rows if r.get('husband_id') == hid), hid)
        epic = hid.split('::')[0] if '::' in hid else ''
        table.append([name, epic, n])
    print_table(["Husband", "Epic", "Wives"], table, [28, 18, 6])

    print("Most husbands per wife:\n")
    table = []
    for wid, n in w_counts.most_common(10):
        name = next((r.get('wife', '') for r in rows if r.get('wife_id') == wid), wid)
        epic = wid.split('::')[0] if '::' in wid else ''
        table.append([name, epic, n])
    print_table(["Wife", "Epic", "Husbands"], table, [28, 18, 9])
else:
    print("  (husband_id/wife_id columns not found; skipping structured analysis)")
    print()


# ── 5. Children per Couple ───────────────────────────────────────────────────

print("=" * 70)
print("  5. CHILDREN PER COUPLE")
print("=" * 70)

totals = sorted(total(r) for r in rows if r['row_type'].strip() != 'mythical_count')

def percentile(data, p):
    k = (len(data) - 1) * p / 100
    f = int(k)
    c = min(f + 1, len(data) - 1)
    return data[f] + (k - f) * (data[c] - data[f])

print(f"\nExcluding mythical_count rows (N = {len(totals)}):\n")
print(f"  Mean children per couple:   {sum(totals)/len(totals):.1f}")
print(f"  Median:                     {percentile(totals, 50):.1f}")
print(f"  25th percentile:            {percentile(totals, 25):.1f}")
print(f"  75th percentile:            {percentile(totals, 75):.1f}")
print(f"  90th percentile:            {percentile(totals, 90):.1f}")
print(f"  Max:                        {max(totals):.1f}")
print()

buckets = [(0, 1), (1, 2), (2, 3), (3, 5), (5, 10), (10, 20), (20, 50), (50, float('inf'))]
print("Distribution:\n")
table = []
for lo, hi in buckets:
    label = f"{lo:.0f}" if hi == lo + 1 else (f"{lo:.0f}–{hi-1:.0f}" if hi != float('inf') else f"{lo:.0f}+")
    n = sum(1 for t in totals if lo <= t < hi)
    pct = 100 * n / len(totals)
    bar = "█" * int(pct / 2)
    table.append([label, n, f"{pct:.0f}%", bar])
print_table(["Children", "N", "%", ""], table, [10, 5, 5, 40])

all_sons = [sons(r) for r in rows if r['row_type'].strip() != 'mythical_count']
all_daughters = [daughters(r) for r in rows if r['row_type'].strip() != 'mythical_count']
print(f"  Mean sons per couple:       {sum(all_sons)/len(all_sons):.1f}")
print(f"  Mean daughters per couple:  {sum(all_daughters)/len(all_daughters):.1f}")
print(f"  Couples with 0 sons:        {sum(1 for s in all_sons if s == 0)} ({100*sum(1 for s in all_sons if s==0)/len(all_sons):.0f}%)")
print(f"  Couples with 0 daughters:   {sum(1 for d in all_daughters if d == 0)} ({100*sum(1 for d in all_daughters if d==0)/len(all_daughters):.0f}%)")
print()


# ── 6. Cross-Tradition Parallels ─────────────────────────────────────────────

print("=" * 70)
print("  6. CROSS-TRADITION PARALLELS (family_id)")
print("=" * 70)

fids = defaultdict(list)
for r in rows:
    fid = r.get('family_id', '').strip()
    if fid:
        fids[fid].append(r)

print(f"\n  {len(fids)} unique family IDs linking {sum(len(v) for v in fids.values())} rows\n")
table = []
for fid, rr in sorted(fids.items()):
    epics = ", ".join(sorted(set(r['epic'].strip() for r in rr)))
    table.append([fid, len(rr), epics])
print_table(["family_id", "N rows", "Epics"], table, [22, 8, 40])


# ── 7. Plots ─────────────────────────────────────────────────────────────────

print("=" * 70)
print("  7. GENERATING PLOTS")
print("=" * 70)

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    # ── PLOT 1: % Male by Tradition ──────────────────────────────────────

    plot_data = []
    for g, s in trad.items():
        t = s['s'] + s['d']
        if t >= 8:
            plot_data.append((g, 100 * s['s'] / t, s['n'], t))
    plot_data.sort(key=lambda x: x[1])

    labels = [d[0] for d in plot_data]
    pcts = [d[1] for d in plot_data]
    ns = [d[2] for d in plot_data]

    fig, ax = plt.subplots(figsize=(10, 7.5))

    colors = []
    for p in pcts:
        if p >= 90: colors.append('#c0392b')
        elif p >= 75: colors.append('#e67e22')
        elif p >= 60: colors.append('#f39c12')
        else: colors.append('#2980b9')

    bars = ax.barh(range(len(labels)), pcts, color=colors, edgecolor='white',
                   linewidth=0.5, height=0.7)

    ax.axvline(x=51.2, color='#2c3e50', linestyle='--', linewidth=1, alpha=0.7, zorder=0)
    ax.text(52, len(labels) - 0.3, 'biological expectation (51%)',
            fontsize=7.5, color='#2c3e50', va='top')

    ax.axvline(x=85, color='#7f8c8d', linestyle=':', linewidth=1, alpha=0.5, zorder=0)
    ax.text(85.5, 0.5, 'dataset avg (85%)', fontsize=7.5, color='#7f8c8d', va='bottom')

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([f"{l}  (n={n})" for l, n in zip(labels, ns)], fontsize=9)
    ax.set_xlabel('% of children who are sons', fontsize=11, fontweight='bold')
    ax.set_title('Son Preference Across Mythological Traditions',
                 fontsize=14, fontweight='bold', pad=15)
    ax.set_xlim(0, 105)

    for i, (bar, pct) in enumerate(zip(bars, pcts)):
        ax.text(pct + 1, i, f'{pct:.0f}%', va='center', fontsize=8.5,
                fontweight='bold', color='#2c3e50')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)

    plt.tight_layout()
    plt.savefig('plot_by_tradition.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()
    print("\n  Saved: plot_by_tradition.png")

    # ── PLOT 2: The Vanishing Daughters ──────────────────────────────────

    hist_zero = defaultdict(lambda: {"zero_d": 0, "zero_s": 0, "total": 0})
    for r in rows:
        if r['row_type'].strip() == 'mythical_count':
            continue
        h = r.get('historicity', 'legendary').strip()
        ns_val = sons(r)
        nd_val = daughters(r)
        hist_zero[h]["total"] += 1
        if nd_val == 0: hist_zero[h]["zero_d"] += 1
        if ns_val == 0: hist_zero[h]["zero_s"] += 1

    cats = ['Legendary\nfamilies', 'Mythological\nfamilies', 'Historical\nfamilies']
    keys = ['legendary', 'mythological', 'historical']
    zero_s = [100 * hist_zero[k]['zero_s'] / hist_zero[k]['total'] for k in keys]
    zero_d = [100 * hist_zero[k]['zero_d'] / hist_zero[k]['total'] for k in keys]
    n_vals = [hist_zero[k]['total'] for k in keys]

    fig, ax = plt.subplots(figsize=(8, 6.5))

    x = np.arange(len(cats))
    width = 0.32

    bars_s = ax.bar(x - width/2, zero_s, width, color='#3498db',
                    label='Zero sons', edgecolor='white', linewidth=0.5)
    bars_d = ax.bar(x + width/2, zero_d, width, color='#e74c3c',
                    label='Zero daughters', edgecolor='white', linewidth=0.5)

    for bar, val in zip(bars_s, zero_s):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'{val:.0f}%', ha='center', va='bottom', fontsize=11,
                fontweight='bold', color='#2c3e50')
    for bar, val in zip(bars_d, zero_d):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'{val:.0f}%', ha='center', va='bottom', fontsize=11,
                fontweight='bold', color='#2c3e50')

    for i, n in enumerate(n_vals):
        ax.text(i, -4, f'n = {n}', ha='center', fontsize=8.5, color='#7f8c8d')

    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=11)
    ax.set_ylabel('% of couples', fontsize=11, fontweight='bold')

    ax.set_title('The Vanishing Daughters', fontsize=15, fontweight='bold', pad=22)
    fig.text(0.5, 0.93,
             'Share of couples with zero sons vs. zero daughters, by historicity of source',
             fontsize=9, color='#7f8c8d', ha='center')

    ax.set_ylim(-6, 84)
    ax.legend(fontsize=10, loc='upper right', framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.annotate(f'{zero_d[0]:.0f}% of legendary couples\nhave no named daughters.\nOnly {zero_s[0]:.0f}% have no sons.',
                xy=(0 + width/2, zero_d[0]), xytext=(0.9, 60),
                fontsize=8.5, color='#c0392b', style='italic',
                arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.2))

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig('plot_vanishing_daughters.png', dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()
    print("  Saved: plot_vanishing_daughters.png")

except ImportError:
    print("\n  matplotlib not installed — skipping plots.")
    print("  Install with: pip install matplotlib")

print("\n" + "─" * 70)
print(f"  Done. {len(rows)} rows analyzed.")
