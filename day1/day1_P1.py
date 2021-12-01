prev = 99999
count = 0
with open('input.txt') as f:
    for line in f:
        if(int(line) > prev): count += 1
        prev = int(line)

print(count)