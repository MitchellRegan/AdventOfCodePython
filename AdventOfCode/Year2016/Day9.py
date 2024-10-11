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
    
    testing and print(inpt)
    i = 0
    while i < len(inpt):
        if inpt[i] == '(':
            x = i+1
            while inpt[x] != 'x':
                x += 1
            end = x+2
            while inpt[end] != ')':
                end += 1
            
            numChar = int(inpt[i+1:x])
            amt = int(inpt[x+1:end])
            substr = inpt[end+1:end+1+numChar]
            fullDupe = ""
            for a in range(amt-1):
                fullDupe = fullDupe + substr
                
            inpt = inpt[:i] + fullDupe + inpt[end+1:]
            i += numChar * amt
        else:
            i += 1

    return len(inpt)


def solution2():
    inpt = getInput()
    
    i = 0
    while i < len(inpt):
        if inpt[i] == '(':
            x = i+1
            while inpt[x] != 'x':
                x += 1
            end = x+2
            while inpt[end] != ')':
                end += 1
            
            numChar = int(inpt[i+1:x])
            amt = int(inpt[x+1:end])
            substr = inpt[end+1:end+1+numChar]
            fullDupe = ""
            for a in range(amt-1):
                fullDupe = fullDupe + substr
                
            inpt = inpt[:i] + fullDupe + inpt[end+1:]
        else:
            i += 1

    testing and print(inpt)
    return len(inpt)


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())