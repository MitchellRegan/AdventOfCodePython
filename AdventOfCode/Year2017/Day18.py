aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
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
            
            if line[1] not in regs.keys():
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
    
    if testing:
        print("Registers:", regs)
        print("Instructions:")
        for i in inpt:
            print("\t", i)
        
    iptr = 0
    soundFreq = 0
    while iptr > -1 and iptr < len(inpt):
        i = inpt[iptr]
        testing and print(i)
        val2 = 0
        if len(i) > 2:
            val2 = i[2]
            if type(val2) is not int:
                val2 = regs[val2]
        
        if i[0] == "snd": #play sound
            soundFreq = regs[i[1]]
            iptr += 1
        elif i[0] == "set": #sets value of register
            regs[i[1]] = val2
            iptr += 1
        elif i[0] == "add": #adds value to register
            regs[i[1]] += val2
            iptr += 1
        elif i[0] == "mul": #multiplies value of register
            regs[i[1]] *= val2
            iptr += 1
        elif i[0] == "mod": #modulo value of reg
            regs[i[1]] = regs[i[1]] % val2
            iptr += 1
        elif i[0] == "rcv": #recovers last sound played
            if regs[i[1]] != 0 and soundFreq != 0:
                return soundFreq
            else:
                iptr += 1
        elif i[0] == "jgz": #jumps if greater than zero
            if regs[i[1]] > 0:
                iptr += val2
            else:
                iptr += 1
                
        testing and print("    Reg a:", regs['a'], "    index ptr:", iptr, "    Sound Freq:", soundFreq)
    
    return soundFreq


def solution2():
    inpt, regs0 = getInput()
    regs1 = {}
    for k in regs0.keys():
        regs1[k] = 0
        
    #Setting initial register values denoted by the instructions
    regs0['p'] = 0
    regs1['p'] = 1

    #Vars for the instruction index pointers for both programs
    iptr_0 = 0
    iptr_1 = 0
    #Vars for the queues that store values sent to each-other
    q0 = []
    q1 = []
    ans = 0
    while True:
        i0 = inpt[iptr_0]
        i1 = inpt[iptr_1]
        testing and print("\nI_0:", i0, "    I_1:", i1)
        
        #If both programs are trying to recieve values and none remain, terminate
        if i0[0] == "rcv" and i1[0] == "rcv" and len(q0) == 0 and len(q1) == 0:
            return ans
        
        #Handling program 0
        val2 = 0
        if len(i0) > 2:
            val2 = i0[2]
            if type(val2) is not int:
                val2 = regs0[val2]
        
        if i0[0] == "snd": #send value to program 1
            q1.append(regs0[i0[1]])
            iptr_0 += 1
        elif i0[0] == "set": #sets value of register
            regs0[i0[1]] = val2
            iptr_0 += 1
        elif i0[0] == "add": #adds value to register
            regs0[i0[1]] += val2
            iptr_0 += 1
        elif i0[0] == "mul": #multiplies value of register
            regs0[i0[1]] *= val2
            iptr_0 += 1
        elif i0[0] == "mod": #modulo value of reg
            regs0[i0[1]] = regs0[i0[1]] % val2
            iptr_0 += 1
        elif i0[0] == "rcv": #recieves the last value sent from program 1
            if len(q0) > 0:
                regs0[i0[1]] = q0.pop(0)
                iptr_0 += 1
        elif i0[0] == "jgz": #jumps if greater than zero
            if regs0[i0[1]] > 0:
                iptr_0 += val2
            else:
                iptr_0 += 1
        
        #Handling program 1
        val2 = 0
        if len(i1) > 2:
            val2 = i1[2]
            if type(val2) is not int:
                val2 = regs1[val2]
        
        if i1[0] == "snd": #send value to program 0
            q0.append(regs1[i1[1]])
            iptr_1 += 1
            ans += 1
        elif i1[0] == "set": #sets value of register
            regs1[i1[1]] = val2
            iptr_1 += 1
        elif i1[0] == "add": #adds value to register
            regs1[i1[1]] += val2
            iptr_1 += 1
        elif i1[0] == "mul": #multiplies value of register
            regs1[i1[1]] *= val2
            iptr_1 += 1
        elif i1[0] == "mod": #modulo value of reg
            regs1[i1[1]] = regs1[i1[1]] % val2
            iptr_1 += 1
        elif i1[0] == "rcv": #recieves the last value sent from program 0
            if len(q1) > 0:
                regs1[i1[1]] = q1.pop(0)
                iptr_1 += 1
        elif i1[0] == "jgz": #jumps if greater than zero
            if regs1[i1[1]] > 0:
                iptr_1 += val2
            else:
                iptr_1 += 1
                
        testing and print("\tRegs0:", regs0, "\n\tQue0: ", q0, "\n\tRegs1:", regs1, "\n\tQue1: ", q1)
    
    return


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())