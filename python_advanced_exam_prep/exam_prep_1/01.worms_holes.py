from collections import deque


def read_worms():
    line = input()
    parts = line.split(" ")
    worms = []
    for i, part in enumerate(parts):
        worm = int(part)
        if not (1 <= worm <= 50):
            raise ValueError(f"Bad value for '{worm}' for worm at index #{i}!")
        worms.append(worm)

    return deque(worms)


def read_holes():
    line = input()
    parts = line.split(" ")
    holes = []
    for i, part in enumerate(parts):
        hole = int(part)
        if not (1 <= hole <= 50):
            raise ValueError(f"Bad value for '{hole}' for hole at index #{i}!")
        holes.append(hole)

    return deque(holes)


def main():
    worms = read_worms()
    holes = read_holes()
    matches = []
    initial_worms_count = len(worms)

    while worms and holes:
        worm = worms.pop()

        if worm <= 0:
            continue

        hole = holes.popleft()
        if worm == hole:
            matches.append((worm, hole))
            continue

        worm_reduced = worm - 3
        worms.append(worm_reduced)

    worms_left = []
    while worms:
        worms_left.append(str(worms.popleft()))

    holes_left = []
    while holes:
        holes_left.append(str(holes.popleft()))

    if matches:
        print(f"Matches: {len(matches)}")
    else:
        print("There are no matches.")

    if len(matches) == initial_worms_count:
        print("Every worm found a suitable hole!")
    elif worms_left:
        print("Worms left: " + ", ".join(worms_left))
    elif not worms:
        print("Worms left: none")

    if holes_left:
        print("Holes left: " + ", ".join(holes_left))
    else:
        print("Holes left: none")


if __name__ == "__main__":
    main()
