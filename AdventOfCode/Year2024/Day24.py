aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    gates = {}
    ins = []

    with open(inFile, 'r') as f:
        onGates = True
        for line in f:
            line = line.replace('\n', '')

            if line == '':
                onGates = False
            elif onGates:
                gate,val = line.split(': ')
                gates[gate] = int(val)
            else:
                line = line.split(' ')
                line.pop(3)
                ins.append(line)

    return gates, ins
            

def solution1():
    gates, ins = getInput()

    while len(ins) > 0:
        i = 0
        while i < len(ins):
            g1, opp, g2, z = ins[i]

            #If one of the gates used in the opperation isn't defined yet, we skip and come back later
            if g1 not in gates.keys() or g2 not in gates.keys():
                i += 1
            #Otherwise we can proceed with the operation
            else:
                if opp == "AND":
                    gates[z] = (gates[g1] & gates[g2])
                elif opp == "OR":
                    gates[z] = (gates[g1] | gates[g2])
                elif opp == "XOR":
                    gates[z] = (gates[g1] ^ gates[g2])

                #Removing this instruction from the list before moving to the next one
                ins.pop(i)

    allZgates = [x for x in gates.keys() if x[0] == 'z']
    allZgates.sort(reverse=True)
    ans = [str(gates[z]) for z in allZgates]
    ans = int(''.join(ans), 2)

    return ans


def solution2():
    gates, ins = getInput()

    allXgates = [x for x in gates.keys() if x[0] == 'x']
    allXgates.sort(reverse=True)
    xVal = [str(gates[x]) for x in allXgates]
    xVal = int(''.join(xVal), 2)

    allYgates = [y for y in gates.keys() if y[0] == 'y']
    allYgates.sort(reverse=True)
    yVal = [str(gates[y]) for y in allYgates]
    yVal = int(''.join(yVal), 2)

    testing and print("X value:", xVal, "    Y value:", yVal)

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())