from collections import deque

queue = deque()
water_quantity = int(input())
name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    command = command.split()
    if len(command) == 1:
        water_wanted = int(command[0])
        if water_quantity - water_wanted >= 0:
            print(f"{queue.popleft()} got water")
            water_quantity -= water_wanted
        else:
            print(f"{queue.popleft()} must wait")
    else:
        liters_to_add = int(command[1])
        water_quantity += liters_to_add
    command = input()

print(f"{water_quantity} liters left")



