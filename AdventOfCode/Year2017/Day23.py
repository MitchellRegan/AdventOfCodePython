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
            line = line.replace('\n', '').split(' ')
            
            if line[1].isdigit():
                line[1] = int(line[1])
            elif line[1] not in regs.keys():
                regs[line[1]] = 0
                
            if len(line) > 2:
                if line[2].isdigit() or line[2][0] == '-':
                    line[2] = int(line[2])
                elif line[2] not in regs.keys():
                    regs[line[2]] = 0
            inpt.append(line)
    return inpt, regs
            

def solution1():
    inpt, regs = getInput()
    
    if True:
        print("Registers:")
        for r in regs.keys():
            print("\t", r, ":", regs[r])
        print("Input Instructions:")
        for i in inpt:
            print("\t", i)

    iptr = 0
    ans = 0
    while iptr > -1 and iptr < len(inpt):
        i = inpt[iptr]
        val2 = 0
        if len(i) > 2:
            val2 = i[2]
            if type(val2) is not int:
                val2 = regs[val2]
                
        if i[0] == "set":
            regs[i[1]] = val2
            iptr += 1
        elif i[0] == "sub":
            regs[i[1]] -= val2
            iptr += 1
        elif i[0] == "mul":
            regs[i[1]] *= val2
            ans += 1
            iptr += 1
        elif i[0] == "jnz":
            val1 = i[1]
            if type(val1) is not int:
                val1 = regs[val1]
            if val1 != 0:
                iptr += val2
            else:
                iptr += 1

    return ans


def solution2():
    inpt, regs = getInput()
    regs['a'] = 1

    iptr = 0
    t = 0
    while iptr > -1 and iptr < len(inpt):
        i = inpt[iptr]
        print("iptr =", iptr, ":", i)
        if type(i[1]) is not int:
            print("\t", i[1], ":", regs[i[1]])
        if type(i[2]) is not int:
            print("\t", i[2], ":", regs[i[2]])
        val2 = 0
        if len(i) > 2:
            val2 = i[2]
            if type(val2) is not int:
                val2 = regs[val2]
                
        if i[0] == "set":
            regs[i[1]] = val2
            iptr += 1
        elif i[0] == "sub":
            regs[i[1]] -= val2
            iptr += 1
        elif i[0] == "mul":
            regs[i[1]] *= val2
            iptr += 1
        elif i[0] == "jnz":
            val1 = i[1]
            if type(val1) is not int:
                val1 = regs[val1]
            if val1 != 0:
                iptr += val2
            else:
                iptr += 1
                
        if i[1] == 'h':
            print("t =", t, "    h:", regs['h'])
        t += 1

    return regs['h']


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())