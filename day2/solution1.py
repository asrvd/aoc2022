move_sequences = {
    "move_point": {"rock": 1, "paper": 2, "scissors": 3},
    "round_point": {"win": 6, "draw": 3, "lose": 0},
    "outcome": {
        "rock": {"rock": "draw", "paper": "win", "scissors": "lose"},
        "paper": {"rock": "lose", "paper": "draw", "scissors": "win"},
        "scissors": {"rock": "win", "paper": "lose", "scissors": "draw"},
    },
}


def transform_move(move: str) -> str:
    return (
        "rock" if move in ["X", "A"] else "paper" if move in ["Y", "B"] else "scissors"
    )


def get_points(move: list) -> int:
    return (
        move_sequences["round_point"][
            move_sequences["outcome"][move[0]][move[1]]
        ]
        + move_sequences["move_point"][move[1]]
    )


print(
    sum(
        list(
            map(
                lambda x: get_points(list(x)),
                list(
                    map(
                        lambda x: map(lambda x: transform_move(x), x.split(" ")),
                        open("input.txt", "r").read().split("\n"),
                    )
                ),
            )
        )
    )
)
