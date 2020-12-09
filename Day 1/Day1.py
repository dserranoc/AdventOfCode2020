file = open("./input.txt", "r")

input = [int(x) for x in file.readlines()]

complements = {}

for num in input:
    complements[num] = True
    numToFind = 2020 - num

    if numToFind in complements:
        print(num*numToFind)