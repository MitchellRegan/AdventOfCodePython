#https://adventofcode.com/2019/day/8
#https://adventofcode.com/2019/day/8#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d8_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d8_real.txt")


def getInput():
    inputList = []

    with open(inFile, 'r') as f:
        for line in f:
            inputList = line.replace('\n', '')

    return inputList
            

def solution1():
    inputList = getInput()
    r = 6
    c = 25
    
    bestLayer = 0
    leastZeros = -1
    score = 0
    for i in range(0, len(inputList), r*c):
        layer = inputList[i : i + (r*c)]
        zeroCount = layer.count('0')
                
        if leastZeros == -1 or zeroCount < leastZeros:
            bestLayer = layer
            leastZeros = zeroCount
            score = layer.count('1') * layer.count('2')
        
    return score


def solution2():
    return


print("Year 2019, Day 8 solution part 1:", solution1())
print("Year 2019, Day 8 solution part 2:", solution2())