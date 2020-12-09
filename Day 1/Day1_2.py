file = open("./input.txt", "r")

input = [int(x) for x in file.readlines()]

complements = {}

for num in input:
    complements[num] = True
    numToSubstract = 2020 - num

    for num2 in input:
        complements[num2] = True
        numToFind = numToSubstract - num2
        if numToFind in complements:
            print(num*numToFind*num2)
            done = True
        
            