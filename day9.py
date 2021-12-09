# Advent of Code 2021, Day 9, d3vyce

from collections import deque

def check_coord(x, y, matrix):
    x_max = len(file)
    y_max = len(file[0])

    if(x < 0 or x >= x_max or y < 0 or y >= y_max): return 10
    else : return int(matrix[x][y])

with open('input/day9.txt') as f:
    file = [i for i in f.read().splitlines()]

x_max = len(file)
y_max = len(file[0])

# Part 1
result = 0

for x in range(x_max):
    for y in range(y_max):
        val = check_coord(x, y, file)
        if(
            val < check_coord(x-1, y, file)
            and val < check_coord(x+1, y, file)
            and val < check_coord(x, y-1, file)
            and val < check_coord(x, y+1, file)
        ): result += int(file[x][y])+1
      

print("Part 1 : ", result)

# Part 2
print("Part 2 : ", result)