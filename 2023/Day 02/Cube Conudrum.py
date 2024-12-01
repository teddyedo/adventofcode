import re

maxCubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

potenzaTotale = 0


def calcolaPotenzaGioco(rounds):
    maxRed = 1
    maxGreen = 1
    maxBlue = 1

    for draw in rounds:
        if "red" in draw:
            value = int(draw.split()[0])
            if (value > maxRed):
                maxRed = value
        if "green" in draw:
            value = int(draw.split()[0])
            if (value > maxGreen):
                maxGreen = value
        if "blue" in draw:
            value = int(draw.split()[0])
            if (value > maxBlue):
                maxBlue = value

    return maxRed * maxGreen * maxBlue


with open('input.txt', 'r') as file:
    for riga in file:
        gameIndex = int(riga[5: riga.find(":")])
        riga = riga[riga.find(":") + 1:]
        rounds = [element.strip() for element in re.split(';|,', riga)]
        potenzaGioco = calcolaPotenzaGioco(rounds)
        print(str(gameIndex) + ": " + str(potenzaGioco))
        potenzaTotale += potenzaGioco

print(potenzaTotale)
