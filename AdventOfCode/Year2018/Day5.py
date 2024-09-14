from collections import deque
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = ""

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            inpt = line
    return inpt
            

def solution1():
    inpt = getInput()
    
    stack = deque()
    stack.append(inpt[0])
    testing and print("Input:", inpt, "\nStack:", stack)
    for i in range(1, len(inpt)):
        #If stack is empty, nothing to compare
        if len(stack) == 0:
            stack.append(inpt[i])
            continue
        
        cur = inpt[i]
        prev = stack[-1]
        testing and print("\tIndex:", i, "    Prev: ", prev, "    Cur:", cur)
        #If the current letter is upper-case and the previous letter is lower-case
        if ord(cur) <= 90 and ord(prev) >=  97 and ord(cur) == ord(prev)-32:
            testing and print("\t\tSame letter. Destroying")
            stack.pop()
        #If the current letter is lower-case and the previous letter is upper-case
        elif ord(cur) >= 97 and ord(prev) <= 90 and ord(cur)-32 == ord(prev):
            testing and print("\t\tSame letter. Destroying")
            stack.pop()
        #No match, so adding it to the stack
        else:
            stack.append(inpt[i])

    return len(stack)


def solution2():
    inpt = getInput()
    
    #Iterating through all letters in the alphabet to see which one works best when removed
    bestLetter = None
    bestSize = None
    for letter in "abcdefghijklmnopqrstuvwxyz":
        upperLetter = chr(ord(letter)-32)
        #If the letter isn't in the input, we ignore it completely
        if letter not in inpt:
            continue

        newInpt = [x for x in inpt if x != letter and x != upperLetter]
        testing and print("Input after removing", letter, "/", upperLetter, ":", newInpt)
        stack = deque()
        stack.append(newInpt[0])
    
        for i in range(1, len(newInpt)):
            #If stack is empty, nothing to compare
            if len(stack) == 0:
                stack.append(newInpt[i])
                continue
        
            cur = newInpt[i]
            prev = stack[-1]
        
            #If the current letter is upper-case and the previous letter is lower-case
            if ord(cur) <= 90 and ord(prev) >=  97 and ord(cur) == ord(prev)-32:
                stack.pop()
            #If the current letter is lower-case and the previous letter is upper-case
            elif ord(cur) >= 97 and ord(prev) <= 90 and ord(cur)-32 == ord(prev):
                stack.pop()
            #No match, so adding it to the stack
            else:
                stack.append(newInpt[i])
                
        testing and print("\tFinal stack:", stack)
        if bestSize is None or bestSize > len(stack):
            bestSize = len(stack)
            bestLetter = letter
    
    testing and print("Removing letter", bestLetter, "gives stack size", bestSize)
    return bestSize


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())