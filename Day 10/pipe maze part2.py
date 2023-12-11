maze = []


def find_starting_coords():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return i, j


def find_next_coords(previous_coords, current_coords, direction):
    curr_x, curr_y = current_coords
    prev_x, prev_y = previous_coords

    if direction == "|":
        return (curr_x - 1, curr_y) if prev_x > curr_x else (curr_x + 1, curr_y)
    elif direction == "-":
        return (curr_x, curr_y - 1) if prev_y > curr_y else (curr_x, curr_y + 1)
    elif direction == "L":
        return (curr_x, curr_y + 1) if prev_x < curr_x else (curr_x - 1, curr_y)
    elif direction == "J":
        return (curr_x, curr_y - 1) if prev_x < curr_x else (curr_x - 1, curr_y)
    elif direction == "F":
        return (curr_x, curr_y + 1) if prev_x > curr_x else (curr_x + 1, curr_y)
    elif direction == "7":
        return (curr_x, curr_y - 1) if prev_x > curr_x else (curr_x + 1, curr_y)
    elif direction == "S":
        if maze[curr_x][curr_y - 1] in ("-", "L", "F"):
            return (curr_x, curr_y - 1)
        elif maze[curr_x][curr_y + 1] in ("-", "J", "7"):
            return (curr_x, curr_y + 1)
        elif maze[curr_x - 1][curr_y] in ("|", "F", "7"):
            return (curr_x - 1, curr_y)
        elif maze[curr_x + 1][curr_y] in ("|", "J", "L"):
            return (curr_x + 1, curr_y)




def walk_through_maze():
    steps = 0
    coords_list = []
    coords_list.append(find_starting_coords())
    current_coords = find_next_coords(find_starting_coords(),
                                      find_starting_coords(), "S")
    maze_solved[current_coords[0]][current_coords[1]] = maze[current_coords[0]][
        current_coords[1]]
    
    coords_list.append(current_coords)
    steps += 1
    while maze[current_coords[0]][current_coords[1]] != "S":
        current_coords = find_next_coords(coords_list[steps - 1],
                                          coords_list[steps - 0],
                                          maze[current_coords[0]][
                                              current_coords[1]])
        maze_solved[current_coords[0]][current_coords[1]] = maze[current_coords[0]][
            current_coords[1]]
        coords_list.append(current_coords)
        steps += 1

def is_inside_maze(coords):
    right_walls = 0
    for j in range(coords[1] + 1, len(maze_solved[coords[0]])):
        if maze_solved[coords[0]][j] == "|":
            right_walls += 1
        elif maze_solved[coords[0]][j] == "L":
            while maze_solved[coords[0]][j+1] in ("-"):
                j+=1
            if maze_solved[coords[0]][j+1] == "7":
                j+=1
                right_walls += 1
        elif maze_solved[coords[0]][j] == "F":
            while maze_solved[coords[0]][j+1] in ("-"):
                j += 1
            if maze_solved[coords[0]][j+1] == "J":
                j += 1
                right_walls += 1

                
    return right_walls % 2 != 0

with open("input.txt") as file:
    for line in file:
        maze.append(list(line.strip()))
        

maze_solved = [['.' for _ in range(len(maze[0]))] for _ in range(len(maze))]
walk_through_maze()

tiles_inside_maze = 0

for i in range(len(maze_solved)):
    for j in range(len(maze_solved[i])):
        if maze_solved[i][j] == "." and is_inside_maze((i, j)):
            print("Tile inside maze:", (i, j))
            maze_solved[i][j] = "#"
            tiles_inside_maze += 1

with open('matrice.txt', 'w') as file:
    for riga in maze_solved:
        file.write(''.join(riga) + '\n')

print(tiles_inside_maze)