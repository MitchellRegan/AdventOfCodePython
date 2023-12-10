#https://adventofcode.com/2023/day/10
#https://adventofcode.com/2023/day/10#part2

import os
inFileDir = os.path.dirname(__file__)
inFile = ""
if 0:
    inFile = os.path.join(inFileDir, "InputTestFiles/d10_test.txt")
else:
    inFile = os.path.join(inFileDir, "InputRealFiles/d10_real.txt")


def getInput():
    input = []

    with open(inFile, 'r') as f:
        lineNum = 0

        for line in f:
            line = line.replace('\n', '')
            input.append(line)
            lineNum += 1

    return input


def getTileMap(input:list):
    tileMap = {}
    start = None

    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            tile = input[row][col]
            if tile == '.':
                continue
            elif tile == 'S':
                start = (row,col)
                up = left = right = down = False
                if row > 0 and input[row-1][col] in ['|', '7', 'F']:
                    up = True
                if row < len(input)-1 and input[row+1][col] in ['|', 'J', 'L']:
                    down = True
                if col > 0 and input[row][col-1] in ['-', 'F', 'L']:
                    left = True
                if col < len(input[0])-1 and input[row][col+1] in ['-', 'J', '7']:
                    right = True

                if up and down:
                    tile = '|'
                elif left and right:
                    tile = '-'
                elif up and right:
                    tile = 'L'
                elif up and left:
                    tile = 'J'
                elif down and right:
                    tile = 'F'
                elif down and left:
                    tile = '7'

            if tile == '|':
                if row > 0 and row < len(input)-1:
                    tileMap[(row,col)] = [(row-1,col), (row+1,col)]
            elif tile == '-':
                if col > 0 and col < len(input[0])-1:
                    tileMap[(row,col)] = [(row,col-1), (row,col+1)]
            elif tile == 'L':
                if row > 0 and col < len(input[0])-1:
                    tileMap[(row,col)] = [(row-1,col), (row,col+1)]
            elif tile == 'J':
                if row > 0 and col > 0:
                    tileMap[(row,col)] = [(row-1,col), (row,col-1)]
            elif tile == '7':
                if row < len(input)-1 and col > 0:
                    tileMap[(row,col)] = [(row+1,col), (row,col-1)]
            elif tile == 'F':
                if row < len(input)-1 and col < len(input[0])-1:
                    tileMap[(row,col)] = [(row+1,col), (row,col+1)]
    
    return tileMap, start


def solution1():
    input = getInput()
    tileMap, start = getTileMap(input)

    #BFS search for tile furthest away from start
    que = [start]                
    dists = {start:0}
    while len(que) > 0:
        pos = que.pop(0)
        connection1 = tileMap[pos][0]
        connection2 = tileMap[pos][1]
        
        if connection1 not in dists.keys():
            dists[connection1] = dists[pos]+1
            que.append(connection1)
        if connection2 not in dists.keys():
            dists[connection2] = dists[pos]+1
            que.append(connection2)

    return max(dists.values())


def solution2():
    input = getInput()
    tileMap, start = getTileMap(input)

    #Doubling the size of the input, filling the extra rows and columns with dummy chars to be overwritten
    for i in range(0, (len(input)*2)-1):
        if i % 2 == 0:
            newLine = []
            for char in input[i]:
                newLine.append(char)
                newLine.append('?')
            newLine = newLine[:-1]
            input[i] = newLine
        else:
            newLine = ['?'] * len(input[0])
            input.insert(i, newLine)

    #Iterating through all tiles in the closed loop and marking them with 'X'
    path = [start]
    while len(path) > 0:
        pos = path.pop(0)
        c1 = tileMap[pos][0]
        c2 = tileMap[pos][1]

        if input[c1[0]*2][c1[1]*2] != 'X':
            path.append(c1)
        if input[c2[0]*2][c2[1]*2] != 'X':
            path.append(c2)

        posChar = input[pos[0]*2][pos[1]*2]
        input[pos[0]*2][pos[1]*2] = 'X'
        
        if posChar == '|':
            input[(pos[0]*2)-1][(pos[1]*2)] = 'X'
            input[(pos[0]*2)+1][(pos[1]*2)] = 'X'
        elif posChar == '-':
            input[(pos[0]*2)][(pos[1]*2)-1] = 'X'
            input[(pos[0]*2)][(pos[1]*2)+1] = 'X'
        elif posChar == 'L':
            input[(pos[0]*2)-1][(pos[1]*2)] = 'X'
            input[(pos[0]*2)][(pos[1]*2)+1] = 'X'
        elif posChar == 'J':
            input[(pos[0]*2)-1][(pos[1]*2)] = 'X'
            input[(pos[0]*2)][(pos[1]*2)-1] = 'X'
        elif posChar == '7':
            input[(pos[0]*2)+1][(pos[1]*2)] = 'X'
            input[(pos[0]*2)][(pos[1]*2)-1] = 'X'
        elif posChar == 'F':
            input[(pos[0]*2)+1][(pos[1]*2)] = 'X'
            input[(pos[0]*2)][(pos[1]*2)+1] = 'X'

    #Looking through the input for any tiles that haven't already been identified
    for row in range(0, len(input)):
        for col in range(0, len(input[0])):
            if input[row][col] not in ['X', ' ', '!']:
                #Non-identified tiles can be flood-filled to be replaced with blank
                touchesEdge = False
                q = [(row,col)]
                found = []
                while len(q) > 0:
                    pos = q.pop(0)
                    pr = pos[0]
                    pc = pos[1]
                    #Previously identified tiles are ignored
                    if input[pr][pc] in ['X', ' ', '!']:
                        continue

                    #Adding adjacent tiles to the que to search
                    if pr > 0:#up
                        q.append((pr-1,pc))
                    else:
                        touchesEdge = True
                    if pr < len(input)-1:#down
                        q.append((pr+1,pc))
                    else:
                        touchesEdge = True
                    if pc > 0:#left
                        q.append((pr,pc-1))
                    else:
                        touchesEdge = True
                    if pc < len(input[0])-1:
                        q.append((pr,pc+1))
                    else:
                        touchesEdge = True

                    #Marking this tile blank to identify it as found
                    found.append(pos)
                    input[pr][pc] = ' '

                #If the flood fill never reached the edge of the grid, all tiles are contained
                if not touchesEdge:
                    for x in found:
                        input[x[0]][x[1]] = '!'

    #Searching through the grid again to count the number of contained tiles,
    #but making sure to ignore all of the ones that were in the added rows/cols
    #newInput = []
    contained = 0
    for i in range(0, len(input)):
        if i % 2 == 0:
            #newLine = []
            for j in range(0, len(input[i])):
                if j % 2 == 0:
                    #newLine.append(input[i][j])
                    if input[i][j] == '!':
                        contained += 1
            #newInput.append(newLine)

    #for line in newInput:
    #    print(''.join(line))
    return contained


print("Year 2023, Day 10 solution part 1:", solution1())
print("Year 2023, Day 10 solution part 2:", solution2())