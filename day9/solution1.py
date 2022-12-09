motions = list(map(lambda x: x.split(" "), open("input.txt").read().split("\n")))

head_pos = [0, 0]
tail_pos = [0, 0]
tail_coords = set()
tail_coords.add((0, 0))

for motion in motions:
    direction = motion[0]
    steps = int(motion[1])

    for _ in range(steps):
        if direction == "R":
            head_pos[0] += 1
        elif direction == "L":
            head_pos[0] -= 1
        elif direction == "U":
            head_pos[1] += 1
        elif direction == "D":
            head_pos[1] -= 1

        # check if tail and head are not adjacent to each other and if they are not, move tail
        if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
            if head_pos[0] != tail_pos[0]:
                if head_pos[0] > tail_pos[0]:
                    tail_pos[0] += 1
                else:
                    tail_pos[0] -= 1

            if head_pos[1] != tail_pos[1]:
                if head_pos[1] > tail_pos[1]:
                    tail_pos[1] += 1
                else:
                    tail_pos[1] -= 1

        tail_coords.add((tail_pos[0], tail_pos[1]))

print(len(tail_coords))
