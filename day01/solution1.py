"""
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?
"""

print(
    sorted(
        list(
            map(
                lambda x: sum(list(x)),
                list(
                    map(
                        lambda x: map(lambda x: int(x), x.split("\n")),
                        open("input.txt", "r").read().split("\n\n"),
                    )
                ),
            )
        ),
        reverse=True,
    )[0]
)
