maze = []
maze_solved = [['.' for _ in range(140)] for _ in range(140)]


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
    coords_list.append(current_coords)
    steps += 1
    while maze[current_coords[0]][current_coords[1]] != "S":
        current_coords = find_next_coords(coords_list[steps - 1],
                                          coords_list[steps - 0],
                                          maze[current_coords[0]][
                                              current_coords[1]])
        maze_solved[current_coords[0]][current_coords[1]] = str(steps)
        coords_list.append(current_coords)
        steps += 1
    print(steps / 2)


with open("input.txt") as file:
    for line in file:
        maze.append(list(line.strip()))

walk_through_maze()
