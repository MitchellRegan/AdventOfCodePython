#https://adventofcode.com/2023/day/23
#https://adventofcode.com/2023/day/23#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 1:
    inFile = os.path.join(inFileDir, "InputTestFiles/d23_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d23_real.txt")


def getInput():
    input = []
    start = None
    end = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace('.', ' ')
            line = [x for x in line]
            if start is None:
                for c in range(0, len(line)):
                    if line[c] == ' ':
                        start = (0, c)
                        #line[c] = 'v'
            input.append(line)

    for c in range(0, len(input[0])):
        if input[-1][c] == ' ':
            end = (len(input)-1, c)
            #input[-1][c] = 'v'
            break
    return input, start, end


def nextSlopes(start_, grid_):
    q = []
    seen = {start_:0}

    if grid_[start_[0]][start_[1]] == '>':
        q.append((start_[0], start_[1]+1, 1))
    elif grid_[start_[0]][start_[1]] == '<':
        q.append((start_[0], start_[1]-1, 1))
    elif grid_[start_[0]][start_[1]] == '^':
        q.append((start_[0]-1, start_[1], 1))
    elif grid_[start_[0]][start_[1]] == 'v':
        q.append((start_[0]+1, start_[1], 1))

    otherSlopes = []
    while len(q) > 0:
        r,c,steps = q.pop(0)
        
        seen[(r,c)] = steps

        if grid_[r][c] in ['>', '<', 'v', '^'] and (r,c) != start_ and (r,c,steps) not in otherSlopes:
            otherSlopes.append((r,c,steps))
            seen[(r,c,)] = steps
        else:
            if c < len(grid_[0])-1 and grid_[r][c+1] != '#' and (r,c+1) not in seen.keys():
                q.append((r,c+1,steps+1))
            if c > 0 and grid_[r][c-1] != '#' and (r,c-1) not in seen.keys():
                q.append((r,c-1,steps+1))
            if r < len(grid_)-1 and grid_[r+1][c] != '#' and (r+1,c) not in seen.keys():
                q.append((r+1,c,steps+1))
            if r > 0 and grid_[r-1][c] != '#' and (r-1,c) not in seen.keys():
                q.append((r-1,c,steps+1))

    return otherSlopes


def solution1():
    grid, start, end = getInput()

    path = {start:None} #tile's (r,c) -> prev tile's (r,c)
    dist = {start:0} #tile's (r,c) -> distance int
    q = [start]
    while len(q) > 0:
        cur = q.pop(0)
        r = cur[0]
        c = cur[1]

        nextTiles = []
        if grid[r][c] == ' ': nextTiles = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        elif grid[r][c] == '>': nextTiles = [(r,c+1)]
        elif grid[r][c] == '<': nextTiles = [(r,c-1)]
        elif grid[r][c] == '^': nextTiles = [(r-1,c)]
        elif grid[r][c] == 'v': nextTiles = [(r+1,c)]

        for tile in nextTiles:
            #Checking for out of bounds tiles
            if tile[0] < 0 or tile[1] < 0 or tile[0] > len(grid)-1 or tile[1] > len(grid[0])-1:
                continue
            #Checking if the tile is blocked or the previously-traversed tile
            if grid[tile[0]][tile[1]] == '#' or tile == path[cur]:
                continue
            #Checking if the tile has already been traversed with a longer path
            if tile in dist.keys() and dist[tile] > dist[cur]+1:
                continue

            q.append(tile)
            path[tile] = cur
            dist[tile] = dist[cur]+1

    #Getting the longest path traveled by looking at the distance taken to get to the end point
    return dist[end]


def solution2():
    grid, start, end = getInput()

    path = {start:None} #tile's (r,c) -> prev tile's (r,c)
    dist = {start:0} #tile's (r,c) -> distance int
    q = [start]
    while len(q) > 0:
        cur = q.pop(0)
        r = cur[0]
        c = cur[1]

        nextTiles = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        for tile in nextTiles:
            #Checking for out of bounds tiles
            if tile[0] < 0 or tile[1] < 0 or tile[0] > len(grid)-1 or tile[1] > len(grid[0])-1:
                continue
            #Checking if the tile is blocked or the previously-traversed tile
            if grid[tile[0]][tile[1]] == '#' or tile == path[cur]:
                continue
            #Checking if the tile has already been traversed with a longer path
            if tile in dist.keys() and dist[tile] > dist[cur]+1:
                continue

            q.append(tile)
            path[tile] = cur
            dist[tile] = dist[cur]+1

    #Getting the longest path traveled by looking at the distance taken to get to the end point
    return dist[end]


print("Year 2023, Day 23 solution part 1:", solution1())
print("Year 2023, Day 23 solution part 2:", solution2())