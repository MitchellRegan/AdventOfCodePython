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
            line = line.replace('\n', '').replace('\t', ' ').split(' ')
            inpt.append([int(x) for x in line])
    return inpt
            

def solution1():
    inpt = getInput()
    
    ans = 0
    for row in inpt:
        ans += max(row) - min(row)

    return ans


def solution2():
    inpt = getInput()
    
    ans = 0
    for row in inpt:
        for i in range(0, len(row)-1):
            for j in range(i+1, len(row)):
                if row[i] % row[j] == 0:
                    ans += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    ans += row[j] // row[i]
    
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())