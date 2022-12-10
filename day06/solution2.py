input = open("input.txt", "r").read()

marker = 14 # initial position of marker should be minimum 14

while True:
    four_chars = input[:14]

    if len(set(four_chars)) == len(four_chars): # check for unique characters
        break

    marker += 1
    input = input[1:] # keep reducing the input by 1 character

print(marker)