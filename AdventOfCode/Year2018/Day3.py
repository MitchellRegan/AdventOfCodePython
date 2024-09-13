aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}

    with open(inFile, 'r') as f:
        lineNum = 1
        for line in f:
            line = line.replace('\n', '')
            pos = line.split(' @ ')[1].split(': ')[0].split(',')
            dim = line.split(': ')[1].split('x')
            inpt[lineNum] = [int(pos[0]), int(pos[1]), int(dim[0]), int(dim[1])]
            lineNum += 1
    return inpt
            

def solution1():
    inpt = getInput()
    seenPos = {}
    
    for x in inpt.keys():
        testing and print(x, ":", inpt[x])
        xOffset, yOffset, width, height = inpt[x]
        for x in range(width):
            for y in range(height):
                pos = (x + xOffset, y + yOffset)
                if pos in seenPos.keys():
                    seenPos[pos] += 1
                else:
                    seenPos[pos] = 1

    ans = 0
    for pos in seenPos.keys():
        if seenPos[pos] > 1:
            ans += 1
            testing and print("\tPos", pos, "has", seenPos[pos], "overlaps")
    return ans


def solution2():
    inpt = getInput()
    seenPos = {}
    
    for claim in inpt.keys():
        testing and print(claim, ":", inpt[claim])
        xOffset, yOffset, width, height = inpt[claim]
        for x in range(width):
            for y in range(height):
                pos = (x + xOffset, y + yOffset)
                if pos in seenPos.keys():
                    seenPos[pos] += 1
                else:
                    seenPos[pos] = 1
                    
    #Looking for the ID number of the input that doesn't overlap with any other input
    for claim in inpt.keys():
        testing and print("Checking claim", claim)
        overlaps = False
        xOffset, yOffset, width, height = inpt[claim]
        for x in range(width):
            for y in range(height):
                pos = (x + xOffset, y + yOffset)
                if seenPos[pos] > 1:
                    testing and print("\t", pos, "seen", seenPos[pos], "times")
                    overlaps = True
                    break
            if overlaps:
                break

        if not overlaps:
            return claim
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())