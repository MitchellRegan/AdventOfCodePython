aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}
    grid = []

    with open(inFile, 'r') as f:
        r = 0
        for line in f:
            line = line.replace('\n', '')
            grid.append([x for x in line])
            for c in range(len(line)):
                if line[c] != '.':
                    if line[c] not in inpt.keys():
                        inpt[line[c]] = [(r,c)]
                    else:
                        inpt[line[c]].append((r,c))
            r += 1
    return inpt, grid
            

def solution1():
    inpt, grid = getInput()
    
    antinodes = []
    for k in inpt.keys():
        if len(inpt[k]) == 1:
            continue

        for i in range(len(inpt[k])-1):
            r1,c1 = inpt[k][i]
            for j in range(i+1, len(inpt[k])):
                r2,c2 = inpt[k][j]

                #Getting the antinode on the opposite side of node 2 from node 1
                r3 = r2 + (r2-r1)
                c3 = c2 + (c2-c1)
                if r3 < len(grid) and r3 > -1 and c3 < len(grid[0]) and c3 > -1:
                    if (r3,c3) not in antinodes:
                        antinodes.append((r3,c3))

                #Getting the antinode on the opposite side of node 1 from node 2
                r3 = r1 - (r2-r1)
                c3 = c1 - (c2-c1)
                if r3 < len(grid) and r3 > -1 and c3 < len(grid[0]) and c3 > -1:
                    if (r3,c3) not in antinodes:
                        antinodes.append((r3,c3))

    return len(antinodes)


def solution2():
    inpt, grid = getInput()
    
    antinodes = []
    for k in inpt.keys():
        if len(inpt[k]) == 1:
            continue

        for i in range(len(inpt[k])-1):
            r1,c1 = inpt[k][i]
            #Including node 1's position as an antinode
            if (r1,c1) not in antinodes:
                antinodes.append((r1,c1))
            for j in range(i+1, len(inpt[k])):
                r2,c2 = inpt[k][j]
                #Including node 2's position as an antinode
                if (r2,c2) not in antinodes:
                    antinodes.append((r2,c2))

                #Getting all antinodes in a ray starting at node 1 and going past node 2
                r3 = r2 + (r2-r1)
                c3 = c2 + (c2-c1)
                while r3 < len(grid) and r3 > -1 and c3 < len(grid[0]) and c3 > -1:
                    if (r3,c3) not in antinodes:
                        antinodes.append((r3,c3))
                    r3 += (r2-r1)
                    c3 += (c2-c1)

                #Getting all antinodes in a ray starting at node 2 and going past node 1
                r3 = r1 - (r2-r1)
                c3 = c1 - (c2-c1)
                while r3 < len(grid) and r3 > -1 and c3 < len(grid[0]) and c3 > -1:
                    if (r3,c3) not in antinodes:
                        antinodes.append((r3,c3))
                    r3 -= (r2-r1)
                    c3 -= (c2-c1)

    return len(antinodes)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())