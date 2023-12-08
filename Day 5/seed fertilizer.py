seeds = [1514493331, 295250933, 3793791524, 105394212, 828589016, 654882197, 658370118, 49359719, 4055197159, 59237418, 314462259, 268880047, 2249227634, 74967914, 2370414906, 38444198, 3291001718, 85800943, 2102534948, 5923540]
steps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"] 

lowest_location = None

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
            

for seed in seeds:
    location = seed
    for step in steps:
        location = find_next_number(location, step)
    print(location)
    