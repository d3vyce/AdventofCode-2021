# Advent of Code 2021, Day 3, d3vyce

with open('input/day3.txt') as f:
    file = [i for i in f.read().splitlines()]

# Part 1
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = ""
epsilon = ""

for i in file:
    for y in range(len(i)):
        if(int(i[y]) == 1):count[y] += 1

for i in count:
    if(i < 500):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("Part 1 : ", int(gamma, 2)*int(epsilon, 2))

