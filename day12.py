# Advent of Code 2021, Day 12, d3vyce

from collections import defaultdict

def part1(D, src, dst):
    stack = [(src, {src})]
    nb_path = 0

    while stack:
        node, visited = stack.pop()

        if(node == dst):
            nb_path += 1

        for i in D[node]:
            if(i in visited and i.islower()):
                continue

            stack.append((i, visited | {i})) # "|" = union of 2 sets

    return nb_path

def part2(D, src, dst):
    stack = [(src, {src}, False)]
    nb_path = 0

    while stack:
        node, visited, double = stack.pop()

        if node == dst:
            nb_path += 1
            continue

        for n in D[node]:
            if(n not in visited or n.isupper()):
                stack.append((n, visited | {n}, double))
                continue
            elif double:
                continue

            stack.append((n, visited, True))

    return nb_path


with open('input/day12.txt') as f:
    file = [i.split('-') for i in f.read().splitlines()]

D = defaultdict(list)

for x, y in file:
    if(y != 'start'):
        D[x].append(y)
    if(x != 'start'):
        D[y].append(x)

# Part 1
print("Part 1 : ",part1(D, 'start', 'end'))

# Part 2
print("Part 2 : ",part2(D, 'start', 'end'))