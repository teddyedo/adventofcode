

def calculate_differences(numbers):
    differences = []
    for i in range(len(numbers) - 1):
        differences.append(numbers[i + 1] - numbers[i])
    return differences

def calculate_next_history(numbers):
    next_history = 0
    for i in range(len(numbers)):
        if(i % 2 == 0):
            next_history += numbers[i][0]
        else:
            next_history -= numbers[i][0]
    return next_history        

def find_next_history(numbers):
    current_numbers = numbers
    numbers = [numbers]
    while any(elemento != 0 for elemento in current_numbers):
        current_numbers = calculate_differences(current_numbers)
        numbers.append(current_numbers)
    return calculate_next_history(numbers)

total_history = 0

with open("input.txt") as file:
    for line in file:
        total_history += find_next_history([int(value) for value in line.split()])
    print(total_history)