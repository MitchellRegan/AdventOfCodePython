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
            line = line.replace('\n', '').split(', ')
            cRange = []
            rRange = []
            if line[0][0] == 'x':
                cRange = [int(line[0][2:]), int(line[0][2:])]
                rRange = [int(line[1].replace('y=', '').split('..')[0]), int(line[1].replace('y=', '').split('..')[1])]
            else:
                rRange = [int(line[0][2:]), int(line[0][2:])]
                cRange = [int(line[1].replace('x=', '').split('..')[0]), int(line[1].replace('x=', '').split('..')[1])]
            inpt.append([rRange, cRange])
    return inpt
            

def solution1():
    inpt = getInput() #Row ranges, then col ranges
    
    #Finding the min and max row,col
    gridRanges = [None, None, None, None] #min row, max row, min col, max col
    for line in inpt:
        rr, cr = line
        if gridRanges[0] is None or rr[0] < gridRanges[0]:
            gridRanges[0] = rr[0]
        if gridRanges[1] is None or rr[1] > gridRanges[1]:
            gridRanges[1] = rr[1]
        if gridRanges[2] is None or cr[0] < gridRanges[2]:
            gridRanges[2] = cr[0]
        if gridRanges[3] is None or cr[1] > gridRanges[3]:
            gridRanges[3] = cr[1]
        testing and print("Row Range:", rr, "    Col Range:", cr)
    #Adding empty columns to the left and right to account for potentially falling water
    gridRanges[2] -= 1
    gridRanges[3] += 1
    #If the minimum row isn't 0, we extend the range upward, because the water falls from row 0
    if gridRanges[0] > 0:
        gridRanges[0] = 0
    testing and print("Grid row range:", gridRanges[:2], "    col range:", gridRanges[2:])
    
    #Creating the 2D grid of characters to display the walls and water
    grid = []
    for row in range(gridRanges[0], gridRanges[1]+1):
        newRow = ['.'] * (gridRanges[3] - gridRanges[2])
        grid.append(newRow)
    for line in inpt:
        rr, cr = line
        for r in range(rr[0], rr[1]+1):
            for c in range(cr[0], cr[1]+1):
                grid[r][c-gridRanges[2]] = '#'
    grid[0][500-gridRanges[2]] = '+'
    
    if testing:
        for line in grid:
            print(''.join(line))
        
    #Locations of each water faucet. Goes until the area below it overflows or goes out of bounds
    faucets = [(0,500-gridRanges[2])]
    while len(faucets) > 0:
        r,c = faucets.pop(0)
        testing and print("Faucet", r,c)
        
        #Flowing down until the water goes out of bounds or hits something
        waterRow = r
        oob = False
        while True:
            if waterRow == len(grid)-1:
                testing and print("Faucet", r,c, "out of bounds at", waterRow,c)
                oob = True
                break
            elif grid[waterRow+1][c] == '.':
                grid[waterRow+1][c] = '|'
                waterRow += 1
            elif grid[waterRow+1][c] == '|':
                oob = True
                break
            else:
                testing and print("Faucet", r, c, "hits floor at", waterRow,c)
                break
                
        if oob:
            continue
            
        #Filling the row where the water hits until it overflows
        while True:
            testing and print("\tWater row:", waterRow)
            #Searching for a wall or dropoff to the left
            leftC = c-1
            leftWall = False
            while True:
                if grid[waterRow][leftC] == '#':
                    leftWall = True
                    break
                elif waterRow < len(grid)-1 and grid[waterRow+1][leftC] == '.':
                    break
                else:
                    leftC -= 1
            #Searching for a wall or dropoff to the right
            rightC = c+1
            rightWall = False
            while True:
                if grid[waterRow][rightC] == '#':
                    rightWall = True
                    break
                elif waterRow < len(grid)-1 and grid[waterRow+1][rightC] == '.':
                    break
                else:
                    rightC += 1
            
            #If both left and right are walls, we fill this area in with stationary water
            if leftWall and rightWall:
                testing and print("\t\tWalls left and right. Filling row", waterRow)
                for i in range(leftC+1, rightC):
                    grid[waterRow][i] = '~'
                waterRow -= 1
            #If there's a gap that water flows through, it's filled with flowing water
            else:
                testing and print("\t\tOverflowing left?", leftWall, "    Overflowing right?", rightWall)
                for i in range(leftC+1, rightC):
                    grid[waterRow][i] = '|'
                #Adding the dropoff points as new "faucets" since water flows down from there
                if not leftWall:
                    faucets.append((waterRow,leftC))
                    grid[waterRow][leftC] = '|'
                if not rightWall:
                    faucets.append((waterRow,rightC))
                    grid[waterRow][rightC] = '|'
                        
                for newR in range(r, waterRow):
                    grid[newR][c] = '|'
                if testing:
                    for line in grid:
                        testing and print(''.join(line))
                break
                
    grid[0][500-gridRanges[2]] = '+'
    ans = 0
    testing and print("\n\nFinal result")
    ignoreTop = True
    for line in grid:
        testing and print(''.join(line))
        #Ignoring all of the falling water that's above the first row of walls from our input (they don't count)
        if ignoreTop and line.count('#') > 0:
            ignoreTop = False
        if not ignoreTop:
            ans += line.count('|') + line.count('~')
    return ans


def solution2():
    inpt = getInput() #Row ranges, then col ranges
    
    #Finding the min and max row,col
    gridRanges = [None, None, None, None] #min row, max row, min col, max col
    for line in inpt:
        rr, cr = line
        if gridRanges[0] is None or rr[0] < gridRanges[0]:
            gridRanges[0] = rr[0]
        if gridRanges[1] is None or rr[1] > gridRanges[1]:
            gridRanges[1] = rr[1]
        if gridRanges[2] is None or cr[0] < gridRanges[2]:
            gridRanges[2] = cr[0]
        if gridRanges[3] is None or cr[1] > gridRanges[3]:
            gridRanges[3] = cr[1]
    #Adding empty columns to the left and right to account for potentially falling water
    gridRanges[2] -= 1
    gridRanges[3] += 1
    #If the minimum row isn't 0, we extend the range upward, because the water falls from row 0
    if gridRanges[0] > 0:
        gridRanges[0] = 0
    
    #Creating the 2D grid of characters to display the walls and water
    grid = []
    for row in range(gridRanges[0], gridRanges[1]+1):
        newRow = ['.'] * (gridRanges[3] - gridRanges[2])
        grid.append(newRow)
    for line in inpt:
        rr, cr = line
        for r in range(rr[0], rr[1]+1):
            for c in range(cr[0], cr[1]+1):
                grid[r][c-gridRanges[2]] = '#'
    grid[0][500-gridRanges[2]] = '+'
    
    if testing:
        for line in grid:
            print(''.join(line))
        
    #Locations of each water faucet. Goes until the area below it overflows or goes out of bounds
    faucets = [(0,500-gridRanges[2])]
    while len(faucets) > 0:
        r,c = faucets.pop(0)
        
        #Flowing down until the water goes out of bounds or hits something
        waterRow = r
        oob = False
        while True:
            if waterRow == len(grid)-1:
                oob = True
                break
            elif grid[waterRow+1][c] == '.':
                grid[waterRow+1][c] = '|'
                waterRow += 1
            elif grid[waterRow+1][c] == '|':
                oob = True
                break
            else: #grid[waterRow+1][c] == '#' or grid[waterRow+1][c] == '~':
                break
                
        if oob:
            continue
            
        #Filling the row where the water hits until it overflows
        while True:
            #Searching for a wall or dropoff to the left
            leftC = c-1
            leftWall = False
            while True:
                if grid[waterRow][leftC] == '#':
                    leftWall = True
                    break
                elif waterRow < len(grid)-1 and grid[waterRow+1][leftC] == '.':
                    break
                else:
                    leftC -= 1
            #Searching for a wall or dropoff to the right
            rightC = c+1
            rightWall = False
            while True:
                if grid[waterRow][rightC] == '#':
                    rightWall = True
                    break
                elif waterRow < len(grid)-1 and grid[waterRow+1][rightC] == '.':
                    break
                else:
                    rightC += 1
            
            #If both left and right are walls, we fill this area in with stationary water
            if leftWall and rightWall:
                for i in range(leftC+1, rightC):
                    grid[waterRow][i] = '~'
                waterRow -= 1
            #If there's a gap that water flows through, it's filled with flowing water
            else:
                for i in range(leftC+1, rightC):
                    grid[waterRow][i] = '|'
                #Adding the dropoff points as new "faucets" since water flows down from there
                if not leftWall:
                    faucets.append((waterRow,leftC))
                    grid[waterRow][leftC] = '|'
                if not rightWall:
                    faucets.append((waterRow,rightC))
                    grid[waterRow][rightC] = '|'
                        
                for newR in range(r, waterRow):
                    grid[newR][c] = '|'
                if testing:
                    for line in grid:
                        testing and print(''.join(line))
                break
                
    grid[0][500-gridRanges[2]] = '+'
    ans = 0
    for line in grid:
        ans += line.count('~')
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())