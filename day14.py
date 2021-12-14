# Advent of Code 2021, Day 14, d3vyce

def polymerization(formula, input):
    output = ""

    for i in range(len(formula)-1):
        output += formula[i]+input[formula[i:i+2]]
    output += formula[-1]

    return output

def count(formula):
    nb = []
    for i in ["C", "H", "B", "N"]:
        nb.append(formula.count(i))
    return max(nb) - min(nb)

with open('input/day14.txt') as f:
    formula = f.readline().strip('\n')
    for line in f:
        input = dict(i.rstrip().split(' -> ', 1) for i in f)

# Part 1
for _ in range(10):
    formula = polymerization(formula, input)

print("Part 1 : ",count(formula))

# Part 2
