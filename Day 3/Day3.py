file = open("./input.txt")

input = [line for line in file.read().splitlines()]

treeCounter = 0
currentPos = [0, 0]

while True:

    if input[currentPos[0]][currentPos[1] % len(input[0])] == "#":
        treeCounter += 1
    if currentPos[0] == len(input)-1:
        break

    currentPos[0] += 1
    currentPos[1] += 3

print(treeCounter)
