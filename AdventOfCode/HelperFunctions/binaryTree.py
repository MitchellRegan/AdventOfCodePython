class Node:
    '''Nodes used in the Binary Search Tree to store data values.
    '''
    def __init__(self, data):
        '''Constructor for the Binary Tree.
        - data: The data to be stored in this node.
        '''
        self.data = data
        self.left = None
        self.right = None
    

    def printTree(self):
        '''Prints all data values in the binary tree from smallest to largest.
        '''
        if self.left:
            self.left.printTree()
        print(self.data, end='')
        if self.right:
            self.right.printTree()


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
        del self
            
    
    def toList(self, binList):
        '''Appends this node's data and all child data to the given list.
        '''
        if self.left:
            self.left.toList(binList)
        print("2")
        binList.append(self.data)
        print("3")
        if self.right:
            self.right.toList(binList)
        print("4")


class BinaryTree:
    '''Binary search tree. Stores the head node and meta-data about the tree.
    '''
    def __init__(self, data=None, lambdaComp=None):
        '''Constructor for the Binary Tree.
        - data: Initial data value to be stored in the binary tree's head node. Can be left empty.
        - lambdaComp: Lambda comparison function. Required for data structures that don't have a built-in method for "less than"
        '''
        self.head = None
        self._size = 0
        self.lambdaComp = lambdaComp

        if data:
            self.head = Node(data, lambdaComp)
            self._size = 1

    
    @property
    def size(self):
        '''The number of elements in this binary tree.
        '''
        return self._size


    def printTree(self):
        '''Prints all data values in the binary tree from smallest to largest.
        '''
        if self.head:
            self.head.printTree()
            print('\n')
        else:
            print("None")

    
    def insert(self, data):
        '''Inserts a new data value into the binary tree.
        Return: Bool for if the insertion was successful.
        '''
        #If this tree is empty, we set the new value as the head node
        if self.head is None:
            self.head = Node(data)
            self._size += 1
            return True

        #If there's at least one node in this tree, we have to find where to put the new value
        ptr = self.head
        while ptr is not None:
            #If the current value is already in the tree, we break
            if ptr.data == data:
                return False

            #If the new value is less than the current node's value, we go left
            if (self.lambdaComp is not None and self.lambdaComp(data, ptr.data)) or data < ptr.data:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = Node(data)
                    self._size += 1
                    return True
            #Otherwise we go right
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = Node(data)
                    self._size += 1
                    return True


    def remove(self, value):
        '''Removes the specified value from this binary tree and returns it.
        '''
        prev = None
        ptrDir = None
        ptr = self.head
        returnVal = None

        while ptr is not None:
            if ptr.data == value:
                returnVal = ptr.data
                
                #If the node has no children, deletes itself
                if ptr.left is None and ptr.right is None:
                    if ptr.data == self.head.data:
                        self.deleteTree()
                    else:
                        ptr.deleteNode()
                        self._size -= 1
                        if ptrDir == 'R':
                            prev.right = None
                        elif ptrDir == 'L':
                            prev.left = None

                #If the node only has one child to the left
                elif ptr.left is not None and ptr.right is None:
                    if ptrDir == 'R':
                        prev.right = ptr.left
                    elif ptrDir == 'L':
                        prev.left = ptr.left
                    del ptr
                    self._size -= 1

                #If the node only has one child to the right
                elif ptr.left is None and ptr.right is not None:
                    if ptrDir == 'R':
                        prev.right = ptr.right
                    elif ptrDir == 'L':
                        prev.left = ptr.right
                    del ptr
                    self._size -= 1

                #If the node has both left and right children
                #else:

                #Returning the value stored in the deleted node
                return returnVal
            #If we should use the custom lambda comparison function, we use that to shift left or right
            elif self.lambdaComp is not None:
                if self.lambdaComp(value, ptr.data):
                    prev = ptr
                    ptrDir = 'L'
                    ptr = ptr.left
                else:
                    prev = ptr
                    ptrDir = 'R'
                    ptr = ptr.right
            #Otherwise we use the '<' comparison to shift left or right
            else:
                if value < ptr.data:
                    prev = ptr
                    ptrDir = 'L'
                    ptr = ptr.left
                else:
                    prev = ptr
                    ptrDir = 'R'
                    ptr = ptr.right

        return None


    def toList(self):
        '''Returns all elements in this binary tree as a sorted list from smallest to largest. If empty, returns None.
        '''
        if self.head:
            binList = []
            self.head.toList(binList)
            return binList

        return None


    def inTree(self, value):
        '''Checks if a given value is in this binary tree.
        '''
        if self.head is None:
            return False

        ptr = self.head
        while ptr is not None:
            if ptr.data == value:
                return True
            elif (self.lambdaComp is not None and self.lambdaComp(data, ptr.data)) or value < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return False


    def deleteTree(self):
        '''Completely clears all values stored in this binary tree.
        '''
        if self.head:
            self.head.deleteNode()

        self.head = None
        self._size = 0


    def listToBinaryTree(self, li):
        '''Inserts all values of a sorted list into this binary tree.
        '''
        #add the middle value
        if li is None:
            return

        middleIndex = len(li) // 2
        self.insert(li[middleIndex])

        #Then do a recursive call to the values to the left and to the right of the middle value
        if middleIndex > 0:
            leftList = li[0:middleIndex]
            self.listToBinaryTree(leftList)

        if middleIndex < len(li)-1:
            rightList = li[middleIndex+1:]
            self.listToBinaryTree(rightList)


    def balanceTree(self):
        '''Method to re-order the binary tree balanced to have equal node depth on either side.
        '''
        if self.head is None:
            return
        print("A")
        #Converting the tree into an ordered list
        vals = self.toList()
        print("B")
        #Clearing the current tree
        self.deleteTree()
        print("C")
        #Adding the elements back in using our list-to-binary tree method which inserts everything in a balanced way.
        self.listToBinaryTree(vals)
        print("D")