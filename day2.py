# Advent of Code 2021, Day 2, d3vyce

with open('input/day2.txt') as f:
    file = [i for i in f.read().splitlines()]
    
# Part 1
forward = 0
depth = 0

for i in file:
    x = i.split()
    if(x[0] == "forward"): forward += int(x[1])
    elif(x[0] == "up"): depth -= int(x[1])
    elif(x[0] == "down"): depth += int(x[1])

print("Part 1 : ", forward*depth)

# Part 2
forward = 0
depth = 0
aim = 0

for i in file:
    x = i.split()
    if(x[0] == "forward"): 
        forward += int(x[1])
        depth += aim*int(x[1])
    elif(x[0] == "up"): aim -= int(x[1])
    elif(x[0] == "down"): aim += int(x[1])

print("Part 2 : ", forward*depth)