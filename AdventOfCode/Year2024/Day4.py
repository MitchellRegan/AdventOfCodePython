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
    
    numRow = len(inpt)
    numCol = len(inpt[0])

    ans = 0
    for r in range(numRow):
        for c in range(numCol):
            if inpt[r][c] == 'X':
                #Checking left-to-right
                if numCol - c > 3 and inpt[r][c:c+4] == "XMAS":
                    ans += 1
                    testing and print("Found XMAS --->")
                #Checking right-to-left
                if c > 2 and inpt[r][c-3:c+1] == "SAMX":
                    ans += 1
                    testing and print("Found SAMX <----")
                #Checking top-to-bottom
                if numRow - r > 3 and inpt[r][c] == 'X' and inpt[r+1][c] == 'M' and inpt[r+2][c] == 'A' and inpt[r+3][c] == 'S':
                    ans += 1
                    testing and print("Found XMAS v")
                #Checking bottom-to-top
                if r > 2 and inpt[r][c] == 'X' and inpt[r-1][c] == 'M' and inpt[r-2][c] == 'A' and inpt[r-3][c] == 'S':
                    ans += 1
                    testing and print("Found SAMX ^")
                #Checking diagonal down-right
                if numCol - c > 3 and numRow - r > 3 and inpt[r][c] == 'X' and inpt[r+1][c+1] == 'M' and inpt[r+2][c+2] == 'A' and inpt[r+3][c+3] == 'S':
                    ans += 1
                    testing and print("Found XMAS \\")
                #Checking diagonal up-right
                if numCol - c > 3 and r > 2 and inpt[r][c] == 'X' and inpt[r-1][c+1] == 'M' and inpt[r-2][c+2] == 'A' and inpt[r-3][c+3] == 'S':
                    ans += 1
                    testing and print("Found XMAS /")
                #Checking diagonal down-left
                if c > 2 and r > 2 and inpt[r][c] == 'X' and inpt[r-1][c-1] == 'M' and inpt[r-2][c-2] == 'A' and inpt[r-3][c-3] == 'S':
                    ans += 1
                    testing and print("Found SAMX /")
                #Checking diagonal up-left
                if c > 2 and numRow - r > 3 and inpt[r][c] == 'X' and inpt[r+1][c-1] == 'M' and inpt[r+2][c-2] == 'A' and inpt[r+3][c-3] == 'S':
                    ans += 1
                    testing and print("Found SAMX \\")
    return ans


def solution2():
    inpt = getInput()

    ans = 0
    for r in range(1, len(inpt)-1):
        for c in range(1, len(inpt[0])-1):
            if inpt[r][c] == 'A':
                adj = '' + inpt[r-1][c-1] + inpt[r-1][c+1] + inpt[r+1][c-1] + inpt[r+1][c+1]

                if adj.count("M") == 2 and adj.count("S") == 2 and adj[0] != adj[3]:
                    ans += 1
                    testing and print("r =", r, "   c =", c, "   ", adj)

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())