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
            inpt = int(line.replace('\n', ''))

    return inpt
            

def solution1():
    inpt = getInput()
    
    numChain = {0:0}
    curVal = 0
    for i in range(1, 2018):
        for x in range(inpt % i):
            curVal = numChain[curVal]
        numChain[i] = numChain[curVal]
        numChain[curVal] = i
        curVal = i
        
    return numChain[2017]


def solution2():
    inpt = getInput()
    
    valAfter0 = None
    ptr = 0
    for i in range(1, 50000001):
        ptr = ((ptr + inpt) % i) + 1
        if ptr == 0:
            ptr = i
        if ptr == 1:
            valAfter0 = i
            
    return valAfter0    


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
# 63038 too low
# 2719747 too low
# 6043091 too low
# 26271115 not it