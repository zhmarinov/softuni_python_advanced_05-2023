rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

sub_matrix = []
max_sum = float('-inf')

for rol_idx in range(rows-1):
    for col_idx in range(cols-1):
        current_element = matrix[rol_idx][col_idx]
        element_below = matrix[rol_idx][col_idx+1]
        next_element = matrix[rol_idx+1][col_idx]
        diagonal_element = matrix[rol_idx+1][col_idx+1]

        current_sum = current_element + element_below + next_element + diagonal_element

        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [current_element, element_below, next_element, diagonal_element]

print(f"{sub_matrix[0]} {sub_matrix[1]}")
print(f"{sub_matrix[2]} {sub_matrix[3]}")

print(max_sum)