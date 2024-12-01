def count_arrangements(spring_map, spring_groups):
    if spring_map == "":
        return 1 if spring_groups == () else 0

    if spring_groups == ():
        return 0 if "#" in spring_map else 1

    result = 0

    if spring_map[0] in ".?":
        result += count_arrangements(spring_map[1:], spring_groups)

    if spring_map[0] in "#?":
        if spring_groups[0] <= len(spring_map) and "." not in spring_map[:spring_groups[0]] and (spring_groups[0] == len(spring_map) or spring_map[spring_groups[0]] != "#"):
            result += count_arrangements(spring_map[spring_groups[0] + 1:], spring_groups[1:])

    return result


total = 0

for line in open("input.txt"):
    spring_map, spring_groups = line.split()
    spring_groups = tuple(map(int, spring_groups.split(",")))
    total += count_arrangements(spring_map, spring_groups)

print(total)
