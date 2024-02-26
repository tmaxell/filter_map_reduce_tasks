from functools import reduce

print("Введите id клиента:")
target_customer_id = int(input())
orders = [
    {"order_id": 1, "customer_id": 101, "amount": 78.0},
    {"order_id": 2, "customer_id": 102, "amount": 88.5},
    {"order_id": 3, "customer_id": 101, "amount": 84.0},
    {"order_id": 4, "customer_id": 103, "amount": 784.0},
    {"order_id": 5, "customer_id": 103, "amount": 81.0},
    {"order_id": 6, "customer_id": 101, "amount": 811.0},
    {"order_id": 7, "customer_id": 104, "amount": 170.0},
    {"order_id": 8, "customer_id": 101, "amount": 685.0},
    {"order_id": 9, "customer_id": 104, "amount": 679.0},
    {"order_id": 10, "customer_id": 102, "amount": 760.0},
    {"order_id": 11, "customer_id": 103, "amount": 306.0},
    {"order_id": 12, "customer_id": 105, "amount": 700.0},
    {"order_id": 13, "customer_id": 102, "amount": 770.0},
    {"order_id": 14, "customer_id": 101, "amount": 722.0},
    {"order_id": 15, "customer_id": 103, "amount": 651.0},
    {"order_id": 16, "customer_id": 105, "amount": 913.0},
    {"order_id": 17, "customer_id": 104, "amount": 774.0},
    {"order_id": 18, "customer_id": 101, "amount": 656.0},
    {"order_id": 19, "customer_id": 102, "amount": 794.0},
    {"order_id": 20, "customer_id": 103, "amount": 711.0},
]

def filter_orders(order, customer_id):
    return order["customer_id"] == customer_id

def calculate_total_amount(total, order):
    return total + order["amount"]

filtered_orders = filter(lambda order: filter_orders(order, target_customer_id), orders)

filtered_orders_list = list(filtered_orders)

total_amount = reduce(calculate_total_amount, filtered_orders_list, 0)

num_orders = len(filtered_orders_list)
average_amount = total_amount / num_orders if num_orders > 0 else 0

print(f"Заказы клиента {target_customer_id}: {filtered_orders_list}")
print(f"Общая сумма заказов для клиента {target_customer_id}: {total_amount}")
print(f"Средняя стоимость заказов для клиента {target_customer_id}: {average_amount}")

