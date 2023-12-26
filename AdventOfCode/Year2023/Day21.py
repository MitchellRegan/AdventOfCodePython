#https://adventofcode.com/2023/day/21
#https://adventofcode.com/2023/day/21#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d21_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d21_real.txt")


def getInput():
    input = []
    start = None

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.replace('\n', '')
            line = [c for c in line]

            #Finding the row,col position of the starting point
            if start is None:
                for c in range(0, len(line)):
                    if line[c] == 'S':
                        start = (lineNum, c)
                        line[c] = '.'

            input.append(line)
            lineNum += 1

    return input, start


def solution1():
    input, start = getInput()
    
    steps = 64

    numGarden = 0
    tileDist = {}
    #Queue storing each tile's row, column, and steps remaining
    q = [(start[0], start[1], steps)]
    while len(q) > 0:
        r, c, s = q.pop(0)

        #If it's been visited or it's an impassable rock, we ignore it
        if (r,c) in tileDist.keys() or input[r][c] == '#':
            continue
        #Otherwise we mark it as visited
        else:
            tileDist[(r,c)] = steps - s
        
        #Tiles with an even number of spaces are viable to end on
        if s % 2 == 0:
            numGarden += 1

        #If there are steps remaining, we find the up, down, left, and right tiles to add to the queue
        if s > 0:
            if r > 0:
                q.append((r-1, c, s-1))
            if r < len(input)-1:
                q.append((r+1, c, s-1))
            if c > 0:
                q.append((r, c-1, s-1))
            if c < len(input[0])-1:
                q.append((r, c+1, s-1))

    return numGarden


def solution2():
    input, start = getInput()
    
    steps = 26501365
    remain = steps % 2

    numGarden = 0
    tileDist = {}
    #Queue storing each tile's row, column, and steps remaining
    q = [(start[0], start[1], steps)]
    while len(q) > 0:
        r, c, s = q.pop(0)

        #Row,Col variables that are normalized to the bounds of the input grid
        normR = r % len(input)
        normC = c % len(input[0])

        #If it's been visited or it's an impassable rock, we ignore it
        if (r,c) in tileDist.keys() or input[normR][normC] == '#':
            continue
        #Otherwise we mark it as visited
        else:
            tileDist[(r,c)] = steps - s
        
        #Even-numbered tiles (for even steps) or odd-numbered tiles (for odd steps) are viable to end on
        if s % 2 == remain:
            numGarden += 1

        #If there are steps remaining, we find the up, down, left, and right tiles to add to the queue
        if s > 0:
            q.append((r-1, c, s-1))
            q.append((r+1, c, s-1))
            q.append((r, c-1, s-1))
            q.append((r, c+1, s-1))

    for line in input:
        print(''.join(line))

    return numGarden


print("Year 2023, Day 21 solution part 1:", solution1())
print("Year 2023, Day 21 solution part 2:", solution2())