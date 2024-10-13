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
            
            if len(line) == 3:
                val = line[0]
                if val.isdigit():
                    val = int(val)
                inpt.append(("S", val, line[2]))
                    
            elif len(line) == 4:
                val = line[1]
                if val.isdigit():
                    val = int(val)
                inpt.append(("N", val, line[3]))
                
            else:
                val1 = line[0]
                if val1.isdigit():
                    val1 = int(val1)
                val2 = line[2]
                if val2.isdigit():
                    val2 = int(val2)
                inpt.append((line[1][0], val1, val2, line[4]))
                
    return inpt
            

def solution1():
    inpt = getInput()
    wires = {}
    
    for i in inpt:
        testing and print(i)
        if i[0] == "S":
            wires[i[2]] = i[1]
        else:
            wires[i[-1]] = i[:-1]
            
    def getWireVal(w_:str)->int:
        i = wires[w_]
        if type(i) is int:
            return i
        elif type(i) is str:
            return getWireVal(i)
        
        if i[0] == "N": #not
            val1 = i[1]
            if type(i[1]) is not int:
                val1 = getWireVal(i[1])
            wires[w_] = (1 << 16) - 1 - val1
                
        elif i[0] == "A": #and
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 & val2
            
        elif i[0] == "O": #or
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 | val2
            
        elif i[0] == "R": #right-shift
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 >> val2
            
        elif i[0] == "L": #left-shift
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 << val2
            
        testing and print("Wire", w_, "=", wires[w_])
        return wires[w_]
    
        
    if testing:
        print("\nFinal Wires:")
        for k in wires.keys():
            print("\t", k, ":", wires[k])

    return getWireVal('a')


def solution2():
    inpt = getInput()
    wires = {}
    
    for i in inpt:
        if i[0] == "S":
            wires[i[2]] = i[1]
        else:
            wires[i[-1]] = i[:-1]
            
    def getWireVal(w_:str)->int:
        i = wires[w_]
        if type(i) is int:
            return i
        elif type(i) is str:
            return getWireVal(i)
        
        if i[0] == "N": #not
            val1 = i[1]
            if type(i[1]) is not int:
                val1 = getWireVal(i[1])
            wires[w_] = (1 << 16) - 1 - val1
                
        elif i[0] == "A": #and
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 & val2
            
        elif i[0] == "O": #or
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 | val2
            
        elif i[0] == "R": #right-shift
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 >> val2
            
        elif i[0] == "L": #left-shift
            val1 = i[1]
            if type(val1) is not int:
                val1 = getWireVal(val1)
            val2 = i[2]
            if type(val2) is not int:
                val2 = getWireVal(val2)
            wires[w_] = val1 << val2
            
        testing and print("Wire", w_, "=", wires[w_])
        return wires[w_]
    
    firstAVal = getWireVal('a')
    for i in inpt:
        if i[0] == "S":
            wires[i[2]] = i[1]
        else:
            wires[i[-1]] = i[:-1]
    wires['b'] = firstAVal

    return getWireVal('a')


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())