def calculate_hash(text, current_value):
    ascii_code = ord(text)
    current_value += ascii_code
    current_value *= 17
    current_value = current_value % 256
    return current_value


total_value = 0

with open("input.txt") as file:
    init_sequence = file.read().split(",")
    current_value = 0
    for step in init_sequence:
        for char in step:
            current_value = calculate_hash(char, current_value)
        print(current_value)
        total_value += current_value
        current_value = 0
    print(total_value)
    
