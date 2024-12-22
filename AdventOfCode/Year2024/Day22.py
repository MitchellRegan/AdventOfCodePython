aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"
import math

def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt.append(int(line))

    return inpt


def getNextSecretNumber(num_:int)->int:
    #Multiply by 64, then mix by performing bitwise XOR, then prune with mod 16777216
    nextNum = (num_ * 64) ^ num_
    nextNum = nextNum % 16777216

    #Divide by 32 rounding down, then mix and prune
    nextNum = math.floor(nextNum / 32) ^ nextNum
    nextNum = nextNum % 16777216

    #Multiply by 2048, then mix and prune
    nextNum = (nextNum * 2048) ^ nextNum
    nextNum = nextNum % 16777216

    return nextNum


def solution1():
    inpt = getInput()
    
    ans = 0
    for num in inpt:
        testing and print("Initial number:", num)
        finalNum = num
        for x in range(2000):
            finalNum = getNextSecretNumber(finalNum)
            if x < 10:
                testing and print("\t", finalNum)
        testing and print("\t\t2000th number:", finalNum)
        ans += finalNum

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for num in inpt:
        testing and print("Initial number:", num)
        finalNum = num
        for x in range(2000):
            finalNum = getNextSecretNumber(finalNum)
            if x < 10:
                testing and print("\t", finalNum)
        testing and print("\t\t2000th number:", finalNum)
        ans += finalNum

    return ans


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())