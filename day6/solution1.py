input = open("input.txt", "r").read()

marker = 4 # initial position of marker should be minimum 4

while True:
    four_chars = input[:4]

    if len(set(four_chars)) == len(four_chars):
        print("Found it!")
        break

    marker += 1
    input = input[1:] # keep reducing the input by 1 character

print(marker)
