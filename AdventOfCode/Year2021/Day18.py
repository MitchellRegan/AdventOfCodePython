#https://adventofcode.com/2021/day/18
#https://adventofcode.com/2021/day/18#part2

import os
import math as Math
inFileDir = os.path.dirname(__file__)
inFile = os.path.join(inFileDir, "InputTestFiles/d18_test.txt")
#inFile = os.path.join(inFileDir, "InputRealFiles/d18_real.txt")


class Node:
    '''Nodes used in a Binary Tree to store data values.
    '''
    def __init__(self, data, parent=None):
        '''Constructor for the Binary Tree Node.
        - data: The data to be stored in this node.
        - parent: The Node class above this one in the binary tree
        '''
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


    def deleteNode(self):
        '''Deletes this node and all of its child nodes.
        '''
        if self.left:
            self.left.deleteNode()
            self.left = None
        if self.right:
            self.right.deleteNode()
            self.right = None
        self.data = None
        self.parent = None
        del self


def getInput():
    #List to hold each line of input as a string
    data = []

    with open(inFile, 'r') as f:
        for line in f:
            if line[-1] == '\n':
                line = line[:-1]
            data.append(line)

    return data


def readNodeTree(root_:Node):
    if root_ is None:
        return
    if root_.data == ',':
        print("[", end='')
    readNodeTree(root_.left)
    print(root_.data, end='')
    readNodeTree(root_.right)
    if root_.data == ',':
        print("]", end='')
        if root_.parent is None:
            print()
    return


def solution1():
    #Parsing each line of input their own binary tree and storing the root nodes into the nodeRootList
    input = getInput()
    nodeRootList = []

    for line in input:
        print("\t", line)
        root = None
        nodeStack = []
        numVal = None
        #Iterating through each char
        for i in range(0, len(line)):
            print('\t', line[i])
            #If this is the beginning of a pair, we create a new Node to store it
            if line[i] == '[':
                #If this is a child node, we assign it to the top node in the stack
                if len(nodeStack) > 0:
                    n = Node(",", nodeStack[-1])
                    nodeStack.append(n)
                #Otherwise this is the root node
                else:
                    print("\t\tStart of root node")
                    root = Node(",")
                    nodeStack.append(root)
                print("\t\tAdded node to stack. Stack size:", len(nodeStack))
            #If this is the end of a pair, we pop the top node in the stack
            elif line[i] == ']':
                #If there's a number value that needs to be assigned to the right-side of a pair, we store it
                if numVal is not None:
                    print("\t\tStoring right-side number", numVal)
                    nodeStack[-1].right = Node(numVal, nodeStack[-1])
                    numVal = None
                
                #Storing this child node in the correct side of the parent node
                if len(nodeStack) > 1 and nodeStack[-2].left is None:
                    nodeStack[-2].left = nodeStack[-1]
                elif len(nodeStack) > 1 and nodeStack[-2].right is None:
                    nodeStack[-2].right = nodeStack[-1]
                
                nodeStack.pop(-1)
                print("\t\tPopping node from stack. Stack size:", len(nodeStack))
            #Commas denote a split between the left and right side values of a pair
            elif line[i] == ',':
                #If there's a number value that needs to be assigned to the left-side of a pair, we store it
                if numVal is not None:
                    print("\t\tStoring left-side number", numVal)
                    nodeStack[-1].left = Node(numVal, nodeStack[-1])
                    numVal = None
            #If this index is a number (or part of a number), we need to store it until we know where it ends
            else:
                if numVal is None:
                    numVal = int(line[i])
                    print("\t\tIs number. Stored", numVal)
                else:
                    numVal = (numVal * 10) + int(line[i])
                    print("\t\tPart of number. Stored", numVal)

        #Once all values have been stored in the binary tree, we store the root node in our list of all root nodes
        nodeRootList.append(root)
        print("\tAdded root to root list. Size:", len(nodeRootList))

    print("Reading node list")
    for i in nodeRootList:
        readNodeTree(i)
    return


def solution2():
    
    return


print("Year 2021, Day 18 solution part 1:", solution1())
print("Year 2021, Day 18 solution part 2:", solution2())