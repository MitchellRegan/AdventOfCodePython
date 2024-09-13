aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if line[0] == '+':
                inpt.append(int(line[1:]))
            else:
                inpt.append(int(line))

    return inpt
            

def solution1():
    inpt = getInput()
    
    if testing:
        print(inpt)

    return sum(inpt)


def solution2():
    inpt = getInput()
    
    freq = 0
    seenFreq = {0:1}
    while True:
        for val in inpt:
            freq += val
            if freq in seenFreq.keys():
                return freq
            seenFreq[freq] = 1
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())