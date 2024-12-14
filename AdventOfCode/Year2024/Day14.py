aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            p = [int(x) for x in line[0][2:].split(',')]
            v = [int(x) for x in line[1][2:].split(',')]
            inpt.append((p,v))

    return inpt
            

def solution1():
    inpt = getInput()

    #Defining the rectangular grid that the robots will occupy, starting at (0,0)
    gridWidth = 101
    gridHeight = 103
    numSec = 100
    if testing:
        gridWidth = 11
        gridHeight = 7
    
    quads = [0,0,0,0]
    for robot in inpt:
        x,y = robot[0]
        xVel,yVel = robot[1]

        #Using the good old Displacement Formula: d = p + vt + 0.5at^2
        endX = x + (xVel * numSec)
        endY = y + (yVel * numSec)

        endX = endX % gridWidth
        endY = endY % gridHeight

        if endX < (gridWidth - 1)//2: #Left half
            if endY < (gridHeight - 1)//2: #Top-left quad
                quads[1] += 1
            elif endY > (gridHeight - 1)//2: #Bottom-left quad
                quads[2] += 1
        elif endX > (gridWidth - 1)//2: #Right half
            if endY < (gridHeight - 1)//2: #Top-right quad
                quads[0] += 1
            elif endY > (gridHeight - 1)//2: #Bottom-right quad
                quads[3] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


def solution2():
    inpt = getInput()

    #Defining the rectangular grid that the robots will occupy, starting at (0,0)
    gridWidth = 101
    gridHeight = 103
    
    firstTreeConfig = None
    #Looping until no robot overlaps with the position of another robot
    t = 1
    while True:
        #if t % 1000 == 0:
        #    print("t =", t)
        isValid = True
        seen = {} #Dict where key = (x,y) pos of robot, value = True. This is just to quickly track positions without a grid
        for robot in range(len(inpt)):
            x,y = inpt[robot][0]
            xVel,yVel = inpt[robot][1]

            #Using the good old Displacement Formula: d = p + vt + 0.5at^2
            #d is end position, p is starting position, v is velocity, t is time, and a is acceleration (not used)
            #Then we constrain the values to the grid sizes defined by the problem
            endX = (x + (xVel * t)) % gridWidth
            endY = (y + (yVel * t)) % gridHeight

            if (endX,endY) not in seen.keys():
                seen[(endX,endY)] = 1
            else:
                #isValid = False
                #break
                seen[(endX,endY)] += 1

        #If there's at least one spot where two robots overlap, we increase time by 1sec and try again
        if not isValid:
            t += 1
        #Otherwise we've found the right value for t
        else:
            #print("\tConvergence at t =", t)
            #if (t - 6870) % 10403 == 0:
            #    print("\t\tChristmas Tree")
            #    t += 1

            displayGrid = []
            for r in range(gridHeight - 27 - 43):
                newRow = ['.'] * (gridWidth - 32 - 38)
                displayGrid.append(newRow)

            for k in [bot for bot in seen.keys()]:
                if k[1] > 26 and k[1] < gridHeight - 43 and k[0] < gridWidth - 32 and k[0] > 37:
                    displayGrid[k[1]-27][k[0]-38] = '#'
                else:
                    seen.pop(k)

            if firstTreeConfig is None:
                firstTreeConfig = seen
            else:
                if firstTreeConfig == seen:
                    print("Tree config seen before.")
                    return

            for line in displayGrid:
                print(''.join(line))

            print("t =", t)
            #yn = input("Easter Egg? Type y/n: ")
            #if yn == 'y' or yn == 'Y':
            #    break
            #else:
            t += 1

    return t


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())