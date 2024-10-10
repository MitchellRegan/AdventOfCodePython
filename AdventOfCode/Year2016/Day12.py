aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []
    reg = {}

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if line[1].isdigit() or line[1][0] == '-':
                line[1] = int(line[1])
                
            if len(line) == 3 and (line[2].isdigit() or line[2][0] == '-'):
                line[2] = int(line[2])
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    reg = {'a':0, 'b':0, 'c':0, 'd':0}
    
    ptr = 0
    while ptr > -1 and ptr < len(inpt):
        line = inpt[ptr]
        testing and print("Ptr:", ptr, "    Instruction:", line)
        if line[0] == "cpy":
            if type(line[1]) is int:
                reg[line[2]] = line[1]
            else:
                reg[line[2]] = reg[line[1]]
            ptr += 1
        elif line[0] == "inc":
            reg[line[1]] += 1
            ptr += 1
        elif line[0] == "dec":
            reg[line[1]] -= 1
            ptr += 1
        elif line[0] == "jnz":
            if (type(line[1]) is int and line[1] != 0) or reg[line[1]] != 0:
                if type(line[2]) is int:
                    ptr += line[2]
                else:
                    ptr += reg[line[2]]
            else:
                ptr += 1
                
        testing and print("Ptr:", ptr, "    Registers:", reg, '\n')
                
    return reg['a']


def solution2():
    inpt = getInput()
    reg = {'a':0, 'b':0, 'c':1, 'd':0}
    
    ptr = 0
    while ptr > -1 and ptr < len(inpt):
        line = inpt[ptr]
        
        if line[0] == "cpy":
            if type(line[1]) is int:
                reg[line[2]] = line[1]
            else:
                reg[line[2]] = reg[line[1]]
            ptr += 1
        elif line[0] == "inc":
            reg[line[1]] += 1
            ptr += 1
        elif line[0] == "dec":
            reg[line[1]] -= 1
            ptr += 1
        elif line[0] == "jnz":
            if (type(line[1]) is int and line[1] != 0) or reg[line[1]] != 0:
                if type(line[2]) is int:
                    ptr += line[2]
                else:
                    ptr += reg[line[2]]
            else:
                ptr += 1
                
    return reg['a']


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())