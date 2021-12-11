# Advent of Code 2021, Day 11, d3vyce

neighbors = (
    (1, -1),    (1, 0),     (1, 1),
    (0, -1),                (0, 1),
    (-1, -1),   (-1, 0),    (-1, 1)
)

def check_coord(matrix, x, y, x_max, y_max):
    if(0 <= x < x_max and 0 <= y < y_max): return
    else : return -1

def steps(matrix, x_max, y_max):
    nb_flash = 0

    for x in range(x_max):
        for y in range(y_max):
            matrix[x][y] += 1


    for x in range(x_max):
        for y in range(y_max): 
            flash(matrix, x, y, x_max, y_max)

    for x in range(x_max):
        for y in range(y_max):
            if(matrix[x][y] == -1):
                nb_flash += 1
                matrix[x][y] = 0

    return nb_flash

def flash(matrix, x, y, x_max, y_max):
    if(matrix[x][y] <= 9): return
    matrix[x][y] = -1

    for nx, ny in neighbors:
        if(check_coord(matrix, x+nx, y+ny, x_max, y_max) != -1 and matrix[x+nx][y+ny] != -1):
            matrix[x+nx][y+ny] += 1
            flash(matrix, x+nx, y+ny, x_max, y_max)


with open('input/day11.txt') as f:
    lines = map(str.rstrip, f)
    matrix = list(list(map(int, row)) for row in lines)

cp_matrix = matrix

x_max = len(matrix)
y_max = len(matrix[0])

# Part 1
result = sum(steps(matrix, x_max, y_max) for i in range(100))

print("Part 1 : ", result)

# Part 2
for count in range(1, 1000):
    if(steps(matrix, x_max, y_max) == x_max*y_max):
        break

print("Part 2 : ", count)