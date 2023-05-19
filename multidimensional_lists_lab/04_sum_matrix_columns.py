rows, cols = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

for col_idx in range(cols):
    sum_columns = 0
    for row_idx in range(rows):
        sum_columns += matrix[row_idx][col_idx]

    print(sum_columns)