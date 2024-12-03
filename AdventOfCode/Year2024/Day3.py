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
        i = 0
        while i < len(line):
            if i+4 < len(line) and line[i:i+4] == 'mul(':
                endInd = i+4
                while endInd < len(line) and line[endInd] in "01234567890,)":
                    if line[endInd] == ')':
                        endInd += 1
                        break
                    endInd += 1
                testing and print("======", line[i:endInd])
                if line[endInd-1] == ')':
                    mulStr = line[i+4:endInd-1]
                    mulStr = mulStr.replace(')','').split(',')
                    if len(mulStr) == 2:
                        testing and print("\t====", mulStr, '    =', int(mulStr[0]) * int(mulStr[1]))
                        ans += int(mulStr[0]) * int(mulStr[1])
            i += 1

    return ans


def solution2():
    inpt = getInput()

    mulEnabled = True
    
    ans = 0
    for line in inpt:
        i = 0
        while i < len(line):
            if i+4 < len(line) and line[i:i+4] == 'mul(':
                endInd = i+4
                while endInd < len(line) and line[endInd] in "01234567890,)":
                    if line[endInd] == ')':
                        endInd += 1
                        break
                    endInd += 1
                testing and print("======", line[i:endInd])
                if line[endInd-1] == ')':
                    mulStr = line[i+4:endInd-1]
                    mulStr = mulStr.replace(')','').split(',')
                    if len(mulStr) == 2:
                        testing and print("\t====", mulStr, '    =', int(mulStr[0]) * int(mulStr[1]))
                        if mulEnabled:
                            ans += int(mulStr[0]) * int(mulStr[1])
                        else:
                            testing and print("Can't add. Mul is disabled")
            elif line[i] == 'd':
                if i+6 < len(line) and line[i:i+7] == 'don\'t()':
                    testing and print("Mul disabled")
                    mulEnabled = False
                elif i+3 < len(line) and line[i:i+4] == 'do()':
                    testing and print("Mul enabled")
                    mulEnabled = True
            i += 1

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())