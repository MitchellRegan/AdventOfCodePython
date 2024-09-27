import re
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
    testing and print("Input:", inpt)

    #Removing all '!' chars and the ones that follow
    i = 0
    while i < len(inpt):
        if inpt[i] == '!':
            inpt = inpt[:i] + inpt[i+2:]
        else:
            i += 1
    testing and print("Input after removing !*:", inpt)
    
    #Removing all chars enclosed within garbage markers '<' and '>'
    garbageStartInd = None
    i = 0
    while i < len(inpt):
        if inpt[i] == '<' and garbageStartInd is None:
            garbageStartInd = i
        elif inpt[i] == '>' and garbageStartInd is not None:
            if garbageStartInd == 0:
                inpt = inpt[i+1:]
                i = 0
            else:
                inpt = inpt[:garbageStartInd] + inpt[i+1:]
                i = garbageStartInd
            garbageStartInd = None
        else:
            i += 1
    testing and print("Input after removing <garbage>:", inpt)
    
    #parents = {} #Key = starting index of a group, Value = starting index of the parent node
    stack = deque()
    groups = []
    for i in range(len(inpt)):
        if inpt[i] == '{':
            stack.append(i)
        elif inpt[i] == '}':
            if len(stack) > 0:
                #Each group is (starting index, end index, score before offset)
                groups.append((stack[-1], i, len(stack)))
                stack.pop()
                
    ans = 0
    testing and print("Groups:", len(groups))
    for g in groups:
        testing and print("\tSubGroup:", inpt[g[0]:g[1]+1], "    Score:", g[2]-len(stack))
        ans += g[2]-len(stack)
        
    return ans


def solution2():
    inpt = getInput()
    testing and print("Input:", inpt)

    #Removing all '!' chars and the ones that follow
    i = 0
    while i < len(inpt):
        if inpt[i] == '!':
            inpt = inpt[:i] + inpt[i+2:]
        else:
            i += 1
    testing and print("Input after removing !*:", inpt)
    
    #Removing all chars enclosed within garbage markers '<' and '>'
    garbageStartInd = None
    i = 0
    ans = 0
    while i < len(inpt):
        if inpt[i] == '<' and garbageStartInd is None:
            garbageStartInd = i
        elif inpt[i] == '>' and garbageStartInd is not None:
            ans += i - garbageStartInd - 1
            if garbageStartInd == 0:
                inpt = inpt[i+1:]
                i = 0
            else:
                inpt = inpt[:garbageStartInd] + inpt[i+1:]
                i = garbageStartInd
            garbageStartInd = None
        else:
            i += 1
    testing and print("Input after removing <garbage>:", inpt)
    
    return ans


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
# 6681 too low