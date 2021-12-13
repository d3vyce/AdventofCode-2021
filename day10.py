# Advent of Code 2021, Day 10, d3vyce

char = {")": "(", "]": "[", "}": "{", ">": "<"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_bis = {"(": 1, "[": 2, "{": 3, "<": 4}

def check_illegal(line):
    tab = []

    for i in line:
        if i in char.values(): 
            tab.append(i)
        elif char[i] == tab[-1]:
            tab.pop()
        else:
            #print("Expected ",tab[-1],", but found ", i , " instead.")
            return score[i]
    
    return 0

def check_completion(file):
    tab = []
    score = 0
    result = []

    for line in file:
        if check_illegal(line) != 0: continue

        for i in line:
            if i in char.values(): 
                tab.append(i)
            elif char[i] == tab[-1]:
                tab.pop()

        tab.reverse()     
        for i in tab:
            score = (score*5) + score_bis[i]

        result.append(score)
        score = 0
        tab.clear()

    result.sort()
    return result[int(len(result)/2)]


with open('input/day10.txt') as f:
    file = [i for i in f.read().splitlines()]

# Part 1
result = sum(check_illegal(line) for line in file)

print("Part 1 : ", result)

# Part 2

print("Part 2 : ", check_completion(file))