def multiply(*args):
    sum_of_multiplied_numbers = 1

    for number in args:
        sum_of_multiplied_numbers *= number

    return sum_of_multiplied_numbers


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
