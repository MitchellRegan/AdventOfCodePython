#https://adventofcode.com/2022/day/18
#https://adventofcode.com/2022/day/18#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d18_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d18_real.txt")


def getInput():
    lava = []
    with open(inFile, 'r') as f:
        for line in f:
            line = line.split(',')
            x = int(line[0])
            y = int(line[1])
            z = line[2]
            if z[-1] == '\n':
                z = z[:-1]
            z = int(z)
            lava.append((x,y,z))
    return lava


def solution1():
    surfaceArea = 0
    lava = getInput()

    for drop in lava:
        x = drop[0]
        y = drop[1]
        z = drop[2]
        adjacent = [(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]

        for other in lava:
            if other in adjacent:
                adjacent.remove(other)

        surfaceArea += len(adjacent)

    return surfaceArea


def solution2():
    surfaceArea = 0
    lava = getInput()
    air = []

    for drop in lava:
        x = drop[0]
        y = drop[1]
        z = drop[2]
        adjacent = [(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]

        for other in lava:
            if other in adjacent:
                adjacent.remove(other)

        surfaceArea += len(adjacent)
        for a in adjacent:
            if a not in air:
                air.append(a)

    for bubble in air:
        x = bubble[0]
        y = bubble[1]
        z = bubble[2]
        adjacent = [(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]

        for drop in lava:
            if drop in adjacent:
                adjacent.remove(drop)
        
        if len(adjacent) == 0:
            surfaceArea -= 6

    return surfaceArea


print("Year 2022, Day 18 solution part 1:", solution1())
print("Year 2022, Day 18 solution part 2:", solution2())
#3284 too high