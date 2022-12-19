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

    #Variables to store the min and max edges of the problem space
    minX = min([x for (x,y,z) in lava]) - 1
    minY = min([y for (x,y,z) in lava]) - 1
    minZ = min([z for (x,y,z) in lava]) - 1
    maxX = max([x for (x,y,z) in lava]) + 1
    maxY = max([y for (x,y,z) in lava]) + 1
    maxZ = max([z for (x,y,z) in lava]) + 1
    
    print("Min/max X:", minX, "-", maxX)
    print("Min/max Y:", minY, "-", maxY)
    print("Min/max Z:", minZ, "-", maxZ)
    print("Volume:", (maxX-minX+1) * (maxY-minY+1) * (maxZ-minZ+1))

    for drop in lava:
        x = drop[0]
        y = drop[1]
        z = drop[2]

        #Creating a list to store the coordinates of all adjacent spaces to this drop of lava
        adjacent = [(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]

        #If another drop of lava is in one of the adjacent spaces, we remove that space from our list (i.e. it is occupied)
        for other in lava:
            if other in adjacent:
                adjacent.remove(other)

        #The open adjacent spaces are then added to the list to track which ones are known to be air
        for a in adjacent:
            if a not in air:
                air.append(a)

    #Perform a BFS flood fill starting from the min xyz corner of the problem space
    q = [(minX, minY, minZ)]
    found = [(minX, minY, minZ)]
    while len(q) > 0:
        cur = q.pop(0)
        
        #Any spaces that are found in this method that are inside the "air" list are removed
        #Up
        if cur[1] < maxY:
            up = (cur[0], cur[1]+1, cur[2])
            if up not in q and up not in found and up not in lava:
                q.append(up)
                found.append(up)
                if up in air:
                    air.remove(up)
        #Down
        if cur[1] > minY:
            down = (cur[0], cur[1]-1, cur[2])
            if down not in q and down not in found and down not in lava:
                q.append(down)
                found.append(down)
                if down in air:
                    air.remove(down)
        #Right
        if cur[0] < maxX:
            right = (cur[0]+1, cur[1], cur[2])
            if right not in q and right not in found and right not in lava:
                q.append(right)
                found.append(right)
                if right in air:
                    air.remove(right)
        #Left
        if cur[0] > minX:
            left = (cur[0]-1, cur[1], cur[2])
            if left not in q and left not in found and left not in lava:
                q.append(left)
                found.append(left)
                if left in air:
                    air.remove(left)
        #Front
        if cur[2] < maxZ:
            front = (cur[0], cur[1], cur[2]+1)
            if front not in q and front not in found and front not in lava:
                q.append(front)
                found.append(front)
                if front in air:
                    air.remove(front)
        #Back
        if cur[2] > minZ:
            back = (cur[0], cur[1], cur[2]-1)
            if back not in q and back not in found and back not in lava:
                q.append(back)
                found.append(back)
                if back in air:
                    air.remove(back)

    #Check the adjacent tiles for each lava block again
    for drop in lava:
        #If an adjacent air space is in the remaining list of air blocks, it's an interior block and doesn't count
        x = drop[0]
        y = drop[1]
        z = drop[2]

        #Creating a list to store the coordinates of all adjacent spaces to this drop of lava
        adjacent = [(x-1,y,z), (x+1,y,z), (x,y-1,z), (x,y+1,z), (x,y,z-1), (x,y,z+1)]

        #If another drop of lava is in one of the adjacent spaces, we remove that space from our list (i.e. it is occupied)
        for other in lava:
            if other in adjacent:
                adjacent.remove(other)

        #If a remaining air block is in one of the adjacent spaces, it's an internal air block and doesn't count
        for a in air:
            if a in adjacent:
                adjacent.remove(a)

        # The surface area for this drop is the number of remaining adjacent spaces left
        surfaceArea += len(adjacent)

    return surfaceArea


print("Year 2022, Day 18 solution part 1:", solution1())
print("Year 2022, Day 18 solution part 2:", solution2())