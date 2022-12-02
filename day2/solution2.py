move_sequences = {
    "move_played": {
        "A": {"draw": 1, "win": 2, "lose": 3},
        "B": {"draw": 2, "win": 3, "lose": 1},
        "C": {"draw": 3, "win": 1, "lose": 2},
    },
    "expected_outcome": {
        "X": {"outcome": "lose", "points": 0},
        "Y": {"outcome": "draw", "points": 3},
        "Z": {"outcome": "win", "points": 6},
    },
}


def get_points(move: list) -> int:
    return (
        move_sequences["expected_outcome"][move[1]]["points"]
        + move_sequences["move_played"][move[0]][
            move_sequences["expected_outcome"][move[1]]["outcome"]
        ]
    )


print(
    sum(
        list(
            map(
                lambda x: get_points(list(x)),
                list(
                    map(
                        lambda x: map(lambda x: x, x.split(" ")),
                        open("input.txt", "r").read().split("\n"),
                    )
                ),
            )
        )
    )
)
