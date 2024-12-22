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
    startPos = None
    endPos = None

    with open(inFile, 'r') as f:
        r = 0
        for line in f:
            line = [x for x in line.replace('\n', '')]
            if 'S' in line:
                startPos = (r, line.index('S'))
                line[startPos[1]] = '.'
            if 'E' in line:
                endPos = (r, line.index('E'))
                line[endPos[1]] = '.'
            inpt.append(line)
            r += 1

    return inpt, startPos, endPos
            

def bfsCheat(grid_:list, start_:tuple, end_:tuple, numCheatSec_:int, cheatStartTime_:int)->int:
    '''Performs a BFS search on the given grid and starting/ending positions. Frontier of the search will go through walls
    for a number of seconds (numCheatSec_) at a given starting time (cheatStartTime_).
    
    Returns
    ----------
    Int for the number of seconds it takes to reach the end.
    '''
    seen = {start_:0} #Key = (row,col) position of tile visited, Value = time stamp when visited
    q = deque()
    q.append(start_)

    while len(q) > 0:
        head = q.popleft()
        r,c = head

        if head == end_:
            return seen[head]

        canCheat = False
        if seen[head] + 1 >= cheatStartTime_ and seen[head] + 1 < cheatStartTime_ + numCheatSec_:
            canCheat = True

        if grid_[r][c] == '#' and not canCheat:
            continue
        else:
            for adj in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                #Making sure the adjacent location isn't going off the grid or has been seen before
                if adj[0] >= 0 and adj[0] < len(grid_) and adj[1] >= 0 and adj[1] < len(grid_[0]) and adj not in seen.keys():
                    #If the tile isn't a wall OR it is a wall and it's during the cheat time, it's allowed
                    if grid_[adj[0]][adj[1]] != '#' or canCheat:
                        seen[adj] = seen[head] + 1
                        q.append(adj)
    return -1


def solution1():
    inpt, startPos, endPos = getInput()
    
    baselineTime = bfsCheat(inpt, startPos, endPos, 2, -2)
    print("Baseline bfs time:", baselineTime)

    ans = 0
    for t in range(0, baselineTime-100):
        if t % 20 == 0:
            print("Checking t =", t)
        cheatTime = bfsCheat(inpt, startPos, endPos, 2, t)
        savedTime = baselineTime - cheatTime
        if savedTime >= 100:
            ans += 1
        testing and print("\tCheating at t =", t, "gives time of", cheatTime, "saving", savedTime, "sec")

    return ans


def solution2():
    inpt = getInput()



    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#1305 not right
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())