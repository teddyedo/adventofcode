def read_universe():
    universe = []
    galaxy_id = 1
    
    with open("input.txt") as file:
        counter = 0
        for line in file:
            universe.append(list(line.strip()))
            if not "#" in line:
                empty_rows.append(counter)
            counter += 1
            
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                universe[i][j] = str(galaxy_id)
                galaxy_id += 1
    
    
    for i in range(len(universe[0])):
        is_empty = True
        for row in universe:
            if row[i] != ".":
                is_empty = False
                break
        if is_empty:
            empty_columns.append(i)
            
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
                y1 = galaxy_coords[i][0] + 999999 * sum(1 for x in empty_rows if x < galaxy_coords[i][0])
                x1 = galaxy_coords[i][1] + 999999 * sum(1 for x in empty_columns if x < galaxy_coords[i][1])
                y2 = galaxy_coords[j][0] + 999999 * sum(1 for x in empty_rows if x < galaxy_coords[j][0])
                x2 = galaxy_coords[j][1] + 999999 * sum(1 for x in empty_columns if x < galaxy_coords[j][1])
                paths[(i, j)] = abs(x1 - x2) + abs(y1 - y2)

    return paths

empty_rows = []
empty_columns = []
universe = read_universe()
galaxy_coords = save_galaxy_coords(universe)
paths = calculate_paths(galaxy_coords)

print(sum(paths.values()))

