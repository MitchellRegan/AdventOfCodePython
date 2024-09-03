#https://adventofcode.com/2019/day/20
#https://adventofcode.com/2019/day/20#part2

import os
import itertools
inFileDir = os.path.dirname(__file__)
inFile = ""
testing = 1
if testing:
    inFile = os.path.join(inFileDir, "InputTestFiles/d20_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d20_real.txt")


def getInput():
    grid = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            grid.append(line)
    return grid
            

def solution1():
    grid = getInput()
    portalPositions = {}
    portalNames = {}
    
    #Finding the positions of each teleporter
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] not in [' ', '.', '#', '@']:
                portName = ''
                print(r,c, grid[r][c])
                
                if r == 0:
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r+2, c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r+2,c)]
                    else:
                        portalNames[portName].append((r+2,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif grid[r-1][c] == '.':
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r-1, c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r-1,c)]
                    else:
                        portalNames[portName].append((r-1,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif c == 0:
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c+2)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c+2)]
                    else:
                        portalNames[portName].append((r,c+2))
                    grid[r] = '##' + grid[r][c+2:]
                    
                elif grid[r][c-1] == '.':
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c-1)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c-1)]
                    else:
                        portalNames[portName].append((r,c-1))
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r][c+2] == '.':
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c+2)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c+2)]
                    else:
                        portalNames[portName].append((r,c+2))
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r+2][c] == '.':
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r+2,c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r+2,c)]
                    else:
                        portalNames[portName].append((r+2,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]

    #BFS from AA to ZZ
    startPoint = None
    endPoint = None
    for k in portalPositions.keys():
        if portalPositions[k] == 'AA':
            startPoint = k
        elif portalPositions[k] == 'ZZ':
            endPoint = k
    portalPositions.pop(startPoint)
    portalPositions.pop(endPoint)
    
    portalPositions = {}
    for n in portalNames.keys():
        if len(portalNames[n]) > 1:
            portalPositions[portalNames[n][0]] = portalNames[n][1]
            portalPositions[portalNames[n][1]] = portalNames[n][0]

    seen = {startPoint:0}
    q = [startPoint]
    while len(q) > 0:
        r,c = q.pop(0)
        
        #Exit found
        if (r,c) == endPoint:
            break
        
        if (r,c) in portalPositions.keys() and portalPositions[(r,c)] not in seen.keys():
            #print("Portal found at", (r,c), "->", portalPositions[(r,c)])
            #for x in portalNames.keys():
                #if (r,c) in portalNames[x]:
                #    print("\tDistance to portal", x, ":", seen[(r,c)])
            seen[portalPositions[(r,c)]] = seen[(r,c)] + 1
            q.append(portalPositions[(r,c)])
        
        #Checking up
        if r != 0 and grid[r-1][c] != '#':
            if (r-1,c) not in seen.keys():
                seen[(r-1,c)] = 1 + seen[(r,c)]
                q.append((r-1,c))
                
        #Checking down
        if r < len(grid) and grid[r+1][c] != '#':
            if (r+1,c) not in seen.keys():
                seen[(r+1,c)] = 1 + seen[(r,c)]
                q.append((r+1,c))
                
        #Checking left
        if c != 0 and grid[r][c-1] is not '#':
            if (r,c-1) not in seen.keys():
                seen[(r,c-1)] = 1 + seen[(r,c)]
                q.append((r,c-1))
                
        #Checking right
        if c < len(grid[r]) and grid[r][c+1] != '#':
            if (r,c+1) not in seen.keys():
                seen[(r,c+1)] = 1 + seen[(r,c)]
                q.append((r,c+1))

    for pn in portalNames.keys():
        for x in portalNames[pn]:
            grid[x[0]] = grid[x[0]][:x[1]] + '?' + grid[x[0]][x[1]+1:]

    for x in seen.keys():
        if x in portalPositions.keys():
            grid[x[0]] = grid[x[0]][:x[1]] + 'O' + grid[x[0]][x[1]+1:]
        else:
            grid[x[0]] = grid[x[0]][:x[1]] + ',' + grid[x[0]][x[1]+1:]
        
    for line in grid:
        print(line.replace('.', ' '))
    return seen[endPoint]


def solution2():
    grid = getInput()
    portalPositions = {}
    portalNames = {}
    
    #Finding the positions of each teleporter
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] not in [' ', '.', '#', '@']:
                portName = ''
                print(r,c, grid[r][c])
                
                if r == 0:
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r+2, c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r+2,c)]
                    else:
                        portalNames[portName].append((r+2,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif grid[r-1][c] == '.':
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r-1, c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r-1,c)]
                    else:
                        portalNames[portName].append((r-1,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif c == 0:
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c+2)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c+2)]
                    else:
                        portalNames[portName].append((r,c+2))
                    grid[r] = '##' + grid[r][c+2:]
                    
                elif grid[r][c-1] == '.':
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c-1)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c-1)]
                    else:
                        portalNames[portName].append((r,c-1))
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r][c+2] == '.':
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portalPositions[(r, c+2)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r,c+2)]
                    else:
                        portalNames[portName].append((r,c+2))
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r+2][c] == '.':
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portalPositions[(r+2,c)] = portName
                    if portName not in portalNames.keys():
                        portalNames[portName] = [(r+2,c)]
                    else:
                        portalNames[portName].append((r+2,c))
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]

    #BFS from AA to ZZ
    startPoint = None
    endPoint = None
    for k in portalPositions.keys():
        if portalPositions[k] == 'AA':
            startPoint = (k[0], k[1], 0)
        elif portalPositions[k] == 'ZZ':
            endPoint = (k[0], k[1], 0)
    portalPositions.pop((startPoint[0], startPoint[1]))
    portalPositions.pop((endPoint[0], endPoint[1]))
    
    portalPositions = {}
    for n in portalNames.keys():
        if len(portalNames[n]) > 1:
            portalPositions[portalNames[n][0]] = portalNames[n][1]
            portalPositions[portalNames[n][1]] = portalNames[n][0]

    seen = {startPoint:0}
    q = [startPoint]
    while len(q) > 0:
        r,c,d = q.pop(0)
        
        #Exit found
        if (r,c,d) == endPoint:
            break
        
        if (r,c) in portalPositions.keys() and portalPositions[(r,c)] not in seen.keys():
            #print("Portal found at", (r,c), "->", portalPositions[(r,c)])
            #for x in portalNames.keys():
                #if (r,c) in portalNames[x]:
                #    print("\tDistance to portal", x, ":", seen[(r,c)])
            seen[portalPositions[(r,c)]] = seen[(r,c)] + 1
            q.append(portalPositions[(r,c)])
        
        #Checking up
        if r != 0 and grid[r-1][c] != '#':
            if (r-1,c) not in seen.keys():
                seen[(r-1,c)] = 1 + seen[(r,c)]
                q.append((r-1,c))
                
        #Checking down
        if r < len(grid) and grid[r+1][c] != '#':
            if (r+1,c) not in seen.keys():
                seen[(r+1,c)] = 1 + seen[(r,c)]
                q.append((r+1,c))
                
        #Checking left
        if c != 0 and grid[r][c-1] is not '#':
            if (r,c-1) not in seen.keys():
                seen[(r,c-1)] = 1 + seen[(r,c)]
                q.append((r,c-1))
                
        #Checking right
        if c < len(grid[r]) and grid[r][c+1] != '#':
            if (r,c+1) not in seen.keys():
                seen[(r,c+1)] = 1 + seen[(r,c)]
                q.append((r,c+1))

    for pn in portalNames.keys():
        for x in portalNames[pn]:
            grid[x[0]] = grid[x[0]][:x[1]] + '?' + grid[x[0]][x[1]+1:]

    for x in seen.keys():
        if x in portalPositions.keys():
            grid[x[0]] = grid[x[0]][:x[1]] + 'O' + grid[x[0]][x[1]+1:]
        else:
            grid[x[0]] = grid[x[0]][:x[1]] + ',' + grid[x[0]][x[1]+1:]
        
    for line in grid:
        print(line.replace('.', ' '))
    return seen[endPoint]


print("Year 2019, Day 20 solution part 1:", solution1())
print("Year 2019, Day 20 solution part 2:", solution2())