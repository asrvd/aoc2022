import requests

input = requests.get("https://adventofcode.com/2022/day/1/input")

print(input.text)
