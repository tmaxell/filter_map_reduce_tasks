from functools import reduce
import statistics
import numbers

students = [
    {"name": "Grisha", "age": 20, "subject": "Math", "grades": [76, 80, 64, 78]},
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
print("Введите возраст, по которому хотите отфилтьровать студентов:")
target_age = int(input())
print("Введите предмет, по которому хотите сделать выборку студентов:")
target_subject = input()

def calculate_average_grades(students):
    student_averages = []
    total_sum = 0
    total_count = 0

    for student in students:
        grades = student["grades"]
        average = sum(grades) / len(grades)
        student_averages.append({"name": student["name"], "average": average})
        total_sum += sum(grades)
        total_count += len(grades)

    overall_average = total_sum / total_count
    return student_averages, overall_average

def find_top_students(students):
    student_averages, _ = calculate_average_grades(students)
    top_students = []

    max_average = max(student["average"] for student in student_averages)

    for student in student_averages:
        if student["average"] == max_average:
            top_students.append(student["name"])

    return top_students
student_averages, overall_average = calculate_average_grades(students)
top_students = find_top_students(students)

print("Средний балл для каждого студента:")
for student in student_averages:
    print(f"{student['name']}: {student['average']}")

print(f"Общий средний балл по всем студентам: {overall_average}")

print("Студент(ы) с самым высоким средним баллом:")
for student in top_students:
    print(student)
def filter_students_by_age(students, target_age):
    filtered_students_age = []
    for student in students:
        if student["age"] == target_age:
            filtered_students_age.append(student)
    return filtered_students_age

def filter_students_by_subject(students, target_subject):
    filtered_students = []
    for student in students:
        if student["subject"] == target_subject:
            filtered_students.append(student)
    return filtered_students

# Примеры использования функций для фильтрации студентов
filtered_by_age_20 = filter_students_by_age(students, target_age)
filtered_by_subject_math = filter_students_by_subject(students, target_subject)

print(f"Студенты с возрастом {target_age}:")
for student in filtered_by_age_20:
    print(student["name"])

print("Студенты по предмету:")
for student in filtered_by_subject_math:
    print(student["name"])

