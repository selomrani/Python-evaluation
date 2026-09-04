def vendre(stock, produit, quantite):
    if produit in stock:
        if stock[produit] >= quantite:
            stock[produit] -= quantite
            print(f"Vente enregistree : {quantite} {produit}.")
        else:
            print(f"Stock insuffisant pour {produit} (disponible : {stock[produit]}).")
    else:
        print(f"Produit {produit} non trouve dans le stock.")

def total_par_client(commandes):
    totals = {}
    for cmd in commandes:
        client = cmd["client"]
        if client in totals:
            totals[client] += cmd["quantite"]
        else:
            totals[client] = cmd["quantite"]
    return totals

stock = {"pommes": 50, "bananes": 30, "oranges": 0}
vendre(stock, "pommes", 20)
vendre(stock, "oranges", 5)
print(f"Etat final de stock : {stock}")

commandes = [
    {"client": "Ali", "produit": "pommes", "quantite": 5},
    {"client": "Sara", "produit": "bananes", "quantite": 10},
    {"client": "Ali", "produit": "oranges", "quantite": 2},
]
print(f"total_par_client : {total_par_client(commandes)}")

def longueurs_mots(mots):
    return {mot: len(mot) for mot in mots}

mots = ["chat", "elephant", "abeille", "riz"]
print(f"longueurs : {longueurs_mots(mots)}")

def compter_employes(entreprise):
    for dept, employes in entreprise.items():
        print(f"{dept} : {len(employes)} employe(s)")

entreprise = {
    "IT": ["Ali", "Sara", "Omar"],
    "RH": ["Lina"],
    "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}
compter_employes(entreprise)

