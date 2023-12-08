instructions = "LRRLRRRLLRRRLRRRLLRRLRRRLRRLRRLRLRLRLRLRLLRRRLRRLRLRRRLRRRLRLRRRLRLRRLRRRLRRRLRLLRRRLRLLLRLRRRLRLRRLRRLLLLRRLRRLRLRLRRLRLRRLRRRLRRRLRLRLRRLLLLRRLRLRRLLRRRLRLRLRLRRRLRLLLRLRLRRRLRLRRRLRRRLRRRLLRRLRRRLRRRLRRRLRRRLRLLRRRLRLRRRLRLRLRRRLRRLRRLLRRRLRRRLRRRLRLRLRLRRLRRRLRRLRLRLRLRRRR"

node_map = {}
steps = 0
current_keys = []
final_keys = []

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        node_map[line.split("=")[0].strip()] = {"L": line.split("=")[1].split(",")[0].strip().removeprefix("("), "R": line.split("=")[1].split(",")[1].strip().removesuffix(")")}
        
for key in node_map.keys():
    if key.endswith("A"):
        current_keys.append(key)
    if key.endswith("Z"):
        final_keys.append(key)
        
# print(current_keys)
# print(final_keys)        
        
while current_keys != final_keys:
    for i in range(len(current_keys)):
        if instructions[steps % len(instructions)] == "L":
            current_keys[i] = node_map[current_keys[i]]["L"]
        else:
            current_keys[i] = node_map[current_keys[i]]["R"]
    steps += 1
    print(current_keys)
        
print(steps)