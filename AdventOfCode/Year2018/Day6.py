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
            line = line.replace('\n', '').split(', ')
            inpt.append((int(line[0]), int(line[1])))
    return inpt
            

def solution1():
    inpt = getInput()
    
    minMaxX = [None, None]
    minMaxY = [None, None]
    for point in inpt:
        x,y = point
        if minMaxX[0] is None or x < minMaxX[0]:
            minMaxX[0] = x
        if minMaxX[1] is None or x > minMaxX[1]:
            minMaxX[1] = x
        if minMaxY[0] is None or y < minMaxY[0]:
            minMaxY[0] = y
        if minMaxY[1] is None or y > minMaxY[1]:
            minMaxY[1] = y
    testing and print("X Range:", minMaxX, "    Y Range:", minMaxY)
    
    #Performing a BFS search from every starting point
    found = {} #Key is (x,y) point, value pair is (int for distance, XY pos of starting point)
    q = [] #Every element is (x,y) position to check
    ignorePoints = [] #List of points that seem to go out infinitely, so we ignore them in the final result
    for p in inpt:
        q.append(p)
        found[p] = (0,p)
    while len(q) > 0:
        currPoint = q.pop(0)
        x,y = currPoint
        dist, fromPoint = found[currPoint]
        testing and print("Point", currPoint, "   From", fromPoint, "    Distance", dist)
        
        #If the distance of the point is too far, we mark this point to be ignored
        if dist > max(minMaxX[1], minMaxY[1]) * 2:
            if fromPoint not in ignorePoints:
                ignorePoints.append(fromPoint)
        #If this is from a starting point that needs to be ignored, we don't continue the bfs
        #Otherwise we keep doing a bfs outward from this point
        elif fromPoint not in ignorePoints and fromPoint is not None:
            for nextPoint in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                #Checking to see if this point has already been found by another starting point
                if nextPoint in found.keys():
                    if found[nextPoint][1] != fromPoint and found[nextPoint][1] is not None and found[nextPoint][0] == dist+1:
                        #If found by another starting point and at the same distance away, this is an overlapping spot that counts for none of the starting points
                        found[nextPoint] = (-1, None)
                else:
                    found[nextPoint] = (dist+1, fromPoint)
                    q.append(nextPoint)
                    
    testing and print("Ignoring points", ignorePoints)
    posCount = {}
    for x in found:
        if found[x][1] is not None and found[x][1] not in ignorePoints:
            if found[x][1] not in posCount.keys():
                posCount[found[x][1]] = 1
            else:
                posCount[found[x][1]] += 1
                
    return max([posCount[x] for x in posCount.keys()])


def solution2():
    inpt = getInput()
    
    minMaxX = [None, None]
    minMaxY = [None, None]
    for point in inpt:
        x,y = point
        if minMaxX[0] is None or x < minMaxX[0]:
            minMaxX[0] = x
        if minMaxX[1] is None or x > minMaxX[1]:
            minMaxX[1] = x
        if minMaxY[0] is None or y < minMaxY[0]:
            minMaxY[0] = y
        if minMaxY[1] is None or y > minMaxY[1]:
            minMaxY[1] = y
    
    #Defining the total manhattan dist from all points that the target area needs to be within
    targetDist = 10000
    if testing:
        targetDist = 32
    ans = 0
    for x in range(minMaxX[0], minMaxX[1]+1):
        for y in range(minMaxY[0], minMaxY[1]+1):
            score = 0
            for point in inpt:
                score += abs(point[0]-x) + abs(point[1]-y)
            #If the point's total score (manhattan dist sum from all points) is within the target, we count it
            if score < targetDist:
                ans += 1
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1()) #42693 too high
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())