from collections import defaultdict

cmds = open("input.txt", "r").read().split("\n")
dir_sizes = defaultdict(int)
current_path = []

for cmd in cmds:
    words = (
        cmd.strip().split()[1:] if cmd.strip().startswith("$") else cmd.strip().split()
    )  # remove $ if it exists
    if words[0] == "cd":
        if words[1] == "..":
            current_path.pop()
        else:
            current_path.append(words[1])
    elif not words[0].isalpha():
        for i in range(1, len(current_path) + 1):
            dir_sizes["/".join(current_path[:i])] += int(words[0])

total_sum = 0

for key, value in dir_sizes.items():
    if value <= 100000:
        total_sum += value

print(total_sum)
