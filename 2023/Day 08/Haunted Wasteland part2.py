instructions = "LRRLRRRLLRRRLRRRLLRRLRRRLRRLRRLRLRLRLRLRLLRRRLRRLRLRRRLRRRLRLRRRLRLRRLRRRLRRRLRLLRRRLRLLLRLRRRLRLRRLRRLLLLRRLRRLRLRLRRLRLRRLRRRLRRRLRLRLRRLLLLRRLRLRRLLRRRLRLRLRLRRRLRLLLRLRLRRRLRLRRRLRRRLRRRLLRRLRRRLRRRLRRRLRRRLRLLRRRLRLRRRLRLRLRRRLRRLRRLLRRRLRRRLRRRLRLRLRLRRLRRRLRRLRLRLRLRRRR"

node_map = {}
current_keys = []
final_keys = []
total_steps = []


def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(numeri):
    risultato = numeri[0]
    for num in numeri[1:]:
        mcm_ab = risultato * num // mcd(risultato, num)
        risultato = mcm_ab

    return risultato
    

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        node_map[line.split("=")[0].strip()] = {"L": line.split("=")[1].split(",")[0].strip().removeprefix("("), "R": line.split("=")[1].split(",")[1].strip().removesuffix(")")}
        
for key in node_map.keys():
    if key.endswith("A"):
        current_keys.append(key)
    if key.endswith("Z"):
        final_keys.append(key)
      
for i in range(len(current_keys)):
    current_key = current_keys[i]
    steps = 0
    while current_key not in final_keys:
        if instructions[steps % len(instructions)] == "L":
            current_key = node_map[current_key]["L"]
        else:
            current_key = node_map[current_key]["R"]
        steps += 1
    final_keys.remove(current_key)
    total_steps.append(steps)

print(mcm(total_steps))