tree_rows = open("input.txt", "r").read().split("\n")

visible_tress = 0
tress_on_edge = (2 * len(tree_rows)) + (2 * (len(tree_rows[0]) - 2))


for _ in range(0, len(tree_rows)):
    if _ == 0 or _ == (len(tree_rows) - 1):
        pass
    else:
        rows_above = tree_rows[:_]
        rows_below = tree_rows[_ + 1 :]
        current_row = tree_rows[_]

        for i in range(1, len(current_row) - 1):
            is_tallest_top = False
            is_tallest_bottom = False
            is_tallest_left = False
            is_tallest_right = False
            tress_left = current_row[:i]
            tress_right = current_row[i + 1 :]

            for tree in tress_left:
                if int(current_row[i]) > int(tree):
                    is_tallest_left = True
                else:
                    is_tallest_left = False
                    break

            for tree in tress_right:
                if int(current_row[i]) > int(tree):
                    is_tallest_right = True
                else:
                    is_tallest_right = False
                    break

            for row in rows_above:
                if int(current_row[i]) > int(row[i]):
                    is_tallest_top = True
                else:
                    is_tallest_top = False
                    break

            for row in rows_below:
                if int(current_row[i]) > int(row[i]):
                    is_tallest_bottom = True
                else:
                    is_tallest_bottom = False
                    break

            # print(is_tallest_left, is_tallest_right, is_tallest_top, is_tallest_bottom)

            if (
                is_tallest_left
                or is_tallest_right
                or is_tallest_top
                or is_tallest_bottom
            ):
                visible_tress += 1

print(visible_tress + tress_on_edge)
