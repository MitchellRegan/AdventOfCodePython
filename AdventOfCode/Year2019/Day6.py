#https://adventofcode.com/2019/day/6
#https://adventofcode.com/2019/day/6#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d6_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d6_real.txt")


def getInput():
    '''Returns the list of all unique orbiting objects, and a one-way directional graph where each object points to the object it orbits.'''
    objectList = []
    orbits = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(')')
            if line[0] not in objectList:
                objectList.append(line[0])
            if line[1] not in objectList:
                objectList.append(line[1])
            orbits[line[1]] = line[0]

    return objectList, orbits


def getInput2():
    '''Returns a bi-directional graph where each object has a list of objects it orbits, as well as all of the objects orbiting itself.'''
    orbits = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(')')
            if line[0] not in orbits.keys():
                orbits[line[0]] = [line[1]]
            else:
                orbits[line[0]].append(line[1])
                
            if line[1] not in orbits.keys():
                orbits[line[1]] = [line[0]]
            else:
                orbits[line[1]].append(line[0])

    return orbits


def solution1():
    objs, orbits = getInput()
    
    numOrbits = 0
    for o in objs:
        if o == "COM":
            continue
        
        dists = {o:0, orbits[o]:1}
        q = [orbits[o]]
        while len(q) > 0:
            head = q.pop(0)
            if head == "COM":
                numOrbits += dists[head]
                #print("Object", o, "distance:", dists[head])
                break
            else:
                dists[orbits[head]] = dists[head]+1
                q.append(orbits[head])

    return numOrbits


def solution2():
    orbits = getInput2()
    
    dist = {"YOU":0}
    q = ["YOU"]
    
        
    while len(q) > 0:
        head = q.pop(0)
        if head == "SAN":
            #Removing 2 from the distance. The first -1 is because YOU isn't orbiting itself, but another object, so the distance to that parent object is counted as 0.
            #The second -1 is because we aren't moving to SAN, but the object that SAN is orbiting.
            return dist[head] - 2
        
        for o in orbits[head]:
            if o not in dist.keys():
                dist[o] = dist[head] + 1
                q.append(o)
            
    return -1


print("Year 2019, Day 6 solution part 1:", solution1())
print("Year 2019, Day 6 solution part 2:", solution2())