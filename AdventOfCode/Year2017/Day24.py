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
            line = line.replace('\n', '').split('/')
            inpt.append((int(line[0]), int(line[1])))

    return inpt
            

def solution1():
    inpt = getInput()
    pinVals = {}
    for p in inpt:
        v1,v2 = p
        if v1 not in pinVals.keys():
            pinVals[v1] = [p]
        else:
            pinVals[v1].append(p)
        if v2 not in pinVals.keys():
            pinVals[v2] = [p]
        elif v2 !=  v1:
            pinVals[v2].append(p)
            
    def rGetNextPin(curPins_:list, nextPinNum_:int, curScore_:int):
        testing and print(curPins_, "    Next Pin:", nextPinNum_, "    Score:", curScore_)
        bestScore = curScore_
        for p in pinVals[nextPinNum_]:
            if p not in curPins_:
                newPinList = [x for x in curPins_]
                newPinList.append(p)
                newNextPin = [x for x in p]
                newNextPin.remove(nextPinNum_)
                newCurScore = curScore_ + sum(p)
                bestScore = max(bestScore, rGetNextPin(newPinList, newNextPin[0], newCurScore))
        return bestScore

    ans = 0
    for p in pinVals[0]:
        #testing and print("Starting with", p)
        nextPin = [x for x in p]
        nextPin.remove(0)
        #testing and print("\tNext pin:", nextPin[0])
        ans = max(ans, rGetNextPin([p], nextPin[0], sum(p)))

    return ans


def solution2():
    inpt = getInput()
    pinVals = {}
    for p in inpt:
        v1,v2 = p
        if v1 not in pinVals.keys():
            pinVals[v1] = [p]
        else:
            pinVals[v1].append(p)
        if v2 not in pinVals.keys():
            pinVals[v2] = [p]
        elif v2 !=  v1:
            pinVals[v2].append(p)
            
    def rGetNextPin(curPins_:list, nextPinNum_:int, curScore_:int):
        testing and print(curPins_, "    Next Pin:", nextPinNum_, "    Score:", curScore_)
        bestLen = len(curPins_)
        bestScore = curScore_
        for p in pinVals[nextPinNum_]:
            if p not in curPins_:
                newPinList = [x for x in curPins_]
                newPinList.append(p)
                newNextPin = [x for x in p]
                newNextPin.remove(nextPinNum_)
                newCurScore = curScore_ + sum(p)
                s,l = rGetNextPin(newPinList, newNextPin[0], newCurScore)
                if l > bestLen:
                    bestLen = l
                    bestScore = s
                elif l == bestLen and s > bestScore:
                    bestScore = s
        return bestScore, bestLen

    bestLen = 0
    bestScore = 0
    for p in pinVals[0]:
        nextPin = [x for x in p]
        nextPin.remove(0)
        s,l = rGetNextPin([p], nextPin[0], sum(p))
        if l > bestLen:
            bestLen = l
            bestScore = s
        elif l == bestLen and s > bestScore:
            bestScore = s
        testing and print(p,"---------- Best Length:", bestLen, "    Best Score:", bestScore)

    return bestScore


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())