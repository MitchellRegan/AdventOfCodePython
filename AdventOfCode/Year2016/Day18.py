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
    inpt = [getInput()]
    numRows = 40
    if testing:
        numRows = 10

    ans = inpt[0].count('.')
    testing and print(inpt[0], "    Safe tiles:", ans)
    for r in range(1, numRows):
        newRow = ['.'] * len(inpt[0])
        for c in range(len(newRow)):
            left = False
            center = (inpt[r-1][c] == '^')
            right = False
            
            if c != 0:
                left = (inpt[r-1][c-1] == '^')
            if c != len(newRow)-1:
                right = (inpt[r-1][c+1] == '^')
                
            if left and center and not right:
                newRow[c] = '^'
            elif center and right and not left:
                newRow[c] = '^'
            elif left and not center and not right:
                newRow[c] = '^'
            elif right and not center and not left:
                newRow[c] = '^'
        inpt.append(''.join(newRow))
        ans += newRow.count('.')
        testing and print(inpt[-1], "    Safe tiles:", inpt[-1].count('.'))

    return ans


def solution2_v1():
    inpt = [getInput()]
    numRows = 400000

    ans = inpt[0].count('.')
    for r in range(1, numRows):
        newRow = ['.'] * len(inpt[0])
        for c in range(len(newRow)):
            left = False
            center = (inpt[r-1][c] == '^')
            right = False
            
            if c != 0:
                left = (inpt[r-1][c-1] == '^')
            if c != len(newRow)-1:
                right = (inpt[r-1][c+1] == '^')
                
            if left and center and not right:
                newRow[c] = '^'
            elif center and right and not left:
                newRow[c] = '^'
            elif left and not center and not right:
                newRow[c] = '^'
            elif right and not center and not left:
                newRow[c] = '^'
        inpt.append(''.join(newRow))
        ans += newRow.count('.')

    return ans


def solution2():
    inpt = getInput()
    inpt = [(x=='^') for x in inpt]
    newRow = [False for x in inpt]

    ans = inpt.count(False)
    for r in range(400000-1):
        for c in range(len(newRow)):
            left = False
            center = inpt[c]
            right = False
            
            if c != 0:
                left = inpt[c-1]
            if c != len(newRow)-1:
                right = inpt[c+1]
                
            if (left and center and not right) or \
                (center and right and not left) or \
                (left and not center and not right) or \
                (right and not center and not left):
                newRow[c] = True
            else:
                ans += 1
                newRow[c] = False
                
        for c in range(len(newRow)):
            inpt[c] = newRow[c]

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())