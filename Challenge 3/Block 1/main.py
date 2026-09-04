# exceptions and files handling in Python

# 1.1






# 1.2

def secure_division(num1, num2):
    try:
        total = num1 / num2
        print(total)
    except ZeroDivisionError:
        print("You can't divide by zero")

secure_division(10,2)
secure_division(10,0)



#1.3

def convert_int(string):
    try:
        print(int(string))
    except ValueError:
        print("Please enter a valid number")
convert_int("10")
convert_int("abc")






#1.4


def access_element_by_index(list, index):
    try:
        print(list[index])
    except IndexError:
        print("Please enter a valid index")

access_element_by_index(["a", "b", "c"], 0)
access_element_by_index(["a", "b", "c"], 10)


#1.5

eleve = {"nom": "Sara", "age": 20}

def access_key(dict, key):
    try:
        print(dict[key])
    except KeyError:
        print("Please enter a valid key")
access_key(eleve,"nom")
access_key(eleve,"email")


#1.6 use of try / except / else / finally all in 1 case
print(" 1. 6 \n")
def traiter_valeur(valeur):
    try:
        converted_valeur = int(valeur)
        print(f"Conversion reussie : {converted_valeur}")
    except ValueError:
        print(f"Erreur : '{valeur}' n’est pas convertible.")
    finally:
        print("Traitement termine.")

traiter_valeur("8")
traiter_valeur("x")
