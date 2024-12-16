aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
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

    def moveBoxHorizontal(boxRow_:int, boxLeftCol_:int, colOffset_:int)->bool:
        '''Recursive function to try moving a box in the offset direction. Goes off of the LEFT '[' square bracket
        (row,col) position of a box. Returns True if it was moved.'''

        if colOffset_ == -1: #move left
            if grid[boxRow_][boxLeftCol_-1] == '#':
                return False
            if grid[boxRow_][boxLeftCol_-1] == '.' or moveBoxHorizontal(boxRow_, boxLeftCol_-2, colOffset_):
                grid[boxRow_][boxLeftCol_-1] = '['
                grid[boxRow_][boxLeftCol_] = ']'
                grid[boxRow_][boxLeftCol_+1] = '.'
                return True
            return False
        else: #move right
            if grid[boxRow_][boxLeftCol_+2] == '#':
                return False
            if grid[boxRow_][boxLeftCol_+2] == '.' or moveBoxHorizontal(boxRow_, boxLeftCol_+2, colOffset_):
                grid[boxRow_][boxLeftCol_+1] = '['
                grid[boxRow_][boxLeftCol_+2] = ']'
                grid[boxRow_][boxLeftCol_] = '.'
                return True
            return False


    def canMoveBoxVertical(r_:int, c_:int, rowOffset_:int)->bool:
        '''Recursive call to check if a box can be moved vertically (DOES NOT ACTUALLY MOVE THE BOX)'''

        #Defining the (row,col) position for the left '[' and right ']' sides of the box for readability
        leftCol = c_
        rightCol = c_+1
        if grid[r_][c_] == ']':
            leftCol = c_-1
            rightCol = c_

        if grid[r_+rowOffset_][leftCol] == '.' and grid[r_+rowOffset_][rightCol] == '.':
            return True
        
        if grid[r_+rowOffset_][leftCol] == '#' or grid[r_+rowOffset_][rightCol] == '#':
            return False

        if grid[r_+rowOffset_][leftCol] == '[':
            return canMoveBoxVertical(r_+rowOffset_, leftCol, rowOffset_)

        otherBox1 = True 
        if grid[r_+rowOffset_][leftCol] == ']':
            otherBox1 = canMoveBoxVertical(r_+rowOffset_, leftCol, rowOffset_)
        otherBox2 = True
        if grid[r_+rowOffset_][rightCol] == '[':
            otherBox2 = canMoveBoxVertical(r_+rowOffset_, rightCol, rowOffset_)
        return otherBox1 and otherBox2


    def moveBoxVertical(r_:int, c_:int, rowOffset_:int):
        '''Recursive call to move this box and all boxes it runs into.'''

        #Defining the (row,col) position for the left '[' and right ']' sides of the box for readability
        leftCol = c_
        rightCol = c_+1
        if grid[r_][c_] == ']':
            leftCol = c_-1
            rightCol = c_

        if grid[r_+rowOffset_][leftCol] == '[':
            moveBoxVertical(r_+rowOffset_, leftCol, rowOffset_)
        elif grid[r_+rowOffset_][leftCol] == ']':
            moveBoxVertical(r_+rowOffset_, leftCol, rowOffset_)
            if grid[r_+rowOffset_][rightCol] == '[':
                moveBoxVertical(r_+rowOffset_, rightCol, rowOffset_)
        elif grid[r_+rowOffset_][rightCol] == '[':
            moveBoxVertical(r_+rowOffset_, rightCol, rowOffset_)

        grid[r_+rowOffset_][leftCol] = '['
        grid[r_+rowOffset_][rightCol] = ']'
        grid[r_][leftCol] = '.'
        grid[r_][rightCol] = '.'
        return

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
        elif grid[r+offset[0]][c+offset[1]] == '[' or grid[r+offset[0]][c+offset[1]] == ']':
            if dir == '>' and moveBoxHorizontal(r, c+1, 1):
                r += offset[0]
                c += offset[1]
            elif dir == '<' and moveBoxHorizontal(r, c-2, -1):
                r += offset[0]
                c += offset[1]
            elif dir == 'v' or dir == '^':
                if canMoveBoxVertical(r+offset[0], c, offset[0]):
                    moveBoxVertical(r+offset[0], c, offset[0])
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