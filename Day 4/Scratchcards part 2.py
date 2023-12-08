from collections import Counter
import math
occorrenze_gratta_e_vinci = {chiave: 1 for chiave in range(1, 26)}

def calcola_numero_matches(line):
    line = line[10:].strip()
    numbers = line.split("|")
    winning_numbers = numbers[0].split()
    my_numbers = numbers[1].split()
    count_matches = Counter(my_numbers)
    conteggio_comune = {numero: min(count_matches[numero], winning_numbers.count(
        numero)) for numero in count_matches}
    
    return sum(conteggio_comune.values())


with open('input 2.txt', 'r') as file:
    for line in file:
        rowNumber = int(line[5:8])
        print(rowNumber)
        gratta_e_vinci_aperti = 0
        while gratta_e_vinci_aperti < occorrenze_gratta_e_vinci[rowNumber]:
            carte_vinte = calcola_numero_matches(line)
            indice_gratta_e_vinci_vinto = rowNumber + 1
            # print("Row: "  + str(rowNumber) + " carte vinte: " + str(carte_vinte))
            for i in range(carte_vinte):
                if(indice_gratta_e_vinci_vinto <= 25):
                    occorrenze_gratta_e_vinci[indice_gratta_e_vinci_vinto] = occorrenze_gratta_e_vinci.get(
                        indice_gratta_e_vinci_vinto, 0) + 1
                    indice_gratta_e_vinci_vinto += 1
            gratta_e_vinci_aperti += 1
            
print(sum(occorrenze_gratta_e_vinci.values()))
print(occorrenze_gratta_e_vinci)
