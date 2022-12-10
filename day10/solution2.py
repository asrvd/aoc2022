signals = list(map(lambda x: x.split(" "), open("input.txt").read().split("\n")))
x = 1
cycle_and_x = [] # to map every cycle wit its respective value of x
cycle_count = 0

for signal in signals:
    if signal[0] == "noop":
        cycle_count += 1
        cycle_and_x.append((cycle_count, x))
    elif signal[0] == "addx":
        for _ in range(2):
            cycle_count += 1
            cycle_and_x.append((cycle_count, x))
        x += int(signal[1])

row = 0

for _ in range(0, len(cycle_and_x), 40):
    for i in range(_, _ + 40):
        sprite_positions = [
            cycle_and_x[i][1] - 1,
            cycle_and_x[i][1],
            cycle_and_x[i][1] + 1,
        ] # since sprite is 3 characters wide
        print(".", end="") if i - (40 * row) not in sprite_positions else print(
            "#", end=""
        ) # print # only if i overlaps with sprite
    row = row + 1
    print() # print new line
