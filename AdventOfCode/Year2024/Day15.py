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
    moves = ""

    with open(inFile, 'r') as f:
        row = 0
        onGrid = True
        for line in f:
            line = line.replace('\n', '')

            if line == '':
                onGrid = False
            elif onGrid:
                if startPos is None and '@' in line:
                    startPos = [row, line.index('@')]
                    line = line.replace('@', '.')
                grid.append([x for x in line])
                row += 1
            else:
                moves = moves + line
    return grid, startPos, moves
            

def solution1():
    grid, startPos, moves = getInput()
    
    r,c = startPos
    for dir in moves:
        offset = (0,0)
        if dir == '^':
            offset = (-1,0)
        elif dir == 'v':
            offset = (1,0)
        elif dir == '<':
            offset = (0,-1)
        elif dir == '>':
            offset = (0,1)

        #Hitting a wall does nothing
        #if grid[r+offset[0]][c+offset[1]] == '#':

        #Hitting an empty space just moves our (r,c) pos
        if grid[r+offset[0]][c+offset[1]] == '.':
            r += offset[0]
            c += offset[1]
        #Hitting a box attempts to move all boxes in a line
        elif grid[r+offset[0]][c+offset[1]] == 'O':
            targetRow = r + offset[0]
            targetCol = c + offset[1]
            while grid[targetRow][targetCol] is 'O':
                targetRow += offset[0]
                targetCol += offset[1]

            #If the row of boxes can be moved to an empty space, we move them all
            if grid[targetRow][targetCol] == '.':
                grid[r+offset[0]][c+offset[1]] = '.'
                grid[targetRow][targetCol] = 'O'
                r += offset[0]
                c += offset[1]

    #Getting the final score based off of each box's (r,c) position
    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
                ans += (100 * row) + col
    return ans


def solution2():
    grid, startPos, moves = getInput()

    for r in range(len(grid)):
        newLine = ''.join(grid[r])
        newLine = newLine.replace('.', '..').replace('#', '##').replace('O', '[]')
        grid[r] = [x for x in newLine]

    r,c = startPos
    c *= 2
    
    testing and print("Grid:")
    for row in grid:
        print(''.join(row))
    testing and print("\nStart Pos:", (r,c), "\n\nMoves:")
    print(moves)
    return

    for dir in moves:
        testing and print("\nDirection:", dir)
        offset = (0,0)
        if dir == '^':
            offset = (-1,0)
        elif dir == 'v':
            offset = (1,0)
        elif dir == '<':
            offset = (0,-1)
        elif dir == '>':
            offset = (0,1)

        #Hitting a wall does nothing
        #if grid[r+offset[0]][c+offset[1]] == '#':

        #Hitting an empty space just moves our (r,c) pos
        if grid[r+offset[0]][c+offset[1]] == '.':
            r += offset[0]
            c += offset[1]
        #Hitting a box attempts to move all boxes in a line
        elif grid[r+offset[0]][c+offset[1]] == '[' or grid[r+offset[0]][c+offset[1]] == ']':
            targetRow = r + offset[0]
            targetCol = c + offset[1]
            while grid[targetRow][targetCol] == '[' or grid[targetRow][targetCol] == ']':
                targetRow += offset[0]
                targetCol += offset[1]

            #If the row of boxes can be moved to an empty space, we move them all
            if grid[targetRow][targetCol] == '.':
                grid[r+offset[0]][c+offset[1]] = '.'
                grid[targetRow][targetCol] = 'O'
                r += offset[0]
                c += offset[1]

        if testing:
            displayGrid = []
            for row in grid:
                displayGrid.append([x for x in row])
            displayGrid[r][c] = 'X'
            for row in displayGrid:
                print(''.join(row))

    #Getting the final score based off of each box's (r,c) position
    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '[':
                ans += (100 * row) + col
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())