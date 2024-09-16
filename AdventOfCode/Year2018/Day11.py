aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    serialNum = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            serialNum = int(line)
    return serialNum
            

def solution1():
    serialNum = getInput()
    
    def getPower(x_:int, y_:int, s_:int)->int:
        rackID = x_ + 10
        powerLevel = rackID * y_
        powerLevel += s_
        powerLevel *= rackID
        powerLevel = (powerLevel // 100) % 10
        powerLevel -= 5
        return powerLevel

    posPower = {} #Key is (x,y) pos, value is power level
    mostPower = 0
    bestPos = None
    for x in range(1, 298):
        for y in range(1, 298):
            totalPower = 0
            for pos in [(x,y), (x+1,y), (x+2,y), (x,y+1), (x+1,y+1), (x+2,y+1), (x,y+2), (x+1,y+2), (x+2,y+2)]:
                if pos not in posPower.keys():
                    posPower[pos] = getPower(pos[0], pos[1], serialNum)
                totalPower += posPower[pos]
            if totalPower > mostPower:
                mostPower = totalPower
                bestPos = (x,y)
    return bestPos


def solution2():
    serialNum = getInput()
    
    def getPower(x_:int, y_:int, s_:int)->int:
        rackID = x_ + 10
        powerLevel = rackID * y_
        powerLevel += s_
        powerLevel *= rackID
        powerLevel = (powerLevel // 100) % 10
        powerLevel -= 5
        return powerLevel

    #Creating the 300x300 grid of power values for every (x,y) coordinate
    powerGrid = []
    for r in range(1,301):
        newRow = []
        for c in range(1,301):
            newRow.append(getPower(c,r,serialNum))
        powerGrid.append(newRow)

    if testing:
        for r in range(4):
            print(powerGrid[r][:4])
        print()

    mostPower = 0
    bestPos = None
    for r in range(300):
        testing and print("Row =", r+1, "/ 300")
        for c in range(300):
            #testing and print("\tCol =", c+1, "/ 300")
            totalPower = 0
            for size in range(min(300-r, 300-c)):
                #testing and print("\t\tSize =", size+1, "/", min(300-r, 300-c)+1)
                if size == 0:
                    totalPower = powerGrid[r][c]
                    #testing and print("\t\t\tStarting power of 1x1 square:", totalPower)
                else:
                    #Getting the power from the next column to the right
                    for nr in range(0,size):
                        totalPower += powerGrid[r+nr][c+size]
                        #testing and print("\t\t\tAdding value at pos", r+nr, c+size, ":", powerGrid[r+nr][c+size])
                    
                    #Getting the power from the next row down
                    totalPower += sum(powerGrid[r+size][c:c+1+size])
                    #testing and print("\t\t\tAdding sum of row:", powerGrid[r+size][c:c+1+size])
                if totalPower > mostPower:
                    mostPower = totalPower
                    bestPos = (c+1,r+1,size+1)
                #testing and print("\t\t\t==== Total power:", totalPower)
                #if size == 3:
                #    return
    return str(bestPos[0]) + ',' + str(bestPos[1]) + ',' + str(bestPos[2])


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())