from collections import Counter


rock_map = []

with open("input.txt") as file:
    for line in file:
        rock_map.append(list(line.strip()))

for i in range(len(rock_map)):
    for j in range(len(rock_map[i])):
        if rock_map[i][j] == "O":
            row = i
            while row > 0 and rock_map[row-1][j] == ".":
                rock_map[row-1][j] = "O"
                rock_map[row][j] = "."
                row -= 1

total_weight = 0
row_weight = len(rock_map)

for row in rock_map:
    total_weight += row.count("O") * row_weight
    row_weight -= 1
print(total_weight)