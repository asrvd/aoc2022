def check_overlap(assignments: list[str]) -> int:
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

    if set(first).intersection(set(second)):
        return 1
    return 0


print(
    sum(
        list(
            map(
                lambda x: check_overlap(list(x)),
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