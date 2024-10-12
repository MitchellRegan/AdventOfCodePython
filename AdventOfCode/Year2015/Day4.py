import hashlib
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ""

    with open(inFile, 'r') as f:
        for line in f:
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    i = 1
    while True:
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
        if hs[0] == '0' and hs[1] == '0' and hs[2] == '0' and hs[3] == '0' and hs[4] == '0':
            return i
        i += 1

    return


def solution2():
    inpt = getInput()
    
    i = 1
    while True:
        s = inpt + str(i)
        hs = hashlib.md5(s.encode()).hexdigest()
        if hs[0] == '0' and hs[1] == '0' and hs[2] == '0' and hs[3] == '0' and hs[4] == '0' and hs[5] == '0':
            return i
        i += 1

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())