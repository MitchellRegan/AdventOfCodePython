aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').replace("pos=<", '').replace('>', '').replace(" r=", '').split(',')
            inpt.append([int(x) for x in line])

    return inpt
            

def solution1():
    bots = getInput()
    
    #Sorting the bots so that the ones with the highest signal strength is at the top
    bots.sort(key=lambda x: x[3], reverse=True)
    bestBot = bots[0]
    
    #Finding all bots within range (by manhattan distance) of the best bot's signal
    inRange = 0
    for b in bots:
        manDist = abs(b[0] - bestBot[0]) + abs(b[1] - bestBot[1]) + abs(b[2] - bestBot[2])
        if manDist <= bestBot[3]:
            inRange += 1
            testing and print("\tBot", b, "dist:", manDist, "    IN RANGE. Total count:", inRange)
        else:
            testing and print("\tBot", b, "dist:", manDist, "    NOT in range")

    return inRange


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
#156 too low
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())