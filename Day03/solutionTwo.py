import re

def extractInstructions(input):
    # Regular expression pattern to match mul(x, y)
    pattern = r"mul\((\d+),\s*(\d+)\)|(do\(\))|(don't\(\))"

    # Find all matches
    matches = re.findall(pattern, input)

    isEnabled = True

    # Display the matches
    result = 0
    for match in matches:
        if match[0] and isEnabled:
            print(match)
            result += int(match[0]) * int(match[1])
        elif match[2]:
            print(match[2])
            isEnabled = True
        elif match[3]:
            isEnabled = False

        # print(f"Full match: mul({match[0]}, {match[1]}) - x: {match[0]}, y: {match[1]}")

    return result 

with open('input.txt', 'r') as file:
    input = file.read()
    
result = extractInstructions(input)


print(result)
    