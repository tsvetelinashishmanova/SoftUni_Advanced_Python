from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    food_left = food_quantity - order
    if food_left < 0:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        exit()
    else:
        food_quantity -= order
        orders.popleft()

print("Orders complete")
