
from itertools import permutations


spring_map_combinations = 0

def calculate_spring_combinations(line):
    # line = line.strip().split()
    spring_map = [x for x in line[0].split(".") if x != ""]
    spring_occurrences = line[1].split(",")
    # combs = combinations([".", "#"], line.count("?"))
    # print(line)
    # print(combs)


    return 1

with open("input.txt") as file:
    for line in file:
        spring_map_combinations += calculate_spring_combinations(line)
    print(spring_map_combinations)
        


elements = [1, 2, 3, 4]

    # Iterate through combinations of length 2
for combo in permutations(elements, 3):
    print(combo)
    