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
    
    seen = {(0,0):1}#Key is (x,y) pos, Value = number of gifts
    x = 0
    y = 0
    for c in inpt:
        if c == '>':
            x += 1
        elif c == '<':
            x -= 1
        elif c == 'v':
            y -= 1
        else:
            y += 1
            
        if (x,y) not in seen.keys():
            seen[(x,y)] = 1
        else:
            seen[(x,y)] += 1

    return len(seen.keys())


def solution2():
    inpt = getInput()
    
    seen = {(0,0):2}#Key is (x,y) pos, Value = number of gifts
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for i in range(len(inpt)):
        c = inpt[i]
        if i % 2 == 0:
            if c == '>':
                x1 += 1
            elif c == '<':
                x1 -= 1
            elif c == 'v':
                y1 -= 1
            else:
                y1 += 1
            if (x1,y1) not in seen.keys():
                seen[(x1,y1)] = 1
        else:
            if c == '>':
                x2 += 1
            elif c == '<':
                x2 -= 1
            elif c == 'v':
                y2 -= 1
            else:
                y2 += 1
            if (x2,y2) not in seen.keys():
                seen[(x2,y2)] = 1

    return len(seen.keys())


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())