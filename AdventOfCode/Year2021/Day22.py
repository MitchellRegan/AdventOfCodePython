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
        for line in f:
            line = line.replace('\n', '').replace(',', ' ').split(' ')
            state = (line[0] == "on")
            x = [int(x) for x in line[1][2:].split('..')]
            y = [int(y) for y in line[2][2:].split('..')]
            z = [int(z) for z in line[3][2:].split('..')]
            inpt.append((state, x, y, z))

    return inpt
 

def rangeOverlap(r1_:list, r2_:list)->list:
    '''Finds the range of values where the two given ranges overlap. If no overlap, returns None'''
    if (r1_[1] >= r2_[0] and r1_[1] <= r2_[1]) or (r2_[1] >= r1_[0] and r2_[1] <= r1_[1]):
        return [max(r1_[0], r2_[0]), min(r1_[1], r2_[1])]
    return None


def solution1():
    inpt = getInput()
    grid = {}#Key = (x,y,z) pos, Value = bool for if it's on or off
    
    for line in inpt:
        testing and print(line)
        state, xRange, yRange, zRange = line
        #Making sure the ranges are between [-50, 50] inclusive
        xRange = [max(xRange[0], -50), min(xRange[1], 50)]
        yRange = [max(yRange[0], -50), min(yRange[1], 50)]
        zRange = [max(zRange[0], -50), min(zRange[1], 50)]

        for x in range(xRange[0], xRange[1]+1):
            for y in range(yRange[0], yRange[1]+1):
                for z in range(zRange[0], zRange[1]+1):
                    grid[(x,y,z)] = state

    ans = 0
    for k in grid.keys():
        if grid[k]:
            ans += 1
    return ans


def solution2():
    inpt = getInput()
    ans = 0
    
    for i in range(len(inpt)):
        print("Working on line", i)
        state, xr1, yr1, zr1 = inpt[i]
        volume = (xr1[1]-xr1[0]) * (yr1[1]-yr1[0]) * (zr1[1]-zr1[0])

        #Looking for overlapping regions between our current box and all subsequent boxes
        for j in range(i+1, len(inpt)):
            s, xr2, yr2, zr2 = inpt[j]
            #Getting the overlapping region between the boxes
            xo = rangeOverlap(xr1, xr2)
            yo = rangeOverlap(yr1, yr2)
            zo = rangeOverlap(zr1, zr2)
            #An overlap has to happen on all 3 axes
            if xo is not None and yo is not None and zo is not None:
                vo = (xo[1]-xo[0]) * (yo[1]-yo[0]) * (zo[1]-zo[0])
                print("\tCurren Volume:", volume, "    Overlap Volume:", vo, "    Result:", volume - vo)
                volume -= vo
        ans += volume
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())