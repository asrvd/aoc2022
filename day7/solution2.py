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

smallest_dir_size = 1e9
space_needed = dir_sizes["/"] - 40000000

for key, value in dir_sizes.items():
    smallest_dir_size = (
        min(smallest_dir_size, value) if value >= space_needed else smallest_dir_size
    )

print(smallest_dir_size)
