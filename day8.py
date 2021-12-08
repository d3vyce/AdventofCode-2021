# Advent of Code 2021, Day 8, d3vyce

def get_key(dic, val):
    for key, value in dic.items():
         if val == value:
            return int(key)
            
    return "Error : key doesn't exist"

def search_dic(input):
    dic = {}
    for val in input:
        val = "".join(sorted(val))
        if(len(val) == 2): dic[1] = val
        elif(len(val) == 3): dic[7] = val
        elif(len(val) == 4): dic[4] = val
        elif(len(val) == 7): dic[8] = val
    for val in input:
        val = "".join(sorted(val))
        if val in dic.values(): continue
        if(len(val) == 5):
            if(len(list(set(val)&set(dic[1]))) == 2): dic[3] = val
            elif(len(list(set(val)&set(dic[4]))) == 3): dic[5] = val
            else: dic[2] = val
        else:
            if(len(list(set(val)&set(dic[4]))) == 4): dic[9] = val
            elif(len(list(set(val)&set(dic[7]))) == 2): dic[6] = val
            else: dic[0] = val

    return dic


with open('input/day8.txt') as f:
    file = [(line.strip().split(" | ", 1)[0], line.strip().split(" | ", 1)[1]) for line in f]
    data = [(input.split(), output.split()) for input, output in file]

# Part 1
result = 0

for i in range(len(data)):
    for val in data[i][1]:
        if(len(val) in [2, 3, 4, 7]): result += 1

print("Part 1 : ", result)

# Part 2
result = 0

for i in range(len(data)):
    dic = search_dic(data[i][0])
    result += int(get_key(dic, "".join(sorted(data[i][1][0]))))*1000
    result += int(get_key(dic, "".join(sorted(data[i][1][1]))))*100
    result += int(get_key(dic, "".join(sorted(data[i][1][2]))))*10
    result += int(get_key(dic, "".join(sorted(data[i][1][3]))))

print("Part 2 : ", result)
