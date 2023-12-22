accepted_parts = []
total_ratings = 0

def flow(part, wf_id):
    
    if wf_id == "A":
        accepted_parts.append(part)
        return
    elif wf_id == "R":
        return
    
    rules = wfs[wf_id]
    for rule in rules:
        if rule == "A":
            accepted_parts.append(part)
            break
        elif rule == "R":
            break
        elif ":" not in rule:
            flow(part, rule)
            break
        else:
            condition, next_flow = rule.split(":")
            if ">" in condition:
                if part[condition.split(">")[0]] > int(condition.split(">")[1]):
                    flow(part, next_flow)
                    break
            else:
                if part[condition.split("<")[0]] < int(condition.split("<")[1]):
                    flow(part, next_flow)
                    break
    
with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    
wfs = {line.split("{")[0] : line.split("{")[1].strip("}").split(",") for line in lines[:lines.index("")]}
parts = [
    {pair.split("=")[0]: int(pair.split("=")[1])
     for pair in part.strip("{}").split(",")}
    for part in lines[lines.index("") + 1:]
]

for part in parts:
    flow(part, "in")

total_ratings = sum(sum(part.values()) for part in accepted_parts)
print(total_ratings)