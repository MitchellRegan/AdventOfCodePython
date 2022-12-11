#https://adventofcode.com/2022/day/8
#https://adventofcode.com/2022/day/8#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d8_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d8_real.txt")

def solution1():
    visible = []

    treeGrid = []

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            row = [x for x in line]
            row.pop()
            treeGrid.append(row)


    #Getting the outside perimeter
    for col in range(0, len(treeGrid[0])):
        if (0,col) not in visible:
            visible.append((0,col))
        if (len(treeGrid)-1, col) not in visible:
            visible.append((len(treeGrid)-1,col))

    for row in range(0, len(treeGrid)):
        if (row, 0) not in visible:
            visible.append((row,0))
        if (row, len(treeGrid[0])-1) not in visible:
            visible.append((row, len(treeGrid[0])-1))

    #Looking from the left
    for row in range(0, len(treeGrid)):
        curHeight = 0
        for col in range(0, len(treeGrid[row])):
            if int(treeGrid[row][col]) > curHeight:
                curHeight = int(treeGrid[row][col])
                if (row,col) not in visible:
                    visible.append((row,col))

    #Looking from the right
    for row in range(0, len(treeGrid)):
        curHeight = 0
        for col in range(len(treeGrid[row])-1, -1, -1):
            if int(treeGrid[row][col]) > curHeight:
                curHeight = int(treeGrid[row][col])
                if (row,col) not in visible:
                    visible.append((row,col))

    #looking from the top
    for col in range(0, len(treeGrid[0])):
        curHeight = 0
        for row in range(0, len(treeGrid)):
            if int(treeGrid[row][col]) > curHeight:
                curHeight = int(treeGrid[row][col])
                if (row,col) not in visible:
                    visible.append((row,col))

    #Looking from the bottom
    for col in range(0, len(treeGrid[0])):
        curHeight = 0
        for row in range(len(treeGrid)-1, -1, -1):
            if int(treeGrid[row][col]) > curHeight:
                curHeight = int(treeGrid[row][col])
                if (row,col) not in visible:
                    visible.append((row,col))

    return len(visible)


def solution2():
    treeGrid = []
    highScore = 0

    #Looping through each line in the file
    with open(inFile, 'r') as f:
        for line in f:
            row = [x for x in line]
            row.pop()
            treeGrid.append(row)

    #Looping through each tree in the grid
    for r in range(1, len(treeGrid)-1):
        for c in range(1, len(treeGrid[0])-1):
            view = 0
            curHeight = treeGrid[r][c]

            #Look right from the tree
            for i in range(c+1, len(treeGrid[0])):
                if treeGrid[r][i] >= treeGrid[r][c]:
                    view = i - c
                    break
                elif i == len(treeGrid[0])-1 and i is not (c+1):
                    view = i-c
            #Look left from the tree
            for i in range(c-1, -1, -1):
                if treeGrid[r][i] >= treeGrid[r][c]:
                    view *= c - i
                    break
                elif i == 0 and i is not (c-1):
                    view *= c-i
            #Look up from the tree
            for j in range(r-1, -1, -1):
                if treeGrid[j][c] >= treeGrid[r][c]:
                    view *= r - j
                    break
                elif j == 0 and j is not (r-1):
                    view *= r-j
            #Look down from the tree
            for j in range(r+1, len(treeGrid)):
                if treeGrid[j][c] >= treeGrid[r][c]:
                    view *= j - r
                    break
                elif j == len(treeGrid)-1 and j is not (r+1):
                    view *= j-r

            if view > highScore:
                highScore = view

    return highScore


print("Year 2022, Day 8 solution part 1:", solution1())
print("Year 2022, Day 8 solution part 2:", solution2())