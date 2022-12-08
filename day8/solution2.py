tree_rows = open("input.txt", "r").read().split("\n")

visible_tress = 0
tress_on_edge = (2 * len(tree_rows)) + (2 * (len(tree_rows[0]) - 2))

highest_scenic_score = 0

for _ in range(0, len(tree_rows)):
    if _ == 0 or _ == (len(tree_rows) - 1):
        pass
    else:
        rows_above = tree_rows[:_]
        rows_below = tree_rows[_ + 1 :]
        current_row = tree_rows[_]

        for i in range(1, len(current_row) - 1):
            top_score = 0
            bottom_score = 0
            left_score = 0
            right_score = 0

            tress_left = current_row[:i]
            tress_right = current_row[i + 1 :]

            for tree in list(reversed(tress_left)):
                if int(current_row[i]) > int(tree):
                    left_score += 1
                elif int(current_row[i]) == int(tree):
                    left_score += 1
                    break
                else:
                    left_score += 1
                    break

            for tree in tress_right:
                if int(current_row[i]) > int(tree):
                    right_score += 1
                elif int(current_row[i]) == int(tree):
                    right_score += 1
                    break
                else:
                    right_score += 1
                    break

            for row in list(reversed(rows_above)):
                if int(current_row[i]) > int(row[i]):
                    top_score += 1
                elif int(current_row[i]) == int(row[i]):
                    top_score += 1
                    break
                else:
                    top_score += 1
                    break

            for row in rows_below:
                if int(current_row[i]) > int(row[i]):
                    bottom_score += 1
                elif int(current_row[i]) == int(row[i]):
                    bottom_score += 1
                    break
                else:
                    bottom_score += 1
                    break

            # print(is_tallest_left, is_tallest_right, is_tallest_top, is_tallest_bottom)

            scenic_score = top_score * bottom_score * left_score * right_score

            highest_scenic_score = max(highest_scenic_score, scenic_score)

print(highest_scenic_score)
