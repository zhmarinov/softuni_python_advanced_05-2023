#Solution 1:

from collections import deque

list_of_strings = deque([el.split() for el in input().split('|')])
flatten_list = []

while list_of_strings:
    flatten_list.append(list_of_strings.pop())

print(*[' '.join(el) for el in flatten_list if el])

#Solution 2:


numbers = ([el.split() for el in input().split('|')])

print(*[' '.join(el) for el in numbers[::-1] if el])