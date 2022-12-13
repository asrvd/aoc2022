from input import all_lists
from typing import Union
from functools import cmp_to_key


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


packets = [_ for _ in all_lists] + [[[2]], [[6]]]

packets = sorted(packets, key=cmp_to_key(lambda x, y: check_pair(x, y)))

decoder_key = 1

for _ in range(0, len(packets)):
    if packets[_] == [[2]] or packets[_] == [[6]]:
        decoder_key *= _ + 1

print(decoder_key)
