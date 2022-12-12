from collections import deque

map = [i for i in open("input.txt").read().split("\n")]

start_pos = (0, 0)  # y, x
target_pos = (0, 0)
ord_map = [[0 for _ in range(0, len(map[0]))] for __ in range(0, len(map))]
visited = set()
queue = deque()

for _ in range(0, len(map)):
    for __ in range(0, len(map[_])):
        if map[_][__] == "E":
            target_pos = (_, __)
            ord_map[_][__] = 26
        elif map[_][__] == "S":
            start_pos = (_, __)
            ord_map[_][__] = 1
            queue.append(((_, __), 0))
        else:
            if map[_][__] == "a":
                queue.append(((_, __), 0))
            ord_map[_][__] = ord(map[_][__]) - ord("a") + 1

while queue:
    (y, x), moves = queue.popleft()
    if (y, x) in visited:
        continue
    visited.add((y, x))
    if map[y][x] == "E":
        print(moves)
        break
    for a, b in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if (
            0 <= a < len(map)
            and 0 <= b < len(map[0])
            and ord_map[a][b] <= 1 + ord_map[y][x]
        ):
            queue.append(((a, b), moves + 1))
