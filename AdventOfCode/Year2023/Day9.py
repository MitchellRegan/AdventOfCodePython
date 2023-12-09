#https://adventofcode.com/2023/day/9
#https://adventofcode.com/2023/day/9#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d9_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d9_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.replace('\n', '').split(' ')
            for i in range(0, len(line)):
                line[i] = int(line[i])
            input.append(line)
            lineNum += 1

    return input


def solution1():
    input = getInput()
    sum = 0
    
    for row in input:
        steps = [row]
        while True:
            curStep = steps[-1]
            nextStep = []
            allZero = True
            for i in range(0, len(curStep)-1):
                newNum = curStep[i+1] - curStep[i]
                if newNum != 0:
                    allZero = False
                nextStep.append(newNum)

            steps.append(nextStep)

            if allZero:
                break

        #Adding new numbers on the end
        steps[-1].append(0)
        for i in range(len(steps)-2, -1, -1):
            newNum = steps[i+1][-1] + steps[i][-1]
            steps[i].append(newNum)
            
        sum += steps[0][-1]
    return sum


def solution2():
    input = getInput()
    sum = 0
    
    for row in input:
        steps = [row]
        while True:
            curStep = steps[-1]
            nextStep = []
            allZero = True
            for i in range(0, len(curStep)-1):
                newNum = curStep[i+1] - curStep[i]
                if newNum != 0:
                    allZero = False
                nextStep.append(newNum)

            steps.append(nextStep)

            if allZero:
                break

        #adding new numbers to the beginning
        steps[-1].append(0)
        for i in range(len(steps)-2, -1, -1):
            newNum = steps[i][0] - steps[i+1][0]
            steps[i].insert(0,newNum)
            
        sum += steps[0][0]
    return sum


print("Year 2023, Day 9 solution part 1:", solution1())
print("Year 2023, Day 9 solution part 2:", solution2())