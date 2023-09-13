rows = int(input())

matrix = [[int(x) for x in input().split()] for row in range(rows)]

sum_diagonal = 0

for row_index in range(rows):
    sum_diagonal += matrix[row_index][row_index]

print(sum_diagonal)
