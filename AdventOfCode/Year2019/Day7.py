#https://adventofcode.com/2019/day/7
#https://adventofcode.com/2019/day/7#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d7_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d7_real.txt")


def getInput():
    inputSeq = []

    with open(inFile, 'r') as f:
        for line in f:
            inputSeq = line.replace('\n', '').split(',')
            for i in range(0, len(inputSeq)):
                inputSeq[i] = int(inputSeq[i])

    return inputSeq


def solution1():
    insq = getInput()
    
    for i in insq:
        print(i, type(i))
        
    return


def solution2():
    return


print("Year 2019, Day 7 solution part 1:", solution1())
print("Year 2019, Day 7 solution part 2:", solution2())