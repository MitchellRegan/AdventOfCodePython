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
            line = line.replace('\n', '').split(' ')
            for i in range(len(line)):
                line[i] = int(line[i])
            inpt.append(line)

    return inpt
            

def isLineValid(line:list):
    isValid = True
    isInc = (line[0] < line[1])
    for i in range(len(line)-1):
        val = abs(line[i] - line[i+1])
        if val == 0 or val >= 4:
            isValid = False
            break
        elif isInc and line[i] >= line[i+1]:
            isValid = False
            break
        elif not isInc and line[i] <= line[i+1]:
            isValid = False
            break

    return isValid


def solution1():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        if isLineValid(line):
            ans += 1

    return ans


def solution2():
    inpt = getInput()
    testing and print('\n\n')
    
    ans = 0
    for line in inpt:
        if isLineValid(line):
            ans += 1
        else:
            for i in range(len(line)):
                nl = [x for x in line]
                nl.pop(i)
                if isLineValid(nl):
                    ans += 1
                    break

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())