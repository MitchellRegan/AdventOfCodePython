aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        lineNum = 0
        for line in f:
            if lineNum < 2:
                lineNum += 1
            else:
                line = line.replace('\n', '').split(' ')
                while '' in line:
                    line.remove('')
                
                x,y = [int(z) for z in line[0][16:].split('-y')]
                s = int(line[1][:-1])
                u = int(line[2][:-1])
                a = int(line[3][:-1])
                pu = int(line[4][:-1])
                inpt.append((x,y,s,u,a,pu))

    return inpt
            

def solution1():
    inpt = getInput()
        
    ans = 0
    for i in range(len(inpt)-1):
        for j in range(i+1, len(inpt)):
            #xPos, yPos, total available size, size used, available size remaining, and percentage of size used
            x1,y1,s1,u1,a1,pu1 = inpt[i]
            x2,y2,s2,u2,a2,pu2 = inpt[j]
            
            #Node 1's "used" size must not be zero, node 1 and node 2 can't be the same, and node 1's "used" must be less than node 2's "avail"
            if x1 != x2 or y1 != y2:
                if u1 != 0 and u1 <= a2:
                    ans += 1
                elif u2 != 0 and u2 <= a1:
                    ans += 1

    return ans


def solution2():
    inpt = getInput()
    maxX = 0
    maxY = 0
    for i in inpt:
        maxX = max(maxX, i[0])
        maxY = max(maxY, i[1])
        
    #Building a 2D grid
    grid = []
    for r in range(maxY+1):
        newRow = [(0,0)] * (maxX+1)
        grid.append(newRow)
    for i in inpt:
        grid[i[1]][i[0]] = (i[3], i[2])
        
    q = [(len(grid[0])-1, 0)]
    seen = {}
    for row in grid:
        print(row)
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#462 too low
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())