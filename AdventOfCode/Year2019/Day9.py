#https://adventofcode.com/2019/day/9
#https://adventofcode.com/2019/day/9#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d9_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d9_real.txt")


def getInput():
    layers = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')

    return layers
            

def solution1():
    return


def solution2():
    
    return


print("Year 2019, Day 9 solution part 1:", solution1())
print("Year 2019, Day 9 solution part 2:", solution2())