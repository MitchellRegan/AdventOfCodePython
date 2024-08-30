#https://adventofcode.com/2023/day/17
#https://adventofcode.com/2023/day/17#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d17_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d17_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        for line in f:
            line = list(line.replace('\n',''))
            for i in range(0, len(line)):
                line[i] = int(line[i])
            input.append(line)

    return input


def solution1():
    inputGrid = getInput()
    
    #dictionary for each point traveled on the bfs search
    #   key: (row,col) of point along the path
    #   val: (row,col, heat loss, dir) position of the point preceeding it, total heat loss incurred so far, and an int for the number of consecutive spaces traveled in the same direction
    path = {(0,0):(None, 0, 0)}
    maxSpaces = 3

    #BFS search from the top-left to the bottom-right
    q = [(0,0)]
    while len(q) > 0:
        currPos = q.pop(0)
        row = currPos[0]
        col = currPos[1]

        #If the current path has moved too far in the same direction, we pivot 90 degrees
        pivotUD = False
        pivotLR = False
        if path[currPos][2] == maxSpaces:
            if row == path[currPos][0][0]:
                pivotUD = True
            else:
                pivotLR = True
                
        #Checking UP
        if row > 0 and not pivotLR:
            newPos = (row-1, col)
            newHeat = inputGrid[row-1][col] + path[currPos][1]
            consecDist = 0
            if path[currPos][0] is not None and path[currPos][0][0] == row+1:
                consecDist = path[currPos][2] + 1
            if newPos not in path.keys() or path[newPos][1] > newHeat:
                path[newPos] = (currPos, newHeat, consecDist)
                q.append(newPos)
        #Checking DOWN
        if row < len(inputGrid)-1 and not pivotLR:
            newPos = (row+1, col)
            newHeat = inputGrid[row+1][col] + path[currPos][1]
            consecDist = 0
            if path[currPos][0] is not None and path[currPos][0][0] == row-1:
                consecDist = path[currPos][2] + 1
            if newPos not in path.keys() or path[newPos][1] > newHeat:
                path[newPos] = (currPos, newHeat, consecDist)
                q.append(newPos)
        #Checking LEFT
        if col > 0 and not pivotUD:
            newPos = (row, col-1)
            newHeat = inputGrid[row][col-1] + path[currPos][1]
            consecDist = 0
            if path[currPos][0] is not None and path[currPos][0][1] == col+1:
                consecDist = path[currPos][2] + 1
            if newPos not in path.keys() or path[newPos][1] > newHeat:
                path[newPos] = (currPos, newHeat, consecDist)
                q.append(newPos)
        #Checking RIGHT
        if col < len(inputGrid[0])-1 and not pivotUD:
            newPos = (row, col+1)
            newHeat = inputGrid[row][col+1] + path[currPos][1]
            consecDist = 0
            if path[currPos][0] is not None and path[currPos][0][1] == col-1:
                consecDist = path[currPos][2] + 1
            if newPos not in path.keys() or path[newPos][1] > newHeat:
                path[newPos] = (currPos, newHeat, consecDist)
                q.append(newPos)



    #Starting at the ending point, we pathfind backwards to the start
    #endPoint = (len(input)-1, len(input[0])-1)
    #while True:
    #    if endPoint[0] is None:
    #        break
    #    input[endPoint[0]][endPoint[1]] = '.'
    #    endPoint = path[endPoint]

    p = (len(inputGrid)-1, len(inputGrid[0])-1)
    print("End point:", p)
    while p is not None:
        r = p[0]
        c = p[1]
        print("\tGrid value:", inputGrid[r][c])
        inputGrid[r][c] = "+"
        print("\tGrid value:", inputGrid[r][c])
        print("\tPath value:", path[p])
        p = path[p][0]
        print("new point:", p)

    for line in inputGrid:
        lineStr = ''
        for c in line:
            lineStr = lineStr + str(c)
        print(lineStr)

    return path[(len(inputGrid)-1, len(inputGrid[0])-1)][1]


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 17 solution part 1:", solution1())
print("Year 2023, Day 17 solution part 2:", solution2())