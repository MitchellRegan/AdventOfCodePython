aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ""
    molMap = {}

    with open(inFile, 'r') as f:
        molecules = True
        for line in f:
            line = line.replace('\n', '')
            if len(line) == 0:
                molecules = False
            elif molecules:
                line = line.split(' ')
                if line[0] not in molMap.keys():
                    molMap[line[0]] = []
                molMap[line[0]].append(line[2])
            else:
                inpt = line

    return inpt, molMap
            

def solution1():
    inpt, molMap = getInput()
    
    if True:
        print("Input string:", inpt, "\nMolecules:")
        for k in molMap.keys():
            print("\t", k, ":", molMap[k])

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())