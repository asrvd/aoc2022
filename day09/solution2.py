motions = list(map(lambda x: x.split(" "), open("input.txt").read().split("\n")))

all_knots_pos = [[0, 0] for _ in range(10)]
tail_coords = set()
tail_coords.add((0, 0))


for motion in motions:
    direction = motion[0]
    steps = int(motion[1])

    for _ in range(steps):
        if direction == "R":
            all_knots_pos[0][0] += 1
        elif direction == "L":
            all_knots_pos[0][0] -= 1
        elif direction == "U":
            all_knots_pos[0][1] += 1
        elif direction == "D":
            all_knots_pos[0][1] -= 1

        for i in range(1, 10):
            if (
                abs(all_knots_pos[i - 1][0] - all_knots_pos[i][0]) > 1
                or abs(all_knots_pos[i - 1][1] - all_knots_pos[i][1]) > 1
            ):
                if all_knots_pos[i - 1][0] != all_knots_pos[i][0]:
                    if all_knots_pos[i - 1][0] > all_knots_pos[i][0]:
                        all_knots_pos[i][0] += 1
                    else:
                        all_knots_pos[i][0] -= 1

                if all_knots_pos[i - 1][1] != all_knots_pos[i][1]:
                    if all_knots_pos[i - 1][1] > all_knots_pos[i][1]:
                        all_knots_pos[i][1] += 1
                    else:
                        all_knots_pos[i][1] -= 1

        tail_coords.add((all_knots_pos[9][0], all_knots_pos[9][1]))

print(len(tail_coords))
