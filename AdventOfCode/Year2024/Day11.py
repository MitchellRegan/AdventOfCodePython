aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"

import math
import sys
sys.path.append("..")
from HelperFunctions.linkedList import LLNode


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

    #Converting the initial list of stones to a linked list
    head = LLNode(stones[0])
    p = head
    for i in range(1, len(stones)):
        newNode = LLNode(stones[i])
        p.setNext(newNode)
        p = newNode

    ans = len(stones)
        
    print("Blink", 0, "    num stones:", ans)
    blinkNum = 75
    if testing:
        blinkNum = 15
    for blink in range(blinkNum):
        testing and print("\nBlink #", blink)
        ptr = head
        while ptr is not None:
            if ptr.data == 0:
                ptr.data = 1
                testing and print(ptr.data, '', end='')
                ptr = ptr.getNext()

            elif getNumDigits(ptr.data) % 2 == 0:
                numDigits = getNumDigits(ptr.data)//2
                s1 = int(str(ptr.data)[:numDigits])
                s2 = int(str(ptr.data)[numDigits:])
                ptr.data = s1
                newNode = LLNode(s2)
                newNode.setNext(ptr.getNext())
                ptr.setNext(newNode)
                testing and print(ptr.data, ptr.getNext().data, '', end='')
                ptr = newNode.getNext()
                ans += 1

            else:
                ptr.data = ptr.data * 2024
                testing and print(ptr.data, '', end='')
                ptr = ptr.getNext()

        testing and print()
        print("Blink", blink+1, "    num stones:", ans)


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
        

    return ans


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())