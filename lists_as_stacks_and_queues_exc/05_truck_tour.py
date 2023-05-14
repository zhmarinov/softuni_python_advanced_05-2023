from collections import deque

tank = 0

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()

starting_position = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    tank += petrol

    if tank >= distance:
        tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        starting_position += 1
        tank = 0

print(starting_position)
