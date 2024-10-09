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
    
    charCounts = []
    for i in range(len(inpt[0])):
        cci = {}
        charCounts.append(cci)

    for line in inpt:
        testing and print(line)
        for i in range(len(line)):
            c = line[i]
            if c not in charCounts[i].keys():
                charCounts[i][c] = 1
            else:
                charCounts[i][c] += 1
        
    ans = ""
    testing and print(charCounts[0])
    for cc in range(len(charCounts)):
        testing and print("Index", cc, ":", charCounts[cc])
        maxVal = max([charCounts[cc][x] for x in charCounts[cc].keys()])
        testing and print("\tMax Value:", maxVal)
        for k in charCounts[cc].keys():
            if charCounts[cc][k] == maxVal:
                ans = ans + k
                break

    return ans


def solution2():
    inpt = getInput()
    
    charCounts = []
    for i in range(len(inpt[0])):
        cci = {}
        charCounts.append(cci)

    for line in inpt:
        testing and print(line)
        for i in range(len(line)):
            c = line[i]
            if c not in charCounts[i].keys():
                charCounts[i][c] = 1
            else:
                charCounts[i][c] += 1
        
    ans = ""
    testing and print(charCounts[0])
    for cc in range(len(charCounts)):
        testing and print("Index", cc, ":", charCounts[cc])
        minVal = min([charCounts[cc][x] for x in charCounts[cc].keys()])
        testing and print("\tMin Value:", minVal)
        for k in charCounts[cc].keys():
            if charCounts[cc][k] == minVal:
                ans = ans + k
                break

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())