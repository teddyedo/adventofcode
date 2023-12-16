boxes = {key: [] for key in range(256)}

def calculate_hash(text, current_value):
    ascii_code = ord(text)
    current_value += ascii_code
    current_value *= 17
    current_value = current_value % 256
    return current_value

def calculate_box(sequence):
    box_id = 0
    for char in sequence:
        box_id = calculate_hash(box_id)
    return box_id 

def elaborate_sequence(sequence):
    operation = ""
    label = ""
    lens_value = 0
    box_to_operate = calculate_box(sequence)
    
    if "=" in sequence:
        operation = "="
        label = sequence.split("=")[0]
        focal_length = int(sequence.split("=")[1])
        if label in boxes[box_to_operate]:
            
    else:
        operation = "-"
        label = sequence.split("-")[0]
        if label in boxes[box_to_operate]:
            boxes[box_to_operate].remove(label)

    
    print(label, operation)

init_sequence = []

with open("input.txt") as file:
    init_sequence = file.read().split(",")
    for i in range(10):
        elaborate_sequence(init_sequence[i])