from collections import deque

quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if order <= quantity_of_food:
        orders.popleft()
        quantity_of_food -= order
    else:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break

if not orders:
    print(f"Orders complete")
