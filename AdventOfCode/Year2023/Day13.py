#https://adventofcode.com/2023/day/13
#https://adventofcode.com/2023/day/13#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d13_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d13_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        group = []

        for line in f:
            if line == '\n':
                input.append(group)
                group = []
            else:
                if line[-1] == '\n':
                    line = line[:-1]
                group.append(line)
        if len(group) > 0:
            input.append(group)

    return input


def checkReflectionVertical(group:list)->int:
    newGroup = []
    for c in range(0, len(group[0])):
        line = ''
        for r in range(0, len(group)):
            line = line + group[r][c]
        newGroup.append(line)

    return checkReflectionHorizontal(newGroup) //100


def checkReflectionHorizontal(group:list)->int:
    for startInd in range(0, len(group)-1):
        if group[startInd] == group[startInd+1]:
            left = startInd - 1
            right = startInd + 2
            isReflection = True

            while left > -1 and right < len(group):
                if group[left] != group[right]:
                    isReflection = False
                    break
                left -= 1
                right += 1

            if isReflection:
                return (startInd + 1) * 100
    return 0


def horizontalCheck_v2(group:list)->int:
    for startInd in range(0, len(group)-1):
        left = startInd
        right = startInd + 1
        numDifferences = 0

        while left > -1 and right < len(group):
            for c in range(0, len(group[0])):
                if group[left][c] != group[right][c]:
                    numDifferences += 1
                    if numDifferences > 1:
                        left = -1
                        break
            left -= 1
            right += 1

        if numDifferences == 1:
            return (startInd + 1) * 100
    return 0


def solution1():
    input = getInput()
    
    total = 0
    for group in input:
        total += checkReflectionHorizontal(group) + checkReflectionVertical(group)

    return total


def solution2():
    input = getInput()
    
    total = 0
    for group in input:
        #Getting the rotated version for vertical check
        rotatedGroup = []
        for c in range(0, len(group[0])):
            line = ''
            for r in range(0, len(group)):
                line = line + group[r][c]
            rotatedGroup.append(line)

        h = horizontalCheck_v2(group)
        v = horizontalCheck_v2(rotatedGroup) // 100

        total += h + v

    return total


print("Year 2023, Day 13 solution part 1:", solution1())
print("Year 2023, Day 13 solution part 2:", solution2())