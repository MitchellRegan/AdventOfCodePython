aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt = int(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    ring = 0
    ringNumbers = [[1]]
    testing and print("Ring level:", ring, "    Max Value:", ringNumbers[ring][-1])
    while inpt > ringNumbers[-1][-1]:
        testing and print("\t", inpt, ">", ringNumbers[ring][-1], "    Increasing ring")
        maxVal = 4 + (4 * ((ring * 2) + 1)) + ringNumbers[ring][-1]
        ringNumbers.append([x for x in range(ringNumbers[ring][-1] + 1, maxVal + 1)])
        ring += 1
        testing and print("Ring level:", ring, "    Max Value:", ringNumbers[ring][-1])
    testing and print("\t\tInput is on ring", ring, "\n", ringNumbers[ring])

    return


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())