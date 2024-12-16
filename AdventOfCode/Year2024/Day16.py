aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    grid = []
    startPos = None
    endPos = None

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            line = line.replace('\n', '')
            if 'S' in line:
                startPos = (row, line.index('S'))
                line = line.replace('S', '.')
            if 'E' in line:
                endPos = (row, line.index('E'))
                line = line.replace('E', '.')
            grid.append(line)
            row += 1

    return grid, startPos, endPos
            

def solution1():
    grid, startPos, endPos = getInput()
    
    if testing:
        print("Start:", startPos, "\nEnd: ", endPos)
        for line in grid:
            print(line)

    q = [(startPos, '>', 0)] #Each element is ((row,col) position, direction facing, current score)
    seen = {} #Key = (row,col) position, value = score

    while len(q) > 0:
        pos, dir, curScore = q.pop(0)

        #If we found the end position, this is definitionally the lowest score since we sort the que by lowest score
        if pos == endPos:
            return curScore

        validDirs = []

        if dir == '>':
            validDirs = [('>', 0, 1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == '<':
            validDirs = [('<', 0, -1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == 'v':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('v', 1, 0)]
        elif dir == '^':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('^', -1, 0)]

        for nextDir in validDirs:
            nextScore = curScore
            nextRow = pos[0] + nextDir[1]
            nextCol = pos[1] + nextDir[2]

            #Moving in this direction is only valid if it's not blocked by a wall
            if grid[nextRow][nextCol] == '.':
                #Travelling in the same direction only adds 1 to the score
                if nextDir[0] == dir:
                    nextScore += 1
                #Making a turn 90 degrees adds 1000 to the score
                else:
                    nextScore += 1001

                if (nextRow, nextCol) not in seen.keys() or seen[(nextRow, nextCol)] > nextScore:
                    seen[(nextRow, nextCol)] = nextScore
                    q.append(((nextRow, nextCol), nextDir[0], nextScore))
                    #Sorting the que so that the lowest score always goes first (Dijkstra's algorithm)
                    q.sort(key = lambda x: x[2])

    return


def solution2():
    grid, startPos, endPos = getInput()
    
    q = [(startPos, '>', 0)] #Each element is ((row,col) position, direction facing, current score)
    seen = {} #Key = (row,col) position, value = score
    prev = {startPos:None} #Key = (row,col) position, value = (row,col) of the previous tile in the path
    multiHit = {} #Key = (row,col) position, value = ((row,col) of an intersection where scores were tied, score when hit)

    bestScore = None
    while len(q) > 0:
        pos, dir, curScore = q.pop(0)

        #If we found the end position, this is definitionally the lowest score since we sort the que by lowest score
        if pos == endPos and (bestScore is None or bestScore > curScore):
            bestScore = curScore
            #break

        validDirs = []

        if dir == '>':
            validDirs = [('>', 0, 1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == '<':
            validDirs = [('<', 0, -1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == 'v':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('v', 1, 0)]
        elif dir == '^':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('^', -1, 0)]

        for nextDir in validDirs:
            #testing and print("\tTrying dir", nextDir)
            nextScore = curScore
            nextRow = pos[0] + nextDir[1]
            nextCol = pos[1] + nextDir[2]

            #Moving in this direction is only valid if it's not blocked by a wall
            if grid[nextRow][nextCol] == '.':
                #Travelling in the same direction only adds 1 to the score
                if nextDir[0] == dir:
                    nextScore += 1
                #Making a turn 90 degrees adds 1000 to the score
                else:
                    nextScore += 1001

                if (nextRow, nextCol) not in seen.keys() or seen[(nextRow, nextCol)] > nextScore:
                    #if (nextRow, nextCol) in seen.keys() and seen[(nextRow, nextCol)] == nextScore:
                    #    multiTile = [x for x in prev[(nextRow, nextCol)]].append(pos)
                    #    prev[(nextRow, nextCol)]
                    #else:
                    prev[(nextRow, nextCol)] = pos
                    seen[(nextRow, nextCol)] = nextScore
                    #testing and print("\t\tadding element:", ((nextRow, nextCol), nextDir[0], nextScore))
                    q.append(((nextRow, nextCol), nextDir[0], nextScore))
                    #Sorting the que so that the lowest score always goes first (Dijkstra's algorithm)
                    q.sort(key = lambda x: x[2])
                elif (nextRow, nextCol) in seen.keys() and seen[(nextRow, nextCol)] == nextScore:
                    multiHit[pos] = ((nextRow, nextCol), nextScore)

    if testing:
        print()
        for r in range(len(grid)):
            grid[r] = [x for x in grid[r]]

    ans = 1
    tile = endPos
    while tile is not None:
        if testing:
            grid[tile[0]][tile[1]] = 'O'
        tile = prev[tile]
        ans += 1

    for mh in multiHit.keys():
        grid[mh[0]][mh[1]] = '?'
        print("==== Multi-hit at", mh)

    if testing:
        for row in grid:
            prow = ''.join(row)
            prow = prow.replace('.', ' ').replace('O', '.')
            print(prow)
        print()
    return ans 


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())