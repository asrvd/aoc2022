from input import all_lists
from typing import Union

correct_pairs = 0


def check_pair(p1: Union[int, list], p2: Union[int, list]) -> int:
    if type(p1) == int and type(p2) == int:
        return -1 if p1 < p2 else 0 if p1 == p2 else 1

    elif type(p1) == list and type(p2) == list:
        for y1, y2 in zip(p1, p2):
            n = check_pair(y1, y2)

            if n != 0:
                return n

        return -1 if len(p1) < len(p2) else 0 if len(p1) == len(p2) else 1

    elif type(p1) == int:
        return check_pair([p1], p2)

    else:
        return check_pair(p1, [p2])


pair = 1
for _ in range(0, len(all_lists), 2):
    if check_pair(all_lists[_], all_lists[_ + 1]) == -1:
        correct_pairs += pair
    pair += 1

print(correct_pairs)
