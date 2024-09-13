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
            line = line.replace('\n', '')
            inpt.append(line)
    return inpt
            

def solution1():
    inpt = getInput()
    
    doubles = 0
    triples = 0
    for box in inpt:
        testing and print(box)
        isDouble = False
        isTriple = False
        for c in box:
            charCount = box.count(c)
            if charCount == 2:
                isDouble = True
            if charCount == 3:
                isTriple = True
        if isDouble:
            doubles += 1
            testing and print("\tIs double")
        if isTriple:
            triples += 1
            testing and print("\tIs triple")

    return doubles * triples


def solution2():
    inpt = getInput()
    
    for i in range(0, len(inpt)-1):
        for j in range(i+1, len(inpt)):
            box1 = inpt[i]
            box2 = inpt[j]
            diff = 0
            badIndex = -1
            for c in range(len(box1)):
                if box1[c] != box2[c]:
                    diff += 1
                    badIndex = c
            if diff == 1:
                testing and print("Boxes", box1, "and", box2, "differ by 1 at index", badIndex)
                return box1[:badIndex] + box1[badIndex+1:]

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())