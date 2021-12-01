prev = 99999
count = 0
with open('input.txt') as f:
    tab = []
    for line in f:
        tab.append(int(line.rstrip('\n')))

for i in range(len(tab)):
    try :
        current = tab[i]+tab[i+1]+tab[i+2]
    except:
        break
    if(current > prev): count += 1
    prev = current

print(count)