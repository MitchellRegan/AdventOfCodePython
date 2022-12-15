#https://adventofcode.com/2022/day/15
#https://adventofcode.com/2022/day/15#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d15_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d15_real.txt")


def getInput():
    inputList = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.split(' ')
            #Getting the xy coordinate of the sensor
            x1 = int(line[2][2:-1])
            y1 = int(line[3][2:-1])
            #Getting the xy coordinate of the beacon
            x2 = int(line[8][2:-1])
            y2 = line[9][2:]
            if y2[-1] == '\n':
                y2 = int(y2[:-1])
            else:
                y2 = int(y2)
            #Getting the sensor radius as the Manhattan distance from sensor to beacon
            manhattan = abs(x2 - x1) + abs(y2 - y1)

            inputList.append([(x1,y1),(x2,y2),manhattan])
    return inputList


def solution1(displaySolution=False):
    air = '.'
    beacon = 'B'
    sensor = 'S'
    invalid = 'X'

    sensors = getInput()
    minMaxX = [0,0]
    minMaxY = [0,0]
    for s in sensors:
        #Checking the x values from each coordinate to find the smallest x
        if min(s[0][0], s[1][0]) < minMaxX[0]:
            minMaxX[0] = min(s[0][0], s[1][0])
        #Checking the x values from each coordinate to find the largest x
        if max(s[0][0], s[1][0]) > minMaxX[1]:
            minMaxX[1] = max(s[0][0], s[1][0])
            
        #Checking the y values from each coordinate to find the smallest y
        if min(s[0][1], s[1][1]) < minMaxY[0]:
            minMaxY[0] = min(s[0][1], s[1][1])
        #Checking the y values from each coordinate to find the largest y
        if max(s[0][1], s[1][1]) > minMaxY[1]:
            minMaxY[1] = max(s[0][1], s[1][1])

    grid = []
    for r in range(minMaxY[0], minMaxY[1] + 1):
        grid.append([air] * (minMaxX[1] + 1 - minMaxX[0]))

    sensorRanges = []
    for s in sensors:
        x1 = s[0][0] - minMaxX[0]
        x2 = s[1][0] - minMaxX[0]
        y1 = s[0][1] - minMaxY[0]
        y2 = s[1][1] - minMaxY[0]
        grid[y1][x1] = sensor
        grid[y2][x2] = beacon
        #print("Sensor", s[0], "radius is", s[2])

    #Looping through each row/col position in the grid at the designated row to search
    row = 2000000 - minMaxY[0]
    invalidSpots = 0
    for col in range(0, len(grid[row])):
        if grid[row][col] is air:
            #Checking this position's manhattan distance away from each of the sensors
            for s in sensors:
                manhattan = abs(s[0][0] - (col + minMaxX[0])) + abs(s[0][1] - row)
                #If this location's distance from the sensor is within the sensor's radius, it's invalid
                if manhattan <= s[2]:
                    #print("Invalid pos:", row, col) 
                    #print(" - In range of sensor", s[0], "with radius", s[2])
                    #print(" - Distance:", manhattan)
                    #print(" - - X diff:", s[0][0], "-", (col + minMaxX[0]), "=", abs(s[0][0] - (col + minMaxX[0])))
                    grid[row][col] = invalid
                    invalidSpots += 1
                    break

    if displaySolution:
        for row in grid:
            print(''.join(row))
    return invalidSpots


def solution2():
    return


print("Year 2022, Day 15 solution part 1:", solution1(False))
print("Year 2022, Day 15 solution part 2:", solution2())