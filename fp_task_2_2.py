users = [
    {"name": "Grigoriy", "expenses": [240, 80, 100, 78]},
    {"name": "Viktor", "expenses": [91, 100, 79, 88]},
    {"name": "Ivan", "expenses": [70, 71, 600, 84]},
    {"name": "Alexander", "expenses": [140, 350, 74, 78]},
    {"name": "Mikhail", "expenses": [90, 500, 76, 81]},
    {"name": "Mark", "expenses": [78, 91, 200, 81]},
    {"name": "Vica", "expenses": [91, 82, 86, 170]},
    {"name": "Nikita", "expenses": [80, 73, 83, 68]},
    {"name": "Maxim", "expenses": [84, 78, 62, 67]},
    {"name": "Ksenia", "expenses": [90, 81, 92, 76]},
    {"name": "Maria", "expenses": [94, 75, 92, 76]},
    {"name": "Kirill", "expenses": [65, 120, 67, 76]},
    {"name": "Tatyana", "expenses": [75, 82, 67, 77]},
    {"name": "Yaroslav", "expenses": [64, 68, 65, 72]},
    {"name": "Vasiliy", "expenses": [80, 79, 87, 65]},
    {"name": "Varvara", "expenses": [89, 79, 270, 91]},
    {"name": "Amelia", "expenses": [90, 82, 96, 77]},
    {"name": "Alexey", "expenses": [75, 75, 65, 65]},
    {"name": "Sophia", "expenses": [68, 87, 73, 79]},
    {"name": "Vladislav", "expenses": [75, 88, 69, 71]},
]
def filter_users(user):
    # Здесь можно установить критерий фильтрации
    return sum(user["expenses"]) > 400

filtered_users = list(filter(filter_users, users))

def calculate_total_expenses(user):
    return {"name": user["name"], "total_expenses": sum(user["expenses"])}

users_with_total_expenses = list(map(calculate_total_expenses, filtered_users))

total_expenses_all_users = sum(user["total_expenses"] for user in users_with_total_expenses)

print("Отфильтрованные пользователи:")
for user in users_with_total_expenses:
    print(f"{user['name']}: {user['total_expenses']}")

print(f"Общая сумма расходов всех отфильтрованных пользователей: {total_expenses_all_users}")