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
        newGrid = []
        for line in f:
            line = line.replace('\n', '')

            if line == '':
                inpt.append(newGrid)
                newGrid = []
            else:
                newGrid.append(line)
        inpt.append(newGrid)

    return inpt
            

def solution1():
    inpt = getInput()
    
    keys = []
    locks = []
    for grid in inpt:
        isKey = False
        #If the top row of the grid is empty, it's a key
        if grid[0] == ".....":
            isKey = True
        
        pins0 = [x[0] for x in grid].count('#') - 1
        pins1 = [x[1] for x in grid].count('#') - 1
        pins2 = [x[2] for x in grid].count('#') - 1
        pins3 = [x[3] for x in grid].count('#') - 1
        pins4 = [x[4] for x in grid].count('#') - 1

        if isKey:
            keys.append((pins0, pins1, pins2, pins3, pins4))
        else:
            locks.append((pins0, pins1, pins2, pins3, pins4))

    testing and print("Keys:", keys)
    testing and print("Locks:", locks)

    ans = 0
    for k in keys:
        for l in locks:
            p0 = k[0] + l[0]
            p1 = k[1] + l[1]
            p2 = k[2] + l[2]
            p3 = k[3] + l[3]
            p4 = k[4] + l[4]

            if p0 < 6 and p1 < 6 and p2 < 6 and p3 < 6 and p4 < 6:
                ans += 1
                testing and print("\tKey", k, "fits with lock", l)
    return ans 


def solution2():
    inpt = getInput()



    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())