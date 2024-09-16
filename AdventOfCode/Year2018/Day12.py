aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    state = ''
    notes = []

    with open(inFile, 'r') as f:
        lineNum = 0
        for line in f:
            line = line.replace('\n', '')
            #First line is initial state
            if lineNum == 0:
                state = line.split(': ')[1]
            #All lines after line 1 (blank) are notes
            elif lineNum > 1:
                notes.append(line.split(" => "))
            lineNum += 1

    return state, notes
            

def solution1():
    state, notes = getInput()
    
    def patternIndexes(n_:str, s_:str)->list:
        '''Finds the CENTER index of each occurrance of the note substring in the state's string.
        Parameters
        ----------
            n_: Note designating a substring to find in the state's string.
            s_: String for the current state to check.
            
        Returns
        ----------
            List of CENTER indeces where each occurrance of the substring was found.
        '''
        foundIndex = []
        for i in range(len(s_) - len(n_)+1):
            if ''.join(s_[i:i+len(n_)]) == n_:
                foundIndex.append(i+2)
        return foundIndex

    #Temporarily adding padding of 3 empty spaces to the front and end of the state to accomodate for growth
    state = "..." + state + "..."
    offset = 3
    testing and print(state, "    0")
    for gen in range(20):
        newState = ['.'] * len(state)
        for n in notes:
            patternInd = patternIndexes(n[0], state)
            for pi in patternInd:
                newState[pi] = n[1]
                
        state = ''.join(newState)
        #Accomodating for future growth if the outside edges aren't filled with 3 empty pots
        if state[0:3] != "...":
            state = "..." + state
            offset += 3
        if state[-3:] != "...":
            state = state + "..."
            
        if testing:
            printState = ''
            if state[offset] == '#':
                printState = state[:offset] + "X" + state[offset+1:]
            else:
                printState = state[:offset] + "_" + state[offset+1:]
                print(printState, "   ", gen+1)
        
    ans = 0
    for i in range(len(state)):
        if state[i] == '#':
            ans += i - offset
    return ans


def solution2():
    inpt = getInput()
    
    return


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())