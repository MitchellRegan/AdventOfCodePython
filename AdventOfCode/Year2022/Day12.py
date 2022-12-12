#https://adventofcode.com/2022/day/12
#https://adventofcode.com/2022/day/12#part2

from HelperFunctions import inputReaders as ir
import os
inFileDir = os.path.dirname(__file__)
#inFile = os.path.join(inFileDir, "InputTestFiles/d12_test.txt")
inFile = os.path.join(inFileDir, "InputRealFiles/d12_real.txt")

def solution1():
    #helper function to get input as grid
    grid = ir.to2DList(inFile)

    #Getting the start and end pos
    start = None
    end = None
    #converting all other positions into int values based on ascii codes
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] is 'S':
               start = (r,c)
               grid[r][c] = 0
            elif grid[r][c] is 'E':
                end = (r,c)
                asciiCode = ord('z') - 97
                grid[r][c] = asciiCode
            else:
                asciiCode = ord(grid[r][c]) - 97
                grid[r][c] = asciiCode
    
    #BFS search from S to E
    q = [start]
    dists = {start:0}
    while len(q) > 0:
        cur = q.pop(0)
        #print(cur)
        curHeight = grid[cur[0]][cur[1]]
        curDist = dists[cur]

        if cur == end:
            break
        
        #Checking up
        if cur[0] > 0:
            #print(" - U")
            r = cur[0]-1
            c = cur[1]
            up = (r,c)
            height = grid[r][c]
            if height - curHeight < 2:
                if up not in dists.keys():
                    dists[up] = curDist + 1
                    q.append(up)
                elif dists[up] > (curDist + 1):
                    dists[up] = curDist + 1
        #Checking down
        if cur[0] < len(grid) - 1:
            #print(" - D")
            r = cur[0]+1
            c = cur[1]
            down = (r,c)
            height = grid[r][c]
            if height - curHeight < 2:
                if down not in dists.keys():
                    dists[down] = curDist + 1
                    q.append(down)
                elif dists[down] > (curDist + 1):
                    dists[down] = curDist + 1
        #Checking left
        if cur[1] > 0:
            #print(" - L")
            r = cur[0]
            c = cur[1]-1
            left = (r,c)
            height = grid[r][c]
            if height - curHeight < 2:
                if left not in dists.keys():
                    dists[left] = curDist + 1
                    q.append(left)
                elif dists[left] > (curDist + 1):
                    dists[left] = curDist + 1
        #Checking right
        if cur[1] < len(grid[0])-1:
            #print(" - R")
            r = cur[0]
            c = cur[1]+1
            right = (r,c)
            height = grid[r][c]
            if height - curHeight < 2:
                if right not in dists.keys():
                    dists[right] = curDist + 1
                    q.append(right)
                elif dists[right] > (curDist + 1):
                    dists[right] = curDist + 1

    return dists[end]


def solution2():
    #helper function to get input as grid
    grid = ir.to2DList(inFile)

    #Getting the start and end pos
    start = []
    end = None
    #converting all other positions into int values based on ascii codes
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] is 'S':
               grid[r][c] = 0
            elif grid[r][c] is 'E':
                end = (r,c)
                asciiCode = ord('z') - 97
                grid[r][c] = asciiCode
            elif grid[r][c] is 'a':
                start.append((r,c))
                asciiCode = ord(grid[r][c]) - 97
                grid[r][c] = asciiCode
            else:
                asciiCode = ord(grid[r][c]) - 97
                grid[r][c] = asciiCode
    
    leastSteps = float('inf')
    for s in start:
        #BFS search from S to E
        q = [s]
        dists = {s:0}
        while len(q) > 0:
            cur = q.pop(0)
            #print(cur)
            curHeight = grid[cur[0]][cur[1]]
            curDist = dists[cur]

            if cur == end:
                break
        
            #Checking up
            if cur[0] > 0:
                #print(" - U")
                r = cur[0]-1
                c = cur[1]
                up = (r,c)
                height = grid[r][c]
                if height - curHeight < 2:
                    if up not in dists.keys():
                        dists[up] = curDist + 1
                        q.append(up)
                    elif dists[up] > (curDist + 1):
                        dists[up] = curDist + 1
            #Checking down
            if cur[0] < len(grid) - 1:
                #print(" - D")
                r = cur[0]+1
                c = cur[1]
                down = (r,c)
                height = grid[r][c]
                if height - curHeight < 2:
                    if down not in dists.keys():
                        dists[down] = curDist + 1
                        q.append(down)
                    elif dists[down] > (curDist + 1):
                        dists[down] = curDist + 1
            #Checking left
            if cur[1] > 0:
                #print(" - L")
                r = cur[0]
                c = cur[1]-1
                left = (r,c)
                height = grid[r][c]
                if height - curHeight < 2:
                    if left not in dists.keys():
                        dists[left] = curDist + 1
                        q.append(left)
                    elif dists[left] > (curDist + 1):
                        dists[left] = curDist + 1
            #Checking right
            if cur[1] < len(grid[0])-1:
                #print(" - R")
                r = cur[0]
                c = cur[1]+1
                right = (r,c)
                height = grid[r][c]
                if height - curHeight < 2:
                    if right not in dists.keys():
                        dists[right] = curDist + 1
                        q.append(right)
                    elif dists[right] > (curDist + 1):
                        dists[right] = curDist + 1

        if end in dists.keys():
            if dists[end] < leastSteps:
                leastSteps = dists[end]

    return leastSteps


print("Year 2022, Day 1 solution part 1:", solution1())
print("Year 2022, Day 1 solution part 2:", solution2())