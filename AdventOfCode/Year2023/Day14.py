#https://adventofcode.com/2023/day/14
#https://adventofcode.com/2023/day/14#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d14_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d14_real.txt")


def getInput():
    input = []
    rocks = []

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            lineChars = []
            for col in range(0, len(line)):
                if line[col] == '\n':
                    break
                else:
                    lineChars.append(line[col])
                    if line[col] == 'O':
                        rocks.append([row,col])
            input.append(lineChars)
            row += 1

    return input, rocks


def moveRockUp(input:list, rocks:list, rockIndex:int):
    currentRow = rocks[rockIndex][0]
    col = rocks[rockIndex][1]

    while currentRow > 0:
        charUp = input[currentRow-1][col]

        if charUp == 'O':
            otherRockIndex = rocks.index([currentRow-1,col])
            moveRockUp(input, rocks, otherRockIndex)
            if input[currentRow-1][col] == 'O':
                rocks[rockIndex] = [currentRow, col]
                return
        elif charUp == '#':
            rocks[rockIndex] = [currentRow, col]
            return
        elif charUp == '.':
            input[currentRow][col] = '.'
            input[currentRow-1][col] = 'O'
            currentRow -= 1
    rocks[rockIndex] = [currentRow, col]


def moveRockDown(input:list, rocks:list, rockIndex:int):
    currentRow = rocks[rockIndex][0]
    col = rocks[rockIndex][1]

    while currentRow < len(input)-1:
        charDown = input[currentRow+1][col]

        if charDown == 'O':
            otherRockIndex = rocks.index([currentRow+1,col])
            moveRockDown(input, rocks, otherRockIndex)
            if input[currentRow+1][col] == 'O':
                rocks[rockIndex] = [currentRow, col]
                return
        elif charDown == '#':
            rocks[rockIndex] = [currentRow, col]
            return
        elif charDown == '.':
            input[currentRow][col] = '.'
            input[currentRow+1][col] = 'O'
            currentRow += 1
    rocks[rockIndex] = [currentRow, col]


def moveRockLeft(input:list, rocks:list, rockIndex:int):
    row = rocks[rockIndex][0]
    currentCol = rocks[rockIndex][1]

    while currentCol > 0:
        charLeft = input[row][currentCol-1]

        if charLeft == 'O':
            otherRockIndex = rocks.index([row, currentCol-1])
            moveRockLeft(input, rocks, otherRockIndex)
            if input[row][currentCol-1] == 'O':
                rocks[rockIndex] = [row, currentCol]
                return
        elif charLeft == '#':
            rocks[rockIndex] = [row, currentCol]
            return
        elif charLeft == '.':
            input[row][currentCol] = '.'
            input[row][currentCol-1] = 'O'
            currentCol -= 1
    rocks[rockIndex] = [row, currentCol]


def moveRockRight(input:list, rocks:list, rockIndex:int):
    row = rocks[rockIndex][0]
    currentCol = rocks[rockIndex][1]

    while currentCol < len(input[0])-1:
        charRight = input[row][currentCol+1]

        if charRight == 'O':
            otherRockIndex = rocks.index([row, currentCol+1])
            moveRockRight(input, rocks, otherRockIndex)
            if input[row][currentCol+1] == 'O':
                rocks[rockIndex] = [row, currentCol]
                return
        elif charRight == '#':
            rocks[rockIndex] = [row, currentCol]
            return
        elif charRight == '.':
            input[row][currentCol] = '.'
            input[row][currentCol+1] = 'O'
            currentCol += 1
    rocks[rockIndex] = [row, currentCol]


def solution1():
    input, rocks = getInput()
    
    for r in range(0, len(rocks)):
        moveRockUp(input, rocks, r)

    weight = 0
    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] == 'O':
                weight += len(input) - row

    return weight


def solution2():
    input, rocks = getInput()

    #Need to run for 1000000000 cycles...
    for cycle in range(0, 1000):
        for r in range(0, len(rocks)):
            moveRockUp(input, rocks, r)
        for r in range(0, len(rocks)):
            moveRockLeft(input, rocks, r)
        for r in range(0, len(rocks)):
            moveRockDown(input, rocks, r)
        for r in range(0, len(rocks)):
            moveRockRight(input, rocks, r)

    weight = 0
    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] == 'O':
                weight += len(input) - row

    return weight


print("Year 2023, Day 14 solution part 1:", solution1())
print("Year 2023, Day 14 solution part 2:", solution2())