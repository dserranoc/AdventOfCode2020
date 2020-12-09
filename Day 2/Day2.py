file = open("./input.txt", "r")
input = [line.replace(":", "").split() for line in file.readlines()]

counter = 0

for password in input:
    min,max = password[0].split("-")
    numOfTimes = password[2].count(password[1])
    if numOfTimes >= int(min) and numOfTimes <= int(max):
        counter+=1

print(counter)