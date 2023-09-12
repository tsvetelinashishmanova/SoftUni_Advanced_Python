numbers = set([int(x) for x in input().split()])
target = int(input())
elements = []

for num in numbers:
    for number in numbers:
        if num != number and num + number == target:
            if num not in elements and number not in elements:
                elements.append(num)
                elements.append(number)

for index in range(0, len(elements), 2):
    print(f"{elements[index]} + {elements[index + 1]} = {target}")

