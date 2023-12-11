totalNumber = 0

numbers = ["one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]

reversed_numbers = [number[::-1] for number in numbers]


def trovaPrimoNumero(line, numbers):
    digitPosition = None
    digit = None

    # find digit
    for char in line:
        if char.isdigit():
            digitPosition = line.index(char)
            digit = char
            break

    wordPosition = 3000
    wordNumber = None

    # find word
    for word in numbers:
        index = line.find(word)
        if index != -1 and index < wordPosition:
            wordPosition = index
            wordNumber = word
            # print(wordPosition)
            # print(wordNumber)

    if (wordPosition < digitPosition):
        return str(numbers.index(wordNumber) + 1)
    else:
        return digit


with open('input.txt', 'r') as file:
    for line in file:
        firstNumber = trovaPrimoNumero(line, numbers)
        lastNumber = trovaPrimoNumero(line[::-1], reversed_numbers)
        rowNumber = int(firstNumber + lastNumber)
        totalNumber += rowNumber
        print(str(rowNumber) + ": " + line)

print(totalNumber)
