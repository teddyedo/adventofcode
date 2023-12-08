time = 48938595
distance = 296192812361391


total_combinations = 0


def calculate_combinations(time, distance):
    combinations = 0
    for i in range(time):
        speed = i
        time_remaining = time - i
        max_distance = time_remaining * speed
        if max_distance > distance:
            combinations += 1
    return combinations


print(calculate_combinations(time, distance))
