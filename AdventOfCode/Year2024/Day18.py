aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"
from collections import deque

def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(',')
            inpt.append([int(x) for x in line])

    return inpt
            

def solution1():
    inpt = getInput()
    width = 70
    height = 70
    numBytes = 1024
    if testing:
        width = 6
        height = 6
        numBytes = 12
    
    walls = {}
    for w in range(numBytes):
        x,y = inpt[w]
        walls[(x,y)] = True

    startPos = (0,0)
    endPos = (width, height)
    seen = {startPos:0} #Key = (x,y) position, Value = distance from start
    q = deque()
    q.append(startPos)
    while len(q) > 0:
        head = q.popleft()

        if head == endPos:
            return seen[head]

        for adj in [(head[0]+1, head[1]), (head[0]-1, head[1]), (head[0], head[1]+1), (head[0], head[1]-1)]:
            if adj[0] >= 0 and adj[0] <= width and adj[1] >=0 and adj[1] <= height:
                if adj not in seen.keys() and adj not in walls.keys():
                    q.append(adj)
                    seen[adj] = seen[head]+1

    return


def solution2():
    inpt = getInput()
    width = 70
    height = 70
    if testing:
        width = 6
        height = 6
    
    walls = {} #Key = (x,y) position of blocked space, Value doesn't matter

    for w in range(len(inpt)):
        x,y = inpt[w]
        walls[(x,y)] = True
        isValid = False

        startPos = (0,0)
        endPos = (width, height)
        seen = {startPos:0} #Key = (x,y) position, Value = distance from start
        q = deque()
        q.append(startPos)
        while len(q) > 0:
            head = q.popleft()

            if head == endPos:
                isValid = True
                break

            for adj in [(head[0]+1, head[1]), (head[0]-1, head[1]), (head[0], head[1]+1), (head[0], head[1]-1)]:
                if adj[0] >= 0 and adj[0] <= width and adj[1] >=0 and adj[1] <= height:
                    if adj not in seen.keys() and adj not in walls.keys():
                        q.append(adj)
                        seen[adj] = seen[head]+1
        if not isValid:
            return "" + str(x) + ',' + str(y)
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())