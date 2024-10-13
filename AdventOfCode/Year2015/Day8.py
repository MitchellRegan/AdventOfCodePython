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
            inpt.append(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        testing and print("\n", line)
        totalLen = len(line)
        sLen = 0
        i = 1
        while i < len(line)-1:
            if line[i] != '\\':
                sLen += 1
                i += 1
            else:
                if line[i+1] == 'x':
                    sLen += 1
                    i += 4
                else:
                    sLen += 1
                    i += 2
        testing and print("\tTotal Length:", totalLen, "    String Length:", sLen)
        ans += totalLen - sLen

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for line in inpt:
        testing and print("\n", line)
        totalLen = len(line)
        sLen = 6
        i = 1
        while i < len(line)-1:
            if line[i] != '\\':
                sLen += 1
                i += 1
            else:
                if line[i+1] == 'x':
                    sLen += 5
                    i += 4
                else:
                    sLen += 4
                    i += 2
        testing and print("\tTotal Length:", totalLen, "    String Length:", sLen)
        ans += sLen - totalLen

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())