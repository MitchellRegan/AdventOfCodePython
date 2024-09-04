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
                #print(r,c, grid[r][c])
                
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
        
    #for line in grid:
    #    print(line.replace('.', ' '))
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
                portPos = None
                
                if r == 0: #Portal leads up to depth +1
                    portName = '' + grid[r][c] + grid[r+1][c] + "_U"
                    portPos = (r+2, c)
                    #portalPositions[(r+2, c)] = portName
                    #portalNames[portName] = (r+2,c)
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif grid[r-1][c] == '.':
                    portName = '' + grid[r][c] + grid[r+1][c]
                    portPos = (r-1, c)
                    if r == len(grid)-2: #Portal leads up to depth +1
                        portName = portName + "_U"
                    else: #Portal leads down to depth -1
                        portName = portName + "_D"
                    #portalPositions[(r-1, c)] = portName
                    #portalNames[portName] = (r-1,c)
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                elif c == 0: #Portal leads up to depth +1
                    portName = '' + grid[r][c] + grid[r][c+1] + "_U"
                    portPos = (r, c+2)
                    #portalPositions[(r, c+2)] = portName
                    #portalNames[portName] = (r,c+2)
                    grid[r] = '##' + grid[r][c+2:]
                    
                elif grid[r][c-1] == '.':
                    portName = '' + grid[r][c] + grid[r][c+1]
                    portPos = (r, c-1)
                    if c == len(grid[r])-2: #Portal leads up to depth +1
                        portName = portName + "_U"
                    else: #Portal leads down to depth -1
                        portName = portName + "_D"
                    #portalPositions[(r, c-1)] = portName
                    #portalNames[portName] = (r,c-1)
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r][c+2] == '.': #Portal leads down to depth -1
                    portName = '' + grid[r][c] + grid[r][c+1] + "_D"
                    portPos = (r, c+2)
                    #portalPositions[(r, c+2)] = portName
                    #portalNames[portName] = (r,c+2)
                    grid[r] = grid[r][:c] + '##' + grid[r][c+2:]
                    
                elif grid[r+2][c] == '.': #Portal leads down to depth -1
                    portName = '' + grid[r][c] + grid[r+1][c] + "_D"
                    portPos = (r+2, c)
                    #portalPositions[(r+2,c)] = portName
                    #portalNames[portName] = (r+2,c)
                    grid[r] = grid[r][:c] + '#' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '#' + grid[r+1][c+1:]
                    
                if portName[0:2] == "AA" or portName[0:2] == "ZZ":
                    portName = portName[0:2]
                portalPositions[portPos] = portName
                portalNames[portName] = portPos

    #BFS from AA to ZZ
    startPoint = None
    endPoint = None
    #print("Portal Positions:")
    for k in portalPositions.keys():
        #print("\t", k, "=", portalPositions[k], "___Double-check position:", portalNames[portalPositions[k]])
        if k != portalNames[portalPositions[k]]:
            print("===== ERROR: Mismatched position for", k)
            print("\tPortal Positions:", k, ":", portalPositions[k])
            print("\tPortal Names:    ", portalPositions[k], ":", portalNames[portalPositions[k]])
            return -1
        if portalPositions[k][0:2] == 'AA':
            startPoint = (portalPositions[k], 0)
        elif portalPositions[k][0:2] == 'ZZ':
            endPoint = (portalPositions[k], 0)

    #Finding distances from each portal to every other portal
    connections = {} #Dict where key is portalName and value-pair is list of connected portnames
    edgeLengths = {} #Dict where key is (min(portnames), max(portnames)) and value-pair is the distance between them
    
    for p in portalNames.keys():
        connections[p] = []
        dist = {portalNames[p]:0}
        q = [portalNames[p]]
        while len(q) > 0:
            head = q.pop(0)
            r,c = head
            
            if head in portalPositions.keys() and portalPositions[head] != p:
                #print("\tFound portal", portalPositions[head], "at distance", dist[head])
                if portalPositions[head][0:2] != "AA": #Ignore all distances traveling TO the maze start AA
                    connections[p].append(portalPositions[head])
                    edge = (min(p, portalPositions[head]), max(p, portalPositions[head]))
                    if edge not in edgeLengths:
                        edgeLengths[edge] = dist[head]
            
            #Up
            if r > 0 and (r-1,c) not in dist.keys() and grid[r-1][c] != '#':
                dist[(r-1,c)] = 1 + dist[head]
                q.append((r-1,c))
            #Down
            if r < len(grid)-1 and (r+1,c) not in dist.keys() and grid[r+1][c] != '#':
                dist[(r+1,c)] = 1 + dist[head]
                q.append((r+1,c))
            #Left
            if c > 0 and (r,c-1) not in dist.keys() and grid[r][c-1] != '#':
                dist[(r,c-1)] = 1 + dist[head]
                q.append((r,c-1))
            #Right
            if c < len(grid[r])-1 and (r,c+1) not in dist.keys() and grid[r][c+1] != '#':
                dist[(r,c+1)] = 1 + dist[head]
                q.append((r,c+1))
            
    if testing:
        print("Connections:")
        for c in connections.keys():
            print("\t", c, ":", connections[c])
        print("Edge Lengths:")
        for e in edgeLengths.keys():
            print("\t", e, ":", edgeLengths[e])
                
    seen = {startPoint:0} #Dict where key is (portName, depth) and value-pair is totalDist
    q = [] #Each value is (portName, depth, totalDist)
    for con in connections[startPoint[0]]:
        q.append((con, 0, edgeLengths[("AA", con)]))
        seen[(con, 0)] = edgeLengths[("AA", con)]
    testing and print("\nStarting recursive bfs starting with", startPoint, "and travelling to", endPoint)
    testing and print("Que:", q)
    testing and print("Seen:", seen)

    while len(q) > 0:
        port, depth, totalDist = q.pop(0)
        testing and print(port, "depth", depth, "at distance", totalDist)
        
        #Quitting when the exit is found, because the first instance found will have the shortest distance
        if port == "ZZ" and depth == 0:
            return totalDist

        #Otherwise, we take this portal to the next depth up/down
        else:
            newPort = ""
            newDepth = depth
            if port[-1] == "U":
                newPort = port[0:-1] + "D"
                newDepth += 1
            else:
                newPort = port[0:-1] + "U"
                newDepth -= 1
                
            seen[(newPort, newDepth)] = totalDist + 1
            testing and print("\tTaking portal", port, "to", newPort, "depth", newDepth, "at distance", seen[(newPort, newDepth)])
            for con in connections[newPort]:
                #Ignoring connections to the exit that aren't on depth 0 because that's the only one that exists
                if newDepth != 0 and con == "ZZ":
                    continue
                testing and print("\t\t", newPort, "->", con, "depth", newDepth, "    path dist:", edgeLengths[(min(newPort, con), max(newPort, con))])
                q.append((con, newDepth, totalDist + 1 + edgeLengths[(min(newPort, con), max(newPort, con))]))
                seen[(con, newDepth)] = totalDist + 1 + edgeLengths[(min(newPort, con), max(newPort, con))]
        
            #Sorting the que so the ones with the smallest distance are at the front
            q.sort(key=lambda x: x[2])
            
        #print("\tQue:", q)
        #break
            
    return -1


print("Year 2019, Day 20 solution part 1:", solution1())
print("Year 2019, Day 20 solution part 2:", solution2())
#4506 too low