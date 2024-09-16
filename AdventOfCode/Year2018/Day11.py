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


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())