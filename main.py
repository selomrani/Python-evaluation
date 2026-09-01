def menu():
    while True:
     print("** Student's grade manager **")
     print("1) - Calculate Grades Avg .")
     print("2) - Calculate Average class grades. ")
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
menu()