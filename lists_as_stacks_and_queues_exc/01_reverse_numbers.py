# solving the task using stack

numbers = input().split()

for _ in range(len(numbers)):
    reversed_numbers = numbers.pop()
    print(reversed_numbers, end=' ')
