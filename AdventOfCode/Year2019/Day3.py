#https://adventofcode.com/2019/day/3
#https://adventofcode.com/2019/day/3#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputTestFiles\\d3_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputRealFiles\\d3_real.txt"


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
    for r in range(abs(T) + abs(B) + 2):
        row = ['.'] * (abs(L) + abs(R) + 2)
        grid.append(row)

    crossings = []

    #Mapping out all of the coordinates for the first line
    for a in range(0, len(coords[0])-1):
        xs = [coords[0][a][0] + abs(L), coords[0][a+1][0] + abs(L)]
        ys = [coords[0][a][1] + abs(B)+1, coords[0][a+1][1] + abs(B)+1]

        #If the x coordinates are the same, we draw a vertical line
        if xs[0] == xs[1]:
            for yval in range(min(ys), max(ys)):
                grid[yval][xs[0]] = '|'
        #If the y coordinates are the same, we draw a horizontal line
        if ys[0] == ys[1]:
            for xval in range(min(xs), max(xs)):
                grid[ys[0]][xval] = '-'
                
        grid[ys[1]][xs[1]] = '+'
        grid[ys[0]][xs[0]] = '+'

    #Mapping out all of the coordinates for the second line
    for a in range(0, len(coords[1])-1):
        xs = [coords[1][a][0] + abs(L), coords[1][a+1][0] + abs(L)]
        ys = [coords[1][a][1] + abs(B)+1, coords[1][a+1][1] + abs(B)+1]

        #If the x coordinates are the same, we draw a vertical line
        if xs[0] == xs[1]:
            for yval in range(min(ys), max(ys)):
                if grid[yval][xs[0]] == '.':
                    grid[yval][xs[0]] = 'I'
                elif grid[yval][xs[0]] == '|' or grid[yval][xs[0]] == '-':
                    grid[yval][xs[0]] = 'X'
                    crossings.append((xs[0] - abs(L), yval - abs(B)-1))
        #If the y coordinates are the same, we draw a horizontal line
        if ys[0] == ys[1]:
            for xval in range(min(xs), max(xs)):
                if grid[ys[0]][xval] == '.':
                    grid[ys[0]][xval] = '='
                elif grid[ys[0]][xval] == '|' or grid[ys[0]][xval] == '-':
                    grid[ys[0]][xval] = 'X'
                    crossings.append((xval - abs(L), ys[0] - abs(B)-1))
                    
        grid[ys[0]][xs[0]] = '#'
        grid[ys[1]][xs[1]] = '#'

    #Setting the starting point to O
    grid[abs(B)+1][abs(L)] = 'O'


    dists = []
    for c in crossings:
        dists.append((abs(c[0]) + abs(c[1])))

    return min(dists)


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

    # it is NOT 1285. correct answer is 870
    
    return printInput(wires)


def solution2():
    return 0

    
print("Year 2019, Day 3 solution part 1:", solution1())
print("Year 2019, Day 3 solution part 2:", solution2())