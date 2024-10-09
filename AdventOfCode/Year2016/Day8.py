aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if line[0] == "rect":
                w = int(line[1].split('x')[0])
                h = int(line[1].split('x')[1])
                inpt.append(("rect", w, h))
            else:
                xy = line[2][0]
                val = int(line[2][2:])
                amt = int(line[-1])
                inpt.append((xy, val, amt))

    return inpt
            

def solution1():
    inpt = getInput()
    gridSize = (50,6)
    if testing:
        gridSize = (7,3)
    grid = []
    for y in range(gridSize[1]):
        newRow = ['.'] * gridSize[0]
        grid.append(newRow)

    for i in inpt:
        if i[0] == "rect":
            for r in range(i[2]):
                for c in range(i[1]):
                    grid[r][c] = '#'
        elif i[0] == "x":
            newCol = ""
            for row in range(len(grid)):
                newCol = newCol + grid[row][i[1]]
            newCol = newCol[-i[2]:] + newCol[:-i[2]]
            for row in range(len(grid)):
                grid[row][i[1]] = newCol[row]
        elif i[0] == "y":
            newRow = grid[i[1]][-i[2]:]
            newRow.extend(grid[i[1]][:-i[2]])
            grid[i[1]] = newRow

        if testing:
            print("\n", i, "_______________________________")
            for row in grid:
                print(''.join(row))

    ans = 0
    for row in grid:
        for col in row:
            if col == '#':
                ans += 1
    return ans


def solution2():
    inpt = getInput()
    gridSize = (50,6)
    if testing:
        gridSize = (7,3)
    grid = []
    for y in range(gridSize[1]):
        newRow = ['.'] * gridSize[0]
        grid.append(newRow)

    for i in inpt:
        if i[0] == "rect":
            for r in range(i[2]):
                for c in range(i[1]):
                    grid[r][c] = '#'
        elif i[0] == "x":
            newCol = ""
            for row in range(len(grid)):
                newCol = newCol + grid[row][i[1]]
            newCol = newCol[-i[2]:] + newCol[:-i[2]]
            for row in range(len(grid)):
                grid[row][i[1]] = newCol[row]
        elif i[0] == "y":
            newRow = grid[i[1]][-i[2]:]
            newRow.extend(grid[i[1]][:-i[2]])
            grid[i[1]] = newRow

    for row in grid:
        print(''.join(row).replace('.', ' '))
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())