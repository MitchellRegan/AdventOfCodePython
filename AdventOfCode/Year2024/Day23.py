aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = {}

    with open(inFile, 'r') as f:
        for line in f:
            c1,c2 = line.replace('\n', '').split('-')

            if c1 not in inpt.keys():
                inpt[c1] = []
            inpt[c1].append(c2)
            if c2 not in inpt.keys():
                inpt[c2] = []
            inpt[c2].append(c1)

    for k in inpt.keys():
        inpt[k].sort()

    return inpt
            

def solution1():
    cmap = getInput()
    
    ans = 0
    setsOfThree = []
    for c in cmap.keys():
        testing and print(c, ":", cmap[c])
        for i in range(len(cmap[c])-1):
            for j in range(i+1, len(cmap[c])):
                if cmap[c][i] in cmap[cmap[c][j]]:
                    compGroup = [c, cmap[c][i], cmap[c][j]]
                    compGroup.sort()
                    if compGroup not in setsOfThree:
                        setsOfThree.append(compGroup)
                        testing and print("\t", compGroup)
                        #If any of the computers in this group have a name that begins with 't' it's added to our final answer
                        if compGroup[0][0] == 't' or compGroup[1][0] == 't' or compGroup[2][0] == 't':
                            ans += 1

    return ans


def solution2():
    cmap = getInput()
    
    ans = 0
    setsOfThree = []
    for c in cmap.keys():
        print(c, ":", cmap[c])
        #Checking every computer in this list against every other computer
        mostConnections = 0
        for i in range(len(cmap[c])):
            numConnections = 1
            for j in range(len(cmap[c])):
                if i != j and cmap[c][j] in cmap[cmap[c][i]]:
                    numConnections += 1
                    print("\t", cmap[c][i], "connected to", cmap[c][j])
            print("\t------------------")
            if numConnections > mostConnections:
                mostConnections = numConnections
        print("\t\tNum connections:", mostConnections)

    return


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())