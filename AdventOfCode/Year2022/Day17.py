#https://adventofcode.com/2022/day/17
#https://adventofcode.com/2022/day/17#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d17_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d17_real.txt")

airSymb = '-'
rockSymb = 'O'
floorSymb = '#'
part1Iterations = 16
part2Iterations = 1000000 #1000000000000

def spawnRock(rockID, rockGrid):
    #Finding the number of empty rows at the top of the grid
    empty = 0
    needed = 4
    for r in range(0, len(rockGrid)):
        if floorSymb in rockGrid[r]:
            empty = r
            break

    #Getting the spawn coordinates for the new rock based on the rock ID
    # - 0 = Horizontal line, 1 = Cross, 2 = Backwards L shape, 3 = Vertical line, 4 = Square
    rockPos = []
    if rockID == 0:
        rockPos = [[2,0], [3,0], [4,0], [5,0]]
    elif rockID == 1:
        rockPos = [[3,2], [2,1], [3,1], [4,1], [3,0]]
        needed = 6
    elif rockID == 2:
        rockPos = [[2,2], [3,2], [4,2], [4,1],[4,0]]
        needed = 6
    elif rockID == 3:
        rockPos = [[2,3], [2,2], [2,1], [2,0]]
        needed = 7
    elif rockID == 4:
        rockPos = [[2,1], [3,1], [2,0], [3,0]]
        needed = 5
    else:
        print("Spawn Rock invalid input:", rockID)
        rockPos = None

    #If we need to add more rows to the top of the grid
    if needed - empty > 0:
        #Adding new lines to the grid to accomodate the spawned rock's location
        for l in range(0, needed - empty):
            rockGrid.insert(0, [airSymb, airSymb, airSymb, airSymb, airSymb, airSymb, airSymb])
    #If we have too many rows
    elif needed - empty < 0:
        for l in range(0, empty - needed):
            rockGrid.pop(0)

    #Placing the rock tiles in the grid
    for r in rockPos:
        rockGrid[r[1]][r[0]] = rockSymb

    return rockPos


def spawnRock_v2(rockID, rockGrid):
    #Finding the number of empty rows at the top of the grid
    empty = 0
    needed = 4
    for r in range(0, len(rockGrid)):
        if rockGrid[r] > 0:
            empty = r
            break

    # 2D list for rock coordinates. Each sub-list contains the row at index 0, and an int representing the binary state of the rock in that row
    rockPos = []

    #Getting the spawn coordinates for the new rock based on the rock ID
    if rockID == 0: # Horizontal line
        rockPos = [[0, 30]]
    elif rockID == 1: # Cross
        rockPos = [[0,8], [1,28], [2,8]]
        needed = 6
    elif rockID == 2: # Backwards L
        rockPos = [[0,4], [1,4], [2,28]]
        needed = 6
    elif rockID == 3: # Vertical line
        rockPos = [[0,16], [1,16], [2,16], [3,16]]
        needed = 7
    elif rockID == 4: # Square
        rockPos = [[0,24], [1,24]]
        needed = 5
    else:
        print("Spawn Rock invalid input:", rockID)
        rockPos = None

    #If we need to add more rows to the top of the grid
    if needed - empty > 0:
        #Adding new lines to the grid to accomodate the spawned rock's location
        for l in range(0, needed - empty):
            rockGrid.insert(0, 0)
    #If we have too many rows
    elif needed - empty < 0:
        for l in range(0, empty - needed):
            rockGrid.pop(0)

    return rockPos


def spawnRock_v3(rockID, rockGrid):
    #Finding the number of empty rows at the top of the grid
    empty = 0
    needed = 4
    for r in range(0, len(rockGrid)):
        if rockGrid[r] > 0:
            empty = r
            break

    # 2D list for rock coordinates. Each sub-list contains the row at index 0, and an int representing the binary state of the rock in that row
    rockPos = []

    #Getting the spawn coordinates for the new rock based on the rock ID
    if rockID == 0: # Horizontal line
        # Shape: |--1111-| = 30
        rockPos = [[0, 30]]
    elif rockID == 1: # Cross
        # Shape: |---1---| = 8
        #        |--111--| = 28
        #        |---1---| = 8
        rockPos = [[0,8], [1,28], [2,8]]
        needed = 6
    elif rockID == 2: # Backwards L
        # Shape: |----1--| = 4
        #        |----1--| = 4
        #        |--111--| = 28
        rockPos = [[0,4], [1,4], [2,28]]
        needed = 6
    elif rockID == 3: # Vertical line
        # Shape: |--1----| = 16
        #        |--1----| = 16
        #        |--1----| = 16
        #        |--1----| = 16
        rockPos = [[0,16], [1,16], [2,16], [3,16]]
        needed = 7
    elif rockID == 4: # Square
        # Shape: |--11---| = 24
        #        |--11---| = 24
        rockPos = [[0,24], [1,24]]
        needed = 5
    else:
        print("Spawn Rock invalid input:", rockID)
        rockPos = None

    #If we need to add more rows to the top of the grid
    if needed - empty > 0:
        #Adding new lines to the grid to accomodate the spawned rock's location
        for l in range(0, needed - empty):
            rockGrid.insert(0, 0)
    #If we have too many rows
    elif needed - empty < 0:
        for l in range(0, empty - needed):
            rockGrid.pop(0)

    return rockPos


def solution1():
    #Getting the inputs for the direction the wind will be blowing, and the index to track it's current movement
    wi = 0
    wind = ""
    with open(inFile, 'r') as f:
        for line in f:
            wind = line
            
    #Variable to track the height of the rock stack
    maxHeight = 0

    #2D Grid to hold the rocks that's 7 tiles wide
    grid = [[floorSymb, floorSymb, floorSymb, floorSymb, floorSymb, floorSymb, floorSymb]]

    #List to hold the coordinate points of each tile for the current rock
    currRock = []

    #Cycling through 2022 rocks falling
    for i in range(0, part1Iterations):
        print("Wind Index at start of iteration", i, "is:", wi)
        #Getting a new rock each cycle, which also increases the grid height to fit
        currRock = spawnRock(i % 5, grid)

        #Looping until the rock comes to rest
        rockFalling = True
        while rockFalling:
            #Gust of wind goes either left or right
            if wind[wi] is '>':
                #Checking all rock movements to the right to see if it can be shifted
                canMove = True
                for r in currRock:
                    if r[0] + 1 > 6:
                        canMove = False
                        break
                    elif grid[r[1]][r[0]+1] is floorSymb:
                        canMove = False
                        break
                #If it can be moved, we update the position of the rock right
                if canMove:
                    for r in currRock:
                        grid[r[1]][r[0]] = airSymb
                    for r in currRock:
                        grid[r[1]][r[0]+1] = rockSymb
                        r[0] += 1
            elif wind[wi] is '<':
                #Checking all rock movements to the left to see if it can be shifted
                canMove = True
                for r in currRock:
                    if r[0] - 1 < 0:
                        canMove = False
                        break
                    elif grid[r[1]][r[0]-1] is floorSymb:
                        canMove = False
                        break
                #If it can be moved, we update the position of the rock left
                if canMove:
                    for r in currRock:
                        grid[r[1]][r[0]] = airSymb
                    for r in currRock:
                        grid[r[1]][r[0]-1] = rockSymb
                        r[0] -= 1

            #incrementing the wind index for the next loop
            wi += 1
            if wi >= len(wind):
                wi = 0

            #Checking if the rock can move down
            canMove = True
            for r in currRock:
                if grid[r[1]+1][r[0]] is floorSymb:
                    canMove = False
                    break
            #If it can be moved, we update the position of each falling rock in the grid
            if canMove:
                for r in currRock:
                    grid[r[1]][r[0]] = airSymb
                for r in currRock:
                    grid[r[1]+1][r[0]] = rockSymb
                    r[1] += 1
            #If it can't move, we lock the positions in place and move to the next rock
            else:
                rowsUsed = []
                for r in currRock:
                    grid[r[1]][r[0]] = floorSymb
                    if r[1] not in rowsUsed:
                        rowsUsed.append(r[1])
                rockFalling = False

                #Checking if any of the rows taken up by this rock block off previous rows
                spaces = [0] * 7
                for r in rowsUsed:
                    for c in range(0, len(grid[r])):
                        if grid[r][c] is floorSymb:
                            spaces[c] += 1
                rowsFull = True
                for s in spaces:
                    if s == 0:
                        rowsFull = False
                        break

        #print("Iteration", i)
        #for r in grid:
        #    print(''.join(r))
        #print()

    for r in range(0, len(grid)):
        if floorSymb in grid[r]:
            maxHeight += len(grid) - r - 1
            break
    return maxHeight


def patternFinder(heights_):
    #print("Pattern Finder")
    #print(heights_)
    #print("Initial value of i:", int(len(heights_)/2))
    #Looking for patterns starting with the first half of the list and working down to smaller list sizes
    for i in range(int(len(heights_)/2), 1, -1):
        subList = heights_[:i]
        #print("\t", subList, " Initial sublist")
        patternFound = True
        #Checking the first sublist against all possible sublists of the same size in the rest of the list
        for j in range(1, int(len(heights_)/i)):
            nextSubList = heights_[i*j:i*(j+1)]
            #print("\t", nextSubList, " <-- Checking")
            #If the pattern doesn't match any of the other sublists, we move to the next pattern
            if nextSubList != subList:
                patternFound = False
                break
        #If a pattern was found, we output the length of the pattern and all of the values in it
        if patternFound:
            print("PATTERN FOUND! LENGTH:", i)
            for p in subList:
                print(p)
            return
    #Otherwise we indicate that no pattern was found
    print("No pattern found")


def solution2():
    #Getting the inputs for the direction the wind will be blowing, and the index to track it's current movement
    wi = 0
    wind = None
    with open(inFile, 'r') as f:
        for line in f:
            wind = [0] * len(line)
            for c in range(0, len(line)):
                if line[c] is '>':
                    wind[c] = 1
                elif line[c] is '<':
                    wind[c] = -1
                else:
                    print("READING ERROR", line[c])
            
    #Key: (grid height, wind index, shape index). Value: Grid's current state
    memo = {}
    #List to track the max height after each block lands
    heightTracker = [0]

    #Variable to track the height of the rock stack
    maxHeight = 0

    #"grid" to hold the number of wall tiles in each row. These are represented by binary values where 0=air and 1=wall
    grid = [127]

    #List to hold the coordinate points of each tile for the current rock
    currRock = []

    #Cycling through 1000000000000 rocks falling
    for i in range(0, part2Iterations):
        #Getting a new rock each cycle, which also increases the grid height to fit
        currRock = spawnRock_v3(i % 5, grid)

        #Looping until the rock comes to rest
        rockFalling = True
        while rockFalling:
            #Gust of wind goes either left or right
            if wind[wi] == 1:
                #Checking all rock movements to the right to see if it can be shifted
                canMove = True
                for r in currRock:
                    if r[1] % 2 == 1: #The 1st bit is 1, so if it's 1, can't go further right
                        canMove = False
                        break
                    elif grid[r[0]] & (r[1]>>1) > 0: #Bitwise comparison to see if there's overlap
                        canMove = False
                        break
                #If it can be moved, we update the position of the rock right
                if canMove:
                    for r in currRock:
                        r[1] = r[1] >> 1
            elif wind[wi] == -1:
                #Checking all rock movements to the left to see if it can be shifted
                canMove = True
                for r in currRock:
                    if r[1] > 63: #The 7th bit is 64, so if it's 1, can't go further left
                        canMove = False
                        break
                    elif grid[r[0]] & (r[1]<<1) > 0: #Bitwise comparison to see if there's overlap
                        canMove = False
                        break
                #If it can be moved, we update the position of the rock left
                if canMove:
                    for r in currRock:
                        r[1] = r[1] << 1

            #incrementing the wind index for the next loop
            wi += 1
            if wi >= len(wind):
                wi = 0

            #Checking if the rock can move down
            canMove = True
            for r in currRock:
                if grid[r[0]+1] & r[1] > 0: #Bitwise comparison to see if there's overlap
                    canMove = False
                    break
            #If it can be moved, we update the position of each falling rock in the grid
            if canMove:
                for r in currRock:
                    r[0] += 1
            #If it can't move, we lock the positions in place and move to the next rock
            else:
                rowsUsed = []
                for r in currRock:
                    grid[r[0]] += r[1]
                    #If this grid row is full, we mark it as a point where we can cut off the bottom of the list
                    if grid[r[0]] == 127:
                        rowsUsed.append(r[0])
                rockFalling = False

                tempHeight = maxHeight
                for r in range(0, len(grid)):
                    if grid[r] > 0:
                        tempHeight += len(grid) - r - 1
                        break


                #If there is a blockage, we can remove all rows below the last one taken up by the new rock
                if len(rowsUsed) > 0:
                    maxHeight += len(grid) - max(rowsUsed) - 1
                    grid = grid[:max(rowsUsed)+1]

                    #If this state has been seen before in our memoization, we make a note of it
                    m = (len(grid), wi, i % 5)
                    if m in memo.keys():
                        if grid == memo[m][1]:
                            print("======= FOUND A MATCH AT ROCK", memo[m][0])
                            return
                    else:
                        memo[m] = (i, grid)

        #print("Iteration", i)
    for r in range(0, len(grid)):
        binStr = bin(grid[r])[2:].zfill(7)
        #print(binStr)
        if grid[r] > 0:
            maxHeight += len(grid) - r - 1
            break

    #Looking for patterns in how much each block increases the stack height
    for i in range(len(heightTracker)-1, 0, -1):
        heightTracker[i] -= heightTracker[i-1]
    heightTracker.pop(0)
    patternFinder(heightTracker)
    return maxHeight


import time
if False:
    #startTime = time.time()
    print("Year 2022, Day 17 solution part 1:", solution1())
    #endTime1 = time.time() - startTime
    #print("Part 1 time: ", endTime1, "sec")
    #ips = part1Iterations / endTime1
    #completionTime = 1000000000000 / ips
    #completionTime /= 60
    #completionTime /= 60
    #completionTime /= 24
    #print("Estimated completion time of full input: ", completionTime, "days")

if True:
    #startTime = time.time()
    print("Year 2022, Day 17 solution part 2:", solution2())
    #endTime2 = time.time() - startTime
    #print("Part 2 time: ", endTime2, "sec")
    #ips = part2Iterations / endTime2
    #completionTime = 1000000000000 / ips
    #completionTime /= 60
    #completionTime /= 60
    #completionTime /= 24
    #print("Estimated completion time of full input: ", completionTime, "days")

#for i in range(1, 101):
#    part2Iterations = i*10000
#    print(i*10000, "=", solution2())