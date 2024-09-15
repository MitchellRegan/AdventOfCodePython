import sys
sys.path.append("..")
from HelperFunctions.linkedList import LinkedList, LLNode

aocDate = [__file__.split('\\')[-2][4:], __file__.split('\\')[-1][3:-3]]
inFile = ""
testing = 0
if testing:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputTestFiles/d" + aocDate[1] + "_test.txt"
else:
    inFile = '/'.join(__file__.split('\\')[:-1]) + "/InputRealFiles/d" + aocDate[1] + "_real.txt"


def getInput():
    numPlayers = 0
    lastPoints = 0

    with open(inFile, 'r') as f:
        for line in f:
            line = line.replace('\n', '').split(' ')
            numPlayers = int(line[0])
            lastPoints = int(line[6])
    return numPlayers, lastPoints
            

def solution1():
    numPlayers, lastPoints = getInput()
    
    scores = {}
    for i in range(numPlayers):
        scores[i+1] = 0
        
    marbles = [0] #list to store the order of each marble number
    player = 1 #current player's ID number
    prevIndex = 0
    for m in range(1,lastPoints+1):

        if m % 23 == 0:
            testing and print("\tMultiple of 23")
            scores[player] += m
            nextIndex = prevIndex - 7
            if nextIndex < 0:
                nextIndex += len(marbles)
            scores[player] += marbles.pop(nextIndex)
            prevIndex = nextIndex
        #Placing the current marble between the ones +1 and +2 to the right of the previous index
        else:
            nextIndex = (prevIndex + 2) % len(marbles)
            if nextIndex == 0:
                marbles.append(m)
                prevIndex = len(marbles)-1
            else:
                marbles.insert(nextIndex, m)
                prevIndex = nextIndex
            
        testing and print("P", player, "   M", m, ":", marbles)
        player += 1
        if player > numPlayers:
            player = 1

    return max([scores[x] for x in scores.keys()])


def solution2():
    numPlayers, lastPoints = getInput()
    
    scores = {}
    for i in range(numPlayers):
        scores[i+1] = 0
        
    player = 1 #current player's ID number
    #Using doubly-linked list nodes for quick traversal forward and backward
    currNode = LLNode(0)
    currNode.setNext(currNode)
    currNode.setPrev(currNode)
    for m in range(1,(lastPoints*100)+1):
        testing and print(m, "Current node: ...", currNode.getPrev().data, "<->", currNode.data, "<->", currNode.getNext().data, "...")
        
        if m % 23 == 0:
            scores[player] += m
            for i in range(6):
                currNode = currNode.getPrev()
            scores[player] += currNode.getPrev().data
            currNode.setPrev(currNode.getPrev().getPrev())
            currNode.getPrev().setNext(currNode)
        #Placing the current marble between the ones +1 and +2 to the right of the previous index
        else:
            currNode = currNode.getNext()
            newNode = LLNode(m, prev_=currNode, next_=currNode.getNext())
            currNode.getNext().setPrev(newNode)
            currNode.setNext(newNode)
            currNode = newNode
            
        player += 1
        if player > numPlayers:
            player = 1

    return max([scores[x] for x in scores.keys()])


print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 1:", solution1())
print("Year " + aocDate[0] + " Day " + aocDate[1] + " solution part 2:", solution2())
#33965633 too low