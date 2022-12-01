"""
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?
"""

from functools import reduce

input_array = open("input.txt", "r").read().split("\n\n")
elves_with_calories = list(
    map(lambda x: map(lambda x: int(x), x.split("\n")), input_array)
)

highest_sum = 0

for i in range(0, len(elves_with_calories)):
    calorie_sum = reduce(lambda x, y: x + y, elves_with_calories[i])
    if calorie_sum > highest_sum:
        highest_sum = calorie_sum

print(highest_sum)
