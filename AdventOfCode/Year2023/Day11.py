#https://adventofcode.com/2023/day/11
#https://adventofcode.com/2023/day/11#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d11_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d11_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:

        for line in f:
            line = line.replace('\n','')
            row = []

            for char in line:
                row.append(char)
            input.append(row)
                
    return input


def manhattanDist(p1_:tuple, p2_:tuple)->int:
    return abs(p1_[0]-p2_[0]) + abs(p1_[1]-p2_[1])


def solution1():
    input = getInput()
    
    #Checking for empty '.' columns
    col = 0
    while col < len(input[0]):
        isEmpty = True
        for line in input:
            if line[col] is not '.':
                isEmpty = False
        if isEmpty:
            for line in range(0, len(input)):
                input[line].insert(col, '.')
            col += 2
        else:
            col += 1

    #Checking for empty '.' rows
    row = 0
    while row < len(input):
        isEmpty = True
        for char in input[row]:
            if char is not '.':
                isEmpty = False
        if isEmpty:
            newRow = ['.'] * len(input[0])
            input.insert(row, newRow)
            row += 2
        else:
            row += 1

    pointLocs = []
    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] is not '.':
                pointLocs.append((row,col))

    pairs = {}
    distSum = 0
    for i in range(0, len(pointLocs)-1):
        for j in range(i+1, len(pointLocs)):
            p1 = pointLocs[i]
            p2 = pointLocs[j]

            distSum += manhattanDist(p1,p2)

    return distSum


def solution2():
    input = getInput()

    pointLocs = []
    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] is not '.':
                pointLocs.append([row,col])
    
    #Checking for empty '.' columns
    emptyColIndexes = []
    for c in range(0, len(input[0])):
        isEmpty = True
        for row in input:
            if row[c] is not '.':
                isEmpty = False
        if isEmpty:
            emptyColIndexes.append(c)

    #Checking for empty '.' rows
    emptyRowIndexes = []
    for r in range(0, len(input)):
        isEmpty = True
        for char in input[r]:
            if char is not '.':
                isEmpty = False
        if isEmpty:
            emptyRowIndexes.append(r)
            
    emptySpaceMult = 1000000
    for pl in range(0, len(pointLocs)):
        oldRow = pointLocs[pl][0]
        oldCol = pointLocs[pl][1]
        newRow = oldRow
        newCol = oldCol

        for eci in emptyColIndexes:
            if oldCol > eci:
                newCol += emptySpaceMult-1
            else:
                break
        for eri in emptyRowIndexes:
            if oldRow > eri:
                newRow += emptySpaceMult-1
            else:
                break

        pointLocs[pl] = (newRow,newCol)
    
    distSum = 0
    for i in range(0, len(pointLocs)-1):
        for j in range(i+1, len(pointLocs)):
            p1 = pointLocs[i]
            p2 = pointLocs[j]

            distSum += manhattanDist(p1,p2)

    return distSum


print("Year 2023, Day 11 solution part 1:", solution1())
print("Year 2023, Day 11 solution part 2:", solution2())