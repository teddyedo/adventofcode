def read_universe():
    universe = []
    galaxy_id = 1
    with open("input.txt") as file:
        for line in file:
            universe.append(list(line.strip()))
            if not "#" in line:
                universe.append(list(line.strip()))
    
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                universe[i][j] = str(galaxy_id)
                galaxy_id += 1
    
    empty_column = []
    
    for i in range(len(universe[0])):
        is_empty = True
        for row in universe:
            if row[i] != ".":
                is_empty = False
                break
        if is_empty:
            empty_column.append(i)
    for i in range(len(empty_column)):
        for j in range(len(universe)):
            universe[j].insert(empty_column[i] + i, ".")
            
    return universe

def save_galaxy_coords(universe):
    galaxy_coords = {}
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] != ".":
                galaxy_coords[universe[i][j]] = (i, j)
    return galaxy_coords
    
def calculate_paths(galaxy_coords):
    paths = {}
    for i in galaxy_coords:
        for j in galaxy_coords:
            if i != j and (i, j) not in paths and (j, i) not in paths:
                paths[(i, j)] = abs(galaxy_coords[i][0] - galaxy_coords[j][0]) + abs(galaxy_coords[i][1] - galaxy_coords[j][1])
    return paths

universe = read_universe()
galaxy_coords = save_galaxy_coords(universe)
paths = calculate_paths(galaxy_coords)

print(sum(paths.values()))

# with open('matrice.txt', 'w') as file:
#     for riga in universe:
#         file.write(''.join(riga) + '\n')
