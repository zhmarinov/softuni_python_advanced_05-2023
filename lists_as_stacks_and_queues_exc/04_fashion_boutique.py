from collections import deque

delivery = deque([int(x) for x in input().split()])
capacity_of_one_rack = int(input())

rack_count = 1
current_rack_space = capacity_of_one_rack

while delivery:
    cloth = delivery.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        rack_count += 1
        current_rack_space = capacity_of_one_rack - cloth

print(rack_count)