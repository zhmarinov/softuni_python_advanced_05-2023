n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]

# primary_diagonal_list = []
# secondary_diagonal_list = []

primary_diagonal_list = [matrix[idx][idx] for idx in range(n)]
# for idx in range(n):
#     primary_diagonal_list.append(matrix[idx][idx])

secondary_diagonal_list = [matrix[idx][n-idx-1] for idx in range(n)]
# for idx in range(n):
#     secondary_diagonal_list.append(matrix[idx][n-idx-1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_list)}. Sum: {sum(primary_diagonal_list)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal_list)}. Sum: {sum(secondary_diagonal_list)}")
