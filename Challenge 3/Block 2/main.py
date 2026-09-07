# 2.1 use raise to throw an exception
from string.templatelib import convert


def verify_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    else:
        print("Age is valid")

verify_age(20)
verify_age(-1)

# 2.2

def traiter_liste_de_valeurs(list):
    for item in list:
        item = int(item)


traiter_liste_de_valeurs(["3", "9", "x", "5"])


# 2.3
print(" # 2.3 ")
class StockInsuffisantError(Exception):
    pass

demande = 10
bananas = 4

def try_to_buy_bananas(bananas, demande):
    if bananas < demande:
        raise StockInsuffisantError(f"Stock insuffisant. Il manque {demande - bananas} bananes.")
    return "Achat réussi !"
try:
    resultat = try_to_buy_bananas(bananas, demande)
    print(resultat)
except StockInsuffisantError as e:
    print(f"Erreur d'achat : {e}")

try_to_buy_bananas(bananas,demande)

#2.4

