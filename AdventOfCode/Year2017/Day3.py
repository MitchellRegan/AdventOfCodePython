aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = None

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt = int(line)

    return inpt
            

def solution1():
    inpt = getInput()
    
    ring = 0
    ringNumbers = {1:(0,0)} #Key = number, Val = (x,y) coordinate of the number
    maxVal = 1
    testing and print("Ring level:", ring, "    Max Value:", maxVal)
    while inpt > maxVal:
        testing and print("\tInput", inpt, "> max value", maxVal, "    Increasing to ring level", ring+1)
        newMaxVal = 4 + (4 * ((ring * 2) + 1)) + maxVal
        newNums = [x for x in range(maxVal+1, newMaxVal+1)]
        
        #Helper values to reduce the arbitrary additions and subtractions
        maxXY = ring+1
        minXY = -1 * maxXY
        edgeSize = (ring*2)+1
        
        testing and print("Min/max XY:", minXY, maxXY, "    Edge size:", edgeSize)
        for i in range(len(newNums)):
            #Right column
            if i == 0 or i < ((ring+1) * 2):
                ringNumbers[newNums[i]] = (maxXY, i-ring)
                testing and print("\t\tNum", newNums[i], "position at", ringNumbers[newNums[i]], "    Right")
            #Top row
            elif i < (4 * (ring+1)):
                #ringNumbers[newNums[i]] = (-1 * (i-((ring+1)*2)-ring), maxXY)
                ringNumbers[newNums[i]] = (maxXY - (i-edgeSize), maxXY)
                testing and print("\t\tNum", newNums[i], "position at", ringNumbers[newNums[i]], "    Top")
            #Left column
            elif i < (6 * (ring+1)):
                ringNumbers[newNums[i]] = (minXY, maxXY - (i - (2*edgeSize)-1))
                testing and print("\t\tNum", newNums[i], "position at", ringNumbers[newNums[i]], "    Left")
            #Bottom row
            else:
                ringNumbers[newNums[i]] = (minXY + (i - (3*edgeSize)-2), minXY)
                testing and print("\t\tNum", newNums[i], "position at", ringNumbers[newNums[i]], "    Bottom")
        ring += 1
        maxVal = newMaxVal
        testing and print("Ring level:", ring, "    Max Value:", ringNumbers[ring][-1])
    testing and print("========================================\nInput", inpt, "is on ring", ring)

    return abs(ringNumbers[inpt][0]) + abs(ringNumbers[inpt][1])


def solution2():
    inpt = getInput()
    
    ring = 0
    maxVal = 1
    ringNumbers = {(0,0):1} #Key = (x,y) coordinate of the number, Value = sum of adjacent squares when created
    while True:
        newMaxVal = 4 + (4 * ((ring * 2) + 1)) + maxVal
        newNums = [x for x in range(maxVal+1, newMaxVal+1)]
        
        #Helper values to reduce the arbitrary additions and subtractions
        maxXY = ring+1
        minXY = -1 * maxXY
        edgeSize = (ring*2)+1
        
        for i in range(len(newNums)):
            x = None
            y = None
            #Right column
            if i == 0 or i < ((ring+1) * 2):
                x,y = (maxXY, i-ring)
            #Top row
            elif i < (4 * (ring+1)):
                x,y = (maxXY - (i-edgeSize), maxXY)
            #Left column
            elif i < (6 * (ring+1)):
                x,y = (minXY, maxXY - (i - (2*edgeSize)-1))
            #Bottom row
            else:
                x,y = (minXY + (i - (3*edgeSize)-2), minXY)
                
            val = 0
            for adj in [(x+1,y), (x+1,y+1), (x,y+1), (x-1,y+1), (x-1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]:
                if adj in ringNumbers.keys():
                    val += ringNumbers[adj]
            ringNumbers[(x,y)] = val
            testing and print("\tPos", (x,y), "=", val)
            if val > inpt:
                return val
        ring += 1
        maxVal = newMaxVal

    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())