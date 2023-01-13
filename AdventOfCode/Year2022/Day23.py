#https://adventofcode.com/2022/day/23
#https://adventofcode.com/2022/day/23#part2

import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d23_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d23_real.txt")


def getInput():
    #Dict to store the row,col position of each elf
    elfLocs = {}

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            for col in range(0, len(line)):
                if line[col] == '#':
                    elfLocs[(row, col)] = True
            row += 1

    return elfLocs


def solution1():
    #Dict to store the row,col location of each elf and their step order
    elfLocs = getInput()
    stepOrder = [0, 1, 2, 3] # 0=N, 1=S, 2=W, 3=E

    #Iterating through 10 loops before getting the final output
    for i in range(0, 10):
        #Dictionary to store the destination locations for each elf
        destinations = {}
        collisions = {}

        #Getting the destination for each elf, one by one
        for elf in elfLocs.keys():
            r = elf[0]
            c = elf[1]

            #If there are no elves in the 8 positions adjacent, they don't do anything
            adjacent = [(r+1,c), (r+1,c+1), (r,c+1), (r-1,c+1), (r-1,c), (r-1,c-1), (r,c-1), (r+1,c-1)]
            adjacent = [x for x in adjacent if x not in elfLocs.keys()]
            #if not any(i in adjacent for i in elfLocs):
            if len(adjacent) == 8:
                #print("Elf", elf, "is not adjacent to others. No movement")
                continue

            #If there are elves adjacent, we go by the step order
            for step in stepOrder:
                #If no elf in N, NE, or NW, they try going north
                if step == 0:
                    north = [(r-1,c+1), (r-1,c), (r-1,c-1)]
                    if len([x for x in north if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r-1,c) in destinations.keys():
                            #destinations.pop((r-1,c))
                            collisions[(r-1,c)] = True
                        elif (r-1,c) not in collisions.keys():
                            destinations[(r-1,c)] = elf
                        break
                #If no elf in the S, SE, or SW, they try going south
                elif step == 1:
                    south = [(r+1,c+1), (r+1,c), (r+1,c-1)]
                    if len([x for x in south if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r+1,c) in destinations.keys():
                            #destinations.pop((r+1,c))
                            collisions[(r+1,c)] = True
                        elif (r+1,c) not in collisions.keys():
                            destinations[(r+1,c)] = elf
                        break
                #If no elf in the W, NW, or SW, they try going west
                elif step == 2:
                    west = [(r,c-1), (r-1,c-1), (r+1,c-1)]
                    if len([x for x in west if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r,c-1) in destinations.keys():
                            #destinations.pop((r,c-1))
                            collisions[(r,c-1)] = True
                        elif (r,c-1) not in collisions.keys():
                            destinations[(r,c-1)] = elf
                        break
                #If no elf in the E, NE, or SE, they try going east
                elif step == 3:
                    east = [(r,c+1), (r-1,c+1), (r+1,c+1)]
                    if len([x for x in east if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r,c+1) in destinations.keys():
                            #destinations.pop((r,c+1))
                            collisions[(r,c+1)] = True
                        elif (r,c+1) not in collisions.keys():
                            destinations[(r,c+1)] = elf
                        break

        #Looping through each of the destinations
        for d in destinations.keys():
            elfLocs.pop(destinations[d])
            elfLocs[d] = True

        #Cycling the step order
        f = stepOrder.pop(0)
        stepOrder.append(f)

    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for l in elfLocs:
        if l[0] < ymin:
            ymin = l[0]
        if l[0] > ymax:
            ymax = l[0]
        if l[1] < xmin:
            xmin = l[1]
        if l[1] > xmax:
            xmax = l[1]

    grid = []
    for r in range(0, 1+ymax-ymin):
        row = ['.'] * (1 + xmax-xmin)
        grid.append(row)

    for l in elfLocs:
        grid[l[0] - ymin][l[1] - xmin] = '#'

    #for row in grid:
    #    print(''.join(row))
    return (len(grid) * len(grid[0])) - len(elfLocs)


def solution2():
    #Dict to store the row,col location of each elf and their step order
    elfLocs = getInput()
    stepOrder = [0, 1, 2, 3] # 0=N, 1=S, 2=W, 3=E

    #Iterating through 10 loops before getting the final output
    i = 1
    while True:
        #Dictionary to store the destination locations for each elf
        destinations = {}
        collisions = {}

        #Getting the destination for each elf, one by one
        for elf in elfLocs.keys():
            r = elf[0]
            c = elf[1]

            #If there are no elves in the 8 positions adjacent, they don't do anything
            adjacent = [(r+1,c), (r+1,c+1), (r,c+1), (r-1,c+1), (r-1,c), (r-1,c-1), (r,c-1), (r+1,c-1)]
            adjacent = [x for x in adjacent if x not in elfLocs.keys()]
            #if not any(i in adjacent for i in elfLocs):
            if len(adjacent) == 8:
                #print("Elf", elf, "is not adjacent to others. No movement")
                continue

            #If there are elves adjacent, we go by the step order
            for step in stepOrder:
                #If no elf in N, NE, or NW, they try going north
                if step == 0:
                    north = [(r-1,c+1), (r-1,c), (r-1,c-1)]
                    if len([x for x in north if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r-1,c) in destinations.keys():
                            #destinations.pop((r-1,c))
                            collisions[(r-1,c)] = True
                        elif (r-1,c) not in collisions.keys():
                            destinations[(r-1,c)] = elf
                        break
                #If no elf in the S, SE, or SW, they try going south
                elif step == 1:
                    south = [(r+1,c+1), (r+1,c), (r+1,c-1)]
                    if len([x for x in south if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r+1,c) in destinations.keys():
                            #destinations.pop((r+1,c))
                            collisions[(r+1,c)] = True
                        elif (r+1,c) not in collisions.keys():
                            destinations[(r+1,c)] = elf
                        break
                #If no elf in the W, NW, or SW, they try going west
                elif step == 2:
                    west = [(r,c-1), (r-1,c-1), (r+1,c-1)]
                    if len([x for x in west if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r,c-1) in destinations.keys():
                            #destinations.pop((r,c-1))
                            collisions[(r,c-1)] = True
                        elif (r,c-1) not in collisions.keys():
                            destinations[(r,c-1)] = elf
                        break
                #If no elf in the E, NE, or SE, they try going east
                elif step == 3:
                    east = [(r,c+1), (r-1,c+1), (r+1,c+1)]
                    if len([x for x in east if x in adjacent]) == 3:
                        #print("Elf at", elf, "can go north")
                        if (r,c+1) in destinations.keys():
                            #destinations.pop((r,c+1))
                            collisions[(r,c+1)] = True
                        elif (r,c+1) not in collisions.keys():
                            destinations[(r,c+1)] = elf
                        break

        #If there were no movements this loop, we return the loop number
        if len(destinations.keys()) == 0:
            return i
        i += 1

        #Looping through each of the destinations
        for d in destinations.keys():
            #print("Destination", d, "elves:", destinations[d])
            elfLocs.pop(destinations[d])
            elfLocs[d] = True

        #Cycling the step order
        f = stepOrder.pop(0)
        stepOrder.append(f)

    return "Don't know"


print("Year 2022, Day 23 solution part 1:", solution1())
print("Year 2022, Day 23 solution part 2:", solution2())