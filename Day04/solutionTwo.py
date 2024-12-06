import sys

def search(string, row, col, rowCount, colCount):
    targetString = "MS"
    matchCount = 0 


    rightDiagonal = False
    leftDiagonal = False

    if row + 1 < rowCount and row - 1 >= 0 and col - 1 >= 0 and col + 1 < colCount:
        bottomLeft = string[(row + 1) * rowCount + col - 1]
        topRight = string[(row - 1) * rowCount + col + 1]
        topLeft = string[(row - 1) * rowCount + col - 1]
        bottomRight = string[(row + 1) * rowCount + col + 1]

        print(bottomLeft, topRight, topLeft, bottomRight)
        rightDiagonal = bottomLeft in targetString and topRight in targetString and topRight != bottomLeft
        leftDiagonal = topLeft in targetString and bottomRight in targetString and bottomRight != topLeft

    if leftDiagonal and rightDiagonal:
        return 1
    
    return 0

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
        if input[stringIndex] == "A":
            count += search(input, row, col, rowCount, colCount) 

print(count)
