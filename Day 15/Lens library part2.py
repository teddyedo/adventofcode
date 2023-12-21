boxes = {key: [] for key in range(256)}

def calculate_focus_power(box_id, position, focal_length):
    return (box_id+1) * (position + 1) * focal_length
    

def calculate_hash(text):
    value = 0

    for ch in text:
        value += ord(ch)
        value *= 17
        value %= 256

    return value


def elaborate_sequence(sequence):
    label = ""
    
    if "=" in sequence:
        box_to_operate = calculate_hash(sequence[:sequence.find("=")])
        label = sequence.split("=")[0]
        focal_length = int(sequence.split("=")[1])
        for i in range(len(boxes[box_to_operate])):
            if label == boxes[box_to_operate][i][0]:
                boxes[box_to_operate][i] = (label, focal_length)
                return
        boxes[box_to_operate].append((label, focal_length))
    else:
        box_to_operate = calculate_hash(sequence[:sequence.find("-")])
        label = sequence.split("-")[0]
        for i in range(len(boxes[box_to_operate])):
            if label == boxes[box_to_operate][i][0]:
                boxes[box_to_operate].remove((label, boxes[box_to_operate][i][1]))
                break

init_sequence = []

with open("input.txt") as file:
    init_sequence = file.read().split(",")
    for i in range(len(init_sequence)):
        elaborate_sequence(init_sequence[i])
    
    total_focusing_power = 0
    
    for box_id in range(len(boxes)):
        for lens_id, lens in enumerate(boxes[box_id]):
            total_focusing_power += calculate_focus_power(box_id, lens_id, lens[1])
            
print(total_focusing_power)