import sys

def checkUpdates(updates, rules):
    for index, update in enumerate(updates):
        if update not in rules:
            continue
        
        for rule in rules[update]:
            if rule in updates and index > updates.index(rule):
                return False
    return True


rulesFile = sys.argv[2]

rulesHash = {}
with open(rulesFile, 'r') as file:
    for line in file:
        line = line.strip()
        rule = line.split("|")

        if rule[0] in rulesHash:
            rulesHash[rule[0]].append(rule[1])
        else:
            rulesHash[rule[0]] = [rule[1]] 


updateFile = sys.argv[1]
result = 0
with open(updateFile, 'r') as file:
    for line in file:
        line = line.strip()
        update = line.split(",")
        if checkUpdates(update, rulesHash):
            result += int(update[len(update) // 2])

print(result)