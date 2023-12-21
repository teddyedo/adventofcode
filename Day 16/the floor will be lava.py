def calculate_next_step(coords, direction):
    if direction == "LEFT":
        return (coords[0] - 1, coords[1])
    elif direction == "RIGHT":
        return (coords[0] + 1, coords[1])
    elif direction == "UP":
        return (coords[0], coords[1] - 1)
    elif direction == "DOWN":
        return (coords[0], coords[1] + 1)

def is_valid_step(step, direction):
    return step[0] >= 0 and step[1] >= 0 and step[0] < len(contraption[0]) and step[1] < len(contraption) and (step, direction) not in move_made

def make_a_step(coords, direction):
    next_step = calculate_next_step(coords, direction)
    if is_valid_step(next_step, direction):
        light_map[next_step[1]][next_step[0]] = "#"
        move_made.append((next_step, direction)) # (step, direction)
        if contraption[next_step[1]][next_step[0]] in "\\/|-":
            if contraption[next_step[1]][next_step[0]] == "/":
                if direction == "UP":
                    make_a_step(next_step, "RIGHT")
                elif direction == "RIGHT":
                    make_a_step(next_step, "UP")
                elif direction == "DOWN":
                    make_a_step(next_step, "LEFT")
                elif direction == "LEFT":
                    make_a_step(next_step, "DOWN")
            elif contraption[next_step[1]][next_step[0]] == "\\":
                if direction == "UP":
                    make_a_step(next_step, "LEFT")
                elif direction == "LEFT":
                    make_a_step(next_step, "UP")
                elif direction == "DOWN":
                    make_a_step(next_step, "RIGHT")
                elif direction == "RIGHT":
                    make_a_step(next_step, "DOWN")
            elif contraption[next_step[1]][next_step[0]] == "|":
                if direction == "LEFT" or direction == "RIGHT":
                    make_a_step(next_step, "UP")
                    make_a_step(next_step, "DOWN")
                else:
                    make_a_step(next_step, direction)
            elif contraption[next_step[1]][next_step[0]] == "-":
                if direction == "UP" or direction == "DOWN":
                    make_a_step(next_step, "LEFT")
                    make_a_step(next_step, "RIGHT")
                else:
                    make_a_step(next_step, direction)
        else:
            make_a_step(next_step, direction)


contraption = []
light_map = []
move_made = []
energized_tiles = 0

with open("input.txt") as file:
    for row in file:
        contraption.append(list(row.strip()))

light_map = [["." for _ in range(len(contraption[0]))] for _ in range(len(contraption))]

start_coords = (-1, 0)

make_a_step(start_coords, "RIGHT")

for row in light_map:
    energized_tiles += row.count("#")
print(energized_tiles)