class Node:
    '''Nodes used in the Binary Search Tree to store data values.
    '''
    def __init__(self, data, lambdaComp=None):
        '''Constructor for the Binary Tree.
        - data: The data to be stored in this node.
        - lambdaComp: Lambda comparison function. Required for data structures that don't have a built-in method for "less than"
        '''
        self.data = data
        self.lambdaComp = lambdaComp
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

    
    def insert(self, data):
        '''Inserts a new data value into the binary tree.
        Return: Bool for if the insertion was successful.
        '''
        #If there is no special lambda comparison function, we use '<'
        if self.lambdaComp is None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self.lambdaComp)
                    return True
                else:
                    return self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data, self.lambdaComp)
                    return True
                else:
                    return self.right.insert(data)
        #If there is a lambda comparison function, we use that
        else:
            if self.lambdaComp(data, self.data):
                if self.left is None:
                    self.left = Node(data, self.lambdaComp)
                    return True
                else:
                    return self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data, self.lambdaComp)
                    return True
                else:
                    return self.right.insert(data)

    
    def length(self):
        '''Returns the number of elements in this binary tree.
        '''
        l = 0
        if self.left is not None:
            l = self.left.length()
        r = 0
        if self.right is not None:
            r = self.right.length()

        return 1 + l + r


    def toList(self):
        '''Returns all elements in this binary tree as a sorted list from smallest to largest.
        '''
        binList = []

        if self.left:
            binList = self.left.toList()

        binList.append(self.data)

        if self.right:
            binList.extend(self.right.toList())

        return binList


    def inTree(self, value):
        '''Checks if the given value is in this binary tree.
        '''
        if self.data == value:
            return True
        elif value < self.data and self.left:
            return self.left.inTree(value)
        elif self.left:
            return self.right.inTree(value)
        return False


    def deleteNode(self):
        '''Method to delete this node and all of its child nodes.
        '''
        if self.left:
            self.left.deleteNode()
            self.left = None
        if self.right:
            self.right.deleteNode()
            self.right = None
        self.data = None
        del self


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
        if self.head:
            try:
                if self.head.insert(data):
                    self._size += 1
                    return True
                else:
                    return False
            #If the max recursion limit has been hit, we try rebalancing the tree and inserting again
            except RecursionError as err:
                print("==============================Insert. Num elements:", self.size)
                self.balanceTree()
                if self.head.insert(data):
                    self._size += 1
                    return True
                else:
                    return False


        self.head = Node(data, self.lambdaComp)
        self._size = 1
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
                else:

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
        '''Returns all elements in this binary tree as a sorted list from smallest to largest.
        '''
        if self.head:
            return self.head.toList()
        return []


    def inTree(self, value):
        '''Checks if the given value is in this binary tree.
        '''
        if self.head:
            return self.head.inTree(value)
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
        #Converting the tree into an ordered list
        vals = self.toList()
        #Clearing the current tree
        self.deleteTree()
        #Adding the elements back in using our list-to-binary tree method which inserts everything in a balanced way.
        self.listToBinaryTree(vals)