seeds_with_range = [1514493331, 295250933, 3793791524, 105394212, 828589016, 654882197, 658370118, 49359719, 4055197159, 59237418, 314462259, 268880047, 2249227634, 74967914, 2370414906, 38444198, 3291001718, 85800943, 2102534948, 5923540]
steps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
         "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]

def find_next_number(number, filename):
    with open(f'{filename}.txt', 'r') as file:
        for line in file:
            info = line.split()
            destination = info[0]
            source = info[1]
            intervallo = info[2]
            if number >= int(source) and number <= int(source) + int(intervallo): #Verificare se il compare fatto così è corretto
                return int(destination) + (number - int(source))
        return number
    
    
def get_locations():
    counter = 0
    for i in range(0, len(seeds_with_range), 2):
        min_location = None
        for j in range(seeds_with_range[i], seeds_with_range[i] + seeds_with_range[i+1]):
            counter = counter + 1
            location = j
            for step in steps:
                location = find_next_number(location, step)
            if (min_location == None or min_location > location):
                min_location = location
            if(counter % 100000 == 0):
                print(counter)
        print(min_location)


get_locations()