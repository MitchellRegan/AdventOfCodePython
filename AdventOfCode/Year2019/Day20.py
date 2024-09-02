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
    
    #Finding the positions of each teleporter
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if grid[r][c] not in [' ', '.', '#', '@']:
                if r == 0:
                    portalPositions[(r+1, c)] = '' + grid[r][c] + grid[r+1][c]
                    grid[r] = grid[r][:c] + ' ' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '@' + grid[r+1][c+1:]
                    
                elif grid[r-1][c] == '.':
                    portalPositions[(r, c)] = '' + grid[r][c] + grid[r+1][c]
                    grid[r] = grid[r][:c] + '@' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + ' ' + grid[r+1][c+1:]
                    
                elif c == 0:
                    portalPositions[(r, c+1)] = '' + grid[r][c] + grid[r][c+1]
                    grid[r] = ' @' + grid[r][c+2:]
                    
                elif c == len(grid[r]) - 2:
                    portalPositions[(r, c+1)] = '' + grid[r][c] + grid[r][c+1]
                    grid[r] = grid[r][:c] + '@ '
                    
                elif grid[r][c-1] == '.':
                    portalPositions[(r, c)] = '' + grid[r][c] + grid[r][c+1]
                    grid[r] = grid[r][:c] + '@ ' + grid[r][c+2:]
                    
                elif grid[r][c+2] == '.':
                    portalPositions[(r, c)] = '' + grid[r][c] + grid[r][c+1]
                    grid[r] = grid[r][:c] + ' @' + grid[r][c+2:]
                    
                elif grid[r+2][c] == '.':
                    portalPositions[(r,c)] = '' + grid[r][c] + grid[r+1][c]
                    grid[r] = grid[r][:c] + ' ' + grid[r][c+1:]
                    grid[r+1] = grid[r+1][:c] + '@' + grid[r+1][c+1:]
        
        grid[r] = grid[r].replace(' ', '#')
        
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
            
    print("Start:", startPoint)
    print("End:  ", endPoint)
    
    for line in grid:
        print(line.replace('.', ' '))

    seen = {startPoint:0}
    q = [startPoint]
    while len(q) > 0:
        r,c = q.pop(0)
        print(r,c)
        
        #Exit found
        if (r,c) == endPoint:
            return seen[endPoint]
        
        #Checking up
        if r != 0 and grid[r-1][c] != '#':
            if (r-1,c) not in seen.keys() or seen[(r-1,c)] > 1 + seen[(r,c)]:
                seen[(r-1,c)] = 1 + seen[(r,c)]
                if (r-1,c) in portalPositions:
                    for k in portalPositions.keys():
                        if k != (r-1,c) and portalPositions[k] == portalPositions[(r-1,c)]:
                            q.append(k)
                            seen[k] = 1 + seen[(r,c)]
                            break
                else:
                    q.append((r-1,c))
                
        #Checking down
        if r != len(grid)-1 and grid[r+1][c] != '#':
            if (r+1,c) not in seen.keys() or seen[(r+1,c)] > 1 + seen[(r,c)]:
                seen[(r+1,c)] = 1 + seen[(r,c)]
                if (r+1,c) in portalPositions:
                    for k in portalPositions.keys():
                        if k != (r+1,c) and portalPositions[k] == portalPositions[(r+1,c)]:
                            q.append(k)
                            seen[k] = 1 + seen[(r,c)]
                            break
                else:
                    q.append((r+1,c))
                
        #Checking left
        if c != 0 and grid[r][c-1] != '#':
            if (r,c-1) not in seen.keys() or seen[(r,c-1)] > 1 + seen[(r,c)]:
                seen[(r,c-1)] = 1 + seen[(r,c)]
                if (r,c-1) in portalPositions:
                    for k in portalPositions.keys():
                        if k != (r,c-1) and portalPositions[k] == portalPositions[(r,c-1)]:
                            q.append(k)
                            seen[k] = 1 + seen[(r,c)]
                            break
                else:
                    q.append((r,c-1))
                
        #Checking right
        if c != len(grid[r])-1 and grid[r][c+1] != '#':
            if (r,c+1) not in seen.keys() or seen[(r,c+1)] > 1 + seen[(r,c)]:
                seen[(r,c+1)] = 1 + seen[(r,c)]
                if (r,c+1) in portalPositions:
                    for k in portalPositions.keys():
                        if k != (r,c+1) and portalPositions[k] == portalPositions[(r,c+1)]:
                            q.append(k)
                            seen[k] = 1 + seen[(r,c)]
                            break
                else:
                    q.append((r,c+1))
                    

    for x in seen.keys():
        grid[x[0]] = grid[x[0]][:x[1]] + '+' + grid[x[0]][x[1]+1:]
        
    for line in grid:
        print(line.replace('.', ' '))
    for x in portalPositions.keys():
        print(portalPositions[x],x)
    return -1


def solution2():
    return


print("Year 2019, Day 20 solution part 1:", solution1())
print("Year 2019, Day 20 solution part 2:", solution2())