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
            inpt = line.replace('\n', '').split(', ')

    return inpt
            

def solution1():
    inpt = getInput()
    
    r = 0
    c = 0
    d = 0 #Direction facing. 0=Up, 1=Right, 2=Down, 3=Left
    for i in inpt:
        steps = int(i[1:])
        if i[0] == 'R':
            d += 1
            if d == 4:
                d = 0
        else:
            d -= 1
            if d == -1:
                d = 3
                
        if d == 0:
            r -= steps
        elif d == 1:
            c += steps
        elif d == 2:
            r += steps
        else:
            c -= steps

    testing and print("Final pos:", (r,c))
    return abs(r) + abs(c)


def solution2():
    inpt = getInput()
    seen = {}
    
    r = 0
    c = 0
    d = 0 #Direction facing. 0=Up, 1=Right, 2=Down, 3=Left
    testing and print("Start:   (0,0)")
    for i in inpt:
        steps = int(i[1:])
        if i[0] == 'R':
            d += 1
            if d == 4:
                d = 0
        else:
            d -= 1
            if d == -1:
                d = 3
                
        nr = 0
        nc = 0
        if d == 0:
            nr = -1
        elif d == 1:
            nc = 1
        elif d == 2:
            nr = 1
        else:
            nc = -1
            
        for x in range(steps):
            r += nr
            c += nc
            if (r,c) in seen.keys():
                return abs(r) + abs(c)
            else:
                seen[(r,c)] = True

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#215 too high