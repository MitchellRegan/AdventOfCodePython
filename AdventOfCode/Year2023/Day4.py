#https://adventofcode.com/2023/day/4
#https://adventofcode.com/2023/day/4#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d4_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d4_real.txt")


def getInput():
    input = []
    with open(inFile, 'r') as f:
        lineNum = 0
        for line in f:
            line = line.split(": ")[1].split(" | ")
            winning = line[0].split(' ')
            other = line[1].split(" ")

            while '' in winning:
                winning.remove('')
            while '' in other:
                other.remove('')

            for i in range(0, len(winning)):
                winning[i] = int(winning[i])

            for i in range(0, len(other)):
                other[i] = int(other[i])

            input.append([winning, other])
            lineNum += 1
            
    return input


def solution1():
    input = getInput()

    sum = 0
    for line in input:
        matches = 0
        for w in line[0]:
            if w in line[1]:
                if matches == 0:
                    matches = 1
                else:
                    matches = matches*2
        sum += matches
    return sum


def solution2():
    input = getInput()
    
    duplicates = {}
    for i in range(1, len(input)+1):
        duplicates[i] = 1

    for i in range(0, len(input)):
        matches = 0

        for w in input[i][0]:
            if w in input[i][1]:
                matches += 1

        for newCard in range(0, matches):
            newIndex = newCard + 2 + i
            duplicates[newIndex] += duplicates[i+1]

    numCards = 0
    for k in duplicates.keys():
        numCards += duplicates[k]
    return numCards


print("Year 2023, Day 4 solution part 1:", solution1())
print("Year 2023, Day 4 solution part 2:", solution2())