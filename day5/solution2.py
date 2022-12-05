[diagram, moves] = open("input.txt", "r").read().split("\n\n")


stackCount = len(diagram.split("\n").pop().replace(" ", ""))

all_crates = diagram.split("\n")

stacks = [
    list(
        filter(
            lambda x: x != " ",
            reversed(
                [
                    crates[diagram.split("\n").pop().index(str(_))]
                    for crates in all_crates
                ]
            ),
        )
    )
    for _ in range(1, stackCount + 1)
]


moves = list(map(lambda x: x.split(" "), moves.split("\n")))

for move in moves:
    from_stack = int(move[3])
    to_stack = int(move[5])
    amount = int(move[1])

    stacks[to_stack - 1] = stacks[to_stack - 1] + stacks[from_stack - 1][-amount:] # don't reverse the list
    stacks[from_stack - 1] = stacks[from_stack - 1][:-amount]

print("".join(["" + stack.pop() for stack in stacks]))
