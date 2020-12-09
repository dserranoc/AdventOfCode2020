file = open("./input.txt", "r")
input = [line.replace(":", "").split() for line in file.readlines()]

counter = 0

for password in input:
    pos1,pos2 = password[0].split("-")
    numOfTimes = 0
    letterToSearch = password[1]
    strPassword = password[2]
    if (strPassword[int(pos1)-1] == letterToSearch and strPassword[int(pos2)-1] != letterToSearch) or (strPassword[int(pos1)-1] != letterToSearch and strPassword[int(pos2)-1] == letterToSearch):
        counter +=1

print(counter)