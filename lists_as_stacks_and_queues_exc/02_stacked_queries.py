numbers = int(input())

empty_stack = []

for _ in range(numbers):
    queries = input().split()
    command = queries[0]

    if len(queries) > 1:
        number_to_add = int(queries[1])
        if command == '1':
            empty_stack.append(number_to_add)

    if empty_stack:
        if command == '2':
            empty_stack.pop()
        elif command == '3':
            print(max(empty_stack))
        elif command == '4':
            print(min(empty_stack))

empty_stack.reverse()

print(*empty_stack, sep=", ")