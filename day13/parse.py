pairs = open("input.txt").read().split("\n\n")

with open("input.py", "w") as f:
    f.write("all_lists = [\n")
    for pair in pairs:
        for line in pair.split("\n"):
            f.write(rf"{line}" + ",\n")
    f.write("]\n")
    f.close()
