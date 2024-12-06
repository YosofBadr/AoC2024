listOne = []
listTwo = []



with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace('   ', ' ')
        
        split = line.split(" ", 1)
        
        listOne.append(int(split[0]))
        listTwo.append(int(split[1]))

listOne.sort()
listTwo.sort()

result = 0
for valueOne, valueTwo in zip(listOne, listTwo):
    result += abs(valueOne - valueTwo)        

print(result)