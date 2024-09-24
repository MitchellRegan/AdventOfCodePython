aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ''

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt = line

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for i in range(len(inpt)-1):
        if inpt[i] == inpt[i+1]:
            ans += int(inpt[i])
            
    if inpt[0] == inpt[-1]:
        ans += int(inpt[0])

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for i in range(len(inpt)):
        nextIndex = i + (len(inpt)//2)
        if nextIndex >= len(inpt):
            nextIndex -= len(inpt)
        if inpt[i] == inpt[nextIndex]:
            ans += int(inpt[i])
    
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())