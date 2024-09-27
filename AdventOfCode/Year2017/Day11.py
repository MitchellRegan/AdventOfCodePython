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
            inpt = line.replace('\n', '').split(',')

    return inpt
            

def solution1():
    inpt = getInput()
    
    #Using these weird cube coordinates from https://www.redblobgames.com/grids/hexagons/#distances
    q = 0
    s = 0
    r = 0
    for hexDir in inpt:
        if hexDir == "n":
            s += 1
            r -= 1
        elif hexDir == "s":
            s -= 1
            r += 1
        elif hexDir == "ne":
            q += 1
            r -= 1
        elif hexDir == "nw":
            q -= 1
            s += 1
        elif hexDir == "se":
            q += 1
            s -= 1
        elif hexDir == "sw":
            q -= 1
            r += 1
            
    return max([q,s,r])


def solution2():
    inpt = getInput()
    
    #Using these weird cube coordinates from https://www.redblobgames.com/grids/hexagons/#distances
    q = 0
    s = 0
    r = 0
    maxDist = 0
    for hexDir in inpt:
        if hexDir == "n":
            s += 1
            r -= 1
        elif hexDir == "s":
            s -= 1
            r += 1
        elif hexDir == "ne":
            q += 1
            r -= 1
        elif hexDir == "nw":
            q -= 1
            s += 1
        elif hexDir == "se":
            q += 1
            s -= 1
        elif hexDir == "sw":
            q -= 1
            r += 1
        
        if max([q,r,s]) > maxDist:
            maxDist = max([q,r,s])
    return maxDist


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
# 768 too high
# 1342 too high
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())