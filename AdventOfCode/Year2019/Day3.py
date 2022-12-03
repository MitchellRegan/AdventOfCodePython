#https://adventofcode.com/2019/day/3
#https://adventofcode.com/2019/day/3#part2

inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputTestFiles\\d3_test.txt"
#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputRealFiles\\d3_real.txt"


def printInput(coords):
    #Finding the bounds of the grid to use
    T = 0
    B = 0
    L = 0
    R = 0

    for i in coords[0]:
        if i[0] < L:
            L = i[0]
        if i[0] > R:
            R = i[0]
        if i[1] < B:
            B = i[1]
        if i[1] > T:
            T = i[1]

    for i in coords[1]:
        if i[0] < L:
            L = i[0]
        if i[0] > R:
            R = i[0]
        if i[1] < B:
            B = i[1]
        if i[1] > T:
            T = i[1]

    # Initializing a blank grid with the rows and columns needed
    grid = []
    for r in range(T-B):
        row = ['.'] * (R-L)
        grid.append(row)

    print("Rows:", len(grid), "Cols:", len(grid[0]))

    for a in range(0, len(coords[0])-1):
        xs = [coords[0][a][0], coords[0][a+1][0]]
        ys = [coords[0][a][1], coords[0][a+1][1]]
        print(xs)
        print(ys)
        print(xs[1], L, ys[1], B)
        grid[ys[1]+B-1][xs[1]+L-1] = 'A'

    for row in range(len(grid)-1, -1, -1):
        for col in range(0, len(grid[r])):
            print(grid[row][col], end=" ")
        print()
    return 0


def solution1():
    #2D list to contain lists for each wire, each of which contains a list of coordinate points
    wires = []

    #Looping through each line in the input file
    with open(inFile, 'r') as f:
        for line in f:
            #delineating the path instructions for this wire (line)
            instructions = line.split(',')

            #Creating a list of coordinate points for where this wire turns, starting at point (0,0)
            wirePoints = [(0,0)]

            # Looping through each instruction to trace the points where the wire turns
            for i in instructions:
                if i[0] == 'U':
                    x = wirePoints[-1][0]
                    y = wirePoints[-1][1] + int(i[1:])
                    wirePoints.append((x,y))
                elif i[0] == 'D':
                    x = wirePoints[-1][0]
                    y = wirePoints[-1][1] - int(i[1:])
                    wirePoints.append((x,y))
                elif i[0] == 'L':
                    x = wirePoints[-1][0] - int(i[1:])
                    y = wirePoints[-1][1]
                    wirePoints.append((x,y))
                elif i[0] == 'R':
                    x = wirePoints[-1][0] + int(i[1:])
                    y = wirePoints[-1][1]
                    wirePoints.append((x,y))
                else:
                    print("ERROR: invalid instruction", i)
                    return 0

            # Adding this wire's coordinate points to the list of all wires
            wires.append(wirePoints)

    #Finding all intersections between the wires
    intersections = []
    for a in range(0, len(wires[0])-1):
        for b in range(0, len(wires[1])-1):
            wireA_x = [wires[0][a][0], wires[0][a+1][0]]
            wireA_y = [wires[0][a][1], wires[0][a+1][1]]
            wireB_x = [wires[1][b][0], wires[1][b+1][0]]
            wireB_y = [wires[1][b][1], wires[1][b+1][1]]

            #if line a is vertical and line b is horizontal
            if (wireA_x[0] == wireA_x[1]) and (wireB_y[0] == wireB_y[1]):
                #checking if the coordinates intersect
                if wireA_x[0] >= min(wireB_x) and wireA_x[0] <= max(wireB_x) and wireB_y[0] >= min(wireA_y) and wireB_y[0] <= max(wireA_y):
                    if (wireA_x[0], wireB_y[0]) not in intersections:
                        intersections.append((wireA_x[0], wireB_y[0]))

            #if line a is horizontal and line b is vertical
            elif (wireA_y[0] == wireA_y[1]) and (wireB_x[0] == wireB_x[1]):
                #checking if the coordinates intersect
                if wireB_x[0] >= min(wireA_x) and wireB_x[0] <= max(wireA_x) and wireA_y[0] >= min(wireB_y) and wireA_y[0] <= max(wireB_y):
                    if (wireB_x[0], wireA_y[0]) not in intersections:
                        intersections.append((wireB_x[0], wireA_y[0]))

    #Finding the shortest manhattan distance from the origin
    intersections.pop(0)
    shortestDist = float('inf')
    for i in intersections:
        dist = abs(i[0]) + abs(i[1])
        #print("Intersection", i, "Manhattan distance:", dist)
        if dist < shortestDist:
            shortestDist = dist

    # it is NOT 1285
    printInput(wires)
    return shortestDist


def solution2():
    return 0

    
print("Year 2019, Day 3 solution part 1:", solution1())
print("Year 2019, Day 3 solution part 2:", solution2())