#https://adventofcode.com/2021/day/19
#https://adventofcode.com/2021/day/19#part2

import os
import math as Math
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d19_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d19_real.txt")


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


def rotateBeacons(beaconList_:list, axis_:str, rot_:int):
    '''Rotates the relative position of all XYZ coordinates in a given list around the origin.
    Parameters
    ----------
        beaconList_: List of 3-dimensional coordinate points to perform the rotation on.
        axis_: Char for which axis to rotate along. Must be X, Y, or Z.
        rot_: The degree of rotation to move the beacons. Must be evenly divisible by 90.

    Returns: List containing the rotated coordinate points.
    '''
    #Performing sanity checks on our inputs to make sure they're valid
    if axis_.lower() not in ['x', 'y', 'z']:
        print("ERROR: Invalid axis rotation. Must be either X, Y, or Z. Axis given:", axis_)
        return

    rot = (rot_/180) * Math.pi

    newList = []

    #Iterating through each beacon for the designated scanner
    for b in beaconList_:
        #Picking the correct axis to turn on, and using linear algebra to move the correct coordinates
        if axis_ == 'x' or axis_ == 'X':
            newY = (b[1] * Math.cos(rot)) - (b[2] * Math.sin(rot))
            newZ = (b[1] * Math.sin(rot)) + (b[2] * Math.cos(rot))
            newList.append([b[0], round(newY), round(newZ)])
        if axis_ == 'y' or axis_ == 'Y':
            newX = (b[0] * Math.cos(rot)) + (b[2] * Math.sin(rot))
            newZ = (b[2] * Math.cos(rot)) - (b[0] * Math.sin(rot))
            newList.append([round(newX), b[1], round(newZ)])
        if axis_ == 'z' or axis_ == 'Z':
            newX = (b[0] * Math.cos(rot)) - (b[1] * Math.sin(rot))
            newY = (b[0] * Math.sin(rot)) + (b[1] * Math.cos(rot))
            newList.append([round(newX), round(newY), b[2]])

    return newList


def combineScanners(scanner1Index_:int, scanner1_:list, scanner2Index_:int, scanner2_:list, matches_:list):
    '''Combines all beacons from two given scanners based on matching points. The result is relative to scanner 1's position.
    Parameters
    ----------
        scanner1_: List of all beacons in the first scanner to combine.
        scanner2_: List of all beacons in the second scanner to combine.
        matches_: List of ordered pairs of indexes for which beacons are shared between the scanners.

    Returns: Combined list of beacons in the correct relative position and orientation to scanner1_. If no valid combination was found, returns None.
    '''
    #Iterating through all 90-degree rotations available for the XYZ orientations that scanner 2 can be in
    for xrot in [0, 90, 180, 270]:
        for yrot in [0, 90, 180, 270]:
            for zrot in [0, 90, 180, 270]:
                #Rotating a copy of the beacons from scanner 2 that have a match in scanner 1
                tempMatch = [y for (x,y) in matches_]
                tempMatch = rotateBeacons(tempMatch, 'x', xrot)
                tempMatch = rotateBeacons(tempMatch, 'y', yrot)
                tempMatch = rotateBeacons(tempMatch, 'z', zrot)

                #Bool to track if this rotation is the correct one
                isValid = True

                #Shifting all of the rotated beacons so that the first matching pair are in the same location
                offset = (matches_[0][0][0] - tempMatch[0][0], matches_[0][0][1] - tempMatch[0][1], matches_[0][0][2] - tempMatch[0][2])
                for i in range(0, len(tempMatch)):
                    tempMatch[i] = [tempMatch[i][0] + offset[0], tempMatch[i][1] + offset[1], tempMatch[i][2] + offset[2]]

                    #If there's one beacon whose xyz coordinate doesn't align with its matching pair in scanner 1, this rotation isn't valid
                    if tempMatch[i] != matches_[i][0]:
                        isValid = False
                        break

                #If we found a valid rotation, we perform the same rotation to all of scanner 2's beacons and combine
                if isValid:
                    #print("Valid alignment of scanners", scanner1Index_, "and", scanner2Index_, "at rotation:", xrot, yrot, zrot, "and offset:", offset)
                    correctS2 = rotateBeacons(scanner2_, 'x', xrot)
                    correctS2 = rotateBeacons(correctS2, 'y', yrot)
                    correctS2 = rotateBeacons(correctS2, 'z', zrot)

                    correctS1 = [x for x in scanner1_]
                    for i in range(0, len(correctS2)):
                        correctS2[i] = [correctS2[i][0] + offset[0], correctS2[i][1] + offset[1], correctS2[i][2] + offset[2]]

                        #If this beacon is a duplicate, we don't want to include it in the final list of combined beacons
                        if correctS2[i] not in correctS1:
                            correctS1.append(correctS2[i])

                    #-------- Addition for Problem 2 --------
                    #If any scanners had previously been merged with scanner 2, we also need to update their relative rotation
                    relPosToAdd = []
                    relPosToRemove = []
                    for rel in scannerRelativePos.keys():
                        if rel[1] == scanner2Index_:
                            oldPos = scannerRelativePos[rel]
                            newPos = [[oldPos[0], oldPos[1], oldPos[2]]]
                            newPos = rotateBeacons(newPos, 'x', xrot)
                            newPos = rotateBeacons(newPos, 'y', yrot)
                            newPos = rotateBeacons(newPos, 'z', zrot)

                            #Changing the relative position of this scanner away from scanner 2 and over to scanner 1
                            #NOTE: Since we can't add or remove these relative positions from the dictionary during iteration, we do it after
                            relPosToAdd.append([rel[1], scanner1Index_, newPos[0]])
                            relPosToRemove.append(rel)

                    #Adding all of the new relative positions to our dictionary
                    for rpta in relPosToAdd:
                        scannerRelativePos[(rpta[0], rpta[1])] = rpta[2]
                    #Removing all of the old relative positions from our dictionary
                    for rptr in relPosToRemove:
                        scannerRelativePos.pop(rptr)

                    #Storing scanner 2's position relative to scanner 1
                    scannerRelativePos[(scanner2Index_, scanner1Index_)] = offset
                    return correctS1

    #If no valid orientation was found, return None
    return None


def solution1():
    #Dictionary where the key is an int for a scanner ID index, and the paired value is a list of tuples for relative (x,y,z) coords of each beacon it sees
    scanners = getInput()

    #Looping the following steps until only one scanner remains
    for loopCount in range(0, 50):
        if len(scanners.keys()) == 1:
            break

        #Dictionary where the key is a tuple for 2 manhattan distances in ascending order, and the paired value is a list where each element is a tuple (scanner#, (beaconX, beaconY, beaconZ))
        distanceDict = {}

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

                #Once all Manhattan distances are found, we sort the list in ascending order so that the first 2 are the shortest
                shortestDists.sort()

                #Storing the 2 shortest distances as a tuple-key and this beacon's ID as one of the values associated with it
                if (shortestDists[0], shortestDists[1]) in distanceDict.keys():
                    distanceDict[(shortestDists[0], shortestDists[1])].append((s,b))
                else:
                    distanceDict[(shortestDists[0], shortestDists[1])] = [(s,b)]
        
        #Dictionary to track which pairs of scanners have matching beacons
            #Key: ordered pair of the scanner indexes (in ascending order) that have at least one shared beacon
            #Pair: list of ordered pairs of indexes for which beacons are the same.
        scannerPairs = {}

        #Looking for manhattan distance meta-data shared between multiple beacons
        for d in distanceDict.keys():
            #When a match is found in separate scanners, we track the scanners that share a matching beacon
            if len(distanceDict[d]) > 1 and distanceDict[d][0][0] != distanceDict[d][1][0]:
                scanPair = (distanceDict[d][0][0], distanceDict[d][1][0])
                beacPair = (distanceDict[d][0][1], distanceDict[d][1][1])
                if scanPair in scannerPairs.keys():
                    scannerPairs[scanPair].append(beacPair)
                else:
                    scannerPairs[scanPair] = [beacPair]

        #Finding the pair of scanners that have the largest number of matches
        bestMatch = None
        numMatches = -1
        for p in scannerPairs.keys():
            if len(scannerPairs[p]) > numMatches:
                bestMatch = p
                numMatches = len(scannerPairs[p])

        if bestMatch is None:
            print("There are no beacons that have matching meta-data.")
            for k in scanners.keys():
                print("\tScanner", k)
                for b in scanners[k]:
                    print("\t\t", b)
            print("\tDistance Dictionary:")
            for d in distanceDict.keys():
                print(d, ":", distanceDict[d])
            return -1

        #Using the combineScanners function to find the appropriate orientation and position to merge all beacons into a single scanner with no duplicates
        mergedScanner = combineScanners(bestMatch[0], scanners[bestMatch[0]], bestMatch[1], scanners[bestMatch[1]], scannerPairs[bestMatch])
        if mergedScanner is None:
            print("FAILED TO COMBINE")
            return -1
        else:
            #Removing the second scanner from the scanners dictionary, and updating the first scanner to include the new beacons
            scanners[bestMatch[0]] = mergedScanner
            scanners.pop(bestMatch[1])

    #Returning the number of beacons in the last remaining scanner
    return len(scanners[0])


def solution2():
    #NOTE: This solution uses the global variable scannerRelativePos that is updated during solution1

    #Getting an easier list of global sensor positions to iterate through
    globalMap = [x for x in scannerRelativePos.keys()]

    #Comparing the Manhattan distances between every pair of sensors to find the largest gap
    maxDist = -1
    for i in range(0, len(globalMap)-1):
        for j in range(i+1, len(globalMap)):
            xdist = abs(scannerRelativePos[globalMap[i]][0] - scannerRelativePos[globalMap[j]][0])
            ydist = abs(scannerRelativePos[globalMap[i]][1] - scannerRelativePos[globalMap[j]][1])
            zdist = abs(scannerRelativePos[globalMap[i]][2] - scannerRelativePos[globalMap[j]][2])

            if xdist + ydist + zdist > maxDist:
                #print("Current best distance is between scanners", globalMap[i][0], "and", globalMap[j][0])
                #print("\tX:", scannerRelativePos[globalMap[i]][0], "-", scannerRelativePos[globalMap[j]][0], "=", xdist)
                #print("\tY:", scannerRelativePos[globalMap[i]][1], "-", scannerRelativePos[globalMap[j]][1], "=", ydist)
                #print("\tZ:", scannerRelativePos[globalMap[i]][2], "-", scannerRelativePos[globalMap[j]][2], "=", zdist)
                #print("\tTotal:", xdist + ydist + zdist)
                maxDist = xdist + ydist + zdist
    return maxDist


#Dictionary for solution 2 to store each scanner's position relative to the scanner it was merged with
    #Key: ordered pair of scanner indexes. The first index is for the scanner that was merged into the index of the second.
    #Pair: tuple designating the 3D positional offset of the first scanner when merged with the second.
        #Example: (5, 0):(22, -49, 3) means that scanner 5 was merged with scanner 0 at the relative position (22, -49, 3)
scannerRelativePos = {}
print("Year 2021, Day 19 solution part 1:", solution1())
print("Year 2021, Day 19 solution part 2:", solution2())