#https://adventofcode.com/2019/day/10
#https://adventofcode.com/2019/day/10#part2

import os
import math
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 0
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d10_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d10_real.txt")


def getInput():
    grid = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            grid.append(line)

    return grid
            

def solution1():
    grid = getInput()
    asteroids = []
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == '#':
                asteroids.append((c,r))
                
    bestAsteroid = None
    bestCount = 0
    for a in asteroids:
        angles = {}
        for b in asteroids:
            if a == b:
                continue
            angle = math.atan2(b[1]-a[1], b[0]-a[0])
            #print("Angle between", a, "and", b, ":", angle)
            if angle not in angles.keys():
                angles[angle] = True
            
        #print(a, "count:", len(angles.keys()))
        if len(angles.keys()) + 1 > bestCount:
            bestCount = len(angles.keys())
            bestAsteroid = a

    return bestCount


def solution2():
    grid = getInput()
    asteroids = []
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] == '#':
                asteroids.append((c,r))
                
    #Finding the location of the asteroid to start at
    bestAsteroid = None
    bestCount = 0
    bestAngles = {}
    for a in asteroids:
        angles = {}
        for b in asteroids:
            if a == b:
                continue
            angle = math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))
            dist = abs(b[1]-a[1]+b[0]-a[0])
            if angle not in angles.keys():
                angles[angle] = [(b, dist)]
            else:
                angles[angle].append((b, dist))
            
        if len(angles.keys()) + 1 > bestCount:
            bestCount = len(angles.keys())
            bestAsteroid = a
            bestAngles = angles
            
    angleList = [x for x in bestAngles.keys()]
    angleList.sort()
    a = angleList.index(-90)
    for angle in angleList:
        bestAngles[angle].sort(key=lambda x: x[1])
    
    maxDestroyed = 200
    for i in range(0, maxDestroyed):
        #Destroying the closest asteroid at the given angle
        destroyed = bestAngles[angleList[a]].pop(0)
        if i == maxDestroyed - 1:
            return (destroyed[0][0] * 100) + destroyed[0][1]
        
        #If the asteroid was the last one along this angle, we remove this angle from the angleList
        if len(bestAngles[angleList[a]]) == 0:
            angleList.pop(a)
        #Move the angle index to point to the next angle
        else:
            a += 1
        #Cycling back to the start of the angle list
        if a >= len(angleList):
            a = 0

    return -1


print("Year 2019, Day 10 solution part 1:", solution1())
print("Year 2019, Day 10 solution part 2:", solution2())