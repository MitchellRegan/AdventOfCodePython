#https://adventofcode.com/2021/day/18
#https://adventofcode.com/2021/day/18#part2

import os
import math
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


.asdf #Need to make a separate function for splitting large numbers
#Loop explosions without splits until all explosions are done
#Perform all splits at once
#Repeat looping explosions without splits
#Keep doing this until no explosions and no splits


def explodeTree(root_, depth_=0):
    '''Recursively traverses the given node tree to look for pairs with a depth of 4 or more.

    Parameters
    ----------
        root_: Node object to traverse.
        depth_: The number of brackets around the current Node.

    Returns: True if there were no explosions and the tree is fully reduced. False if there was an explosion.
    '''
    if root_ is None:
        return True

    if isinstance(root_.data, int):
        return True

    #If this node is a set of brackets with a depth less than 4, we check the left and/or right sides of this bracket
    if root_.data == ',' and depth_ < 4:
        leftIsValid = explodeTree(root_.left, depth_+1)
        if not leftIsValid:
            return False
        return explodeTree(root_.right, depth_+1)

    #If this node is a set of brackets with depth of 4 or more, we explode
    if root_.data == ',' and depth_ >= 4:
        #Sometimes a pair is more than a depth of 4, so we need to go deeper
        if not isinstance(root_.left.data, int) or not isinstance(root_.right.data, int):
            leftIsValid = explodeTree(root_.left, depth_+1)
            if not leftIsValid:
                return False
            return explodeTree(root_.right, depth_+1)

        print("\t\tExploding pair [", root_.left.data, ",", root_.right.data, "]")

        #Traversing up the tree to find a branch to the left to add the left number to
        print("\t\t  Looking for left number...")
        curr = root_.parent
        prev = root_
        goingUp = True
        while True:
            if goingUp:
                #If there aren't any paths upwards, we just drop this left number
                if curr is None:
                    print("\t\t\tNo upwards path. Dropping", root_.left.data)
                    break
                #Once a valid branch opens up to the left, we start traversing down the right path
                if curr.right == prev:
                    goingUp = False
                    prev = curr
                    curr = curr.left
                    print("\t\t\tLeft branch found at value:", curr.data)
                #If there's no branch to the left, we just keep traversing upwards
                else:
                    prev = curr
                    curr = curr.parent
                    print("\t\t\tGoing Up")
            else:
                #If there aren't any remaining path down-right, we've found the number to add to
                if curr.right is None:
                    print("\t\t\tFound value to add to:", curr.data)
                    curr.data = curr.data + root_.left.data
                    #If the new total is larger than 9, it needs to be split
                    if curr.data > 9:
                        leftSplit = Node(math.floor(curr.data/2), curr)
                        rightSplit = Node(math.ceil(curr.data/2), curr)
                        curr.data = ','
                        curr.left = leftSplit
                        curr.right = rightSplit
                    break
                #Otherwise we need to keep going down
                else:
                    prev = curr
                    curr = curr.right
                    print("\t\t\tGoing Down-right. Curr value:", curr.data)
                    

        #Traversing up the tree to find a branch to the right to add the right number to
        print("\t\t  Looking for right number...")
        curr = root_.parent
        prev = root_
        goingUp = True
        while True:
            if goingUp:
                #If there aren't any paths upwards, we just drop this right number
                if curr is None:
                    print("\t\t\tNo upwards path. Dropping", root_.right.data)
                    break
                #Once a valid branch opens up to the right, we start traversing down the left path
                if curr.left == prev:
                    goingUp = False
                    prev = curr
                    curr = curr.right
                    print("\t\t\tRight branch found at value:", curr.data)
                #If there's no branch to the right, we just keep traversing upwards
                else:
                    prev = curr
                    curr = curr.parent
                    print("\t\t\tGoing Up")
            else:
                #If there aren't any remaining path down-left, we've found the number to add to
                if curr.left is None:
                    print("\t\t\tFound value to add to:", curr.data)
                    curr.data = curr.data + root_.right.data
                    #If the new total is larger than 9, it needs to be split
                    if curr.data > 9:
                        leftSplit = Node(math.floor(curr.data/2), curr)
                        rightSplit = Node(math.ceil(curr.data/2), curr)
                        curr.data = ','
                        curr.left = leftSplit
                        curr.right = rightSplit
                        print("\t\t\t\tToo large. Split into [", leftSplit.data, ",", rightSplit.data, "]")
                    break
                #Otherwise we need to keep going down
                else:
                    prev = curr
                    curr = curr.left
                    print("\t\t\tGoing Down-left. Curr value:", curr.data)

        #After exploding, this pair of numbers is removed and replaced with a single number, 0
        root_.left = None
        root_.right = None
        root_.data = 0
    return False


def solution1():
    #Parsing each line of input their own binary tree and storing the root nodes into the nodeRootList
    input = getInput()
    nodeRootList = []
    for line in input:
        root = None
        nodeStack = []
        numVal = None
        #Iterating through each char
        for i in range(0, len(line)):
            #If this is the beginning of a pair, we create a new Node to store it
            if line[i] == '[':
                #If this is a child node, we assign it to the top node in the stack
                if len(nodeStack) > 0:
                    n = Node(",", nodeStack[-1])
                    nodeStack.append(n)
                #Otherwise this is the root node
                else:
                    root = Node(",")
                    nodeStack.append(root)
            #If this is the end of a pair, we pop the top node in the stack
            elif line[i] == ']':
                #If there's a number value that needs to be assigned to the right-side of a pair, we store it
                if numVal is not None:
                    nodeStack[-1].right = Node(numVal, nodeStack[-1])
                    numVal = None
                
                #Storing this child node in the correct side of the parent node
                if len(nodeStack) > 1 and nodeStack[-2].left is None:
                    nodeStack[-2].left = nodeStack[-1]
                elif len(nodeStack) > 1 and nodeStack[-2].right is None:
                    nodeStack[-2].right = nodeStack[-1]
                
                nodeStack.pop(-1)
            #Commas denote a split between the left and right side values of a pair
            elif line[i] == ',':
                #If there's a number value that needs to be assigned to the left-side of a pair, we store it
                if numVal is not None:
                    nodeStack[-1].left = Node(numVal, nodeStack[-1])
                    numVal = None
            #If this index is a number (or part of a number), we need to store it until we know where it ends
            else:
                if numVal is None:
                    numVal = int(line[i])
                else:
                    numVal = (numVal * 10) + int(line[i])

        #Once all values have been stored in the binary tree, we store the root node in our list of all root nodes
        explodeTree(root)
        nodeRootList.append(root)
        readNodeTree(root)

    #Combining each root tree into a single tree (the one at index zero)
    #Check for pairs that are within 4 brackets and explode them
    for i in range(1, len(nodeRootList)):
        print("Combining tree 0 and", i)
        print("\t ", end='')
        readNodeTree(nodeRootList[0])
        print("\t+", end='')
        readNodeTree(nodeRootList[i])

        newRoot = Node(',')
        newRoot.left = nodeRootList[0]
        newRoot.right = nodeRootList[i]
        nodeRootList[0].parent = newRoot
        nodeRootList[i].parent = newRoot
        nodeRootList[0] = newRoot

        print("\t=", end='')
        readNodeTree(nodeRootList[0])

        #After combining, loop until this current tree has no pair that's nested 4 times
        while True:
            doneExploding = explodeTree(nodeRootList[0])
            print("\t=", end='')
            readNodeTree(nodeRootList[0])
            if doneExploding:
                break
        print("\n=====================================\n")
        
        #while not explodeTree(root):
        #    continue

    #Check for any numbers that are greater than 9 and split
    #Find the magnitude of each input line
    #Sum up the magnitude of all input lines
    return


def solution2():
    
    return


print("Year 2021, Day 18 solution part 1:", solution1())
print("Year 2021, Day 18 solution part 2:", solution2())