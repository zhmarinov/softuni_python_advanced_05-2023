original_string = input()
stack_string = list(original_string)


while stack_string:
    removed_elements = stack_string.pop()
    print(removed_elements, end='')


