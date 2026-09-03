def menu():
    while True:
     print("** Student's grade manager **")
     print("1) - Calculate Grades Avg .")
     print("2) - Calculate Average class grades. ")
     print("3) - Sort students by Grades.")
     print("4) - Group Students By grade")
     choice = input("Enter your choice : ")
     match choice:
         case "1":
             name = input("Enter your name : ")
             last_name = input("Enter your last name : ")
             grades = []
             for x in range(0, 3):
                 grades.append(int(input(f"Enter grade number {x + 1} : ")))
             print(f"Full name : {name} " + " " + f" : {last_name}")
             print(f"Average grade : {calculate_avg_grade(grades):.2f}")
             print(f"Appreciation : {appreciation(calculate_avg_grade(grades))}")
         case "2":
             print(f"Average Class grades : {moyenne_groupe(students)}")
         case "3":
             sort_student_by_grade(students)
         case "4":
             notes = []
             coefficients = []
             for x in range(0, 3):
                 notes.append(int(input(f"Enter grade number {x + 1} : ")))
             for y in range(0, 3):
                 coefficients.append(int(input(f"Enter coefficient for grade number {y + 1} : ")))
             print(f"Moyenne ponderee : {calculer_moyenne_ponderee(notes, coefficients):.2f}")
def calculate_avg_grade(grades):
    summ = 0
    for grade in grades:
        summ += int(grade)
    avg = summ / len(grades)
    return avg
def appreciation(avg_grade):
    if avg_grade <= 9.9:
        return "Insuffisant"
    elif avg_grade <= 11.9:
        return "Passable"
    elif avg_grade <= 15.9:
        return "Bien"
    else:
        return "Tres bien"

students = [
{"nom": "Karim", "notes": [12, 15, 9]},
{"nom": "Sara", "notes": [18, 17, 16]},
{"nom": "Lina", "notes": [6, 8, 5]},
]
def moyenne_groupe(students):
    total = 0
    for student in students:
        for grade in student["notes"]:
            total += grade
    return total / len(students)


resultats = {
"Karim": {"moyenne": 12.0, "mention": "Bien"},
"Sara": {"moyenne": 17.0, "mention": "Tres bien"},
"Lina": {"moyenne": 8.7, "mention": "Insuffisant"},
"Nadia": {"moyenne": 13.5, "mention": "Bien"},
}



def sort_student_by_grade(students):
    sorted_students = sorted(students, key=lambda x: calculate_avg_grade(x["notes"]), reverse=True)
    for student in sorted_students:
        print(f"{student['nom']} : {calculate_avg_grade(student['notes']):.2f}")

def regrouper_par_mention(resultats):
    grouped = {}
    for nom, info in resultats.items():
        mention = info["mention"]
        if mention not in grouped:
            grouped[mention] = []
        grouped[mention].append(nom)
    return grouped

def detecter_doublons(noms):
    if len(noms) != len(set(noms)):
        print("Attention, il y a des doublons !")

def calculer_moyenne_ponderee(notes, coefficients):
    total = notes[0] * coefficients[0] + notes[1] * coefficients[1] + notes[2] * coefficients[2]
    moyenne = total / len(notes)
    return moyenne

menu()
