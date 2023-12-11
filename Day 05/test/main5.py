import sys
from datetime import datetime

starting_seeds = {3291001718, 2102534948}

ranges = {85800943, 5923540}

seed_to_soil = set()
soil_to_fertilizer = set()
fertilizer_to_water = set()
water_to_light = set()
light_to_temperature = set()
temperature_to_humidity = set()
humidity_to_location = set()

locations = []


def popola_matrice(filename, matrix):
    with open(f'{filename}.txt', 'r') as file:
        for line in file:
            info = line.split()
            destination = int(info[0])
            source = int(info[1])
            intervallo = int(info[2])
            matrix.add((destination, source, intervallo))


def find_next_number(number, matrix):
    for line in matrix:
        destination, source, intervallo = line
        if source <= number <= source + intervallo:
            return destination + (number - source)
    return number


def get_locations():
    for seed, seed_range in zip(starting_seeds, ranges):
        counter = 0
        min_location = sys.maxsize
        for j in range(seed, seed + seed_range):
            counter += 1
            location = j
            for matrix in steps:
                location = find_next_number(location, matrix)
            if min_location > location:
                min_location = location
            if counter % 100000 == 0:
                print(f"{datetime.now().time()}: elaborati {counter} elementi")
        locations.append(min_location)


popola_matrice("seed-to-soil", seed_to_soil)
popola_matrice("soil-to-fertilizer", soil_to_fertilizer)
popola_matrice("fertilizer-to-water", fertilizer_to_water)
popola_matrice("water-to-light", water_to_light)
popola_matrice("light-to-temperature", light_to_temperature)
popola_matrice("temperature-to-humidity", temperature_to_humidity)
popola_matrice("humidity-to-location", humidity_to_location)

steps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
         light_to_temperature, temperature_to_humidity, humidity_to_location]

get_locations()

print(locations)
