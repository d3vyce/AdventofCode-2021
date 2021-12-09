# Advent of Code 2021, Day 9, d3vyce

from collections import deque

def check_coord(x, y, matrix):
    x_max = len(file)
    y_max = len(file[0])

    if(x < 0 or x >= x_max or y < 0 or y >= y_max): return 10
    else : return int(matrix[x][y])

def check_limit(x, y, matrix):
    result = check_coord(x, y, matrix)
    if(result < 9): return result
    else: return 0

def check_basins(x, y, matrix):
    x_max = len(file)
    y_max = len(file[0])

    basins_loc = set()
    loc_to_check = []
    loc_to_check.append((x, y))

    while len(loc_to_check) > 0:
        x, y = loc_to_check.pop()

        if (x, y) in basins_loc:
            continue
        else: basins_loc.add((x, y))

        val = check_limit(x, y, matrix)
        if check_limit(x - 1, y, matrix) > val:
            loc_to_check.append((x - 1, y))
        if check_limit(x + 1, y, matrix) > val:
            loc_to_check.append((x + 1, y))
        if check_limit(x, y - 1, matrix) > val:
            loc_to_check.append((x, y - 1))
        if check_limit(x, y + 1, matrix) > val:
            loc_to_check.append((x, y + 1))

    return len(basins_loc)


with open('input/day9.txt') as f:
    file = [i for i in f.read().splitlines()]

x_max = len(file)
y_max = len(file[0])

# Part 1
result = 0
low_pt = []

for x in range(x_max):
    for y in range(y_max):
        val = check_coord(x, y, file)
        if(
            val < check_coord(x-1, y, file)
            and val < check_coord(x+1, y, file)
            and val < check_coord(x, y-1, file)
            and val < check_coord(x, y+1, file)
        ): 
            result += int(file[x][y])+1
            low_pt.append((x, y))
      

print("Part 1 : ", result)

# Part 2
basins = []

for x, y in low_pt:
    basins.append(check_basins(x, y, file))

basins.sort(reverse=True)
result = basins[0] * basins[1] * basins[2]

print("Part 2 : ", result)