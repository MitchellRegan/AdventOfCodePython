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
            line[2] = int(line[2])
            line[-1] = int(line[-1])
            if line[1] == "dec":
                line[2] *= -1
            line.pop(3)
            line.pop(1)
            inpt.append(line)
            if line[0] not in reg.keys():
                reg[line[0]] = 0
            if line[-3] not in reg.keys():
                reg[line[-3]] = 0

    return inpt, reg
            

def solution1():
    inpt, reg = getInput()
    
    testing and print("Registers:", reg, "\nInstructions:")
    for line in inpt:
        r1, amt, r2, op, comp = line
        testing and print("\t", line)
        
        if op == ">" and reg[r2] > comp:
            reg[r1] += amt
        elif op == ">=" and reg[r2] >= comp:
            reg[r1] += amt
        elif op == "<" and reg[r2] < comp:
            reg[r1] += amt
        elif op == "<=" and reg[r2] <= comp:
            reg[r1] += amt
        elif op == "==" and reg[r2] == comp:
            reg[r1] += amt
        elif op == "!=" and reg[r2] != comp:
            reg[r1] += amt
            
        testing and print("\tReg:", reg)
        
    ans = None
    for r in reg.keys():
        if ans is None or reg[r] > ans:
            ans = reg[r]

    return ans


def solution2():
    inpt, reg = getInput()
    
    ans = 0
    for line in inpt:
        r1, amt, r2, op, comp = line
        
        if op == ">" and reg[r2] > comp:
            reg[r1] += amt
        elif op == ">=" and reg[r2] >= comp:
            reg[r1] += amt
        elif op == "<" and reg[r2] < comp:
            reg[r1] += amt
        elif op == "<=" and reg[r2] <= comp:
            reg[r1] += amt
        elif op == "==" and reg[r2] == comp:
            reg[r1] += amt
        elif op == "!=" and reg[r2] != comp:
            reg[r1] += amt
            
        if reg[r1] > ans:
            ans = reg[r1]

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())