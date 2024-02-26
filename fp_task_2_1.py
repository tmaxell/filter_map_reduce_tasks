students = [
    {"name": "Grigoriy", "age": 20, "subject": "Math", "grades": [76, 80, 64, 78]},
    {"name": "Viktor", "age": 18, "subject": "Math", "grades": [91, 85, 79, 88]},
    {"name": "Ivan", "age": 19, "subject": "Physics", "grades": [70, 71, 64, 84]},
    {"name": "Alexander", "age": 19, "subject": "Math", "grades": [86, 67, 74, 78]},
    {"name": "Mikhail", "age": 19, "subject": "Math", "grades": [89, 93, 76, 81]},
    {"name": "Mark", "age": 19, "subject": "Physics", "grades": [78, 91, 79, 81]},
    {"name": "Vica", "age": 18, "subject": "Math", "grades": [91, 82, 86, 95]},
    {"name": "Nikita", "age": 20, "subject": "Math", "grades": [80, 73, 83, 68]},
    {"name": "Maxim", "age": 19, "subject": "Physics", "grades": [84, 78, 62, 67]},
    {"name": "Ksenia", "age": 20, "subject": "Math", "grades": [90, 81, 92, 76]},
    {"name": "Maria", "age": 20, "subject": "Math", "grades": [94, 75, 92, 76]},
    {"name": "Kirill", "age": 18, "subject": "Math", "grades": [65, 81, 67, 76]},
    {"name": "Tatyana", "age": 19, "subject": "Math", "grades": [75, 82, 67, 77]},
    {"name": "Yaroslav", "age": 18, "subject": "Math", "grades": [64, 68, 65, 72]},
    {"name": "Vasiliy", "age": 20, "subject": "Math", "grades": [80, 79, 87, 65]},
    {"name": "Varvara", "age": 19, "subject": "Math", "grades": [89, 79, 84, 91]},
    {"name": "Amelia", "age": 18, "subject": "Math", "grades": [90, 82, 96, 77]},
    {"name": "Alexey", "age": 20, "subject": "Math", "grades": [75, 75, 65, 65]},
    {"name": "Sophia", "age": 19, "subject": "Math", "grades": [68, 87, 73, 79]},
    {"name": "Vladislav", "age": 18, "subject": "Math", "grades": [75, 88, 69, 71]},
]
print("Введите возраст, по которому хотите отфильтровать студентов:")
target_age = int(input())
def calculate_average_grade(student):
    grades = student["grades"]
    return sum(grades) / len(grades)

filtered_students = list(filter(lambda student: student["age"] == target_age, students))

average_grades = list(map(calculate_average_grade, students))

best_student = max(students, key=calculate_average_grade)

print(f"Студенты возрастом {target_age} лет:")
for student in filtered_students:
    print(f"{student['name']}: {student['age']} лет")

print("\nСредний балл каждого студента:")
for i, student in enumerate(students):
    print(f"{student['name']}: {average_grades[i]:.2f}")

print("\nЛучший студент:")
print(f"{best_student['name']}: {calculate_average_grade(best_student):.2f}")


