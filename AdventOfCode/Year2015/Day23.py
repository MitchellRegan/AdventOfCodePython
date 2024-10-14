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

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace(',', '').replace('+', '').split(' ')
            if line[1].isdigit() or line[1][0] == '-':
                line[1] = int(line[1])
            if len(line) == 3 and (line[2].isdigit() or line[2][0] == '-'):
                line[2] = int(line[2])
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    regs = {'a':0, 'b':0}
    
    i = 0
    while i > -1 and i < len(inpt):
        testing and print("i =", i, "    ", inpt[i])
        if inpt[i][0] == "hlf":
            regs[inpt[i][1]] = regs[inpt[i][1]] // 2
            i += 1
        elif inpt[i][0] == "tpl":
            regs[inpt[i][1]] = 3 * regs[inpt[i][1]]
            i += 1
        elif inpt[i][0] == "inc":
            regs[inpt[i][1]] += 1
            i += 1
        elif inpt[i][0] == "jmp":
            i += inpt[i][1]
        elif inpt[i][0] == "jie":
            if regs[inpt[i][1]] % 2 == 0:
                i += inpt[i][2]
            else:
                i += 1
        elif inpt[i][0] == "jio":
            if regs[inpt[i][1]] == 1:
                i += inpt[i][2]
            else:
                i += 1
        testing and print("\tNew i =", i, "    Registers:", regs)

    return regs['b']


def solution2():
    inpt = getInput()
    regs = {'a':1, 'b':0}
    
    i = 0
    while i > -1 and i < len(inpt):
        testing and print("i =", i, "    ", inpt[i])
        if inpt[i][0] == "hlf":
            regs[inpt[i][1]] = regs[inpt[i][1]] // 2
            i += 1
        elif inpt[i][0] == "tpl":
            regs[inpt[i][1]] = 3 * regs[inpt[i][1]]
            i += 1
        elif inpt[i][0] == "inc":
            regs[inpt[i][1]] += 1
            i += 1
        elif inpt[i][0] == "jmp":
            i += inpt[i][1]
        elif inpt[i][0] == "jie":
            if regs[inpt[i][1]] % 2 == 0:
                i += inpt[i][2]
            else:
                i += 1
        elif inpt[i][0] == "jio":
            if regs[inpt[i][1]] == 1:
                i += inpt[i][2]
            else:
                i += 1
        testing and print("\tNew i =", i, "    Registers:", regs)

    return regs['b']


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())