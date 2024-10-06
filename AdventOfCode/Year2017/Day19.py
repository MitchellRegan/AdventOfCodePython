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
    
    if testing:
        for line in inpt:
            print(line)
            
    pos = None
    for c in range(0, len(inpt[0])):
        if inpt[0][c] == '|':
            pos = [0,c, 'v'] #Row, Col, Direction
            break
    testing and print("Starting pos:", pos)
    
    seen = {}
    ans = ""
    while True:
        r,c,d = pos
        seen[(r,c)] = True
        testing and print(pos, "    ", inpt[r][c])
        if inpt[r][c] == ' ':
            break
        if inpt[r][c] not in ['-', '|', '+']:
            ans = ans + inpt[r][c]

        nextPos = None
        if inpt[r][c] is not '+':
            if d == 'v':
                nextPos = [r+1,c,d]
            elif d == '^':
                nextPos = [r-1,c,d]
            elif d == '<':
                nextPos = [r,c-1,d]
            elif d == '>':
                nextPos = [r,c+1,d]
        else:
            for adj in [(r+1,c, 'v'), (r-1,c, '^'), (r,c+1, '>'), (r,c-1, '<')]:
                if (adj[0],adj[1]) not in seen.keys() and inpt[adj[0]][adj[1]] != ' ':
                    nextPos = adj
                    
        pos = nextPos

    return ans


def solution2():
    inpt = getInput()
    
    if testing:
        for line in inpt:
            print(line)
            
    pos = None
    for c in range(0, len(inpt[0])):
        if inpt[0][c] == '|':
            pos = [0,c, 'v'] #Row, Col, Direction
            break
    testing and print("Starting pos:", pos)
    
    seen = {}
    ans = 0
    while True:
        r,c,d = pos
        if inpt[r][c] == ' ':
            break
        seen[(r,c)] = True

        nextPos = None
        if inpt[r][c] is not '+':
            if d == 'v':
                nextPos = [r+1,c,d]
            elif d == '^':
                nextPos = [r-1,c,d]
            elif d == '<':
                nextPos = [r,c-1,d]
            elif d == '>':
                nextPos = [r,c+1,d]
        else:
            for adj in [(r+1,c, 'v'), (r-1,c, '^'), (r,c+1, '>'), (r,c-1, '<')]:
                if (adj[0],adj[1]) not in seen.keys() and inpt[adj[0]][adj[1]] != ' ':
                    nextPos = adj
                    
        pos = nextPos
        ans += 1

    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())