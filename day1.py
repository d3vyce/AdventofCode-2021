# Advent of Code 2021, Day 1, d3vyce

with open('input/day1.txt') as f:
    file = [int(i) for i in f.read().splitlines()]
    
# Part 1
count = 0
for i in range(len(file)-1):
    if(file[i] < file[i+1]): count += 1

print("Part 1 : ",count)

# Part 2
count = 0
for i in range(len(file)):
    if(sum(file[i:i+3]) < sum(file[i+1:i+4])): count += 1

print("Part 2 : ",count)