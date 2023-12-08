instructions = "LRRLRRRLLRRRLRRRLLRRLRRRLRRLRRLRLRLRLRLRLLRRRLRRLRLRRRLRRRLRLRRRLRLRRLRRRLRRRLRLLRRRLRLLLRLRRRLRLRRLRRLLLLRRLRRLRLRLRRLRLRRLRRRLRRRLRLRLRRLLLLRRLRLRRLLRRRLRLRLRLRRRLRLLLRLRLRRRLRLRRRLRRRLRRRLLRRLRRRLRRRLRRRLRRRLRLLRRRLRLRRRLRLRLRRRLRRLRRLLRRRLRRRLRRRLRLRLRLRRLRRRLRRLRLRLRLRRRR"

node_map = {}
steps = 0
current_key = "AAA"
final_key = "ZZZ"

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        node_map[line.split("=")[0].strip()] = {"L": line.split("=")[1].split(",")[0].strip().removeprefix("("), "R": line.split("=")[1].split(",")[1].strip().removesuffix(")")}
        
while current_key != final_key:
    if instructions[steps % len(instructions)] == "L":
        current_key = node_map[current_key]["L"]
    else:
        current_key = node_map[current_key]["R"]
    steps += 1
    
print(steps)