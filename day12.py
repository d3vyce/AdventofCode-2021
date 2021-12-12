# Advent of Code 2021, Day 12, d3vyce

from collections import deque, defaultdict

with open('input/day12.txt') as f:
    file = [i.split('-') for i in f.read().splitlines()]

D = defaultdict(list)

for x, y in file:
    if(y != 'start'):
        D[x].append(y)
    if(x != 'start'):
        D[y].append(x)

print(D)