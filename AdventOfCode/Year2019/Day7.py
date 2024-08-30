#https://adventofcode.com/2019/day/7
#https://adventofcode.com/2019/day/7#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d7_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d7_real.txt")


def getInput():
    '''Returns the list of all unique orbiting objects, and a one-way directional graph where each object points to the object it orbits.'''
    objectList = []
    orbits = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(')')
            if line[0] not in objectList:
                objectList.append(line[0])
            if line[1] not in objectList:
                objectList.append(line[1])
            orbits[line[1]] = line[0]

    return objectList, orbits


def solution1():
    return


def solution2():
    return


print("Year 2019, Day 7 solution part 1:", solution1())
print("Year 2019, Day 7 solution part 2:", solution2())