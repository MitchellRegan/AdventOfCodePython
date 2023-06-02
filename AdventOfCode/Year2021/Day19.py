#https://adventofcode.com/2021/day/19
#https://adventofcode.com/2021/day/19#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


def getInput():
    #Dictionary where the key is the ID number of the scanner, and the value is a list of ordered tuples for each beacon's relative coordinates
    scanners = {}

    with open(inFile, 'r') as f:
        scannerIndex = 0
        for line in f:
            #A blank line indicates that we're moving to a new scanner
            if line == '\n':
                scannerIndex += 1
            #If a line is "--- scanner # ---" we can skip it
            elif line[1] == '-':
                continue
            #Otherwise it is a beacon's relative xyz coordinate points
            else:
                if line[-1] == '\n':
                    line = line[:-1]
                vals = line.split(',')
                coords = [int(vals[0]), int(vals[1]), int(vals[2])]
                if scannerIndex not in scanners.keys():
                    scanners[scannerIndex] = [coords]
                else:
                    scanners[scannerIndex].append(coords)

    return scanners


def solution1():
    scanners = getInput()
    for s in scanners.keys():
        print("Scanner", s)
        for b in scanners[s]:
            shortestDist = -1
            #Finding the shortest distance to the nearest beacon
            for o in scanners[s]:
                if b is o:
                    continue
                #Finding the 3-dimensional Manhattan distance between these beacons
                xDist = abs(o[0] - b[0])
                yDist = abs(o[1] - b[1])
                zDist = abs(o[2] - b[2])
                manhattanDist = xDist + yDist +zDist

                if shortestDist == -1:
                    shortestDist = manhattanDist
                elif shortestDist > manhattanDist:
                    shortestDist = manhattanDist

            #Storing the shortest manhattan distance in the beacon
            b.append(shortestDist)
            print("\t", b)

    #Comparing each scanner against each other scanner to look for matching manhattan distances
    for i in range(0, len(scanners.keys())-1):
        for j in range(i+1, len(scanners.keys())):
            sameDists = 0
            for b1 in scanners[i]:
                for b2 in scanners[j]:
                    #If two beacons have the same Manhattan distance, we keep track of the similarity
                    if b1[3] == b2[3]:
                        sameDists += 1
            if sameDists >= 12:
                print("Scanner", i, "and Scanner", j, "have", sameDists, "in common")
    return


def solution2():

    return


print("Year 2021, Day 19 solution part 1:", solution1())
print("Year 2021, Day 19 solution part 2:", solution2())