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
    testing and print("Input string:", inpt)
    
    for x in range(40):
        nextInpt = ""
        i = 0
        while i < len(inpt):
            sameDigit = 1
            j = i+1
            while j < len(inpt):
                if inpt[j] == inpt[i]:
                    sameDigit += 1
                    j += 1
                else:
                    break
            testing and print("\t", inpt[i:j], "becomes", j-i, inpt[i])
            nextInpt = nextInpt + str(j-i) + inpt[i]
            i = j
        inpt = nextInpt

    return len(inpt)


from collections import deque
def nextLookAndSaySeq(lass_:str):
    '''Takes a Look-And-Say-Sequence (LASS) string and returns the next sequence string.'''
    nextS = deque()
    i = 0
    while i < len(lass_):
        sameDigit = 1
        j = i+1
        while j < len(lass_):
            if lass_[j] == lass_[i]:
                sameDigit += 1
                j += 1
            else:
                break
        nextS.append(str(j-i))
        nextS.append(lass_[i])
        i = j
    return ''.join(nextS)


def solution2():
    inpt = getInput()
    
    for x in range(50):
        inpt = nextLookAndSaySeq(inpt)

    return len(inpt)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())