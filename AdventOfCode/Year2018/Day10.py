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
            line = line.replace('\n', '')[10:-1].replace("> velocity=<", ',').replace(' ', '').split(',')
            inpt.append([int(x) for x in line])
    return inpt
            

def solution1():
    state = getInput()
    
    #Looping until the range of y coordinates of all points are within 8 values of each-other
    sec = 0
    yRange = []
    while True:
        sec += 1
        yRange = [None, None]
        nextState = []
        for line in state:
            x,y,xv,yv = line
            nextState.append([x+xv, y+yv, xv, yv])
            
            if yRange[0] is None or yRange[0] > y+yv:
                yRange[0] = y+yv
            if yRange[1] is None or yRange[1] < y+yv:
                yRange[1] = y+yv
            
        state = nextState
        if yRange[1] - yRange[0] <= 10:
            testing and print("\t", sec, "seconds, y-range values clear:", yRange)
            break

    xRange = [min([x for (x,y,xv,yv) in state]), max([x for (x,y,xv,yv) in state])]
    
    testing and print("x-range:", xRange, "    y-range:", yRange)
    
    grid = []
    for row in range(yRange[1] - yRange[0] + 1):
        newRow = [' '] * (xRange[1] - xRange[0] + 1)
        grid.append(newRow)
        
    for line in state:
        x,y,xv,yv = line
        testing and print("\tx =", x, "- offset", xRange[0], "=", x - xRange[0])
        testing and print("\ty =", y, "- offset", yRange[0], "=", y - yRange[0])
        grid[y-yRange[0]][x-xRange[0]] = "#"
        
    for line in grid:
        print(''.join(line))
    return


def solution2():
    state = getInput()
    
    #Looping until the range of y coordinates of all points are within 8 values of each-other
    sec = 0
    yRange = []
    while True:
        sec += 1
        yRange = [None, None]
        nextState = []
        for line in state:
            x,y,xv,yv = line
            nextState.append([x+xv, y+yv, xv, yv])
            
            if yRange[0] is None or yRange[0] > y+yv:
                yRange[0] = y+yv
            if yRange[1] is None or yRange[1] < y+yv:
                yRange[1] = y+yv
            
        state = nextState
        if yRange[1] - yRange[0] <= 10:
            return sec
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())