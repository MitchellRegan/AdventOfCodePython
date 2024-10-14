aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = [(x=='#') for x in line.replace('\n', '')]
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    numCycles = 100
    if testing:
        numCycles = 4
    
    for cycle in range(numCycles):
        testing and print("\nCycle", cycle, "==========================================")
        newInpt = []
        for r in range(len(inpt)):
            testing and print(''.join(['#' if x else '.' for x in inpt[r]]))
            nextRow = [False] * len(inpt)
            for c in range(len(inpt)):
                #Getting the current state of the 8 adjacent tiles around the current (r,c) tile
                onNeighbors = 0
                for adj in [(r-1,c-1), (r-1,c), (r-1,c+1), (r,c+1), (r+1,c+1), (r+1,c), (r+1,c-1), (r,c-1)]:
                    if adj[0] > -1 and adj[0] < len(inpt) and adj[1] > -1 and adj[1] < len(inpt) and inpt[adj[0]][adj[1]]:
                        onNeighbors += 1
                #If this tile is currently on, it only stays on if 2 or 3 neighbors are also on
                if inpt[r][c]:
                    nextRow[c] = (onNeighbors == 2 or onNeighbors == 3)
                #If this tile is currently off, it turns on if exactly 3 neighbors are on
                else:
                    nextRow[c] = (onNeighbors == 3)
            newInpt.append(nextRow)
        inpt = newInpt
        
    ans = 0
    testing and print("\nFinal Result ===========================================")
    for row in inpt:
        testing and print(''.join(['#' if x else '.' for x in row]))
        for col in row:
            if col:
                ans += 1
    return ans


def solution2():
    inpt = getInput()
    maxVal = len(inpt)-1
    #Making sure the corner tiles are initialized to "ON"
    inpt[0][0] = True
    inpt[0][maxVal] = True
    inpt[maxVal][0] = True
    inpt[maxVal][maxVal] = True
    
    numCycles = 100
    if testing:
        numCycles = 5
    
    for cycle in range(numCycles):
        testing and print("\nCycle", cycle, "==========================================")
        newInpt = []
        for r in range(len(inpt)):
            testing and print(''.join(['#' if x else '.' for x in inpt[r]]))
            nextRow = [False] * len(inpt)
            for c in range(len(inpt)):
                #If this is a corner tile, it remains on
                if (r == 0 and c == 0) or (r == 0 and c == maxVal) or (r == maxVal and c == 0) or (r == maxVal and c == maxVal):
                    nextRow[c] = True
                else:
                    #Getting the current state of the 8 adjacent tiles around the current (r,c) tile
                    onNeighbors = 0
                    for adj in [(r-1,c-1), (r-1,c), (r-1,c+1), (r,c+1), (r+1,c+1), (r+1,c), (r+1,c-1), (r,c-1)]:
                        if adj[0] > -1 and adj[0] < len(inpt) and adj[1] > -1 and adj[1] < len(inpt) and inpt[adj[0]][adj[1]]:
                            onNeighbors += 1
                    #If this tile is currently on, it only stays on if 2 or 3 neighbors are also on
                    if inpt[r][c]:
                        nextRow[c] = (onNeighbors == 2 or onNeighbors == 3)
                    #If this tile is currently off, it turns on if exactly 3 neighbors are on
                    else:
                        nextRow[c] = (onNeighbors == 3)
            newInpt.append(nextRow)
        inpt = newInpt
        
    ans = 0
    testing and print("\nFinal Result ===========================================")
    for row in inpt:
        testing and print(''.join(['#' if x else '.' for x in row]))
        for col in row:
            if col:
                ans += 1
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())