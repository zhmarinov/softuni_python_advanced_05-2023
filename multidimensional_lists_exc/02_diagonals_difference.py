n = int(input())
matrix = [[int(el) for el in input().split()]for row in range(n)]

primary_sum = 0
secondary_sum = 0

for idx in range(n):
    primary_sum += matrix[idx][idx]
    secondary_sum += matrix[idx][n-idx-1]

print(abs(primary_sum - secondary_sum))