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
            line = line.replace('\n', '').split(": ")
            inpt.append((int(line[0]), int(line[1])))
    return inpt
            

def solution1():
    inpt = getInput()
    layers = {}#Key = layer depth #, Value = [Max range, current scanner index, and Bool for if the scanner is moving down (T) or up (F)]
    for l in inpt:
        layers[l[0]] = [l[1], 0, True]
    
    curLayer = 0
    ans = 0
    sec = 0
    while curLayer < max(layers.keys()) + 1:
        testing and print("Time:", sec, "    Current layer:", curLayer)
        #If this layer has a scanner and the scanner is at index 0 (our current position), the severity increases by depth x range
        if curLayer in layers.keys() and layers[curLayer][1] == 0:
            testing and print("\tCollision. Severity +", curLayer * layers[curLayer][0])
            ans += curLayer * layers[curLayer][0]
            
        curLayer += 1

        #Updating every layers' scanner by 1 step
        for k in layers.keys():
            #Moving the scanner down 1
            if layers[k][2] is True:
                layers[k][1] += 1
                #If it reaches the bottom, the direction reverses
                if layers[k][1] == layers[k][0] - 1:
                    layers[k][2] = False
            #Moving up 1
            else:
                layers[k][1] -= 1
                if layers[k][1] == 0:
                    layers[k][2] = True
        sec += 1

    return ans


def solution2():
    inpt = getInput()
    
    offset = 0 #delay before starting the next run
    while True:
        testing and print("\nTesting delay", offset, "__________________________")
        wasCaught = False

        for i in inpt:
            layer, depth = i
            testing and print("\tChecking layer", layer, "depth", depth)
            if (layer + offset) % (depth + depth - 2) == 0:
                testing and print("\t\tCaught")
                wasCaught = True
                break

        if wasCaught:
            offset += 1
        else:
            return offset
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())