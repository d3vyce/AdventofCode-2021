# Advent of Code 2021, Day 6, d3vyce

from collections import defaultdict

with open('input/day6.txt') as f:
    file = [int(i) for i in f.read().split(',')]

dic = defaultdict(int)
for i in file:
    dic[i] += 1

print(sum(dic.values()))

days = 256

# Part 1&2
for day in range(days):
    dic_tmp = defaultdict(int)
    for i, j in dic.items():
        i -= 1
        if i < 0:
            dic_tmp[6] += j
            dic_tmp[8] += j
        else:
            dic_tmp[i] += j
    dic = dic_tmp

print(sum(dic.values()))