#https://adventofcode.com/2022/day/14
#https://adventofcode.com/2022/day/14#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d14_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d14_real.txt")


def getInputs():
    inputs = []
    minX = float("inf")
    maxX = -1 * float("inf")
    minY = 0
    maxY = -1 * float("inf")

    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            line = line.replace(" -> ", ",")
            lineInputs = line.split(',')
            pairs = []
            for i in range(0, len(lineInputs), 2):
                pairs.append((int(lineInputs[i]), int(lineInputs[i+1])))
                #Looking for min/max x values
                if pairs[-1][0] < minX:
                    minX = pairs[-1][0]
                elif pairs[-1][0] > maxX:
                    maxX = pairs[-1][0]
                #Looking for min/max y values
                if pairs[-1][1] < minY:
                    minY = pairs[-1][1]
                elif pairs[-1][1] > maxY:
                    maxY = pairs[-1][1]
            inputs.append(pairs)

    inputs.insert(0, (minX, maxX, minY, maxY))

    return inputs


def solution1(showOutput=False):
    air = ' '
    rock = '█'
    sand = '░'

    #Getting the puzzle inputs as lists of ordered pairs. Also index 0 is the dimensions of the cave
    inputs = getInputs()
    #Creating the grid to store the cave coordinates
    grid = []
    for r in range(0, (1 + inputs[0][3] - inputs[0][2])):
        newRow = [air] * (1 + inputs[0][1] - inputs[0][0])
        grid.append(newRow)

    #Filling in each of the correct tiles with rocks based on the inputs
    firstLine = True
    for line in inputs:
        if firstLine:
            firstLine = False
            continue
        #Place rocks in lines based on each point in this input line
        for coord in range(0, len(line)-1):
            x1 = min(line[coord][0], line[coord+1][0]) - inputs[0][0]
            x2 = max(line[coord][0], line[coord+1][0]) - inputs[0][0]
            y1 = min(line[coord][1], line[coord+1][1])
            y2 = max(line[coord][1], line[coord+1][1])

            #If the x values are the same, it's a vertical line
            if x1 == x2:
                for y in range(y1, y2+1):
                    grid[y][x1] = rock
            #If the y values are the same, it's a horizontal line
            elif y1 == y2:
                for x in range(x1, x2+1):
                    grid[y1][x] = rock
        
    #int for how many blocks of sand have fallen and come to rest
    numSand = 0
    #Looping to fill in sand until it goes out of index
    sandCol = 500 - inputs[0][0]
    sandRow = 0
    while True:
        #Checking if the sand falls out of index
        if sandRow+1 >= len(grid):
            break
        #Checking if there's an empty space below the current sand block to fall down
        if grid[sandRow+1][sandCol] == air:
            sandRow += 1
            continue

        #Checking if the sand goes out of index to the left
        if sandCol-1 < 0:
            break
        #If the space below is occupied, we have to check down-left
        if grid[sandRow+1][sandCol-1] == air:
            sandRow += 1
            sandCol -= 1
            continue

        #Checking if the sand goes out of index on the right
        if sandCol+1 >= len(grid[0]):
            break
        #If down-left is occupied, we check down-right
        if grid[sandRow+1][sandCol+1] == air:
            sandRow += 1
            sandCol += 1
            continue

        #If down, down-left, and down-right are occupied, the sand comes to rest and we move on
        else:
            grid[sandRow][sandCol] = sand
            sandRow = 0
            sandCol = 500 - inputs[0][0]
            numSand += 1

    if showOutput:
        grid[0][500 - inputs[0][0]] = "+"
        for r in grid:
            print(''.join(r))
    return numSand


def solution2(showOutput=False):
    air = ' '
    rock = '█'
    sand = '░'

    #Getting the puzzle inputs as lists of ordered pairs. Also index 0 is the dimensions of the cave
    inputs = getInputs()
    #Creating the grid to store the cave coordinates
    grid = []
    for r in range(0, (1 + inputs[0][3] - inputs[0][2])):
        newRow = [air] * (1 + inputs[0][1] - inputs[0][0])
        grid.append(newRow)
    #Adding the new lines below the bottom of the given grid. one row of air, and one of rock
    grid.append([air] * (1 + inputs[0][1] - inputs[0][0]))
    grid.append([rock] * (1 + inputs[0][1] - inputs[0][0]))

    #Filling in each of the correct tiles with rocks based on the inputs
    firstLine = True
    for line in inputs:
        if firstLine:
            firstLine = False
            continue
        #Place rocks in lines based on each point in this input line
        for coord in range(0, len(line)-1):
            x1 = min(line[coord][0], line[coord+1][0]) - inputs[0][0]
            x2 = max(line[coord][0], line[coord+1][0]) - inputs[0][0]
            y1 = min(line[coord][1], line[coord+1][1])
            y2 = max(line[coord][1], line[coord+1][1])

            #If the x values are the same, it's a vertical line
            if x1 == x2:
                for y in range(y1, y2+1):
                    grid[y][x1] = rock
            #If the y values are the same, it's a horizontal line
            elif y1 == y2:
                for x in range(x1, x2+1):
                    grid[y1][x] = rock
        
    #int for how many blocks of sand have fallen and come to rest
    numSand = 0
    #Looping to fill in sand until it goes out of index
    xOffset = 500 - inputs[0][0]
    sandCol = 500 - inputs[0][0]
    sandRow = 0
    while True:
        #Checking if there's an empty space below the current sand block to fall down
        if grid[sandRow+1][sandCol] == air:
            sandRow += 1
            continue

        #Checking if the sand would have out of index to the left, we make a new column
        if sandCol-1 < 0:
            for r in grid:
                r.insert(0, air)
            grid[-1][0] = rock
            xOffset += 1
            sandCol += 1

        #If the space below is occupied, we have to check down-left
        if grid[sandRow+1][sandCol-1] == air:
            sandRow += 1
            sandCol -= 1
            continue

        #Checking if the sand would have out of index on the right
        if sandCol+1 >= len(grid[0]):
            for r in grid:
                r.append(air)
            grid[-1][-1] = rock

        #If down-left is occupied, we check down-right
        if grid[sandRow+1][sandCol+1] == air:
            sandRow += 1
            sandCol += 1
            continue

        #If down, down-left, and down-right are occupied, the sand comes to rest and we move on
        else:
            numSand += 1
            grid[sandRow][sandCol] = sand
            #If the sand stops at the falling point, we break
            if sandRow == 0 and sandCol == xOffset:
                break
            else:
                sandRow = 0
                sandCol = xOffset

    if showOutput:
        for r in grid:
            print(''.join(r))
    return numSand


print("Year 2022, Day 14 solution part 1:", solution1(showOutput=False))
print("Year 2022, Day 14 solution part 2:", solution2(showOutput=False))