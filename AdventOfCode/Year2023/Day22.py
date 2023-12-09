#https://adventofcode.com/2023/day/22
#https://adventofcode.com/2023/day/22#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d22_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d22_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:

            lineNum += 1

    return input


def solution1():
    input = getInput()
    


    return


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 22 solution part 1:", solution1())
print("Year 2023, Day 22 solution part 2:", solution2())