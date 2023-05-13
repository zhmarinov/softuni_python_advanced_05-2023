from collections import deque

names = deque(input().split())
leaving_the_game_toss = int(input())-1

while len(names) > 1:
    names.rotate(-leaving_the_game_toss)
    kid_who_left_the_game = names.popleft()
    print(f"Removed {kid_who_left_the_game}")

print(f"Last is {names.popleft()}")