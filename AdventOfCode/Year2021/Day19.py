#https://adventofcode.com/2021/day/19
#https://adventofcode.com/2021/day/19#part2

import os
import math as Math
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


#Thought Process for Part 1:
    #Get a global hash map to store the scanner and beacon puzzle inputs:
        #Key: index number of the scanner
        #Pair: list of each beacon's xyz coordinate positions relative to the scanner
    #Loop the following until there's only one scanner remaining (because all others have been merged into it)
        #Create meta-data for each beacon to store the Manhattan distances to the 3 nearest beacons in ascending order
            #This step has to be re-done every iteration because a beacon's closest manhattan distances can change after scanners merge
        #Store this data in a hash map
            #Key: tuple of the 3 closest manhattan distances of a beacon. Example: (23, 155, 349)
            #Pair: list of each beacon with this meta-data. Example: [(scanner 1, beacon 3), (scanner 5, beacon 9), ...]
            #Beacons in the paired list with the same hash key will have a high likelihood of being duplicates
        #Create a new hash map to help find the most frequently paired together scanners
            #Key: tuple of the scanners that have at least one set of matching beacons. Example: (scanner 1, scanner 5)
            #Pair: list of which beacons match. Example: [(beacon 3, beacon 9), (beacon 1, beacon 16), ...]
        #Combine the pair of scanners that have the most number of matching beacons
            #The scanner with the lower index number will be designated as "left", and the other designated as "right"
            #Using the first pair of matching beacons, left's beacon acts as a pivot point to rotate all of the right scanner's beacons
            #Iterate through all 90-degree rotations available for the X, Y, and Z orientations for the right scanner
                #Update the position of all of right's beacons so that the first pair of matching beacons are in the same location
                #If, after the current rotation and positional offset, all of the beacons in both scanners are the same, the correct orientation was found
            #Add all of the right scanner's new beacon positions to the left scanner's list of beacons in the global hash map to merge them
            #Remove the right scanner from our global hash map
    #Return the size of the beacon list for the last remaining scanner


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

    rot = (rot_/180) * Math.pi

    #Iterating through each beacon for the designated scanner
    for b in range(len(scanners[sIndex_])):
        #Picking the correct axis to turn on, and using linear algebra to move the correct coordinates
        if axis_ == 'x' or axis_ == 'X':
            newY = (scanners[sIndex_][b][1] * Math.cos(rot)) - (scanners[sIndex_][b][2] * Math.sin(rot))
            newZ = (scanners[sIndex_][b][1] * Math.sin(rot)) + (scanners[sIndex_][b][2] * Math.cos(rot))
            scanners[sIndex_][b] = [scanners[sIndex_][b][0], round(newY), round(newZ)]
        if axis_ == 'y' or axis_ == 'Y':
            newX = (scanners[sIndex_][b][0] * Math.cos(rot)) + (scanners[sIndex_][b][2] * Math.sin(rot))
            newZ = (scanners[sIndex_][b][2] * Math.cos(rot)) - (scanners[sIndex_][b][0] * Math.sin(rot))
            scanners[sIndex_][b] = [round(newX), scanners[sIndex_][b][1], round(newZ)]
        if axis_ == 'z' or axis_ == 'Z':
            newX = (scanners[sIndex_][b][0] * Math.cos(rot)) - (scanners[sIndex_][b][1] * Math.sin(rot))
            newY = (scanners[sIndex_][b][0] * Math.sin(rot)) + (scanners[sIndex_][b][1] * Math.cos(rot))
            scanners[sIndex_][b] = [round(newX), round(newY), scanners[sIndex_][b][2]]
    return


def combineScanners(s1_:int, s1b1_:list, s2_:int, s2b1_:list):
    '''Combines all beacons from two given scanners based on matching points.
    Parameters
    ----------
        s1_: Index for the first scanner to merge.
        s1b1_: Coordinate point for the beacon in scanner 1 that is a matching point to s2b1_.
        s2_: Index for the second scanner to merge.
        s2b1_: Coordinate point for the beacon in scanner 1 that is a matching point to s1b1_.

    Returns: None
    '''
    print("Combining Scanners", s1_, "and", s2_)
    return


def solution1():

    #In each scanner, we need to find the relative distances that each of its beacons are from one another
    for s in scanners.keys():
        #print("Scanner", s)
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

            #print("\tBeacon", b, "distances:", shortestDists[:3])
            
    print("\n====================================================\n")

    #Comparing each scanner against each other scanner to look for matching manhattan distances
    for d in distanceDict.keys():
        #When a match is found, we combine the scanners that share a matching beacon
        if len(distanceDict[d]) > 1:
            print("Matches:", distanceDict[d])
            scanner1 = distanceDict[d][0][0]
            beacon1 = distanceDict[d][0][1]
            scanner2 = distanceDict[d][1][0]
            beacon2 = distanceDict[d][1][1]
            combineScanners(scanner1, beacon1, scanner2, beacon2)
            return
    return


def solution2():

    return


#Dictionary where the key is an int for a scanner ID index, and the paired value is a list of tuples for relative (x,y,z) coords of each beacon it sees
scanners = getInput()
#Dictionary where the key is a tuple for 3 manhattan distances in ascending order, and the paired value is a list where each element is a tuple (scanner#, (beaconX, beaconY, beaconZ))
distanceDict = {}

print("Year 2021, Day 19 solution part 1:", solution1())
print("Year 2021, Day 19 solution part 2:", solution2())