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
    grid, startPos, endPos = getInput()
    
    #Perform BFS starting from the endPos and store the distance each tile is from the endPos using a dict of tile (r,c):dist
    q = deque()
    q.append(startPos)
    tileDists = {startPos:0}
    while len(q) > 0:
        head = q.popleft()
        r,c = head

        for adj in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if adj not in tileDists.keys() and grid[adj[0]][adj[1]] != '#':
                q.append(adj)
                tileDists[adj] = tileDists[head]+1

    testing and print("End tile is at", endPos, "distance", tileDists[endPos], '\n')
    #Iterate through all tiles in the "tileDists" dictionary
    #   Check the tile's adjacent spaces for walls
    #   If the opposite side of that wall is another tile with a smaller distance, we can find the cheat distance
    ans = 0
    for tile in tileDists.keys():
        r,c = tile
        dist = tileDists[tile]

        for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
            cheatTile = None
            #Adjacent tile in this direction is a wall
            if grid[r+dir[0]][c+dir[1]] == '#':
                #One space after that wall isn't a wall and isn't out of bounds
                if r+(2*dir[0]) >= 0 and r+(2*dir[0]) <= len(grid)-1 \
                and c+(2*dir[1]) >= 0 and c+(2*dir[1]) <= len(grid[0])-1 \
                and grid[r+(2*dir[0])][c+(2*dir[1])] != '#':
                    cheatTile = (r+(2*dir[0]), c+(2*dir[1]))
                #Two spaces after that wall isn't a wall and isn't out of bounds
                elif r+(3*dir[0]) >= 0 and r+(3*dir[0]) <= len(grid)-1 \
                and c+(3*dir[1]) >= 0 and c+(3*dir[1]) <= len(grid[0])-1 \
                and grid[r+(3*dir[0])][c+(3*dir[1])] != '#':
                    cheatTile = (r+(3*dir[0]), c+(3*dir[1]))

            #If a cheat tile was found and it's distance is shorter than the current tile's distance, CHEAT!
            if cheatTile is not None and tileDists[cheatTile] > dist:
                savedDist = tileDists[cheatTile] - dist
                savedDist -= abs(r-cheatTile[0]) + abs(c-cheatTile[1])
                testing and print("Cheating from", tile, "dist", tileDists[tile], "to", cheatTile, "dist", tileDists[cheatTile], "saves", savedDist)
                if savedDist >= 100:
                    ans += 1

    return ans


def solution2():
    inpt = getInput()



    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#1305 not right
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())