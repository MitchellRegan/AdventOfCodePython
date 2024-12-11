aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"

import math

def getInput():
    inpt = []

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            inpt = [int(x) for x in line]
    return inpt


def getNumDigits(n_:int)->int:
    '''Helper function to find the number of digits in a given int.'''
    return int(math.log10(n_)) + 1
            

def solution1():
    stones = getInput()

    blinkNum = 25
    if testing:
        blinkNum = 6
    
    for blink in range(blinkNum):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif getNumDigits(stones[i]) % 2 == 0:
                numDigits = getNumDigits(stones[i])//2
                s1 = int(str(stones[i])[:numDigits])
                s2 = int(str(stones[i])[numDigits:])
                stones[i] = s1
                stones.insert(i+1, s2)
                i += 2
            else:
                stones[i] *= 2024
                i += 1

    return len(stones)


def solution2():
    stones = getInput()

    #Pattern problem where numbers seem to be breaking down into reoccurring, smaller numbers
    #   Ex: 0 -> 1 -> 2024 -> 2,0,2,4 which then contains another 0
    #Each individual number can be evaluated on its own and then added to the final sum, since they don't interact together
    #If you can find out the total number of children an individual number spawns, you can condense the process
    #   Ex: Make a dictionary of known values
    #       key = (base element number, t for the blink number)
    #       value is an int for the total children spawned by t = 75
    #           This value could also be a string for a formula, like (0,1) = (0,2) + 1 indicating that key (0,2) has 1
    #           more child than key (0,1), so if the value of (0,1) isn't known yet, we can figure it out later.
    # Then make a recursive function to figure out these (element, t) values. Each value found speeds up future recursions
        
    shortcut = {}#key = (stone value, t), value = number of children spawned by this stone value
    def decayStone(s_:int, t_:int)->int:
        '''Recursive function to decay each stone until the end of the time limit and count how many there are.'''
        
        #Recursion break when time is up
        if t_ == 0:
            testing and print("Decay", s_, "t =", t_)
            return 1

        if (s_,t_) in shortcut.keys():
            testing and print("Decay", s_, "t =", t_, "  ", shortcut[(s_,t_)], "children")
            return shortcut[(s_,t_)]

        #Stones with a value of 0 decay to a value of 1
        if s_ == 0:
            numChildren = decayStone(1, t_-1)
            shortcut[(0,t_)] = numChildren
            return numChildren

        #Stones with an even number of digits split into 2 stones with even number of digits
        if getNumDigits(s_) % 2 == 0:
            numDigits = getNumDigits(s_)//2
            s1 = int(str(s_)[:numDigits])
            s2 = int(str(s_)[numDigits:])

            numChildren = decayStone(s1,t_-1) + decayStone(s2,t_-1)
            shortcut[(s_,t_)] = numChildren
            return numChildren

        #Stones that don't match the other criteria are multiplied by 2024
        numChildren = decayStone(s_*2024, t_-1)
        shortcut[(s_,t_)] = numChildren
        return numChildren

    ans = 0
    numBlinks = 75
    if testing:
        numBlinks = 25
    for stone in stones:
        ans += decayStone(stone, numBlinks)
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())