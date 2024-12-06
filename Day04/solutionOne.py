import sys

def search(string, row, col, rowCount, colCount):
    # Explore words of length 4 in all directions
        # Left, Right, Top, Bottom and Diagonals

    targetString = "MAS"
    matchCount = 0 
   
    # Explore Left
    for i in range(1, 4):
        newCol = col - i
        if newCol >= 0:
            index = row * rowCount + newCol 
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break


    # Explore Right
    for i in range(1, 4):
        newCol = col + i
        if newCol < colCount:
            index = row * rowCount + newCol
            if string[index] == targetString[i - 1]:
                if i == 3:
                    
                    matchCount += 1
                continue
            break
        else:
            break


    # Explore Top
    for i in range(1, 4):
        newRow = row - i
        if newRow >= 0:
            index = newRow * rowCount + col
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break

    # Explore Bottom
    for i in range(1, 4):
        newRow = row + i
        if newRow < rowCount:
            index = newRow * rowCount + col
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break

    # Explore Right Top Diagonal
    for i in range(1, 4):
        newRow = row - i
        newCol = col + i
        if newRow >= 0 and newCol < colCount:
            index = newRow * rowCount + newCol
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break
    
    # Explore Left Top Diagonal
    for i in range(1, 4):
        newRow = row - i
        newCol = col - i
        if newRow >= 0 and newCol >= 0:
            index = newRow * rowCount + newCol
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break

    # Explore Right Bottom Diagonal
    for i in range(1, 4):
        newRow = row + i
        newCol = col + i
        if newRow < rowCount and newCol < colCount:
            index = newRow * rowCount + newCol
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break

    # Explore Left Bottom Diagonal
    for i in range(1, 4):
        newRow = row + i
        newCol = col - i
        if newRow < rowCount and newCol >= 0:
            index = newRow * rowCount + newCol
            if string[index] == targetString[i - 1]:
                if i == 3:
                    matchCount += 1
                continue
            break
        else:
            break

    return matchCount



inputFile = sys.argv[1]
with open(inputFile, 'r') as file:
    input = file.read()
    input = input.replace('\n', '')

count = 0

rowCount = 140
colCount = 140

for row in range(rowCount):
    for col in range(colCount):
        stringIndex = row * rowCount + col  
        if input[stringIndex] == "X":
            count += search(input, row, col, rowCount, colCount) 

print(count)



