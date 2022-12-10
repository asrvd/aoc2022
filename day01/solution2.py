"""
Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?
"""

print(
    sum(
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
        )[:3],
    )
)
