"""
Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?
"""

from functools import reduce

input_array = open("input.txt", "r").read().split("\n\n")
elves_with_calories = []

for i in range(0, len(input_array)):
    elves_with_calories.append(map(lambda x: int(x), input_array[i].split("\n")))

calories_sums = []

for i in range(0, len(elves_with_calories)):
    calories_sums.append(reduce(lambda a, b: a + b, elves_with_calories[i]))

calories_sums.sort(reverse=True)

top_three_sum = reduce(lambda a, b: a + b, calories_sums[:3])

print(top_three_sum)
