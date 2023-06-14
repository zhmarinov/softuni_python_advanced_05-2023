# print(*{input() for _ in range(int(input()))}, sep="\n")

usernames_count = int(input())
names = set()

for _ in range(usernames_count):
    names.add(input())

print(*names, sep="\n")
