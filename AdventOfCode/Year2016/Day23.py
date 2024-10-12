aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []
    regs = {}
    
    print("==============================================\n\tNEED TO TRACE WHERE IT LOOPS\N===================================")

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            
            if line[1].isdigit() or line[1][0] == '-':
                line[1] = int(line[1])
            elif line[1] not in regs.keys():
                regs[line[1]] = 0
                
            if len(line) == 3:
                if line[2].isdigit() or line[2][0] == '-':
                    line[2] = int(line[2])
                elif line[2] not in regs.keys():
                    regs[line[2]] = 0
                    
            inpt.append(line)

    return inpt, regs
            

def solution1():
    inpt, reg = getInput()
    
    if testing:
        print("Registers:", reg)
        print("Input:")
        for i in inpt:
            print("\t", i)
            
    ptr = 0
    while ptr > -1 and ptr < len(inpt):
        line = inpt[ptr]
        testing and print("Ptr:", ptr, "    Instruction:", line)
        if line[0] == "cpy":
            if type(line[2]) is not int:
                if type(line[1]) is int:
                    reg[line[2]] = line[1]
                else:
                    reg[line[2]] = reg[line[1]]
            ptr += 1
        elif line[0] == "inc":
            if type(line[1]) is not int:
                reg[line[1]] += 1
            ptr += 1
        elif line[0] == "dec":
            if type(line[1]) is not int:
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
        elif line[0] == "tgl":
            toggleInd = ptr
            if type(line[1]) is int:
                toggleInd += line[1]
            else:
                toggleInd += reg[line[1]]
            
            if toggleInd < len(inpt):
                #Instructions with 1 argument
                if len(inpt[toggleInd]) == 2:
                    if inpt[toggleInd][0] == "inc":
                        inpt[toggleInd][0] = "dec"
                    else:
                        inpt[toggleInd][0] = "inc"
                #Instructions with 2 arguments
                else:
                    if inpt[toggleInd][0] == "jnz":
                        inpt[toggleInd][0] = "cpy"
                    else:
                        inpt[toggleInd][0] = "jnz"
                testing and print("\tToggled instruction", toggleInd, "to", inpt[toggleInd])
            ptr += 1
    return reg['a']


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())