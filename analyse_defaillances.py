"""Defaillances d'entreprises au Maroc : import du dataset et graphiques.
Usage : python analyse_defaillances.py
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/defaillances_maroc.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Graphique 1 : evolution des defaillances (2021-2026)
ev = df[df.indicateur.isin(["defaillances", "defaillances_prevision"])].copy()
ev["annee"] = ev.annee.astype(int)
ev = ev.sort_values("annee")
colors = ["#c0392b" if s == "verifie" else "#e6a09a" if s == "derive" else "#95a5a6"
          for s in ev.statut]
ax1.bar(ev.annee.astype(str), ev.valeur.astype(float), color=colors)
for x, y in zip(ev.annee.astype(str), ev.valeur.astype(float)):
    ax1.text(x, y + 150, f"{int(y):,}".replace(",", " "), ha="center", fontsize=8)
ax1.set_title("Defaillances d'entreprises au Maroc\n(fonce = publie, clair = derive, gris = prevision)")
ax1.grid(axis="y", alpha=0.3)

# Graphique 2 : repartition sectorielle 2024
sec = df[df.indicateur.str.startswith("part_secteur")].copy()
labels = sec.indicateur.str.replace("part_secteur_", "").str.capitalize().tolist()
vals = sec.valeur.astype(float).tolist()
labels.append("Autres")
vals.append(100 - sum(vals))
ax2.pie(vals, labels=labels, autopct="%1.0f%%", startangle=90)
ax2.set_title("Part des defaillances par secteur, 2024")

plt.tight_layout()
plt.savefig("graphique_defaillances.png", dpi=150)

d = ev.set_index("annee").valeur.astype(float)
print(f"2021 -> 2024 : {d[2024]/d[2021]-1:+.0%}")
print(f"2024 -> 2025 : {d[2025]/d[2024]-1:+.1%}")
