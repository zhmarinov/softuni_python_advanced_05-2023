size_of_matrix = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size_of_matrix)]

sum_diagonals = 0

for idx in range(size_of_matrix):
    sum_diagonals += matrix[idx][idx]

print(sum_diagonals)
