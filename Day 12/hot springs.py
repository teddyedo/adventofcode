import re

spring_map_combinations = 0

def calculate_spring_combinations(line):
    line = line.strip().split()
    spring_map = line[0]
    spring_occurrences = [int(i) for i in line[1].split(",")]
    spring_combinations = get_all_spring_combinations(spring_map)
    occ_matches = 0
    regex = build_regex(spring_occurrences)
    for combination in spring_combinations:
        if sum(spring_occurrences) == combination.count("#") and  re.search(regex, combination):
            occ_matches += 1
    return occ_matches
    
def get_all_spring_combinations(spring_map):
    
    combs = []
    unknown_springs = spring_map.count("?")
    combs.append(spring_map)
    for i in range(unknown_springs):
        copy_combs = combs.copy()
        for i in range(len(combs)):
            combs[i] = combs[i].replace("?", "#", 1)
        for j in range(len(copy_combs)):
            copy_combs[j] = copy_combs[j].replace("?", ".", 1)
        new_combs = []
        for k in range(len(combs)):
            new_combs.append(combs[k])
            new_combs.append(copy_combs[k])
        combs = new_combs
        
    return combs

def build_regex(spring_occurencies):
    regex = r"\.*"
    for i in range(len(spring_occurencies)):
        if i + 1 != len(spring_occurencies):
            regex += "#" * int(spring_occurencies[i])
            regex += r"\.+"
        else:
            regex += "#" * int(spring_occurencies[i])
    regex += r"\.*"
    
    return regex
    

with open("input.txt") as file:
    for line in file:
        spring_map_combinations += calculate_spring_combinations(line)
    print(spring_map_combinations)
            