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
            if line[0] == "toggle":
                i = 't'
                s = [int(x) for x in line[1].split(',')]
                e = [int(x) for x in line[-1].split(',')]
                inpt.append((i,s,e))
            elif line[1] == "on":
                i = 'o'
                s = [int(x) for x in line[2].split(',')]
                e = [int(x) for x in line[-1].split(',')]
                inpt.append((i,s,e))
            else:
                i = 'f'
                s = [int(x) for x in line[2].split(',')]
                e = [int(x) for x in line[-1].split(',')]
                inpt.append((i,s,e))

    return inpt
            

def solution1():
    inpt = getInput()
    grid = []
    for r in range(1000):
        newRow = [False] * 1000
        grid.append(newRow)

    for line in inpt:
        testing and print(line)
        i,s,e = line
        for r in range(s[0], e[0]+1):
            for c in range(s[1], e[1]+1):
                if i == 'o':
                    grid[r][c] = True
                elif i == 'f':
                    grid[r][c] = False
                else:
                    grid[r][c] = not grid[r][c]

    ans = 0
    for r in range(1000):
        for c in range(1000):
            if grid[r][c]:
                ans += 1
    return ans


def solution2():
    inpt = getInput()
    grid = []
    for r in range(1000):
        newRow = [0] * 1000
        grid.append(newRow)

    for line in inpt:
        testing and print(line)
        i,s,e = line
        for r in range(s[0], e[0]+1):
            for c in range(s[1], e[1]+1):
                if i == 'o':
                    grid[r][c] += 1
                elif i == 'f' and grid[r][c] > 0:
                    grid[r][c] -= 1
                elif i == 't':
                    grid[r][c] += 2

    ans = 0
    for r in range(1000):
        for c in range(1000):
            ans += grid[r][c]
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())