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
            inpt.append([int(line[1][1:]), int(line[3]), int(line[-1][:-1])])

    return inpt
            

def solution1():
    inpt = getInput()
    
    t = 0
    while True:
        valid = True
        for i in inpt:
            if (t + i[0] + i[2]) % i[1] != 0:
                valid = False
                break
        if valid:
            return t
        t += 1

    return


def solution2():
    inpt = getInput()
    inpt.append([inpt[-1][0]+1, 11, 0])
    
    t = 0
    while True:
        valid = True
        for i in inpt:
            if (t + i[0] + i[2]) % i[1] != 0:
                valid = False
                break
        if valid:
            return t
        t += 1

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())