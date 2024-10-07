aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


class State:
    def __init__(self, id_:str):
        self.id = id_
        self.compVal1 = None
        self.compVal2 = None
        self.writeVal1 = None
        self.writeVal2 = None
        self.moveVal1 = None
        self.moveVal2 = None
        self.continueState1 = None
        self.continueState2 = None
        
    def __str__(self):
        return f"State {self.id}\n\tIf current value = {self.compVal1} write {self.writeVal1} move {self.moveVal1} go to state {self.continueState1}\n\tIf current value = {self.compVal2} write {self.writeVal2} move {self.moveVal2} go to state {self.continueState2}"


def getInput():
    inpt = {} #Value = state ID char, Value = State class
    beginState = None
    steps = None
    
    newState = None
    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            if beginState is None:
                beginState = line[-1][0]
            elif steps is None:
                steps = int(line[-2])
            elif len(line) == 1 and newState is not None:
                inpt[newState.id] = newState
                newState = None
            elif len(line) > 1:
                if line[0] == "In": #Starting a new state
                    newState = State(line[2][0])
                elif line[2] == "If": #Getting the comparisson values
                    if newState.compVal1 is None:
                        newState.compVal1 = int(line[-1].replace(':', ''))
                    else:
                        newState.compVal2 = int(line[-1].replace(':', ''))
                elif line[5] == "Write": #Getting the values to write
                    if newState.writeVal1 is None:
                        newState.writeVal1 = int(line[-1].replace('.', ''))
                    else:
                        newState.writeVal2 = int(line[-1].replace('.', ''))
                elif line[5] == "Move": #Finding the move value
                    moveVal = 1
                    if line[-1] == "left.":
                        moveVal = -1
                    if newState.moveVal1 is None:
                        newState.moveVal1 = moveVal
                    else:
                        newState.moveVal2 = moveVal
                elif line[5] == "Continue": #Finding the next state
                    if newState.continueState1 is None:
                        newState.continueState1 = line[-1][0]
                    else:
                        newState.continueState2 = line[-1][0]

    inpt[newState.id] = newState
    return inpt, beginState, steps
            

def solution1():
    states, curState, steps = getInput()
    posVals = {} #Key = index int, Value = binary value at the index. Defaults to 0
    
    if testing:
        print("Current State:", curState, "    Number of steps:", steps)
        for s in states.keys():
            print(states[s])

    i = 0
    for step in range(steps):
        if i not in posVals.keys():
            posVals[i] = 0
        if posVals[i] == states[curState].compVal1:
            posVals[i] = states[curState].writeVal1
            i += states[curState].moveVal1
            curState = states[curState].continueState1
        else:
            posVals[i] = states[curState].writeVal2
            i += states[curState].moveVal2
            curState = states[curState].continueState2

    ans = 0
    testing and print(posVals)
    for p in posVals.keys():
        if posVals[p] == 1:
            ans += 1
    return ans


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())