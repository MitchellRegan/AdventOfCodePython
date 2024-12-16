aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 1
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"

from collections import deque

def getInput():
    inpt = ""

    with open(inFile, 'r') as f:
        for line in f:
            inpt = line.replace('\n', '')

    return inpt
            

def solution1():
    inpt = getInput()
    
    testing and print(inpt)
    i = 0
    while i < len(inpt):
        if inpt[i] == '(':
            x = i+1
            while inpt[x] != 'x':
                x += 1
            end = x+2
            while inpt[end] != ')':
                end += 1
            
            numChar = int(inpt[i+1:x])
            amt = int(inpt[x+1:end])
            substr = inpt[end+1:end+1+numChar]
            fullDupe = ""
            for a in range(amt-1):
                fullDupe = fullDupe + substr
                
            inpt = inpt[:i] + fullDupe + inpt[end+1:]
            i += numChar * amt
        else:
            i += 1

    return len(inpt)


def solution2():
    inpt = getInput()
    instructionStack = deque()
    
    isLetters = inpt[0] == '('
    curGroup = ""
    #Iterating through the input string to segment it by instruction
    i = 0
    while i < len(inpt):
        #When we find a decompressor string in the format of (# of chars, # of times multiplied)
        if inpt[i] == '(':
            #Any normal strings found prior to this decompressor are added to the stack first
            if curGroup != "":
                instructionStack.append(len(curGroup))
                curGroup = ""

            #Getting the index range for the decompressor
            x = i+1
            while inpt[x] != 'x':
                x += 1
            end = x+2
            while inpt[end] != ')':
                end += 1

            #Each decompressor string indicates the number of chars to decompress, and the amount of times the chars are copied
            originalLen = len(inpt[i:end+1])
            numChar = int(inpt[i+1:x])
            amt = int(inpt[x+1:end])
            instructionStack.append([originalLen, numChar, amt])
            #instructionStack.append(inpt[i:end+1])
            i = end+1
        #When we find a char in a normal string, we add it to the current group of chars
        else:
            curGroup = curGroup + inpt[i]
            i += 1

    #Cleaning up any remaining normal string and adding it to the stack
    if len(curGroup) > 0:
        instructionStack.append(len(curGroup))

    testing and print(instructionStack)

    #Working through the stack from left-to-right
    ans = 0
    while len(instructionStack) > 0:
        ins = instructionStack.popleft()
        testing and print("\t", ins)

        #Normal strings just have their length added to our total
        if type(ins) is int:
            testing and print("\t\tAdding to current total:", ans, "+", ins, "=", ans+ins)
            ans += ins
        #Decompressor strings recursively duplicate some strings in front of them (including other decompressors)
        else:
            testing and print("\t\tPerforming recursive decompression")
            originalLen, numChar, amt = ins
            testing and print("\t\t- Original Length:", originalLen, "\n\t\t- Num Char:", numChar, "\n\t\t- Amt:", amt)

            subQue = deque()
            while numChar > 0:
                nextIns = instructionStack.popleft()
                if type(nextIns) is int:
                    if nextIns <= numChar:
                        numChar -= nextIns
                        subQue.append(nextIns)
                    else:
                        nextIns -= numChar
                        subQue.append(numChar)
                        numChar = 0
                        instructionStack.appendleft(nextIns)
                else:
                    numChar -= nextIns[0]
                    nextIns[2] = nextIns[2] * amt
                    subQue.append(nextIns)
            testing and print("\t\t- Sub Que:", subQue)
            
            for i in range(len(subQue)-1, -1, -1):
                instructionStack.appendleft(subQue[i])
            testing and print("\t\t\t", instructionStack)
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())