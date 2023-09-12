cars = set()

for _ in range(int(input())):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    print(*cars, sep="\n")
else:
    print("Parking Lot is Empty")
