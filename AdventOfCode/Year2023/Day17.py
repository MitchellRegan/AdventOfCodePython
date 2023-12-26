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
    input = getInput()
    
    #dictionary for each point traveled on the bfs search
    #   key: (row,loc) of point found
    #   val: (row,loc, totalTemp) position of the point preceeding it, and the total temp as of this point found
    path = {(0,0):(None, None)}
    temps = {(0,0): 0}
    maxSpaces = 3

    #BFS search from the top-left to the bottom-right
    q = [(0,0)]
    while len(q) > 0:
        currPos = q.pop(0)
        row = currPos[0]
        col = currPos[1]

        #making a list of the last several spaces to check if this cart has been travelling in too long of a line
        prevPos = [path[currPos]]
        #bools to track if all of the last positions have had either the same row or same column
        sameRow = True
        sameCol = True
        for k in range(0, maxSpaces-1):
            if prevPos[-1] in path.keys():
                pp = path[prevPos[-1]]
                prevPos.append(pp)
                if pp[0] != prevPos[-2][0]:
                    sameRow = False
                if pp[1] != prevPos[-2][1]:
                    sameCol = False
            else:
                break

        if len(prevPos) < maxSpaces:
            sameRow = False
            sameCol = False

        newPositions = []
        #Checking the point above current
        if not sameCol and row > 0 and (row-1, col) != prevPos[0]:
            newPositions.append((row-1, col))
        #Checking the point below current
        if not sameCol and row < len(input)-1 and (row+1, col) != prevPos[0]:
            newPositions.append((row+1, col))
        #Checking the point left of current
        if not sameRow and col > 0 and (row, col-1) != prevPos[0]:
            newPositions.append((row, col-1))
        #Checking the point right of current
        if not sameRow and col < len(input[0])-1 and (row, col+1) != prevPos[0]:
            newPositions.append((row, col+1))

        for newPos in newPositions:
            totalTemp = input[newPos[0]][newPos[1]] + temps[currPos]
            if newPos not in path.keys() or temps[newPos] > totalTemp:
                path[newPos] = currPos
                temps[newPos] = totalTemp
                q.append(newPos)

    #Starting at the ending point, we pathfind backwards to the start
    #endPoint = (len(input)-1, len(input[0])-1)
    #while True:
    #    if endPoint[0] is None:
    #        break
    #    input[endPoint[0]][endPoint[1]] = '.'
    #    endPoint = path[endPoint]

    for p in path.keys():
        if path[p] == (None, None):
            continue
        prev = path[p]
        arrow = ''

        if p[0] < prev[0]:
            arrow = '^'
        elif p[0] > prev[0]:
            arrow = 'v'
        elif p[1] < prev[1]:
            arrow = '<'
        else:
            arrow = '>'
        input[p[0]][p[1]] = arrow

    for line in input:
        lineStr = ''
        for c in line:
            lineStr = lineStr + str(c)
        print(lineStr)

    return temps[(len(input)-1, len(input[0])-1)]


def solution2():
    input = getInput()
    


    return


print("Year 2023, Day 17 solution part 1:", solution1())
print("Year 2023, Day 17 solution part 2:", solution2())