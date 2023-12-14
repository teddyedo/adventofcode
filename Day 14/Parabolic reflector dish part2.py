rock_map = []
rock_map_v2 = []

with open("input.txt") as file:
    for line in file:
        rock_map.append(list(line.strip()))
        rock_map_v2.append(list(line.strip()))

def bend_to_north(rock_map):
    for i in range(len(rock_map)):
        for j in range(len(rock_map[i])):
            if rock_map[i][j] == "O":
                row = i
                while row > 0 and rock_map[row-1][j] == ".":
                    rock_map[row-1][j] = "O"
                    rock_map[row][j] = "."
                    row -= 1

def bend_to_south(rock_map):
    for i in range(len(rock_map) - 1, -1, -1):
        for j in range(len(rock_map[i])):
            if rock_map[i][j] == "O":
                row = i
                while row < len(rock_map)-1 and rock_map[row+1][j] == ".":
                    rock_map[row+1][j] = "O"
                    rock_map[row][j] = "."
                    row += 1

def bend_to_west(rock_map):
    for i in range(len(rock_map)):
        for j in range(len(rock_map[i])):
            if rock_map[i][j] == "O":
                column = j
                while column > 0 and rock_map[i][column-1] == ".":
                    rock_map[i][column-1] = "O"
                    rock_map[i][column] = "."
                    column -= 1

def bend_to_east(rock_map):
    for i in range(len(rock_map)):
        for j in range(len(rock_map[i])-1, -1, -1):
            if rock_map[i][j] == "O":
                column = j
                while column < len(rock_map[i])-1 and rock_map[i][column+1] == ".":
                    rock_map[i][column+1] = "O"
                    rock_map[i][column] = "."
                    column += 1
def print_map(rock_map):
    for row in rock_map:
        print(row)
    print()    

def make_a_cycle(rock_map):
    bend_to_north(rock_map)
    bend_to_west(rock_map)
    bend_to_south(rock_map)
    bend_to_east(rock_map)
    return rock_map    

rock_map = make_a_cycle(rock_map)
rock_map = make_a_cycle(rock_map)

rock_map_v2 = make_a_cycle(rock_map_v2)
counter = 2

while rock_map != rock_map_v2:
    rock_map = make_a_cycle(rock_map)
    counter += 1
    print(counter)

print(counter)


def calculate_weight():
    total_weight = 0
    row_weight = len(rock_map)

    for row in rock_map:
        total_weight += row.count("O") * row_weight
        row_weight -= 1
    print(total_weight)

# calculate_weight()