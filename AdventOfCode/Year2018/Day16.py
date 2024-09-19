aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    instructionExamples = {}
    instructionList = []

    with open(inFile, 'r') as f:
        ins = None
        for line in f:
            line = line.replace('\n', '')
            if len(line) == 0:
                continue
            elif line[0] == 'B': #Values before the instruction
                line = line.replace("Before: [", '').replace(']', '').split(', ')
                ins = [[int(x) for x in line]]
            elif line[0] == 'A': #Values after the instruction
                line = line.replace("After:  [", '').replace(']', '').split(', ')
                ins.append([int(x) for x in line])
                if ins[1] in instructionExamples.keys():
                    instructionExamples[ins[1]].append(ins[0])
                    instructionExamples[ins[1]].append(ins[2])
                else:
                    instructionExamples[ins[1]] = [ins[0], ins[2]]
                ins = None
            else: #Sequence of number values
                line = tuple([int(x) for x in line.split(' ')])
                if ins is None: #Instruction numbers to add to the list
                    instructionList.append(line)
                else: #Middle entry between the "Before" and "After" examples
                    ins.append(line)

    return instructionExamples, instructionList
            

def solution1():
    examples, insList = getInput()
    
    if testing:
        print("\tExamples:")
        for e in examples.keys():
            print("\t\t", e, ":", examples[e])
        print("\n\tInstructions:")
        for i in insList:
            print('\t\t', i)
        print("=========================\n")
            
    #Looping through each instruction in-order to find all that match at least 3 opcodes
    ans = 0
    for ins in examples.keys():
        #Instructions are [opcode, input 1, input 2, and output]
        op, A, B, C = ins
        testing and print("Instruction", ins, "    A:", A, "   B:", B, "   C:", C)
        
        #Iterating through the instruction's examples in groups of 2 (before, after)
        for i in range(0, len(examples[ins]), 2):
            before = examples[ins][i]
            after = examples[ins][i+1]
            possibleOps = []
            testing and print("\tBefore:", before, "    After:", after)

            # ADDR add register: reg A + reg B = reg C
            if before[A] + before[B] == after[C]:
                possibleOps.append("ADDR")
            # ADDI add immediate: reg A + val B = reg C
            if before[A] + B == after[C]:
                possibleOps.append("ADDI")
            # MULR multiply register: reg A * reg B = reg C
            if before[A] * before[B] == after[C]:
                possibleOps.append("MULR")
            # MULI multiply immediate: reg A * val B = reg C
            if before[A] * B == after[C]:
                possibleOps.append("MULI")
            # BANR bitwise AND register: reg A BAND reg B = reg C
            if before[A] & before[B] == after[C]:
                possibleOps.append("BANR")
            # BANI bitwise AND immediate: reg A BAND val B = reg C
            if before[A] & B == after[C]:
                possibleOps.append("BANI")
            # BORR bitwise OR register: reg A BOR reg B = reg C
            if before[A] | before[B] == after[C]:
                possibleOps.append("BORR")
            # BORI bitwise OR immediate: reg A BOR val B = reg C
            if before[A] | B == after[C]:
                possibleOps.append("BORI")
            # SETR set register: reg A = reg C
            if before[A] == after[C]:
                possibleOps.append("SETR")
            # SETI set immediate: val A = reg C
            if A == after[C]:
                possibleOps.append("SETI")
            # GTIR greater-than immediate/register: val A > reg B then reg C = 1, else reg C = 0
            if (A > before[B] and after[C] == 1) or (A <= before[B] and after[C] == 0):
                possibleOps.append("GTIR")
            # GTRI greater-than register/immediate: reg A > val B then reg C = 1, else reg C = 0
            if (before[A] > B and after[C] == 1) or (before[A] <= B and after[C] == 0):
                possibleOps.append("GTRI")
            # GTRR greater-than register/register: reg A > reg B then reg C = 1, else reg C = 0
            if (before[A] > before[B] and after[C] == 1) or (before[A] <= before[B] and after[C] == 0):
                possibleOps.append("GTRR")
            # EQIR equal immediate/register: val A == reg B, then reg C = 1, else reg C = 0
            if (A == before[B] and after[C] == 1) or (A != before[B] and after[C] == 0):
                possibleOps.append("EQIR")
            # EQRI equal register/immediate: reg A == val B, then reg C = 1, else reg C = 0
            if (before[A] == B and after[C] == 1) or (before[A] != B and after[C] == 0):
                possibleOps.append("EQRI")
            # EQRR equal register/register: reg A == reg B, then reg C = 1, else reg C = 0
            if (before[A] == before[B] and after[C] == 1) or (before[A] != before[B] and after[C] == 0):
                possibleOps.append("EQRR")
            
            testing and print("\t\tPossible operations:", possibleOps)
            #If this example has 3 or more possible opcode functions, we add it to our answer
            if len(possibleOps) > 2:
                ans += 1

    return ans


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())