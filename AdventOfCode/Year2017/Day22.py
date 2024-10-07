aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {} #Key = (row,col) pos of tile, Value = True if infected, False if clean
    startPos = [0,0]
    
    with open(inFile, 'r') as f:
        r = 0
        for line in f:
            line = line.replace('\n', '')
            if r == 0:
                startPos[1] = len(line)//2
            for c in range(0, len(line)):
                if line[c] == '#':
                    inpt[(r,c)] = True
                else:
                    inpt[(r,c)] = False
            r += 1

    startPos[0] = (r-1)//2
    return inpt, startPos
            

def solution1():
    inpt, startPos = getInput()
    
    #Setting the virus' starting row, column, and facing direction
    r,c = startPos
    d = 0 #Direction the virus is facing. 0=Up, 1=Right, 2=Down, 3=Left
    
    ans = 0
    for t in range(10000):
        #If a new location is found, it's default state is clean (False)
        if (r,c) not in inpt.keys():
            inpt[(r,c)] = False
            
        #If the current pos is infected, rotates clockwise
        if inpt[(r,c)]:
            d += 1
            if d > 3:
                d = 0
        #If the current pos is clean, rotates counter-clockwise
        else:
            d -= 1
            if d < 0:
                d = 3
                
        #Infected pos become clean, and clean become infected
        inpt[(r,c)] = not inpt[(r,c)]
        if inpt[(r,c)]:
            ans += 1
        
        #Moving 1 space forward in the direction the virus is facing
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        else:
            c -= 1

    return ans


def solution2():
    inpt, startPos = getInput()
    
    #Updating the states of nodes from T/F to int values: 0=Clean, 1=Weak, 2=Infected, 3=Flagged
    for k in inpt.keys():
        if inpt[k]:
            inpt[k] = "i"
        else:
            inpt[k] = "c"
    
    #Setting the virus' starting row, column, and facing direction
    r,c = startPos
    d = 0 #Direction the virus is facing. 0=Up, 1=Right, 2=Down, 3=Left
    
    ans = 0
    for t in range(10000000):
        #If a new location is found, it's default state is clean (0)
        if (r,c) not in inpt.keys():
            inpt[(r,c)] = 'c'
            
        testing and print("t =", t, "    Pos:", (r,c), "    Direction:", d, "    State:", inpt[(r,c)])
            
        #If the current pos is clean, rotates counter-clockwise and pos becomes weak
        if inpt[(r,c)] == 'c':
            d -= 1
            if d < 0:
                d = 3
            inpt[(r,c)] = 'w'
        #If the current pos is weak, direction isn't changed and pos becomes infected
        elif inpt[(r,c)] == 'w':
            inpt[(r,c)] = 'i'
            ans += 1
        #If the current pos is infected, rotates clockwise and pos becomes flagged
        elif inpt[(r,c)] == 'i':
            d += 1
            if d > 3:
                d = 0
            inpt[(r,c)] = 'f'
        #If the current pos is flagged, direction is reversed and pos becomes clean
        elif inpt[(r,c)] == 'f':
            d += 2
            if d > 3:
                d -= 4
            inpt[(r,c)] = 'c'
            
        testing and print("\tNew Direction:", d, "    New State:", inpt[(r,c)])
        
        #Moving 1 space forward in the direction the virus is facing
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        else:
            c -= 1
            
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())