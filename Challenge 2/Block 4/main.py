# 4.1 — Analyse des ventes
def analyser_ventes(ventes):
    total = {}
    for v in ventes:
        produit = v["produit"]
        total[produit] = total.get(produit, 0) + v["montant"]

    meilleur = max(total, key=total.get)
    distincts = set(total.keys())

    return total, meilleur, total[meilleur], distincts

ventes = [
    {"produit": "pommes", "montant": 120},
    {"produit": "bananes", "montant": 80},
    {"produit": "pommes", "montant": 45},
    {"produit": "oranges", "montant": 60},
    {"produit": "bananes", "montant": 30},
]

total, meilleur, meilleur_total, distincts = analyser_ventes(ventes)
print(f"Total par produit : {total}")
print(f"Meilleur produit : {meilleur} ({meilleur_total})")
print(f"Produits distincts : {distincts}")
