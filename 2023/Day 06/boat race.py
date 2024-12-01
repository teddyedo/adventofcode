from functools import reduce

times = [48, 93, 85, 95]
distances = [296, 1928, 1236, 1391]


total_combinations = []


def calculate_combinations(time, distance):
    combinations = 0
    for i in range(time):
        speed = i
        time_remaining = time - i
        max_distance = time_remaining * speed
        if max_distance > distance:
            combinations += 1
    return combinations


for i in range(len(times)):
    total_combinations.append(calculate_combinations(times[i], distances[i]))

print(reduce(lambda x, y: x * y, total_combinations))
