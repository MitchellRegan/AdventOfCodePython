aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []
    guardPos = [0,0]

    with open(inFile, 'r') as f:
        r = 0
        for line in f:
            line = line.replace('\n', '')
            line = [x for x in line]
            inpt.append(line)
            if '^' in line:
                guardPos = [r, line.index('^')]
            r += 1
    return inpt, guardPos[0], guardPos[1]
            

def solution1():
    inpt, r,c = getInput()
    guardDir = '^'

    visitedPos = {(r,c):True}
    while r > -1 and r < len(inpt) and c > -1 and c < len(inpt[0]):
        if guardDir == '^':
            if r == 0:
                r -= 1
            elif inpt[r-1][c] == '#':
                guardDir = '>'
            else:
                r -= 1
                visitedPos[(r,c)] = True
        elif guardDir == '>':
            if c == len(inpt[0])-1:
                c += 1
            elif inpt[r][c+1] == '#':
                guardDir = 'v'
            else:
                c += 1
                visitedPos[(r,c)] = True
        elif guardDir == '<':
            if c == 0:
                c -= 1
            elif inpt[r][c-1] == '#':
                guardDir = '^'
            else:
                c -= 1
                visitedPos[(r,c)] = True
        else:
            if r == len(inpt)-1:
                r += 1
            elif inpt[r+1][c] == '#':
                guardDir = '<'
            else:
                r += 1
                visitedPos[(r,c)] = True

    return len(visitedPos.keys())


def solution2():
    inpt, startRow, startCol = getInput()
    guardDir = '^'

    #Getting every location the guard travels in a normal path
    visitedPos = {}
    r = startRow
    c = startCol
    while r > -1 and r < len(inpt) and c > -1 and c < len(inpt[0]):
        if guardDir == '^':
            if r == 0:
                r -= 1
            elif inpt[r-1][c] == '#':
                guardDir = '>'
            else:
                r -= 1
                visitedPos[(r,c)] = True
        elif guardDir == '>':
            if c == len(inpt[0])-1:
                c += 1
            elif inpt[r][c+1] == '#':
                guardDir = 'v'
            else:
                c += 1
                visitedPos[(r,c)] = True
        elif guardDir == '<':
            if c == 0:
                c -= 1
            elif inpt[r][c-1] == '#':
                guardDir = '^'
            else:
                c -= 1
                visitedPos[(r,c)] = True
        else:
            if r == len(inpt)-1:
                r += 1
            elif inpt[r+1][c] == '#':
                guardDir = '<'
            else:
                r += 1
                visitedPos[(r,c)] = True

    #Looping through all possible locations that an obstacle can be placed along the guard's path
    validPos = 0
    for p in visitedPos.keys():
        #Putting a blocked space on the current path position
        inpt[p[0]][p[1]] = '#'

        #Resetting the vars for this loop
        r = startRow
        c = startCol
        rowMove = -1
        colMove = 0
        guardDir = '^'
        hitPos = {}

        while r + rowMove > -1 and r + rowMove < len(inpt) and c + colMove > -1 and c + colMove < len(inpt[0]):
            if inpt[r+rowMove][c+colMove] == '#':
                curPos = (r,c)
                #If this blockage has been hit in the same spot at the same direction, a loop has happened
                if curPos in hitPos.keys() and guardDir in hitPos[curPos]:
                    validPos += 1
                    break
                #Otherwise this blockage hasn't been hit in this way before so we mark it for future collisions
                else:
                    if curPos not in hitPos.keys():
                        hitPos[curPos] = []
                    hitPos[curPos].append(guardDir)

                #Rotating the guard's facing direction 90 degrees clockwise
                if guardDir == '^':
                    guardDir = '>'
                    rowMove = 0
                    colMove = 1
                elif guardDir == '>':
                    guardDir = 'v'
                    rowMove = 1
                    colMove = 0
                elif guardDir == 'v':
                    guardDir = '<'
                    rowMove = 0
                    colMove = -1
                elif guardDir == '<':
                    guardDir = '^'
                    rowMove = -1
                    colMove = 0
            #If no obstruction, keep moving forward
            else:
                r += rowMove
                c += colMove

        #Removing the added obstacle and replacing it with an open space again
        inpt[p[0]][p[1]] = '.'

    return validPos


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())