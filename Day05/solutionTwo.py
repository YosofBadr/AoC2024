import sys

def breaksRules(update, index, rules):
    if update not in rules:
        return False

    for rule in rules[update]:
        if rule in updates and index < updates.index(rule):
            return True
            
    return False

def checkUpdates(updates, rules):
    for index, update in enumerate(updates):
        if breaksRules(update, index, rules):
            return False
    return True

def fixUpdates(updates, rules):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(updates)):
            currIndex = i

            while currIndex < len(updates) and breaksRules(updates[currIndex], currIndex, rules):
                updates[currIndex], updates[currIndex + 1] = updates[currIndex + 1], updates[currIndex]
                isSorted = False
                currIndex += 1
                
    return updates

rulesFile = sys.argv[2]
rulesHash = {}
with open(rulesFile, 'r') as file:
    for line in file:
        line = line.strip()
        rule = line.split("|")

        if rule[1] in rulesHash:
            rulesHash[rule[1]].append(rule[0])
        else:
            rulesHash[rule[1]] = [rule[0]] 

# for rule in rulesHash:
#     print(rule, rulesHash[rule])

updateFile = sys.argv[1]
result = 0
with open(updateFile, 'r') as file:
    for line in file:
        line = line.strip()
        updates = line.split(",")
        if not checkUpdates(updates, rulesHash):
            updatesCopy = updates.copy()
            fixedUpdates = fixUpdates(updates, rulesHash)
            if not checkUpdates(fixedUpdates, rulesHash):
                print("Error: ", updatesCopy, fixedUpdates)
            result += int(fixedUpdates[len(fixedUpdates) // 2])
    
print(result)


