rows = int(input())

matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(rows)]

# for _ in range(rows):
#     inner_list = [el for el in input().split(', ') if int(el) % 2 == 0]
#     matrix.append(inner_list)

print(matrix)