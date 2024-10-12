import sys
sys.path.append("..")
from HelperFunctions.linkedList import LLNode
aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    inpt = 0

    with open(inFile, 'r') as f:
        for line in f:
            inpt = int(line.replace('\n', ''))

    return inpt
            

def solution1():
    inpt = getInput()
    
    elves = {}#Key = int for elf number, Value = (number of presents the elf has, int for next elf)
    for i in range(1, inpt+1):
        elves[i] = [1, i+1]
    elves[inpt][1] = 1
        
    ce = 1 #Number for the current elf who's turn it is
    while len(elves.keys()) > 1:
        testing and print("Current elf:", ce, "    State:", elves)
        nextElf = elves[ce][1]
        elves[ce][0] += elves[nextElf][0]
        elves[ce][1] = elves[nextElf][1]
        elves.pop(nextElf)
        ce = elves[ce][1]
        
    testing and print("Current elf:", ce, "    State:", elves)
    for k in elves.keys():
        return k


def solution2():
    inpt = getInput()
    
    print("============================\n\tPATTERN RECOGNITION\n=============================")

    elves = [x+1 for x in range(inpt)]
    testing and print("Starting elves:", elves)
    
    i = 0
    while inpt > 1:
        if inpt % 100 == 0:
            print(inpt)
        testing and print(elves)
        opposite = (i + (inpt//2)) % inpt
        testing and print("\ti =", i, "\n\to =", opposite, "\n\tElf:", elves[opposite], '\n')
        #elves.pop(opposite)
        for x in range(opposite, inpt-1):
            elves[x] = elves[x+1]
        elves[inpt-1] = None
        inpt -= 1

        i += 1
        if i > inpt:
            #i -= len(elves)
            i = 0

    return elves[0]


def solution2_v2():
    inpt = getInput()
    
    ptr = LLNode(1)
    startNode = ptr
    for n in range(2, inpt+1):
        newNode = LLNode(n, ptr)
        ptr.setNext(newNode)
        ptr = newNode
    ptr.setNext(startNode)
    startNode.setPrev(ptr)
    ptr = startNode
    
    while inpt > 1:
        #testing and print("Current Node:", ptr.data)
        if inpt % 1000 == 0:
            print(inpt)
        rn = ptr
        for s in range(inpt//2):
            rn = rn.getNext()
            #testing and print("\tStep", s+1, "    RN:", rn.data)
        #testing and print("\t\tRemoving", rn.data)
        rn.getPrev().setNext(rn.getNext())
        rn.getNext().setPrev(rn.getPrev())
        del rn

        ptr = ptr.getNext()
        inpt -= 1

    return ptr.data


#print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#6437 too low