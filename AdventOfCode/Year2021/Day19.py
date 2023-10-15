#https://adventofcode.com/2021/day/19
#https://adventofcode.com/2021/day/19#part2

import os
import math as Math
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


def rotateScanner(sIndex_:int, axis_:str, rot_:int):
    '''Rotates the relative position of all beacons for a given scanner.
    Parameters
    ----------
        sIndex_: Index for the scanner to perform the rotation on.
        axis_: Char for which axis to rotate along. Must be X, Y, or Z.
        rot_: The degree of rotation to move the beacons. Must be evenly divisible by 90.

    Returns: None
    '''
    #Performing sanity checks on our inputs to make sure they're valid
    if axis_.lower() not in ['x', 'y', 'z']:
        print("ERROR: Invalid axis rotation. Must be either X, Y, or Z. Axis given:", axis_)
        return
    if rot_ % 90 != 0:
        print("ERROR: Invalid rotation degree. Must be divisible by 90. Rotation given:", rot_)
        return

    rot = (rot_/180) * Math.pi
    print("Rotating scanner", sIndex_, rot, "degrees along the", axis_, "axis.")
    print("\tBeacon 1 starting position:", scanners[sIndex_][0])

    #Iterating through each beacon for the designated scanner
    for b in range(len(scanners[sIndex_])):
        #Picking the correct axis to turn on
        if axis_ == 'x' or axis_ == 'X':
            newY = (scanners[sIndex_][b][1] * Math.cos(rot)) - (scanners[sIndex_][b][2] * Math.sin(rot))
            newZ = (scanners[sIndex_][b][1] * Math.sin(rot)) + (scanners[sIndex_][b][2] * Math.cos(rot))
            scanners[sIndex_][b] = [scanners[sIndex_][b][0], newY, newZ]
        if axis_ == 'y' or axis_ == 'Y':
            newX = (b[0] * Math.cos(rot)) + (b[2] * Math.sin(rot))
            newZ = (b[2] * Math.cos(rot)) - (b[0] * Math.sin(rot))
            b = [newX, b[1], newZ]
        if axis_ == 'z' or axis_ == 'Z':
            newX = (b[0] * Math.cos(rot)) - (b[1] * Math.sin(rot))
            newY = (b[0] * Math.sin(rot)) + (b[1] * Math.cos(rot))
            b = [newX, newY, b[2]]

    print("\tBeacon 1 new position:", scanners[sIndex_][0])
    return


def combineScanners(s1_:int, s1b1_:list, s1b2_:list, s2_:int, s2b1_:list, s2b2_:list):
    '''Combines all beacons from two given scanners based on matching points.
    Parameters
    ----------
        s1_: Index for the first scanner to merge.
        s1b1_: Coordinate point for the beacon in scanner 1 that is a matching point to s2b1_.
        s1b2_: Coordinate point for the beacon in scanner 1 that is a matching point to s2b2_.
        s2_: Index for the second scanner to merge.
        s2b1_: Coordinate point for the beacon in scanner 1 that is a matching point to s1b1_.
        s2b2_: Coordinate point for the beacon in scanner 1 that is a matching point to s1b2_.

    Returns: None
    '''

    return


def solution1():

    #In each scanner, we need to find the relative distances that each of its beacons are from one another
    for s in scanners.keys():
        print("Scanner", s)
        for b in scanners[s]:
            shortestDists = []
            #Finding the shortest distance to the nearest beacon (besides itself)
            for o in scanners[s]:
                if b is o:
                    continue
                #Finding the 3-dimensional Manhattan distance between these beacons
                xDist = abs(o[0] - b[0])
                yDist = abs(o[1] - b[1])
                zDist = abs(o[2] - b[2])
                shortestDists.append(xDist + yDist + zDist)

            #Once all Manhattan distances are found, we sort the list in ascending order so that the first 3 are the shortest
            shortestDists.sort()

            #Storing the 3 shortest distances as a tuple-key and this beacon's ID as one of the values associated with it
            if (shortestDists[0], shortestDists[1], shortestDists[2]) in distanceDict.keys():
                distanceDict[(shortestDists[0], shortestDists[1], shortestDists[2])].append((s,b))
            else:
                distanceDict[(shortestDists[0], shortestDists[1], shortestDists[2])] = [(s,b)]

            print("\tBeacon", b, "distances:", shortestDists[:3])
            
    print("\n====================================================\n")

    #Comparing each scanner against each other scanner to look for matching manhattan distances
    for d in distanceDict.keys():
        #When a match is found, we combine the scanners that share a matching beacon
        if len(distanceDict[d]) > 1:
            print("Matches:", distanceDict[d])
            combineSensors(distanceDict[d][0][0], distanceDict[d][1][0], )
    return


def solution2():

    return


#Dictionary where the key is an int for a scanner ID index, and the paired value is a list of tuples for relative (x,y,z) coords of each beacon it sees
scanners = getInput()
rotateScanner(0, "xa", 89)
rotateScanner(0, "x", 90)
#Dictionary where the key is a tuple for 3 manhattan distances in ascending order, and the paired value is a list where each element is a tuple (scanner#, (beaconX, beaconY, beaconZ))
distanceDict = {}
#print("Year 2021, Day 19 solution part 1:", solution1())
#print("Year 2021, Day 19 solution part 2:", solution2())