from collections import deque

clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_space = rack_capacity
num_of_racks = 1

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        num_of_racks += 1
        current_rack_space = rack_capacity - cloth

print(f"{num_of_racks}")
