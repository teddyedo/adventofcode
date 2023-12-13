patterns = []

with open("input.txt") as file:
    pattern = []
    for line in file:
        if line.strip() == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())

def get_left_columns(pattern):
    index_first_column = 0
    index_second_column = 1
    is_symmetric = False
    
    while index_second_column < len(pattern[0]):
        first_column = [pattern[x][index_first_column] for x in range(len(pattern))]
        second_column = [pattern[x][index_second_column] for x in range(len(pattern))]
        
        while index_second_column < len(pattern[0]) - 1 and first_column != second_column:
            index_first_column += 1
            index_second_column += 1
            first_column = [pattern[x][index_first_column] for x in range(len(pattern))]
            second_column = [pattern[x][index_second_column] for x in range(len(pattern))]
        
        left_columns = index_first_column + 1
        x1 = index_first_column
        x2 = index_second_column
        
        
        while x1 >= 0 and x2 < len(pattern[0]):
            is_symmetric = True
            first_column = [pattern[x][x1] for x in range(len(pattern))]
            second_column = [pattern[x][x2] for x in range(len(pattern))]
            
            if first_column == second_column:
                x1 -= 1
                x2 += 1
            else:
                is_symmetric = False
                break
            
        if is_symmetric == True:
            break
        else:
            index_first_column += 1
            index_second_column += 1
            
    if is_symmetric == True:
        return left_columns
    else:
        return 0
    
def get_above_rows(pattern):
    index_first_row = 0
    index_second_row = 1
    is_symmetric = False
    
    while index_second_row < len(pattern):
        
        while index_second_row < len(pattern) - 1 and pattern[index_first_row] != pattern[index_second_row]:
            index_first_row += 1
            index_second_row += 1
            
        above_rows = index_first_row + 1
        y1 = index_first_row
        y2 = index_second_row
        
        while y1 >= 0 and y2 < len(pattern):
            is_symmetric = True
            
            if pattern[y1] == pattern[y2]:
                y1 -= 1
                y2 += 1
            else:
                is_symmetric = False
                break
        if is_symmetric == True:
            break
        else:
            index_first_row += 1
            index_second_row += 1

    if is_symmetric == True:
        return above_rows
    else:
        return 0


total_above_rows = 0
total_left_columns = 0

for pattern in patterns:
    total_left_columns += get_left_columns(pattern)
    total_above_rows += get_above_rows(pattern)
    
print(total_above_rows * 100 + total_left_columns)



    