# rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

# for _ in range(rows):
#    matrix.append([int(x) for x in input().split(", ")])

flatten = []

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        flatten.append(matrix[row_index][col_index])

flatted_matrix = [x for sublist in matrix for x in sublist]

print(matrix)
print(flatten)
print(flatted_matrix)
