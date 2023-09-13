rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_matrix = 0

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    sum_matrix += sum(inner_list)
    matrix.append(inner_list)

print(sum_matrix)
print(matrix)
