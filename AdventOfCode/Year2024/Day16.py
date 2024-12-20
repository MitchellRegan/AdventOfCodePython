aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"
from collections import deque

def getInput():
    grid = []
    startPos = None
    endPos = None

    with open(inFile, 'r') as f:
        row = 0
        for line in f:
            line = line.replace('\n', '')
            if 'S' in line:
                startPos = (row, line.index('S'))
                line = line.replace('S', '.')
            if 'E' in line:
                endPos = (row, line.index('E'))
                line = line.replace('E', '.')
            grid.append(line)
            row += 1

    return grid, startPos, endPos
            

def solution1():
    grid, startPos, endPos = getInput()
    
    if testing:
        print("Start:", startPos, "\nEnd: ", endPos)
        for line in grid:
            print(line)

    q = [(startPos, '>', 0)] #Each element is ((row,col) position, direction facing, current score)
    seen = {} #Key = (row,col) position, value = score

    while len(q) > 0:
        pos, dir, curScore = q.pop(0)

        #If we found the end position, this is definitionally the lowest score since we sort the que by lowest score
        if pos == endPos:
            return curScore

        validDirs = []

        if dir == '>':
            validDirs = [('>', 0, 1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == '<':
            validDirs = [('<', 0, -1), ('v', 1, 0), ('^', -1, 0)]
        elif dir == 'v':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('v', 1, 0)]
        elif dir == '^':
            validDirs = [('>', 0, 1), ('<', 0, -1), ('^', -1, 0)]

        for nextDir in validDirs:
            nextScore = curScore
            nextRow = pos[0] + nextDir[1]
            nextCol = pos[1] + nextDir[2]

            #Moving in this direction is only valid if it's not blocked by a wall
            if grid[nextRow][nextCol] == '.':
                #Travelling in the same direction only adds 1 to the score
                if nextDir[0] == dir:
                    nextScore += 1
                #Making a turn 90 degrees adds 1000 to the score
                else:
                    nextScore += 1001

                if (nextRow, nextCol) not in seen.keys() or seen[(nextRow, nextCol)] > nextScore:
                    seen[(nextRow, nextCol)] = nextScore
                    q.append(((nextRow, nextCol), nextDir[0], nextScore))
                    #Sorting the que so that the lowest score always goes first (Dijkstra's algorithm)
                    q.sort(key = lambda x: x[2])

    return


def bfsIntersectionMap(startPos:tuple, endPos:tuple, intersections:dict, removed:list=[]):
    '''Performs a BFS through our map of connected intersection nodes.

    Parameters
    ----------
        startPos: (row, col) position of the starting location.
        endPos: (row, col) position of the destination point to reach.
        intersections: Dictionary where Key = (row, col) for every intersection in the map, and Value = [list of connected intersections]
        removed: List of (row, col) positions to ignore.
    
    Returns
    ----------
        deque for the shortest path to the end position.
        int for the minimal score of the path found. If no path is found, returns None
    '''
    shortestPath = deque()
    minimalScore = None
    q = deque()
    q.append((startPos, 0)) #Each element is ((row,col) pos, score from start)
    seen = {startPos:None} #Key = (r,c) pos of intersections found, Value = prev intersection
    while len(q) > 0:
        head, curScore = q.popleft()
        #testing and print("Checking", head)

        if head == endPos:
            minimalScore = curScore
            while head is not None:
                shortestPath.appendleft(head)
                head = seen[head]
            break

        for adj in intersections[head]:
            #testing and print("\tAdj:", adj)
            if adj in removed:
                continue
            elif adj not in seen.keys():
                d = abs(adj[0] - head[0]) + abs(adj[1] - head[1])
                #Checking to see if any 90 degree turns would be made between the adjacent pos, the head pos, and the head's previous pos
                if seen[head] is not None:
                    rdiff = seen[head][0] - adj[0]
                    cdiff = seen[head][1] - adj[1]
                    if rdiff != 0 and cdiff != 0:
                        d += 1000
                #Since the starting direction is '>' if the tile is adjacent to the start and above it, it counts as a turn
                elif head == startPos and head[0] > adj[0]:
                    d += 1000
                seen[adj] = head
                q.append((adj, d+curScore))
                q = deque(sorted(q, key=lambda x: x[1]))

    return shortestPath, minimalScore


def solution2():
    grid, startPos, endPos = getInput()
    
    #Finding every tile that's an intersection, corner, or dead-end
    intersections = {startPos:[], endPos:[]} #Key = (row,col) position, Value = [list of connected intersections and int for distance between]
    for row in range(len(grid)):
        grid[row] = [x for x in grid[row]]
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                adj = [grid[r][c] for (r,c) in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]].count('#')
                if adj != 2 or (adj == 2 and grid[row+1][col] != grid[row-1][col] and grid[row][col+1] != grid[row][col-1]):
                    grid[row][col] = 'I'
                    intersections[(row,col)] = []
        testing and print('\t', ''.join(grid[row]).replace('.', ' '))
    testing and print()

    #Performing a bfs from each intersection point to get the distances between connected intersections
    dists = {}#Key = (pair of (r,c) pos for connected intersections), Value = int for distance between them
    for i in intersections.keys():
        q = deque()
        q.append(i)
        seen = {i:0}#Key = (r,c) pos of tiles found, Value = distance from the starting intersection tile

        while len(q) > 0:
            r,c = q.popleft()

            #If another intersection point is found, we track the edge connection as well as the distance
            if grid[r][c] == 'I' and (r,c) != i:
                if (r,c) not in intersections[i]:
                    dists[(min(i, (r,c)), max(i, (r,c)))] = seen[(r,c)]
                    intersections[i].append((r,c))

            #Otherwise we keep spreading the bfs
            else:
                for adj in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if grid[adj[0]][adj[1]] != '#' and adj not in seen.keys():
                        seen[adj] = seen[i]+1
                        q.append(adj)

    #Finding the most optimal path to the end point using dijkstra's algorithm
    shortestPath, minimalScore = bfsIntersectionMap(startPos, endPos, intersections)
    allShortestPaths = [shortestPath]
    bestEdges = []
    for x in range(len(shortestPath)-1):
        bestEdges.append((min(shortestPath[x], shortestPath[x+1]), max(shortestPath[x], shortestPath[x+1])))

    #Performing multiple BFS on the grid while ignoring a different intersection each time in order to find all valid paths
    for i in intersections.keys():
        if i != startPos and i != endPos:
            testPath, testScore = bfsIntersectionMap(startPos, endPos, intersections, [i])
            if testScore is not None and testScore == minimalScore:
                for x in range(len(testPath)-1):
                    newEdge = (min(testPath[x], testPath[x+1]), max(testPath[x], testPath[x+1]))
                    if newEdge not in bestEdges:
                        bestEdges.append(newEdge)


    ans = 0
    for e in bestEdges:
        print("\t", e, "   = ", abs(e[0][0] - e[1][0]) + abs(e[0][1] - e[1][1]))
        ans += abs(e[0][0] - e[1][0]) + abs(e[0][1] - e[1][1])
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())