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
    
    currState = [makeBlankGrid(), getInput(), makeBlankGrid()]
    for g in range(0, len(currState)):
        print("Level", g)
        for line in currState[g]:
            print(line)
        print('\n')
    
    step = 0
    while step < 200:
        
        step += 1
            
    return -1


print("Year 2019, Day 24 solution part 1:", solution1())
print("Year 2019, Day 24 solution part 2:", solution2())