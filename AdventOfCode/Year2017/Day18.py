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


class Prog():
    '''Class to handle the programs described in y2017d18p2. Handles its own list of instructions,
    instruction pointer, registers, queue, and sending instructions to/from the other program.'''
    def __init__(self, id_:int, instructions_:list, registers_:dict):
        self.id = id_
        self.inpt = instructions_
        self.regs = registers_
        self.iptr = 0
        self.q = []
        self.otherProg = None
        self.isWaiting = False
        self.numTimesSentVal = 0


    def __str__(self):
        return "Prog" + str(self.id) + ":    iPtr = " + str(self.iptr) + " -> " + str(self.inpt[self.iptr]) + "\n\tRegs: " + str(self.regs) + "\n\tQue:  " + str(self.q) + "\n\tIs waiting: " + str(self.isWaiting) + "\n"


    def update(self):
        '''Performs this program's next instruction at its instruction pointer, unless waiting for input.'''
        if self.isWaiting:
            if len(self.q) > 0:
                self.isWaiting = False
            else:
                return

        #Temp vars for the instruction and values at our iptr's input (for readability)
        ins = self.inpt[self.iptr][0]
        val1 = self.inpt[self.iptr][1]
        val2 = 0
        if len(self.inpt[self.iptr]) > 2:
            val2 = self.inpt[self.iptr][2]
            if type(val2) is not int:
                val2 = self.regs[val2]

        if ins == "snd": #send value to other program
            if type(val1) is int:
                self.otherProg.q.append(val1)
            else:
                self.otherProg.q.append(self.regs[val1])
            self.numTimesSentVal += 1
            self.iptr += 1
        elif ins == "set": #sets value of register
            self.regs[val1] = val2
            self.iptr += 1
        elif ins == "add": #adds value to register
            self.regs[val1] += val2
            self.iptr += 1
        elif ins == "mul": #multiplies value of register
            self.regs[val1] *= val2
            self.iptr += 1
        elif ins == "mod": #modulo value of reg
            self.regs[val1] = self.regs[val1] % val2
            self.iptr += 1
        elif ins == "rcv": #recieves the last value sent from program 1
            if len(self.q) > 0:
                self.regs[val1] = self.q.pop(0)
                self.iptr += 1
            else:
                self.isWaiting = True
        elif ins == "jgz": #jumps if greater than zero
            if (type(val1) is int and val1 > 0) or (type(val1) is not int and self.regs[val1] > 0):
                self.iptr += val2
            else:
                self.iptr += 1
        return


def solution2():
    inpt, regs0 = getInput()
    #Setting initial register values denoted by the instructions
    regs1 = {}
    for k in regs0.keys():
        regs1[k] = 0
    regs0['p'] = 0
    regs1['p'] = 1

    #Creating Prog class instances for each program
    prog0 = Prog(0, inpt, regs0)
    prog1 = Prog(1, inpt, regs1)
    prog0.otherProg = prog1
    prog1.otherProg = prog0

    #Looping until both programs are stuck waiting for instructions from each other
    ans = 0
    while True:
        testing and print("=======================================================================================\n", prog0, "\n", prog1)
        prog0.update()
        prog1.update()
        if prog0.isWaiting and prog1.isWaiting:
            break
    
    return prog1.numTimesSentVal


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())