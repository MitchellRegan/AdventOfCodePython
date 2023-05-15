#https://adventofcode.com/2022/day/17
#https://adventofcode.com/2022/day/17#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d17_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d17_real.txt")

airSymb = '-'
rockSymb = 'O'
floorSymb = '#'
part1Iterations = 2022
part2Iterations = 1000 #1000000000000

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


def spawnRock_v3(rockID, windShift, rockGrid):
    #Finding the number of empty rows at the top of the grid
    empty = 0
    needed = 1
    for r in range(0, len(rockGrid)):
        if rockGrid[r] > 0:
            empty = r
            break

    # 2D list for rock coordinates. Each sub-list contains the row at index 0, and an int representing the binary state of the rock in that row
    rockPos = []

    #Getting the spawn coordinates for the new rock based on the rock ID
    if rockID == 0: # Horizontal line
        if windShift > 0:
            rockPos = [[0, 30>>1]] #can only shift 1 right before hitting a wall
        else:
            if windShift < -2: #Can only shift 2 left before hitting wall
                windShift = -2
            windShift *= -1
            rockPos = [[0, 30<<windShift]]
    elif rockID == 1: # Cross
        if windShift > 0:
            if windShift > 2:
                windShift = 2
            rockPos = [[0,8>>windShift], [1,28>>windShift], [2,8>>windShift]]
        else:
            if windShift < -2:
                windShift = -2
            windShift *= -1
            rockPos = [[0,8<<windShift], [1,28<<windShift], [2,8<<windShift]]
        needed = 3
    elif rockID == 2: # Backwards L
        if windShift > 0:
            if windShift > 2:
                windShift = 2
            rockPos = [[0,4>>windShift], [1,4>>windShift], [2,28>>windShift]]
        else:
            if windShift < -2:
                windShift = -2
            windShift *= -1
            rockPos = [[0,4<<windShift], [1,4<<windShift], [2,28<<windShift]]
        needed = 3
    elif rockID == 3: # Vertical line
        if windShift > 0:
            rockPos = [[0,16>>windShift], [1,16>>windShift], [2,16>>windShift], [3,16>>windShift]]
        else:
            if windShift < -2:
                windShift = -2
            windShift *= -1
            rockPos = [[0,16<<windShift], [1,16<<windShift], [2,16<<windShift], [3,16<<windShift]]
        needed = 4
    elif rockID == 4: # Square
        if windShift > 0:
            rockPos = [[0,24>>windShift], [1,24>>windShift]]
        else:
            if windShift < -2:
                windShift = -2
            windShift *= -1
            rockPos = [[0,24<<windShift], [1,24<<windShift]]
        needed = 2
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
                #If there is a blockage, we can remove all rows below the last one taken up by the new rock
                #if rowsFull:
                #    print("Height:", maxHeight, " Grid before row removal")
                #    for r in grid:
                #        print(''.join(r))
                #    maxHeight += max(rowsUsed)
                #    grid = grid[:maxRowsUsed+1]
                #    print("Height:", maxHeight, " Grid after row removal")
                #    for r in grid:
                #        print(''.join(r))
                #    return

    with open(os.path.join(inFileDir, "day17p2_visualization.txt"), 'w') as o:
        for r in range(0, len(grid)):
            o.write(''.join(grid[r]) + '\n')

    for r in range(0, len(grid)):
        if floorSymb in grid[r]:
            maxHeight += len(grid) - r - 1
            break
    return maxHeight


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

    #Variable to track the height of the rock stack
    maxHeight = 0

    #"grid" to hold the number of wall tiles in each row. These are represented by binary values where 0=air and 1=wall
    grid = [127]

    #List to hold the coordinate points of each tile for the current rock
    currRock = []

    #Cycling through 1000000000000 rocks falling
    for i in range(0, part2Iterations):
        #To eliminate the first 3 steps of falling, we get the sum of the next 3 wind shifts
        windShifts = [0,0,0]
        for b in range(0,3):
            windShifts[b] = wind[wi]
            wi += 1
            if wi == len(wind):
                wi = 0

        #Getting a new rock each cycle, which also increases the grid height to fit
        currRock = spawnRock_v3(i % 5, sum(windShifts), grid)
        #currRock = spawnRock_v2(i % 5, grid)

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

                
                # - 0 = Horizontal line, 1 = Cross, 2 = Backwards L shape, 3 = Vertical line, 4 = Square
                s = ''
                if i%5 == 0:
                    s = "Horizontal Line"
                elif i%5 == 1:
                    s = "Cross"
                elif i%5 == 2:
                    s = "Backwards L"
                elif i%5 == 3:
                    s = "Vertical Line"
                else:
                    s = "Square"
                #print("I = %3d,   Height = %4d,   Shape = %s" %(i, tempHeight, s))
                print(tempHeight)

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

    for r in range(0, len(grid)):
        binStr = bin(grid[r])[2:].zfill(7)
        print(binStr)
        if grid[r] > 0:
            maxHeight += len(grid) - r - 1
            break
    return maxHeight


import time
startTime = time.time()
print("Year 2022, Day 17 solution part 1:", solution1())
endTime1 = time.time() - startTime
print("Part 1 time: ", endTime1, "sec")
ips = part1Iterations / endTime1
completionTime = 1000000000000 / ips
completionTime /= 60
completionTime /= 60
completionTime /= 24
print("Estimated completion time of full input: ", completionTime, "days")

startTime = time.time()
print("Year 2022, Day 17 solution part 2:", solution2())
endTime2 = time.time() - startTime
print("Part 2 time: ", endTime2, "sec")
ips = part2Iterations / endTime2
completionTime = 1000000000000 / ips
completionTime /= 60
completionTime /= 60
completionTime /= 24
print("Estimated completion time of full input: ", completionTime, "days")