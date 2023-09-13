rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
max_sum = 0
sub_matrix = []

for col_index in range(cols - 1):
    for row_index in range(rows - 1):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] + matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[matrix[row_index][col_index], matrix[row_index][col_index + 1]], [matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]]

[print(*inner_list) for inner_list in sub_matrix]
print(max_sum)
