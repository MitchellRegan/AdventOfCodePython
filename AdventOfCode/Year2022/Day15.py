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


def combineRanges(rangeList):
    while True:
        #List to hold any changes to do after looping since we can't do them in the loop
        #First index is i to remove, second is j to remove, and last is the new list to append
        newMerges = []

        for i in range(0, len(rangeList)-1):
            if len(newMerges) > 0:
                break
            for j in range(i+1, len(rangeList)):
                #If i is completely inside j
                if rangeList[i][0] >= rangeList[j][0] and rangeList[i][1] <= rangeList[j][1]:
                    newMerges = [i,j, rangeList[j]]
                    #print(" - 1:", rangeList[i], '+', rangeList[j], "=",  rangeList[j])
                    break
                #If j is completely inside i
                if rangeList[j][0] >= rangeList[i][0] and rangeList[j][1] <= rangeList[i][1]:
                    newMerges = [i,j, rangeList[i]]
                    #print(" - 2:", rangeList[i], '+', rangeList[j], "=",  rangeList[i])
                    break
                #If there's an overlap where i is smaller
                if rangeList[i][0] < rangeList[j][0] and rangeList[i][1] >= rangeList[j][0] and rangeList[i][1] <= rangeList[j][1]:
                    newMerges = [i,j, (rangeList[i][0], rangeList[j][1])]
                    #print(" - 3:", rangeList[i], '+', rangeList[j], "=", (rangeList[i][0], rangeList[j][1]))
                    break
                #If there's an overlap where j is smaller
                if rangeList[j][0] < rangeList[i][0] and rangeList[j][1] >= rangeList[i][0] and rangeList[j][1] <= rangeList[i][1]:
                    #print(" - 4:", rangeList[i], '+', rangeList[j], "=", (rangeList[j][0], rangeList[i][1]))
                    newMerges = [i,j, (rangeList[j][0], rangeList[i][1])]
                    break
                #If the left edge of i touches the right edge of j
                if rangeList[i][1] == rangeList[j][0]-1 or rangeList[i][1] == rangeList[j][0]:
                    #print(" - 5:", rangeList[i], '+', rangeList[j], "=", (rangeList[i][0], rangeList[j][1]))
                    newMerges = [i,j, (rangeList[i][0], rangeList[j][1])]
                    break
                #If the left edge of j touches the right edge of i
                if rangeList[j][1] == rangeList[i][0]-1 or rangeList[j][1] == rangeList[i][0]:
                    #print(" - 6:", rangeList[i], '+', rangeList[j], "=", (rangeList[j][0], rangeList[i][1]))
                    newMerges = [i,j, (rangeList[j][0], rangeList[i][1])]
                    break

        #If there are ranges to merge together we do that
        if len(newMerges) > 0:
            rangeList.append(newMerges[2]) #Append the merged list
            rangeList.pop(newMerges[1]) #Remove index j
            rangeList.pop(newMerges[0]) #Remove index i
        #If there are no merges left, we return the finished list
        else:
            rangeList.sort()
            return rangeList


def solution1():
    sensors = getInput()

    #Finding the size of the grid we're working with
    beacons = []
    minMaxX = [0,0]
    minMaxY = [0,0]
    for s in sensors:
        #Making sure the locations taken by the sensor and beacon are marked
        if s[1] not in beacons:
            beacons.append(s[1])

        #Checking the x values from each coordinate to find the smallest x
        if min(s[0][0] - s[2], s[1][0]) < minMaxX[0]:
            minMaxX[0] = min(s[0][0] - s[2], s[1][0])
        #Checking the x values from each coordinate to find the largest x
        if max(s[0][0] + s[2], s[1][0]) > minMaxX[1]:
            minMaxX[1] = max(s[0][0] + s[2], s[1][0])
            
        #Checking the y values from each coordinate to find the smallest y
        if min(s[0][1] - s[2], s[1][1]) < minMaxY[0]:
            minMaxY[0] = min(s[0][1] - s[2], s[1][1])
        #Checking the y values from each coordinate to find the largest y
        if max(s[0][1] + s[2], s[1][1]) > minMaxY[1]:
            minMaxY[1] = max(s[0][1] + s[2], s[1][1])

    #Looping through each row/col position in the grid at the designated row to search
    row = 2000000
    invalidSpots = 0
    for col in range(minMaxX[0], minMaxX[1]+1):
        #If the current location isn't already taken up by a beacon
        if (col, row) not in beacons:
            #Checking this position's manhattan distance away from each of the sensors
            for s in sensors:
                manhattan = abs(s[0][0] - col) + abs(s[0][1] - row)
                #If this location's distance from the sensor is within the sensor's radius, it's invalid
                if manhattan <= s[2]:
                    invalidSpots += 1
                    break

    return invalidSpots


def solution2():
    sensors = getInput()

    coordCap = 4000000
    #Starting from the point (0,0) and moving diagonally (i.e. (1,1), (2,2), (3,3)...)
    for p in range(0, coordCap+1):
        #Lists to hold the range of values in each row and each column that are covered by scanners in this loop
        colRanges = []
        rowRanges = []

        #Checking the range that each sensor
        for s in sensors:
            #Checking the ranges in this column
            xDiff = abs(s[0][0] - p)
            if xDiff <= s[2]:
                miny = s[0][1] - (s[2] - (xDiff))
                maxy = s[0][1] + (s[2] - (xDiff))
                colRanges.append((miny, maxy))

            yDiff = abs(s[0][1] - p)
            if yDiff < s[2]:
                minx = s[0][0] - ((s[2] - yDiff))
                maxx = s[0][0] + ((s[2] - yDiff))
                rowRanges.append((minx, maxx))
                #print("Row", p, "in range of scanner", s[0], ":distance", s[2], "covers", (minx,p), "to", (maxx,p), " with yDiff =", yDiff)

        colRanges = combineRanges(colRanges)
        if len(colRanges) > 1:
            x = p * 4000000
            y = (colRanges[1][0] + colRanges[0][1])//2
            return x+y
        rowRanges = combineRanges(rowRanges)
        if len(rowRanges) > 1:
            x = (rowRanges[1][0] + rowRanges[0][1])//2
            x *= 4000000
            y = p
            return x+y
    return


print("Year 2022, Day 15 solution part 1:", solution1())
print("Year 2022, Day 15 solution part 2:", solution2())