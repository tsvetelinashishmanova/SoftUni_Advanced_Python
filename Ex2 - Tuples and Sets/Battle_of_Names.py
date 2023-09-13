odd_numbers = set()
even_numbers = set()
current_row = 1

for _ in range(int(input())):
    sum_name = 0
    name = input()
    for char in name:
        sum_name += ord(char)
    if (sum_name // current_row) % 2 == 0:
        even_numbers.add(sum_name // current_row)
    else:
        odd_numbers.add(sum_name // current_row)
    current_row += 1

if sum(odd_numbers) == sum(even_numbers):
    print(*odd_numbers.union(even_numbers), sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=", ")
