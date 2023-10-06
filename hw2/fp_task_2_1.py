from functools import reduce
import statistics
import numbers

students = [
    {"name": "Grisha", "age": 20, "grades": [76, 80, 64, 78]},
    {"name": "Viktor", "age": 18, "grades": [91, 85, 79, 88]},
    {"name": "Ivan", "age": 19, "grades": [70, 71, 64, 84]},
    {"name": "Alexander", "age": 19, "grades": [86, 67, 74, 78]},
    {"name": "Mikhail", "age": 19, "grades": [89, 93, 76, 81]},
    {"name": "Mark", "age": 19, "grades": [78, 91, 79, 81]},
    {"name": "Vica", "age": 18, "grades": [91, 82, 86, 95]},
    {"name": "Nikita", "age": 20, "grades": [80, 73, 83, 68]},
    {"name": "Maxim", "age": 19, "grades": [84, 78, 62, 67]},

]
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

