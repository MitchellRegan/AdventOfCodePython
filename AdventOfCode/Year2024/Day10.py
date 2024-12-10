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
            inpt.append([int(x) for x in line])

    return inpt
            

def solution1():
    inpt = getInput()
    
    startPoints = []
    for r in range(len(inpt)):
        for c in range(len(inpt[r])):
            if inpt[r][c] == 0:
                startPoints.append((r,c))
    testing and print("Start Points:", startPoints)

    ans = 0
    for sp in startPoints:
        q = [sp] #Each element is (row, col)
        score = 0
        reachedNines = []

        while len(q) > 0:
            r,c = q.pop(0)
            val = inpt[r][c]
            if val == 9 and (r,c) not in reachedNines:
                score += 1
                reachedNines.append((r,c))
            else:
                #Checking up
                if r > 0 and inpt[r-1][c] - val == 1:
                    q.append((r-1,c))
                #Checking down
                if r < len(inpt)-1 and inpt[r+1][c] - val == 1:
                    q.append((r+1,c))
                #Checking left
                if c > 0 and inpt[r][c-1] - val == 1:
                    q.append((r,c-1))
                #Checking right
                if c < len(inpt[r])-1 and inpt[r][c+1] - val == 1:
                    q.append((r,c+1))
        testing and print("Starting Point", sp, "score =", score)
        ans += score
    return ans


def solution2():
    inpt = getInput()
    
    startPoints = []
    for r in range(len(inpt)):
        for c in range(len(inpt[r])):
            if inpt[r][c] == 0:
                startPoints.append((r,c))
    testing and print("Start Points:", startPoints)

    ans = 0
    for sp in startPoints:
        q = [sp] #Each element is (row, col)
        score = 0

        while len(q) > 0:
            r,c = q.pop(0)
            val = inpt[r][c]
            if val == 9:
                score += 1
            else:
                #Checking up
                if r > 0 and inpt[r-1][c] - val == 1:
                    q.append((r-1,c))
                #Checking down
                if r < len(inpt)-1 and inpt[r+1][c] - val == 1:
                    q.append((r+1,c))
                #Checking left
                if c > 0 and inpt[r][c-1] - val == 1:
                    q.append((r,c-1))
                #Checking right
                if c < len(inpt[r])-1 and inpt[r][c+1] - val == 1:
                    q.append((r,c+1))
        testing and print("Starting Point", sp, "score =", score)
        ans += score
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())