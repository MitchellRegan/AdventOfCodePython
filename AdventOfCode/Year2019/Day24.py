#https://adventofcode.com/2019/day/24
#https://adventofcode.com/2019/day/24#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d24_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d24_real.txt")


def getInput():
    grid = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            grid.append(line)

    return grid
            

def solution1():
    grid = getInput()
    rows = len(grid)
    cols = len(grid[0])
    
    #Getting the score of the initial grid's state
    initScore = 0
    for r in range(0, rows):
        for c in range(0, cols):
            if grid[r][c] == '#':
                initScore += 2**((r * rows) + c)
    foundScores = {initScore:True}
    
    #Looping until a previously-seen state is found again
    step = 0
    #while step < 10:
    while True:
        #Grid storing the next state, and keeping track of it's score as we update it
        nextGrid = []
        gridScore = 0
        for r in range(rows):
            rowString = ''
            for c in range(cols):
                adjBugs = 0
                if r > 0 and grid[r-1][c] == '#':
                    adjBugs += 1
                if r < rows-1 and grid[r+1][c] == '#':
                    adjBugs += 1
                if c > 0 and grid[r][c-1] == '#':
                    adjBugs += 1
                if c < cols-1 and grid[r][c+1] == '#':
                    adjBugs += 1
                    
                if grid[r][c] == '.': #empty
                    #Exactly 1 or 2 adjacent bugs makes this empty square infested
                    if adjBugs == 1 or adjBugs == 2:
                        rowString = rowString + '#'
                        gridScore += 2**((r * rows) + c)
                    else:
                        rowString = rowString + '.'
                else: #bug
                    #Exactly 1 adjacent bug keeps this square infested
                    if adjBugs == 1:
                        rowString = rowString + '#'
                        gridScore += 2**((r * rows) + c)
                    else:
                        rowString = rowString + '.'
                        
            nextGrid.append(rowString)
            
        #Re-seen grid states give our final answer
        if gridScore in foundScores.keys():
            #print("\n\nMinute", step)
            #for x in nextGrid:
            #    print(x)
            return gridScore
        
        #If the grid state hasn't been seen before, we save it and update the grid to it's next state
        foundScores[gridScore] = True
        grid = nextGrid
        step += 1
            
    return -1


def solution2():
    def makeBlankGrid()->list:
        '''Helper function to create a 5x5 grid of empty spaces.'''
        blank = [".....", ".....", "..?..", ".....", "....."]
        return blank
    
    currState = {-1:makeBlankGrid(), 0:getInput(), 1:makeBlankGrid()}
    currState[0] = [
        currState[0][0],
        currState[0][1],
        ''.join([currState[0][2][0], currState[0][2][1], '?', currState[0][2][3], currState[0][2][4]]),
        currState[0][3],
        currState[0][4]
    ]
    
    
    step = 0
    while step < 200:
        nextState = {}
        
        for level in currState.keys():
            nextLevel = []
            for r in range(5):
                rowStr = ""
                for c in range(5):
                    if r == 2 and c == 2:
                        rowStr = rowStr + '?'
                        continue

                    adjBugs = 0
                    
                    #Check UP--------------------------------------
                    if r == 0:
                        #Checking the next level up, position (1,2)
                        if level+1 in currState.keys() and currState[level+1][1][2] == '#':
                            adjBugs += 1
                    elif currState[level][r-1][c] == '?':
                        #Checking next level down, the entire bottom row
                        if level-1 in currState.keys():
                            adjBugs += currState[level-1][4].count('#')
                    elif currState[level][r-1][c] == '#':
                        adjBugs += 1
                        
                    #Check DOWN------------------------------------
                    if r == 4:
                        #Checking the next level up, position (3,2)
                        if level+1 in currState.keys() and currState[level+1][3][2] == '#':
                            adjBugs += 1
                    elif currState[level][r+1][c] == '?':
                        #Checking next level down, the entire top row
                        if level-1 in currState.keys():
                            adjBugs += currState[level-1][0].count('#')
                    elif currState[level][r+1][c] == '#':
                        adjBugs += 1
                    
                    #Check LEFT------------------------------------
                    if c == 0:
                        #Checking the next level up, position (2,1)
                        if level+1 in currState.keys() and currState[level+1][2][1] == '#':
                            adjBugs += 1
                    elif currState[level][r][c-1] == '?':
                        #Checking next level down, the entire right column
                        if level-1 in currState.keys():
                            adjBugs += [
                                            currState[level-1][0][4],
                                            currState[level-1][1][4],
                                            currState[level-1][2][4],
                                            currState[level-1][3][4],
                                            currState[level-1][4][4]
                                        ].count('#')
                    elif currState[level][r][c-1] == '#':
                        adjBugs += 1
                    
                    #Check RIGHT-----------------------------------
                    if c == 4:
                        #Checking the next level up, position (2,3)
                        if level+1 in currState.keys() and currState[level+1][2][3] == '#':
                            adjBugs += 1
                    elif currState[level][r][c+1] == '?':
                        #Checking next level down, the entire left column
                        if level-1 in currState.keys():
                            adjBugs += [
                                            currState[level-1][0][0],
                                            currState[level-1][1][0],
                                            currState[level-1][2][0],
                                            currState[level-1][3][0],
                                            currState[level-1][4][0]
                                        ].count('#')
                    elif currState[level][r][c+1] == '#':
                        adjBugs += 1
                    
                    #Checking to see if this tile will be bug or empty in the next state
                    if currState[level][r][c] == '#':
                        if adjBugs == 1:
                            rowStr = rowStr + '#'
                        else:
                            rowStr = rowStr + '.'
                    else:
                        if adjBugs == 1 or adjBugs == 2:
                            rowStr = rowStr + '#'
                        else:
                            rowStr = rowStr + '.'
                        
                nextLevel.append(rowStr)
                
            #Storing the state for this level at the next step
            nextState[level] = nextLevel
            
            #If any bugs are on the outside edge of this level, a new level must be created above this one
            if level+1 not in currState.keys():
                if nextLevel[0].count('#') > 0 or nextLevel[4].count('#') > 0 or\
                    nextLevel[1][0] == '#' or nextLevel[1][4] == '#' or\
                    nextLevel[2][0] == '#' or nextLevel[2][4] == '#' or\
                    nextLevel[3][0] == '#' or nextLevel[3][4] == '#':
                    nextState[level+1] = makeBlankGrid()

            #if any bugs are on the inside edge of this level, a new level must be created below this one
            if level-1 not in currState.keys():
                if nextLevel[1][2] == '#' or nextLevel[2][1] == '#' or\
                    nextLevel[2][3] == '#' or nextLevel[3][2] == '#':
                    nextState[level-1] = makeBlankGrid()
            
        step += 1
        currState = nextState
            

    bugCount = 0
    for level in currState.keys():
        #print("=============== LEVEL", level, "===============")
        for r in currState[level]:
            #print(r)
            bugCount += r.count('#')
        #print()
    return bugCount


print("Year 2019, Day 24 solution part 1:", solution1())
print("Year 2019, Day 24 solution part 2:", solution2())