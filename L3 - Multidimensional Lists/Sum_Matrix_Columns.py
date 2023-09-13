rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

for col_index in range(cols):
    sum_col = 0
    for row_index in range(rows):
        sum_col += matrix[row_index][col_index]
    print(sum_col)
