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
            inpt.append(int(line))
    return inpt
            

def solution1():
    inpt = getInput()
    
    currIndex = 0
    steps = 0
    while True:
        steps += 1
        testing and print("Instructions:", inpt, "    CurrIndex:", currIndex)
        nextIndex = currIndex + inpt[currIndex]
        if nextIndex > -1 and nextIndex < len(inpt):
            inpt[currIndex] = inpt[currIndex] + 1
            currIndex = nextIndex
        else:
            break

    return steps


def solution2():
    inpt = getInput()
    
    currIndex = 0
    steps = 0
    while True:
        steps += 1
        testing and print("Instructions:", inpt, "    CurrIndex:", currIndex)
        nextIndex = currIndex + inpt[currIndex]
        
        if inpt[currIndex] >= 3:
            inpt[currIndex] = inpt[currIndex] - 1
        else:
            inpt[currIndex] = inpt[currIndex] + 1
            
        if nextIndex > -1 and nextIndex < len(inpt):
            currIndex = nextIndex
        else:
            break

    return steps


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())