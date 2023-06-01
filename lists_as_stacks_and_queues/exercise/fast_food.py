from collections import deque
from sys import maxsize

food_quantity = int(input())

orders = deque(input().split())
biggest_order = -maxsize

for order in orders:
    current_order = int(order)
    if current_order > biggest_order:
        biggest_order = current_order
print(biggest_order)

for idx in range(len(orders)):
    current_order = int(orders[0])
    if food_quantity >= current_order:
        food_quantity -= current_order
        orders.popleft()
    else:
        break
if len(orders) > 0:
    print(f"Orders left: {' '. join(orders)}")
else:
    print("Orders complete")