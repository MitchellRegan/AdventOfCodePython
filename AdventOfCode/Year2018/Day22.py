aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    depth = None
    target = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if depth is None:
                depth = int(line.replace("depth: ", ''))
            else:
                line = line.replace("target: ", '').split(',')
                target = (int(line[0]), int(line[1]))

    return depth, target
            

def solution1():
    depth, target = getInput()
    
    erosionLevels = {}#Key = (x,y) coordinate, Value = int for the erosion level (required for finding the tile type)
    tileType = {} #Key = (x,y) coordinate, Value = int for the tile type (0:rocky, 1:wet, 2:narrow)
    def getTileType(x_:int, y_:int)->int:
        geoIndex = 0
            
        if (x_,y_) == (0,0) or (x_,y_) == target:
            geoIndex = 0
        elif y_ == 0:
            geoIndex = x_ * 16807
        elif x_ == 0:
            geoIndex = y_ * 48271
        else:
            geoIndex = erosionLevels[(x_-1,y_)] * erosionLevels[(x_,y_-1)]
                
        eroLevel = (geoIndex + depth) % 20183
        erosionLevels[(x_,y_)] = eroLevel
        tileType[(x_,y_)] = eroLevel % 3
        return eroLevel % 3
    
    
    seen = {(0,0):[0,None]} #Key = (x,y) coordinate of a visited tile, Value = [total distance, previous tile]
    q = [(0,0,0,"T")] #Each value in the que is (x coord, y coord, total distance, held tool)
    while len(q) > 0:
        x,y,dist,tool = q.pop(0)
        
        nextTiles = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        for nt in nextTiles:
            #Ignoring tiles with negative x or y values
            if nt[0] < 0 or nt[1] < 0:
                continue
            
            #Any new tiles need their tile type and erosion level calculated and stored
            if nt not in seen.keys():
                getTileType(nt[0], nt[1])
                
            #Based on this next tile's type, our held tool might need to be changed, increasing the travel distance
            travelDist = 1
            nextTool = tool
            #if tool == 'T' and tileType[nt] == 1: #Torch can't be used on wet tiles
                

    return


def solution2():
    depth, target = getInput()
    
    erosionLevels = {} #Key = (x,y) coordinate, Value = erosion level of this coordinate
    
    for x in range(0, target[0]+1):
        for y in range(0, target[1]+1):
            testing and print("\n", (x,y))
            geoIndex = 0
            
            if (x,y) == (0,0) or (x,y) == target:
                geoIndex = 0
                testing and print("\tStart/End pos. Geo Index = 0")
            elif y == 0:
                geoIndex = x * 16807
                testing and print("\t16807 * x", x, "=", geoIndex)
            elif x == 0:
                geoIndex = y * 48271
                testing and print("\t48271 * y", y, "=", geoIndex)
            else:
                geoIndex = erosionLevels[(x-1,y)] * erosionLevels[(x,y-1)]
                testing and print("\t", erosionLevels[(x-1,y)], "*", erosionLevels[(x,y-1)], "=", geoIndex)
                
            eroLevel = (geoIndex + depth) % 20183
            erosionLevels[(x,y)] = eroLevel
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())