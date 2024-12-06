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

        if diff > 3:
            return False

        if isIncreasing and leftValue >= rightValue:
            return False
        elif not isIncreasing and leftValue <= rightValue: 
            return False

        leftIndex += 1
        rightIndex += 1    

    return True 
    
def isSafe(report):
    if safetyCheck(report):
        return True
    else:
        for i in range(len(report)):
            newReport = report[:i] + report[i + 1:]
            if safetyCheck(newReport):
                return True

        return False

safeReports = 0
with open('input.txt', 'r') as file:
    safeReports = 0
    for report in file:
        report = report.strip()
        report = report.split(" ")

        if isSafe(report):
            safeReports += 1
        
    print(safeReports)
    