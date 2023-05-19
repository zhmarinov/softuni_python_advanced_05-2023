rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
flatten = []

for lists in matrix:
    for el in lists:
        flatten.append(el)

print(flatten)