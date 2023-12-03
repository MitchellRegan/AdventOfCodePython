#https://adventofcode.com/2021/day/20
#https://adventofcode.com/2021/day/20#part2

from inspect import getouterframes
import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    alg = ''
    input = []
    with open(inFile, 'r') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n', '').replace('.', '0').replace('#', '1')
            if lineNum == 0:
                alg = line
            elif lineNum > 1:
                input.append(line)
            lineNum += 1

    return input, alg


def outputData(input, printImage=False, printLitPixels=False):
    sum = 0
    for line in input:
        sum += line.count('1')
        if printImage:
            print(line.replace('0',' ').replace('1','#'))
    if printLitPixels:
        print("Lit Pixels:", sum)
    return sum


def getPixel(col:int, row:int, input:list, alg:list):
    valueString = ''

    offsets = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            offsets.append((x, y))

    for o in offsets:
        x = o[0]
        y = o[1]
        val = ''

        #Out of bounds
        if col+x < 0 \
            or row+y < 0 \
            or col+x >= len(input[0]) \
            or row+y >= len(input):
            val = '0'
        #In bounds
        else:
            val = input[row+y][col+x]
            
        valueString = valueString + val

    ind = int(valueString, 2)
    return alg[ind]


def solution1():
    input, alg = getInput()

    for i in range(0, 2):
        newInput = []
        outputData(input, False, True)

        for row in range(-1, len(input)+1):
            newRow = ''
            for col in range(-1, len(input[0])+1):
                newRow = newRow + getPixel(col, row, input, alg)
            newInput.append(newRow)
            
        input = newInput

    return outputData(input, False, True)


def solution2():
    input = getInput()

    return 


print("Year 2021, Day 20 solution part 1:", solution1())
#5278 too high
print("Year 2021, Day 20 solution part 2:", solution2())