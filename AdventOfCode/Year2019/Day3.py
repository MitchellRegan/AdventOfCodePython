#https://adventofcode.com/2019/day/3
#https://adventofcode.com/2019/day/3#part2

#inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputTestFiles\\d3_test.txt"
inFile = "C:\\Users\\Mitch\\source\\repos\\AdventOfCodePython\\AdventOfCode\\Year2019\\InputRealFiles\\d3_real.txt"


def solution1():
    #dictionary where the key is the coordinate point, and the value is the ID of the wire at that point
    wirePoints = {"0,0":'O'}

    wireNum = 1
    minDist = float('inf')
    #Looping through each line in the input file
    with open(inFile, 'r') as f:
        for line in f:
            #delineating the path instructions for this wire (line)
            instructions = line.split(',')
            x = 0
            y = 0
            for w in instructions:
                xdir = 0
                ydir = 0
                if w[0] == 'U':
                    ydir = 1
                elif w[0] == 'D':
                    ydir = -1
                elif w[0] == 'L':
                    xdir = -1
                elif w[0] == 'R':
                    xdir = 1
                else:
                    print("Invalid instruction:", w)

                newX = x + (xdir * int(w[1:]))
                newY = y + (ydir * int(w[1:]))

                # Looping through every point between the current and previous xy points
                for yval in range(min([y,newY]), max([y,newY])+1):
                    for xval in range(min([x,newX]), max([x,newX])+1):
                        point = str(xval)+","+str(yval)

                        #Checking if the current position is empty
                        if point not in wirePoints.keys():
                            wirePoints[point] = str(wireNum)
                        elif wirePoints[point] != str(wireNum) and wirePoints[point] != 'O':
                            wirePoints[point] = 'X'
                            #Checking if the manhattan distance here is less than the current minimum
                            dist = abs(xval) + abs(yval)
                            if dist < minDist:
                                minDist = dist
                # Updating the stored x,y vals for the start of the next instruction
                x = newX
                y = newY

            wireNum += 1

    return minDist


def solution2():
    #Dictionary where they key is the xy coordinate and the value is an ordered pair for the wire ID and the step distance
    wirePoints = {"0,0":[0,0]}

    wireNum = 1
    minDist = float('inf')
    #Looping through each line in the input file
    with open(inFile, 'r') as f:
        for line in f:
            #delineating the path instructions for this wire (line)
            instructions = line.split(',')
            x = 0
            y = 0
            step = 0
            for w in instructions:
                xdir = 0
                ydir = 0
                if w[0] == 'U':
                    ydir = 1
                elif w[0] == 'D':
                    ydir = -1
                elif w[0] == 'L':
                    xdir = -1
                elif w[0] == 'R':
                    xdir = 1
                else:
                    print("Invalid instruction:", w)

                newX = x + (xdir * int(w[1:]))
                xstep = 1
                if xdir == -1:
                    xstep = -1
                newY = y + (ydir * int(w[1:]))
                ystep = 1
                if ydir == -1:
                    ystep = -1
                # Looping through every point between the current and previous xy points
                for yval in range(y, newY+ystep, ystep):
                    for xval in range(x, newX+xstep, xstep):
                        point = str(xval)+","+str(yval)

                        #Checking if the current position is empty
                        if point not in wirePoints.keys():
                            wirePoints[point] = [wireNum, step]
                        elif wirePoints[point][0] != wireNum and wirePoints[point][0] != 0:
                            dist = step + wirePoints[point][1]
                            wirePoints[point] = [wireNum, dist]
                            #Checking if the total step distance is less than the current minimum
                            if dist < minDist:
                                minDist = dist

                        step += 1
                # Updating the stored x,y vals for the start of the next instruction
                x = newX
                y = newY
                step -= 1

            wireNum += 1

    return minDist

    
print("Year 2019, Day 3 solution part 1:", solution1())
print("Year 2019, Day 3 solution part 2:", solution2())