import re

def extractInstructions(input):
    # Regular expression pattern to match mul(x, y)
    pattern = r"mul\((\d+),\s*(\d+)\)"

    # Find all matches
    matches = re.findall(pattern, input)

    # Display the matches
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
        # print(f"Full match: mul({match[0]}, {match[1]}) - x: {match[0]}, y: {match[1]}")

    return result 

with open('input.txt', 'r') as file:
    result = 0
    for line in file:
        result += extractInstructions(line)


    print(result)
    