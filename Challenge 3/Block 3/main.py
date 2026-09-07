# file handling in Python

# 3.1

def ecrire_liste_courses(chemin, articles):
    file_path = chemin
    with open(file_path,"w") as f:
        for article in articles:
            f.write(article + "\n")
articles = ["pommes", "lait", "pain"]

ecrire_liste_courses("courses.txt",articles)


# 3.2
def ajouter_article(chemin, article):
    with open(chemin,"a") as f:
        f.write(article + "\n")



ajouter_article("courses.txt","oeufs")


# 3.3
def lire_fichier(file_path):
    with open(file_path,"r") as f:
        print(f.readlines())


lire_fichier("courses.txt")


# 3.4

def compter_lignes(file_path):
    line_count = 0
    with open(file_path,"r") as f:
        for line in f:
            line_count += 1
    print(f"nombre des lignes : {line_count}")

compter_lignes("courses.txt")