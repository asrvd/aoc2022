def get_priority(rucksack: str) -> int:
    common_letter: str = list(
        set.intersection(
            set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :])
        )
    )[0]
    if common_letter.capitalize() == common_letter:
        return ord(common_letter) - 38
    else:
        return ord(common_letter) - 96


print(
    sum(
        list(
            map(
                lambda x: get_priority(x),
                open("input.txt", "r").read().split("\n"),
            )
        )
    )
)
