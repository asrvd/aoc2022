input_list = open("input.txt", "r").read().split("\n")


def get_priority(rucksacks: list) -> int:
    common_letter: str = list(set.intersection(*map(set, rucksacks)))[0]
    if common_letter.capitalize() == common_letter:
        return ord(common_letter) - 38
    else:
        return ord(common_letter) - 96


print(
    sum(
        list(
            map(
                lambda x: get_priority(x),
                [input_list[_ : _ + 3] for _ in range(0, len(input_list), 3)],
            )
        )
    )
)
