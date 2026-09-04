# 3.1
def comparer_ateliers(atelier_python, atelier_java):
    set_python = set(atelier_python)
    set_java = set(atelier_java)
    return {
        "intersection": set_python & set_java,
        "union": set_python | set_java,
        "difference_python": set_python - set_java
    }

atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]
resultats = comparer_ateliers(atelier_python, atelier_java)
print(f"Inscrits aux deux ateliers : {resultats['intersection']}")
print(f"Inscrits a au moins un atelier : {resultats['union']}")
print(f"Uniquement Python : {resultats['difference_python']}")




# 3.2 — Détection de doublons avec set conversion
def a_des_doublons(liste):
    return len(liste) != len(set(liste))

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]
print(f"a_des_doublons(liste_1) -> {a_des_doublons(liste_1)}")
print(f"a_des_doublons(liste_2) -> {a_des_doublons(liste_2)}")


# 3.3 — Set unique à partir de listes imbriquées
def tous_tags(liste_de_listes):
    return {tag for sous_liste in liste_de_listes for tag in sous_liste}

tags_articles = [
    ["python", "web", "api"],
    ["python", "data"],
    ["web", "css"],
]
print(f"tous_tags : {tous_tags(tags_articles)}")


# 3.4 — Limite des sets : éléments non hashables
coordonnees = {(1, 2), (3, 4)}
print(f"coordonnees : {coordonnees}")