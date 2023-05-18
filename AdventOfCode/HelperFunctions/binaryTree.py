class Node:
    '''Nodes used in the Binary Search Tree to store data values.
    '''
    def __init__(self, data):
        '''Constructor for the Binary Tree Node.
        - data: The data to be stored in this node.
        '''
        self.data = data
        self.left = None
        self.right = None


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
        


class BinarySearchTree:
    '''Binary search tree. Stores the root node and meta-data about the tree.
    '''
    def __init__(self, data=None):
        '''Constructor for the Binary Tree.
        - data: Initial data value to be stored in the binary tree's root node. Can be left empty.
        '''
        self.root = None
        self._size = 0

        if data:
            self.root = Node(data)
            self._size = 1

    
    @property
    def size(self):
        '''The number of elements in this binary tree.
        '''
        return self._size


    def printTree(self):
        '''Prints all data values in the binary tree from smallest to largest.
        '''
        if self.root is None:
            return None

        cur = self.root
        stack = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                print(cur.data, end=" ")
                cur = cur.right
            else:
                print()
                return

    
    def insert(self, data):
        '''Inserts a new data value into the binary tree.
        Return: Bool for if the insertion was successful.
        '''
        #If this tree is empty, we set the new value as the root node
        if self.root is None:
            self.root = Node(data)
            self._size += 1
            return True

        #If there's at least one node in this tree, we have to find where to put the new value
        ptr = self.root
        while ptr is not None:
            #If the current value is already in the tree, we break
            if ptr.data == data:
                return False

            #If the new value is less than the current node's value, we go left
            if data < ptr.data:
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
        ptr = self.root
        returnVal = None

        while ptr is not None:
            if ptr.data == value:
                returnVal = ptr.data
                
                #If the node has no children, deletes itself
                if ptr.left is None and ptr.right is None:
                    if ptr.data == self.root.data:
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
        if self.root is None:
            return None

        binList = []
        cur = self.root
        stack = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                binList.append(cur.data)
                cur = cur.right
            else:
                break

        return binList


    def inTree(self, value):
        '''Returns a bool for if a given value is in this binary tree.
        '''
        if self.root is None:
            return False

        ptr = self.root
        while ptr is not None:
            if ptr.data == value:
                return True
            elif value < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return False


    def deleteTree(self):
        '''Completely clears all values stored in this binary tree.
        '''
        stack = [self.root]

        while len(stack) > 0:
            n = stack.pop(0)

            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

            n.data = None
            n = None

        self.root = None
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
        if self.root is None:
            return

        #Converting the tree into an ordered list
        vals = self.toList()
        #Clearing the current tree
        self.deleteTree()
        #Adding the elements back in using our list-to-binary tree method which inserts everything in a balanced way.
        self.listToBinaryTree(vals)



class BinarySearchTreeComplex:
    '''Binary search tree for complex objects that require a special "less than" comparitor to sort. Stores the root node and meta-data about the tree.
    '''
    def __init__(self, lessThan, data=None):
        '''Constructor for the Binary Tree.
        - lessThan: Lambda comparison function. Required for data structures that don't have a built-in method for "less than"
        - data: Initial data value to be stored in the binary tree's root node. Can be left empty.
        '''
        self.root = None
        self._size = 0
        self.lessThan = lessThan

        if data:
            self.root = Node(data)
            self._size = 1

    
    @property
    def size(self):
        '''The number of elements in this binary tree.
        '''
        return self._size


    def printTree(self):
        '''Prints all data values in the binary tree from smallest to largest.
        '''
        if self.root is None:
            return None

        cur = self.root
        stack = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                print(cur.data, end=" ")
                cur = cur.right
            else:
                print()
                return

    
    def insert(self, data):
        '''Inserts a new data value into the binary tree.
        Return: Bool for if the insertion was successful.
        '''
        #If this tree is empty, we set the new value as the root node
        if self.root is None:
            self.root = Node(data)
            self._size += 1
            return True

        #If there's at least one node in this tree, we have to find where to put the new value
        ptr = self.root
        while ptr is not None:
            #If the current value is already in the tree, we break
            if ptr.data == data:
                return False

            #If the new value is less than the current node's value, we go left
            if self.lessThan(data, ptr.data):
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
        ptr = self.root
        returnVal = None

        while ptr is not None:
            if ptr.data == value:
                returnVal = ptr.data
                
                #If the node has no children, deletes itself
                if ptr.left is None and ptr.right is None:
                    if ptr.data == self.root.data:
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
            elif self.lessThan(value, ptr.data):
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
        if self.root is None:
            return None

        binList = []
        cur = self.root
        stack = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                binList.append(cur.data)
                cur = cur.right
            else:
                break

        return binList


    def inTree(self, value):
        '''Returns a bool for if a given value is in this binary tree.
        '''
        if self.root is None:
            return False

        ptr = self.root
        while ptr is not None:
            if ptr.data == value:
                return True
            elif self.lessThan(value, ptr.data):
                ptr = ptr.left
            else:
                ptr = ptr.right

        return False


    def deleteTree(self):
        '''Completely clears all values stored in this binary tree.
        '''
        stack = [self.root]

        while len(stack) > 0:
            n = stack.pop(0)

            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

            n.data = None
            n = None

        self.root = None
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
        if self.root is None:
            return

        #Converting the tree into an ordered list
        vals = self.toList()
        #Clearing the current tree
        self.deleteTree()
        #Adding the elements back in using our list-to-binary tree method which inserts everything in a balanced way.
        self.listToBinaryTree(vals)