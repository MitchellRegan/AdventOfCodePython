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
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    targetLen = 272
    if testing:
        targetLen = 20
        
    testing and print(inpt)
    while len(inpt) < targetLen:
        newInpt = inpt[::-1]
        newInpt = newInpt.replace('0',' ').replace('1','0').replace(' ','1')
        inpt = inpt + '0' + newInpt
        testing and print(inpt, "    New Inpt:", newInpt)
    inpt = inpt[:targetLen]
    testing and print(inpt, "    Trimmed to length", targetLen)
    
    #Performing checksum until input string length is odd
    while len(inpt) % 2 == 0:
        checkSum = ""
        for i in range(0, len(inpt), 2):
            if inpt[i] == inpt[i+1]:
                checkSum = checkSum + '1'
            else:
                checkSum = checkSum + '0'
        testing and print(inpt, " --> ", checkSum)
        inpt = checkSum

    return inpt


def solution2():
    inpt = getInput()
    targetLen = 35651584
        
    while len(inpt) < targetLen:
        newInpt = inpt[::-1]
        newInpt = newInpt.replace('0',' ').replace('1','0').replace(' ','1')
        inpt = inpt + '0' + newInpt
    inpt = inpt[:targetLen]
    
    #Performing checksum until input string length is odd
    while len(inpt) % 2 == 0:
        checkSum = ""
        for i in range(0, len(inpt), 2):
            if inpt[i] == inpt[i+1]:
                checkSum = checkSum + '1'
            else:
                checkSum = checkSum + '0'
        inpt = checkSum

    return inpt


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())