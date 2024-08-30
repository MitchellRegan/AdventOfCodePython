#https://adventofcode.com/2023/day/18
#https://adventofcode.com/2023/day/18#part2

import os
from tkinter import HORIZONTAL
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d18_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d18_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace('(', '').replace(')', '').split(' ')
            input.append([line[0], int(line[1]), line[2]])
    return input


def solution1():
    input = getInput()
    positions = {(0,0):'#'}
    row = 0
    col = 0

    rowRange = [0,0]
    colRange = [0,0]

    #Finding the size of the grid to make, and identifying which (row,col) positions need to be hollowed out
    for line in input:
        rOffset = 0
        cOffset = 0

        if line[0] == 'R': cOffset = 1
        elif line[0] == 'L': cOffset = -1
        elif line[0] == 'U': rOffset = -1
        elif line[0] == 'D': rOffset = 1

        for i in range(0, line[1]):
            row += rOffset
            col += cOffset
            positions[(row,col)] = '#'

            if row < rowRange[0]:
                rowRange[0] = row
            elif row > rowRange[1]:
                rowRange[1] = row

            if col < colRange[0]:
                colRange[0] = col
            elif col > colRange[1]:
                colRange[1] = col

    #Making a 2D grid of spaces to reflect the spaces that are hollowed out
    grid = []
    for r in range(rowRange[0], rowRange[1]+1):
        newLine = []
        for c in range(colRange[0], colRange[1]+1):
            newLine.append('.')
        grid.append(newLine)

    #Marking the holes designated by the input in our grid
    for hole in positions:
        r = hole[0] - rowRange[0]
        c = hole[1] - colRange[0]
        grid[r][c] = '#'

    #BFS search from the top-left to identify any areas that should and shouldn't be filled in
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == '.':
                q = [(r,c)]
                seen = {}
                empty = False

                while len(q) > 0:
                    head = q.pop(0)
                    hr = head[0]
                    hc = head[1]

                    #If any point is touching the outside edge of the map, all contiguous parts of this flood-fill
                    #are non-hole segments that won't be counted in our final tally
                    if hr == 0 or hc == 0 or hr == len(grid)-1 or hc == len(grid[0])-1:
                        empty = True

                    if hr > 0 and grid[hr-1][hc] == '.' and (hr-1, hc) not in seen.keys() and (hr-1, hc) not in q: #up
                        q.append((hr-1, hc))
                    if hr < len(grid)-1 and grid[hr+1][hc] == '.' and (hr+1, hc) not in seen.keys() and (hr+1, hc) not in q: #down
                        q.append((hr+1, hc))
                    if hc > 0 and grid[hr][hc-1] == '.' and (hr, hc-1) not in seen.keys() and (hr, hc-1) not in q: #left
                        q.append((hr, hc-1))
                    if hc < len(grid[0])-1 and grid[hr][hc+1] == '.' and (hr, hc+1) not in seen.keys() and (hr, hc+1) not in q: #right
                        q.append((hr, hc+1))

                    seen[head] = True

                for tile in seen.keys():
                    if empty:
                        grid[tile[0]][tile[1]] = ' '
                    else:
                        grid[tile[0]][tile[1]] = '#'

    #Getting the total number of empty hole # spaces in the grid as the answer
    holeCount = 0
    for r in grid:
        for c in r:
            if c != ' ':
                holeCount += 1

    return holeCount


def solution2():
    input = getInput()
    vertLines = []
    horizLines = []
    row = 0
    col = 0

    rowRange = [0,0]
    colRange = [0,0]

    #Finding the size of the grid to make, and identifying which (row,col) positions need to be hollowed out
    for line in input:
        rOffset = 0
        cOffset = 0

        hexValue = int('0x'+line[2][1:-1], 16)
        if line[2][-1] == '0': cOffset = 1
        elif line[2][-1] == '1': rOffset = 1
        elif line[2][-1] == '2': cOffset = -1
        elif line[2][-1] == '3': rOffset = -1

        newRow = row + (hexValue * rOffset)
        newCol = col + (hexValue * cOffset)
        edge = (
            min((row, col), (newRow, newCol)),
            max((row, col), (newRow, newCol))
        )

        if rOffset == 0:
            horizLines.append(edge)
        else:
            vertLines.append(edge)

        row = newRow
        col = newCol

    vertLines.sort(key=lambda v: v[0][1])
    horizLines.sort(key=lambda h: h[0][0])

    print("Row Range:", rowRange)
    print("Col Range:", colRange)
    print("Vertical Edges:")
    for ve in vertLines:
        print("\t", ve[0], "to", ve[1])
    print("Horizontal Edges")
    for he in horizLines:
        print("\t", he[0], "to", he[1])

    total = 0
    for r in range(rowRange[0], rowRange[1]+1):
        hInd = 0
        vInd = 0
        inBound = False

        for h in range(0, len(horizLines)):
            if horizLines[h][0][0] >= r:
                hInd = h
                break
        for v in range(0, len(vertLines)):
            if r >= vertLines[v][0][0] and r <= vertLines[v][1][0]:
                vInd = v
                break
        
        col = colRange[0]
        #while col < colRange[1]:



    return 0 


print("Year 2023, Day 18 solution part 1:", solution1())
print("Year 2023, Day 18 solution part 2:", solution2())