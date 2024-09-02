#https://adventofcode.com/2019/day/23
#https://adventofcode.com/2019/day/23#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d23_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d23_real.txt")


def getInput():
    inputSeq = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')

    return 
            

def solution1():
    return


def solution2():
    return


print("Year 2019, Day 23 solution part 1:", solution1())
print("Year 2019, Day 23 solution part 2:", solution2())