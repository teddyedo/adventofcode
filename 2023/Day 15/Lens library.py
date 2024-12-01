def calculate_hash(text):
    value = 0
    
    for char in text:  
        value += ord(char)
        value *= 17
        value %= 256
    
    return value

total_value = 0

with open("input.txt") as file:
    init_sequence = file.read().split(",")
    for step in init_sequence:
        total_value += calculate_hash(step)
    print(total_value)
    
