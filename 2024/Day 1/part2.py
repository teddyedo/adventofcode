left = []
right = {}
with open('input.txt') as f:
    for line in f:
        left.append(int(line.split()[0]))
        if int(line.split()[1]) not in right:
            right[int(line.split()[1])] = 1
        else:
            right[int(line.split()[1])] = right[int(line.split()[1])] + 1

    similarity_score = 0
    for n in left:
        if n in right:
            similarity_score += n * right[n]

    print(similarity_score)
