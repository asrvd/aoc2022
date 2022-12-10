def check_repetition(assignments: list[str]) -> int:
    first = [
        _
        for _ in range(
            int(assignments[0].split("-")[0]), int(assignments[0].split("-")[1]) + 1
        )
    ]
    second = [
        _
        for _ in range(
            int(assignments[1].split("-")[0]), int(assignments[1].split("-")[1]) + 1
        )
    ]

    if set(first).issubset(set(second)) or set(second).issubset(set(first)):
        return 1
    return 0


print(
    sum(
        list(
            map(
                lambda x: check_repetition(list(x)),
                list(
                    map(
                        lambda x: map(lambda x: x, x.split(",")),
                        open("input.txt", "r").read().split("\n"),
                    )
                ),
            )
        )
    )
)
