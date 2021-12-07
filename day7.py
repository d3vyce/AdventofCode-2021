# Advent of Code 2021, Day 7, d3vyce

import numpy as np

with open('input/day7.txt') as f:
    file = [int(i) for i in f.read().split(',')]

# Part 1
fuel = 0

mediane = np.median(file)
for y in file:
    fuel += np.abs(y - mediane)
    
print("Part 1 : ", int(fuel))

# Part 2
fuel = 0
tmp = 0

for i in range(min(file), max(file)):
    for y in file:
        tmp += abs(y - i)*(1+abs(y - i))/2
    if(fuel > tmp or fuel == 0): fuel = tmp
    tmp = 0
    
print("Part 2 : ", int(fuel))