# Advent of Code 2021, Day 9, d3vyce

with open('input/day9.txt') as f:
    file = [i for i in f.read().splitlines()]

x_max = len(file)
y_max = len(file[0])
result = 0
tmp = 0
check = 4

for x in range(x_max):
    for y in range(y_max):
        if(x == 0): check -= 1
        if(x == 99): check -= 1
        if(y == 0): check -= 1
        if(y == 99): check -= 1

        if(x != 0 and file[x][y] < file[x-1][y]): tmp += 1
        if(x != 99 and file[x][y] < file[x+1][y]): tmp += 1
        if(y != 0 and file[x][y] < file[x][y-1]): tmp += 1
        if(y != 99 and file[x][y] < file[x][y+1]): tmp += 1
        if(tmp == check): 
            result += int(file[x][y])+1
        tmp = 0
        check = 4

print("Part 1 : ", result)

#if(file[x][y] < file[x+1][y] and file[x][y] < file[x-1][y] and file[x][y] < file[x][y+1] and file[x][y] < file[x][y-1]): result += 1