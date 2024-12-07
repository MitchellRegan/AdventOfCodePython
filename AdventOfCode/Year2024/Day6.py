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
    inpt, sr,sc = getInput()
    guardDir = '^'

    #Getting every location the guard travels in a normal path
    visitedPos = {}
    r = sr
    c = sc
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

    validPos = 0
    #Looping through all possible locations that an obstacle can be placed along the guard's path
    #vp = [x for x in visitedPos.keys()]
    for p in visitedPos.keys():
        y,x = p
        testing and print("Checking row", y, "col", x)
        inpt[y][x] = '#'
        #Resetting the vars for this loop
        r = sr
        c = sc
        guardDir = '^'
        hitPos = {}

        while r > -1 and r < len(inpt) and c > -1 and c < len(inpt[0]):
            if guardDir == '^':
                if r > 0 and inpt[r-1][c] == '#':
                    if (r,c) in hitPos.keys() and guardDir in hitPos[(r,c)]:
                        validPos += 1
                        testing and print("\tValid pos found at", y,x)
                        break
                    else:
                        if (r,c) not in hitPos.keys():
                            hitPos[(r,c)] = []
                        hitPos[(r,c)].append(guardDir)
                    guardDir = '>'
                else:
                    r -= 1
            elif guardDir == '>':
                if c < len(inpt[0])-1 and inpt[r][c+1] == '#':
                    if (r,c) in hitPos.keys() and guardDir in hitPos[(r,c)]:
                        validPos += 1
                        testing and print("\tValid pos found at", y,x)
                        break
                    else:
                        if (r,c) not in hitPos.keys():
                            hitPos[(r,c)] = []
                        hitPos[(r,c)].append(guardDir)
                    guardDir = 'v'
                else:
                    c += 1
            elif guardDir == '<':
                if c > 0 and inpt[r][c-1] == '#':
                    if (r,c) in hitPos.keys() and guardDir in hitPos[(r,c)]:
                        validPos += 1
                        testing and print("\tValid pos found at", y,x)
                        break
                    else:
                        if (r,c) not in hitPos.keys():
                            hitPos[(r,c)] = []
                        hitPos[(r,c)].append(guardDir)
                    guardDir = '^'
                else:
                    c -= 1
            else:
                if r < len(inpt)-1 and inpt[r+1][c] == '#':
                    if (r,c) in hitPos.keys() and guardDir in hitPos[(r,c)]:
                        validPos += 1
                        testing and print("\tValid pos found at", y,x)
                        break
                    else:
                        if (r,c) not in hitPos.keys():
                            hitPos[(r,c)] = []
                        hitPos[(r,c)].append(guardDir)
                    guardDir = '<'
                else:
                    r += 1

        #Removing the added obstacle and replacing it with an open space again
        inpt[y][x] = '.'

    return validPos


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())