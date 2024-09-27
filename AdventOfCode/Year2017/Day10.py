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
            line = line.replace('\n', '').split(',')
            inpt = [int(x) for x in line]

    return inpt
            

def solution1():
    inpt = getInput()
    
    currIndex = 0
    skipSize = 0
    numberRope = [x for x in range(256)]
    if testing:
        numberRope = [0,1,2,3,4]
        
    for ropeLen in inpt:
        testing and print("\nRope:", numberRope, "    Current Index:", currIndex, "    Rope Length:", ropeLen, "    Skip Size:", skipSize)
        #If the length of rope is 1, there's no point in reversing the numbers because it's the same
        if ropeLen != 1:
            revNums = []
            if currIndex + ropeLen >= len(numberRope):
                revNums = numberRope[currIndex:]
                revNums.extend(numberRope[:currIndex+ropeLen-len(numberRope)])
            else:
                revNums = numberRope[currIndex:currIndex+ropeLen]
            testing and print("\tNumbers to reverse:", revNums)
            revNums.reverse()
        
            for i in range(ropeLen):
                if currIndex + i >= len(numberRope):
                    numberRope[currIndex+i-len(numberRope)] = revNums[i]
                else:
                    numberRope[currIndex+i] = revNums[i]
                
        testing and print("\t\tMoving currIndex forward", ropeLen + skipSize)
        currIndex += ropeLen + skipSize
        while currIndex >= len(numberRope):
            currIndex -= len(numberRope)
        skipSize += 1

    testing and print("Final Rope:", numberRope)
    return numberRope[0] * numberRope[1]


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())