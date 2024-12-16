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

    #CHANGES TO THE INPUT INSTRUCTIONS (these are based on monitoring patterns in the output and simplifying stupid loops)
    #   Loops between iptr 11 - 19 just result in e increasing by g's amount, and g becoming 0
    #inpt[19] = ["sub", "e", "g"]
    #inpt.insert(20, ["set", "g", 0])
    #   Loops between iptr 11 - 24 (was 23 until insert) just result in d increasing by g's amount, and g becoming 0
    #inpt[24] = ["sub", "d", "g"]
    #inpt.insert(25, ["set", "g", 0])
    #   Loops between iptr 8 - 33 (was 31 until inserts)
    #inpt[33][2] = -25
    #inpt.pop(-1)
    #inpt.pop(-1)
    #inpt[-1][2] = 6
    #inpt.append(["sub", "b", -1000])
    #inpt.append(["sub", "d", -1000])
    #inpt.append(["sub", "e", -1000])
    #inpt.append(["set", "g", 0])
    #inpt.append(["jnz", 1, -28])


    loopFinder = {}#Key = iptr at a jnz instruction going backwards, Value = dict of register values
    loopDiff = {}#Key = iptr at a jnz instruction going backwards, Value = value of the register that was checked for jnz

    iptr = 0
    t = 0
    while iptr > -1 and iptr < len(inpt):
        i = inpt[iptr]

        if True:
            print("iptr =", iptr, ":", i)
            #if type(i[1]) is not int:
            #    print("\t", i[1], ":", regs[i[1]])
            #if type(i[2]) is not int:
            #    print("\t", i[2], ":", regs[i[2]])

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
            if i[2] < 0:
                print("==========safety break at line 130")
                return
            val1 = i[1]
            if type(val1) is not int:
                val1 = regs[val1]
            if val1 != 0:
                skipLoop = False
                #Tracking differences in register values when instructions are jumping backwards
                if val2 < 0:
                    regVals = []
                    for k in regs.keys():
                        regVals.append((k, regs[k]))
                    regVals.sort()
                    print("======== iptr =", iptr, "\t", i)
                    #If we haven't jumped backwards from this instruction yet, we track the current register values
                    if iptr not in loopFinder.keys():
                        loopFinder[iptr] = regVals
                        loopDiff[iptr] = val1
                    #If we've seen this instruction already, we're looping so we can initiate a loop skip
                    else:
                        for rv in range(len(regVals)):
                            diff = regVals[rv][1] - loopFinder[iptr][rv][1]
                            #regs[regVals[rv][0]] += diff * abs(regs[i[1]])
                            #print("\t\t", regVals[rv][0], "diff:", diff, "   Value:", loopFinder[iptr][rv][1], "->", regs[regVals[rv][0]])
                        loopFinder[iptr] = regVals

                if not skipLoop:
                    iptr += val2
            else:
                iptr += 1

        print("\t", regs)
                
        if i[1] == 'h':
            print("t =", t, "    h:", regs['h'])
        t += 1

    return regs['h']


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#Isn't 1
#1000 too high