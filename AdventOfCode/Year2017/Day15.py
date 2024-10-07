aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    genA = None
    genB = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if genA is None:
                genA = int(line[-1])
            else:
                genB = int(line[-1])

    return genA, genB
            

def solution1():
    genA, genB = getInput()
    numLoops = 40000000
    
    ans = 0
    for i in range(numLoops):
        if testing and i % 1000000 == 0:
            print("Loop", i, "/ 40,000,000")
        genA = (genA * 16807) % 2147483647
        genB = (genB * 48271) % 2147483647
        #testing and print("Loop", i, "    GenA:", genA, "    GenB:", genB)
        binA = f'{genA:08b}'[-16:]
        binB = f'{genB:08b}'[-16:]
        #testing and print(binA)
        #testing and print(binB, "\n")
        if binA == binB:
            ans += 1

    return ans


def solution2():
    genA, genB = getInput()
    numLoops = 5000000

    ans = 0
    for i in range(numLoops):
        genA = (genA * 16807) % 2147483647
        while genA % 4 != 0:
            genA = (genA * 16807) % 2147483647
        genB = (genB * 48271) % 2147483647
        while genB % 8 != 0:
            genB = (genB * 48271) % 2147483647
            
        binA = f'{genA:08b}'[-16:]
        binB = f'{genB:08b}'[-16:]
        
        if binA == binB:
            ans += 1

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())