aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(" => ")
            inpt[line[0]] = line[1]

    return inpt
            

def solution1():
    inpt = getInput()
    grid = [".#.", "..#", "###"]
        
    def getPattern(tile_:list):
        for i in range(8):
            if i == 4:
                tile_ = [x[::-1] for x in tile_]
            key = '/'.join(tile_)
            #testing and print("Checking for pattern", key)
            #for x in tile_:
            #    print(x)
            if key in inpt.keys():
                testing and print("\tFound", key, "==>", inpt[key])
                return inpt[key]
            tile_ = [''.join(x) for x in list(zip(*tile_[::-1]))]

        
    for t in range(5):
        newGrid = []
        if len(grid[0]) % 2 == 0:
            for r in range(0, len(grid), 2):
                for c in range(0, len(grid[0]), 2):
                    ptrn = getPattern([grid[r][c:c+2], grid[r+1][c:c+2]])
                    ptrn = ptrn.split('/')
                    if c == 0:
                        for x in ptrn:
                            newGrid.append(x)
                    else:
                        i = len(newGrid) - len(ptrn)
                        for x in range(len(ptrn)):
                            newGrid[i+x] = newGrid[i+x] + ptrn[x]
        elif len(grid[0]) % 3 == 0:
            for r in range(0, len(grid), 3):
                for c in range(0, len(grid[0]), 3):
                    ptrn = getPattern([grid[r][c:c+3], grid[r+1][c:c+3], grid[r+2][c:c+3]])
                    ptrn = ptrn.split('/')
                    if c == 0:
                        for x in ptrn:
                            newGrid.append(x)
                    else:
                        i = len(newGrid) - len(ptrn)
                        for x in range(len(ptrn)):
                            newGrid[i+x] = newGrid[i+x] + ptrn[x]
        grid = newGrid
        if testing:
            print("New grid after t =", t)
            for x in grid:
                print(x)
                
    ans = 0
    for row in grid:
        ans += row.count('#')
    return ans


def solution2():
    inpt = getInput()
    grid = [".#.", "..#", "###"]
        
    def getPattern(tile_:list):
        for i in range(8):
            if i == 4:
                tile_ = [x[::-1] for x in tile_]
            key = '/'.join(tile_)
            if key in inpt.keys():
                return inpt[key]
            tile_ = [''.join(x) for x in list(zip(*tile_[::-1]))]

        
    for t in range(18):
        newGrid = []
        if len(grid[0]) % 2 == 0:
            for r in range(0, len(grid), 2):
                for c in range(0, len(grid[0]), 2):
                    ptrn = getPattern([grid[r][c:c+2], grid[r+1][c:c+2]])
                    ptrn = ptrn.split('/')
                    if c == 0:
                        for x in ptrn:
                            newGrid.append(x)
                    else:
                        i = len(newGrid) - len(ptrn)
                        for x in range(len(ptrn)):
                            newGrid[i+x] = newGrid[i+x] + ptrn[x]
        elif len(grid[0]) % 3 == 0:
            for r in range(0, len(grid), 3):
                for c in range(0, len(grid[0]), 3):
                    ptrn = getPattern([grid[r][c:c+3], grid[r+1][c:c+3], grid[r+2][c:c+3]])
                    ptrn = ptrn.split('/')
                    if c == 0:
                        for x in ptrn:
                            newGrid.append(x)
                    else:
                        i = len(newGrid) - len(ptrn)
                        for x in range(len(ptrn)):
                            newGrid[i+x] = newGrid[i+x] + ptrn[x]
        grid = newGrid
                
    ans = 0
    for row in grid:
        ans += row.count('#')
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())