rows = int(input())

matrix = [list(input()) for x in range(rows)]
searched_symbol = input()
searched_symbol_found = False
location = ()

for col_index in range(rows):
    if searched_symbol_found:
        break
    for row_index in range(rows):
        if matrix[row_index][col_index] == searched_symbol:
            searched_symbol_found = True
            location = (row_index, col_index)
            break

if searched_symbol_found:
    print(location)
else:
    print(f"{searched_symbol} does not occur in the matrix")
