# Advent of Code 2021, Day 7, d3vyce

with open('input/day7.txt') as f:
    file = [int(i) for i in f.read().split(',')]

# Part 1
fuel = 0
tmp = 0

for i in range(min(file), max(file)):
    for y in file:
        if(y < i): tmp += i - y
        else: tmp += y - i
    if(fuel > tmp or fuel == 0): fuel = tmp
    tmp = 0
    
print("Part 1 : ", fuel)

# Part 2
fuel = 0
tmp = 0

for i in range(min(file), max(file)):
    for y in file:
        if(y < i): tmp += sum(range((i - y)+1))
        else: tmp += sum(range((y - i)+1))
    if(fuel > tmp or fuel == 0): fuel = tmp
    tmp = 0
    
print("Part 2 : ", fuel)