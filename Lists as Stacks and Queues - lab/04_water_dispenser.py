from collections import deque

quantity_of_water = int(input())

dispenser_queue = deque()

name = input()

while name != 'Start':
    dispenser_queue.append(name)
    name = input()

command = input()

while command != 'End':

    data = command.split()

    if len(data) == 1:
        litters_wanted = int(data[0])

        if litters_wanted <= quantity_of_water:
            quantity_of_water -= litters_wanted
            person = dispenser_queue.popleft()
            print(f"{person} got water")
        else:
            person = dispenser_queue.popleft()
            print(f"{person} must wait")

    else:
        litters_to_refill = int(data[1])
        quantity_of_water += litters_to_refill
    command = input()

print(f"{quantity_of_water} liters left")
