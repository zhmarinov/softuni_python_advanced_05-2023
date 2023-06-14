def print_negative_positive(negative, positive):
    print(negative)
    print(positive)

    if abs(negative) > positive:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
negative_numbers = [el for el in numbers if el < 0]
positive_numbers = [el for el in numbers if el > 0]

sum_of_negative_numbers = sum(negative_numbers)
sum_of_positive_numbers = sum(positive_numbers)

print_negative_positive(sum_of_negative_numbers, sum_of_positive_numbers)