def find_element_in_matrix(matrix, element):
    for row_idx in range(n):
        for col_idx in range(n):
            if matrix[row_idx][col_idx] == element:
                return row_idx, col_idx


n = int(input())

matrix = ([[el for el in list(input())] for _ in range(n)])

symbol = input()

position = find_element_in_matrix(matrix, symbol)

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")