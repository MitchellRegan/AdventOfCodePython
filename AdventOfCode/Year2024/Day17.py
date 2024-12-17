aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"
import math
from collections import deque

def getInput():
    regs = {}
    prog = []

    with open(inFile, 'r') as f:
        onRegs = True
        for line in f:
            line = line.replace('\n', '').split(' ')

            if line[0] == '':
                onRegs = False
            elif onRegs:
                regs[line[1][0]] = int(line[2])
            else:
                prog = line[1].split(',')
                prog = [int(x) for x in prog]

    return regs, prog
            

def solution1():
    regs, prog = getInput()
    output = ""

    iptr = 0
    while iptr < len(prog)-1:
        #Literal operand is the value in the program just after the instruction pointer
        literalOp = prog[iptr+1]
        #Combo operand has weird instructions based on what the literalOp is
        comboOp = literalOp
        if literalOp == 4:
            comboOp = regs['A']
        elif literalOp == 5:
            comboOp = regs['B']
        elif literalOp == 6:
            comboOp = regs['C']

        if prog[iptr] == 0: #adv performs division of reg A and combo
            regs['A'] = math.trunc(regs['A'] / (2**comboOp))

        elif prog[iptr] == 1: #bxl performs bitwise XOR of reg B and literal
            regs['B'] = regs['B'] ^ literalOp

        elif prog[iptr] == 2: #bst performs input val mod 8
            regs['B'] = comboOp % 8

        elif prog[iptr] == 3: #jnz jumps iptr if reg A != 0, otherwise does nothing
            if regs['A'] != 0:
                iptr = literalOp - 2 #The -2 offsets the default +2 after each loop

        elif prog[iptr] == 4: #bxc calculates bitwise XOR of reg B and reg C
            regs['B'] = regs['B'] ^ regs['C']

        elif prog[iptr] == 5: #out calculates the value of combo mod 8 and adds it to the output list
            if output == "":
                output = str(comboOp % 8)
            else:
                output = output + ',' + str(comboOp % 8)

        elif prog[iptr] == 6: #bdv performs division of reg B and combo
            regs['B'] = math.trunc(regs['A'] / (2**comboOp))

        elif prog[iptr] == 7: #cdv
            regs['C'] = math.trunc(regs['A'] / (2**comboOp))

        iptr += 2

    return output


def solution2():
    startingRegs, startingProg = getInput()
    print("List prog: ", startingProg)
    prog = deque()
    for x in startingProg:
        prog.append(x)
    print("Deque prog:", prog)

    newA = 0 #500170000 #Tried up until 100,000,000 no luck
    jumpSize = 7
    if testing:
        newA = 0
    longestOutput = 0
    while True:
        if newA % 500000 == 0:
            print("Testing A =", newA)

        regs = {}
        for x in startingRegs.keys():
            regs[x] = startingRegs[x]
        regs['A'] = newA
        output = deque()
        isValid = True

        iptr = 0
        while iptr < len(prog)-1:
            #Literal operand is the value in the program just after the instruction pointer
            literalOp = prog[iptr+1]
            #Combo operand has weird instructions based on what the literalOp is
            comboOp = literalOp
            if literalOp == 4:
                comboOp = regs['A']
            elif literalOp == 5:
                comboOp = regs['B']
            elif literalOp == 6:
                comboOp = regs['C']

            if prog[iptr] == 0: #adv performs division of reg A and combo
                regs['A'] = math.trunc(regs['A'] / (2**comboOp))

            elif prog[iptr] == 1: #bxl performs bitwise XOR of reg B and literal
                regs['B'] = regs['B'] ^ literalOp

            elif prog[iptr] == 2: #bst performs input val mod 8
                regs['B'] = comboOp % 8

            elif prog[iptr] == 3: #jnz jumps iptr if reg A != 0, otherwise does nothing
                if regs['A'] != 0:
                    iptr = literalOp - 2 #The -2 offsets the default +2 after each loop

            elif prog[iptr] == 4: #bxc calculates bitwise XOR of reg B and reg C
                regs['B'] = regs['B'] ^ regs['C']

            elif prog[iptr] == 5: #out calculates the value of combo mod 8 and adds it to the output list
                output.append(comboOp % 8)
                if prog[len(output)-1] != output[-1]:
                    isValid = False
                    break
                elif len(output) > longestOutput:
                    longestOutput = len(output)
                    print("========== A =", newA, "longest output so far:", longestOutput)

            elif prog[iptr] == 6: #bdv performs division of reg B and combo
                regs['B'] = math.trunc(regs['A'] / (2**comboOp))

            elif prog[iptr] == 7: #cdv
                regs['C'] = math.trunc(regs['A'] / (2**comboOp))

            iptr += 2

        #If the program successfully completes, we have to double-check the output against the program input
        if isValid and output == prog:
            testing and print("\tA =", newA, "is VALID:", output)
            if jumpSize > 1:
                newA -= (jumpSize - 1)
                jumpSize = 1
            else:
                newA += jumpSize
        else:
            newA += jumpSize

    return newA


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())