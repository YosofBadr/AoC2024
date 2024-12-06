def safetyCheck(report):
    if len(report) < 1:
        return True
    
    leftIndex = 0
    rightIndex = 1 

    isIncreasing = False
    if int(report[leftIndex]) < int(report[rightIndex]):
        isIncreasing = True
        
    while rightIndex < len(report):
        leftValue = int(report[leftIndex])
        rightValue = int(report[rightIndex])

        diff = abs(leftValue - rightValue)

        if diff == 0 or diff > 3:
            return False 

        if isIncreasing and leftValue >= rightValue: 
            return False
        elif not isIncreasing and leftValue <= rightValue: 
            print(report[leftIndex] <= report[rightIndex])
            return False 

        leftIndex += 1
        rightIndex += 1    

    return True
    

with open('input.txt', 'r') as file:
    safeReports = 0
    for line in file:
        line = line.strip()
        line = line.split(" ")

        if safetyCheck(line):
            safeReports += 1
        else:
            print(line)

    print(safeReports)
    