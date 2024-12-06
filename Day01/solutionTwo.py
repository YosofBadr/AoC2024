listOne = []

locationIDs = {}

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace('   ', ' ')
        
        split = line.split(" ", 1)

        value = int(split[1])

        listOne.append(int(split[0]))
        
        if value in locationIDs:
            locationIDs[value] += 1
        else:
            locationIDs[value] = 1

result = 0    
for value in listOne:
    if value in locationIDs:
        result += value * locationIDs[value]


print(result)