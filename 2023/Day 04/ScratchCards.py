total_win = 0
from collections import Counter
import math

with open('input.txt', 'r') as file:
    for line in file:
        line = line[10:].strip()
        numbers = line.split("|")
        winning_numbers = numbers[0].split()
        my_numbers = numbers[1].split()
        count_matches = Counter(my_numbers)
        conteggio_comune = {numero: min(count_matches[numero], winning_numbers.count(
            numero)) for numero in count_matches}
        somma_valori = sum(conteggio_comune.values())
        
        if somma_valori > 0:
            total_win += math.ceil(pow(2, somma_valori - 1))
        # print(math.ceil(pow(2, somma_valori - 1)))

        # matches = winning_numbers.intersection(my_numbers)
        # print(matches)
        # total_win += pow(2, len(matches) - 1)
        # print(pow(2, len(matches) - 1))
        
print(total_win)