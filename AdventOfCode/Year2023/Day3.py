#https://adventofcode.com/2023/day/3
#https://adventofcode.com/2023/day/3#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if False:
    inFile = os.path.join(inFileDir, "InputTestFiles/d3_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d3_real.txt")


def solution1():

    with open(inFile, 'r') as f:
        lineNum = 1
        for line in f:

            lineNum += 1

    return


def solution2():
    
    with open(inFile, 'r') as f:
        lineNum = 1
        for line in f:

            lineNum += 1

    return


print("Year 2023, Day 3 solution part 1:", solution1())
print("Year 2023, Day 3 solution part 2:", solution2())