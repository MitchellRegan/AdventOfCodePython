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
        #Getting the cubes at z=0
        r = 0
        for line in f:
            line = line.replace('\n', '')
            for c in range(0, len(line)):
                inpt[(r,c,0)] = line[c]
            r += 1
            
    return inpt
            

def solution1():
    inpt = getInput()
    
    for cycle in range(0, 6):
        #Adding empty spaces to any cubes missing adjacent cubes
        newEmpties = []
        for k in inpt.keys():
            x,y,z = k
            
            for newX in range(x-1, x+2):
                for newY in range(y-1, y+2):
                    for newZ in range(z-1, z+2):
                        if (newX, newY, newZ) not in inpt.keys():
                            newEmpties.append((newX, newY, newZ))
        for ne in newEmpties:
            inpt[ne] = '.'
            
        #Checking the adjacent spaces of each cube to determine their next state
        newInpt = {}
        for k in inpt.keys():
            x,y,z = k
            active = 0
            for newX in range(x-1, x+2):
                for newY in range(y-1, y+2):
                    for newZ in range(z-1, z+2):
                        if x == newX and y == newY and z == newZ:
                            continue
                        elif (newX, newY, newZ) in inpt.keys() and inpt[(newX, newY, newZ)] == '#':
                            active += 1
                    
            #Active cubes stay active if 2 or 3 adjacent are active, and become inactive otherwise
            if inpt[k] == '#':
                if active == 2 or active == 3:
                    newInpt[k] = '#'
                else:
                    newInpt[k] = '.'
            #Inactive cubes become active if exactly 3 adjacent are active, and remain inactive otherwise
            else:
                if active == 3:
                    newInpt[k] = '#'
                else:
                    newInpt[k] = '.'
                    
        inpt = newInpt
        
    #Answer is the number of active cubes after 6 cycles
    answ = 0
    for k in inpt.keys():
        if inpt[k] == '#':
            answ += 1
    return answ


def solution2():
    inpt = getInput()
    #Modifying the input to include the 4th dimension 'w', starting at w=0
    newInpt = {}
    for k in inpt.keys():
        x,y,z = k
        newInpt[(x,y,z,0)] = inpt[k]
    inpt = newInpt
    
    for cycle in range(0, 6):
        #Adding empty spaces to any cubes missing adjacent cubes
        newEmpties = []
        for k in inpt.keys():
            x,y,z,w = k
            
            for newX in range(x-1, x+2):
                for newY in range(y-1, y+2):
                    for newZ in range(z-1, z+2):
                        for newW in range(w-1, w+2):
                            if (newX, newY, newZ, newW) not in inpt.keys():
                                newEmpties.append((newX, newY, newZ, newW))
        for ne in newEmpties:
            inpt[ne] = '.'
            
        #Checking the adjacent spaces of each cube to determine their next state
        newInpt = {}
        for k in inpt.keys():
            x,y,z,w = k
            active = 0
            for newX in range(x-1, x+2):
                for newY in range(y-1, y+2):
                    for newZ in range(z-1, z+2):
                        for newW in range(w-1, w+2):
                            if x == newX and y == newY and z == newZ and w == newW:
                                continue
                            elif (newX, newY, newZ, newW) in inpt.keys() and inpt[(newX, newY, newZ, newW)] == '#':
                                active += 1
                    
            #Active cubes stay active if 2 or 3 adjacent are active, and become inactive otherwise
            if inpt[k] == '#':
                if active == 2 or active == 3:
                    newInpt[k] = '#'
                else:
                    newInpt[k] = '.'
            #Inactive cubes become active if exactly 3 adjacent are active, and remain inactive otherwise
            else:
                if active == 3:
                    newInpt[k] = '#'
                else:
                    newInpt[k] = '.'
                    
        inpt = newInpt
        
    #Answer is the number of active cubes after 6 cycles
    answ = 0
    for k in inpt.keys():
        if inpt[k] == '#':
            answ += 1
    return answ


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())