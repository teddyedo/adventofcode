left = []
right = []
with open('input.txt') as f:
    for line in f:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    left.sort()
    right.sort()
    
    distance = 0
    for i in range(len(left)):
        distance += abs(right[i] - left[i])

    print(distance)
