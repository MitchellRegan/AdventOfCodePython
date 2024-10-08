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
            inpt.append([int(x) for x in line if x != ''])

    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for i in inpt:
        #print(i)
        hyp = max(i)
        i.remove(hyp)
        a,b = i
        testing and print("A:", a, "   B:", b, "   Hypot:", hyp)
        if a + b > hyp:
            ans += 1

    return ans


def solution2():
    inpt = getInput()
    newInpt = []
    for i in range(0, len(inpt), 3):
        newInpt.append([inpt[i][0], inpt[i+1][0], inpt[i+2][0]])
        newInpt.append([inpt[i][1], inpt[i+1][1], inpt[i+2][1]])
        newInpt.append([inpt[i][2], inpt[i+1][2], inpt[i+2][2]])
    
    ans = 0
    for i in newInpt:
        #print(i)
        hyp = max(i)
        i.remove(hyp)
        a,b = i
        testing and print("A:", a, "   B:", b, "   Hypot:", hyp)
        if a + b > hyp:
            ans += 1

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())