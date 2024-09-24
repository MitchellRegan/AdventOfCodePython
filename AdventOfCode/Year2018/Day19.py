aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    insPtr = None
    ins = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if line[0] == '#':
                insPtr = int(line[4:])
            else:
                line = line.split(' ')
                line[0] = line[0].upper()
                for i in range(1, len(line)):
                    line[i] = int(line[i])
                ins.append(line)

    return insPtr, ins
            

def solution1():
    insPtr, insList = getInput()
    
    if testing:
        print("Bound Register Index:", insPtr)
        print("Instruction List:")
        for i in insList:
            print("\t", i)
        print()
        
    # 6 register holders, indexed at 0-5
    reg = [0] * 6
    #Register index pointer that is bound to the instruction pointer
    regPtr = insPtr
    
    #Executing the instruction at the index the instruction pointer is currently set to
    insPtr = 0
    while insPtr < len(insList):
        opr, A, B, C = insList[insPtr]
        testing and print("IP =", insPtr, ":", insList[insPtr])
        testing and print("\tUpdating reg", regPtr, "to insPtr val", insPtr)
        reg[regPtr] = insPtr
        testing and print("\tRegister Before:", reg)

        # ADDR add register: reg A + reg B = reg C
        if opr == "ADDR":
            reg[C] = reg[A] + reg[B]
        # ADDI add immediate: reg A + val B = reg C
        elif opr == "ADDI":
            reg[C] = reg[A] + B
        # MULR multiply register: reg A * reg B = reg C
        elif opr == "MULR":
            reg[C] = reg[A] * reg[B]
        # MULI multiply immediate: reg A * val B = reg C
        elif opr == "MULI":
            reg[C] = reg[A] * B
        # BANR bitwise AND register: reg A BAND reg B = reg C
        elif opr == "BANR":
            reg[C] = reg[A] & reg[B]
        # BANI bitwise AND immediate: reg A BAND val B = reg C
        elif opr == "BANI":
            reg[C] = reg[A] & B
        # BORR bitwise OR register: reg A BOR reg B = reg C
        elif opr == "BORR":
            reg[C] = reg[A] | reg[B]
        # BORI bitwise OR immediate: reg A BOR val B = reg C
        elif opr == "BORI":
            reg[C] = reg[A] | B
        # SETR set register: reg A = reg C
        elif opr == "SETR":
            reg[C] = reg[A]
        # SETI set immediate: val A = reg C
        elif opr == "SETI":
            reg[C] = A
        # GTIR greater-than immediate/register: val A > reg B then reg C = 1, else reg C = 0
        elif opr == "GTIR":
            if A > reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # GTRI greater-than register/immediate: reg A > val B then reg C = 1, else reg C = 0
        elif opr == "GTRI":
            if reg[A] > B:
                reg[C] = 1
            else:
                reg[C] = 0
        # GTRR greater-than register/register: reg A > reg B then reg C = 1, else reg C = 0
        elif opr == "GTRR":
            if reg[A] > reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQIR equal immediate/register: val A == reg B, then reg C = 1, else reg C = 0
        elif opr == "EQIR":
            if A == reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQRI equal register/immediate: reg A == val B, then reg C = 1, else reg C = 0
        elif opr == "EQRI":
            if reg[A] == B:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQRR equal register/register: reg A == reg B, then reg C = 1, else reg C = 0
        elif opr == "EQRR":
            if reg[A] == reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
                
        #After each instruction, the value of the instruction pointer is replaced by the value
        #in the register pointer + 1        
        insPtr = 1 + reg[regPtr]
                
        if testing:
            print("\tRegister After: ", reg)
            blerg = input()
            
    return reg[0]


def solution2():
    insPtr, insList = getInput()
    
    # 6 register holders, indexed at 0-5
    #reg = [1,0,0,0,0,0]
    reg = [0,2,0,11,10551347, 10551348]
    #Register index pointer that is bound to the instruction pointer
    regPtr = insPtr
    
    #Executing the instruction at the index the instruction pointer is currently set to
    #insPtr = 0
    insPtr = 11
    while insPtr < len(insList):
        opr, A, B, C = insList[insPtr]
        reg[regPtr] = insPtr
        print("insPtr:", insPtr, "    Reg:", reg)

        # ADDR add register: reg A + reg B = reg C
        if opr == "ADDR":
            reg[C] = reg[A] + reg[B]
        # ADDI add immediate: reg A + val B = reg C
        elif opr == "ADDI":
            reg[C] = reg[A] + B
        # MULR multiply register: reg A * reg B = reg C
        elif opr == "MULR":
            reg[C] = reg[A] * reg[B]
        # MULI multiply immediate: reg A * val B = reg C
        elif opr == "MULI":
            reg[C] = reg[A] * B
        # BANR bitwise AND register: reg A BAND reg B = reg C
        elif opr == "BANR":
            reg[C] = reg[A] & reg[B]
        # BANI bitwise AND immediate: reg A BAND val B = reg C
        elif opr == "BANI":
            reg[C] = reg[A] & B
        # BORR bitwise OR register: reg A BOR reg B = reg C
        elif opr == "BORR":
            reg[C] = reg[A] | reg[B]
        # BORI bitwise OR immediate: reg A BOR val B = reg C
        elif opr == "BORI":
            reg[C] = reg[A] | B
        # SETR set register: reg A = reg C
        elif opr == "SETR":
            reg[C] = reg[A]
        # SETI set immediate: val A = reg C
        elif opr == "SETI":
            reg[C] = A
        # GTIR greater-than immediate/register: val A > reg B then reg C = 1, else reg C = 0
        elif opr == "GTIR":
            if A > reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # GTRI greater-than register/immediate: reg A > val B then reg C = 1, else reg C = 0
        elif opr == "GTRI":
            if reg[A] > B:
                reg[C] = 1
            else:
                reg[C] = 0
        # GTRR greater-than register/register: reg A > reg B then reg C = 1, else reg C = 0
        elif opr == "GTRR":
            if reg[A] > reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQIR equal immediate/register: val A == reg B, then reg C = 1, else reg C = 0
        elif opr == "EQIR":
            if A == reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQRI equal register/immediate: reg A == val B, then reg C = 1, else reg C = 0
        elif opr == "EQRI":
            if reg[A] == B:
                reg[C] = 1
            else:
                reg[C] = 0
        # EQRR equal register/register: reg A == reg B, then reg C = 1, else reg C = 0
        elif opr == "EQRR":
            if reg[A] == reg[B]:
                reg[C] = 1
            else:
                reg[C] = 0
                
        #After each instruction, the value of the instruction pointer is replaced by the value
        #in the register pointer + 1        
        insPtr = 1 + reg[regPtr]
                
        if testing:
            print("\tRegister After: ", reg)
            blerg = input()
            
    return reg[0]


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())