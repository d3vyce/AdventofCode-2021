# Advent of Code 2021, Day 3, d3vyce

def search_b(search, pos, mode):
    count = 0
    for i in search:
        if(int(i[pos]) == 1): count += 1

    if(count >= len(search)/2 and mode == "more" or count < len(search)/2 and mode == "less"): return '1'
    else: return '0'


with open('input/day3.txt') as f:
    file = [i for i in f.read().splitlines()]

# Part 1
gamma = ""
epsilon = ""

for i in range(len(file[0])):
    gamma += search_b(file, int(i), "more")
    epsilon += search_b(file, int(i), "less")

print("Part 1 : ", int(gamma, 2)*int(epsilon, 2))

# Part 2
search_g = file

for i in range(len(gamma)):
    byte = int(search_b(search_g, i, "more"))
    search_g = [y for y in search_g if int(y[i]) == byte]
    if(len(search_g) == 1): break

search_e = file

for i in range(len(epsilon)):
    byte = int(search_b(search_e, i, "less"))
    search_e = [y for y in search_e if int(y[i]) == byte]
    if(len(search_e) == 1): break

print("Part 2 : ", int(search_g[0], 2)*int(search_e[0], 2))