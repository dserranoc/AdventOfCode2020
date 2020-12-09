file = open("./input.txt")

input = [line for line in file.read().splitlines()]

offsets = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
result = 1
for offset in offsets:
    currentPos = [0, 0]
    treeCounter = 0
    while True:

        if input[currentPos[0]][currentPos[1] % len(input[0])] == "#":
            treeCounter += 1

        if currentPos[0] == len(input)-1:
            result = result*treeCounter
            break

        currentPos[0] += offset[0]
        currentPos[1] += offset[1]

print(result)
